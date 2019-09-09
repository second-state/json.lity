from evmtests import EVMTestCase


class TestCase(EVMTestCase):
    @staticmethod
    def ref(root):
        if root == 1:
            return 'case 1'
        if root == 2:
            return 'case 2'
        if root == 0:
            return 'case 3'
        if root == -1:
            return 'case 4'
        if root == 123:
            return 'case 5'
        if root == -123:
            return 'case 6'
        return 'other'
