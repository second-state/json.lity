from evmtests import EVMTestCase


class TestCase(EVMTestCase):
    @staticmethod
    def ref(root):
        return root['hello']
