#!/usr/bin/env python3
import argparse
import os
import subprocess
import json
import glob
import shlex
import shutil
import contextlib
import sys

LITYC = './lityc'
EVM = './evm'
GENERATE_STRING_INPUT = 'scripts/generate_string_input.py'
PARSE_STRING_OUTPUT = 'scripts/parse_string_output.py'
ENI_LIBRARY_PATH = os.path.abspath('libeni/build/examples/eni')
ENI_LD_LIBRARY_PATH = os.path.abspath('libeni/build')
LD_LIBRARY_PATH = '{}:{}'.format(
    os.environ['LD_LIBRARY_PATH'], ENI_LD_LIBRARY_PATH
) if 'LD_LIBRARY_PATH' in os.environ else ENI_LD_LIBRARY_PATH


def check_call(cmd, **kw):
    print(end='\033[4m', file=sys.stderr)
    print(*map(shlex.quote, cmd), end='\033[0m\n', file=sys.stderr)
    return subprocess.check_call(cmd, **kw)


def run(litysource, inputfile):
    environ = {
        **os.environ,
        'ENI_LIBRARY_PATH': ENI_LIBRARY_PATH,
        'LD_LIBRARY_PATH': LD_LIBRARY_PATH,
    }
    with contextlib.suppress(FileNotFoundError):
        shutil.rmtree('tempdir')
    os.mkdir('tempdir')
    check_call([LITYC, '--bin-runtime', litysource, '--abi', '-o', 'tempdir'])
    with open('tempdir/inputfile', 'wb') as f:
        check_call([GENERATE_STRING_INPUT, inputfile], stdout=f)
    valid_contracts = []
    for contractfile in glob.iglob('tempdir/*.abi'):
        with open(contractfile) as f:
            contract = json.load(f)
        if contract:
            valid_contracts.append(
                os.path.splitext(contractfile)[0] + '.bin-runtime')
    assert len(
        valid_contracts
    ) == 1, 'require exact 1 valid contracts, instead, got {valid_contracts}'.format(valid_contracts=valid_contracts)
    with open('tempdir/outputfile', 'wb') as f:
        check_call([
            EVM, '--codefile', valid_contracts[0], '--inputfile',
            'tempdir/inputfile', '--statdump', '--gas', '1152921504606846975',
            'run'
        ],
                   stdout=f,
                   env=environ)
    check_call([PARSE_STRING_OUTPUT])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('litysource')
    parser.add_argument('inputfile')
    args = parser.parse_args()
    run(**vars(args))


if __name__ == '__main__':
    main()
