import unittest

class TestSomething(unittest.TestCase):
    def test_xyz_not_in_lst(self):
        lst = ['abc', 'def']
        self.assertNotIn('xyz', lst)

unittest.main()