from evmtests import EVMTestCase


class TestCase(EVMTestCase):
    @staticmethod
    def ref(root):
        if isinstance(root, bool):
            return 'BOOL'
        if isinstance(root, (int, float)):
            return 'NUMBER'
        if isinstance(root, str):
            return 'STRING'
        if isinstance(root, list):
            return 'ARRAY'
        if isinstance(root, dict):
            return 'OBJECT'
