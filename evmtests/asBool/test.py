from evmtests import EVMTestCase


class TestCase(EVMTestCase):
    @staticmethod
    def ref(root):
        return ['-false-', '-true-'][root]
