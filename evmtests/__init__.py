import unittest
import json
import os
import glob
import subprocess
import sys
import tempfile
import shutil


def make_test_method(json_file):
    def testfunc(self):
        EVMTestCase._test_json_file(self, json_file)
    return testfunc


class EVMTestCaseMeta(type):
    def __new__(cls, name, bases, namespace, **kwds):
        cls = type.__new__(cls, name, bases, namespace)
        cls.file = sys.modules[namespace['__module__']].__file__
        cls.dir = os.path.dirname(cls.file)
        json_files = sorted(glob.iglob(os.path.join(cls.dir, '*.json')))
        for json_file in json_files:
            methodname = 'test_' + os.path.basename(json_file)[:-5]
            setattr(cls, methodname, make_test_method(json_file))
        return cls


class EVMTestCase(unittest.TestCase, metaclass=EVMTestCaseMeta):
    @property
    def ref(self):
        raise NotImplementedError(
            'subclasses should define this as the equalviant code to the lity test function')

    def _test_json_file(self, json_file):
        with tempfile.TemporaryDirectory() as tmpd:
            with open(json_file) as file:
                raw = file.read()
            root = json.loads(raw)
            py_result = self.ref(root)

            shutil.copy(os.path.join(self.dir, 'test.lity'), tmpd)
            shutil.copy(os.path.join('lity', 'json.lity'), tmpd)
            res = subprocess.run(
                ['python3', 'run.py', os.path.join(tmpd, 'test.lity'), json_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if res.returncode:
                print(res.stderr.decode('utf-8'), file=sys.stderr)
                res.check_returncode()
            evm_result = res.stdout.decode('utf-8').rstrip()

            self.assertEqual(py_result, evm_result, '[input: {}]\n{}'.format(json_file, raw))
