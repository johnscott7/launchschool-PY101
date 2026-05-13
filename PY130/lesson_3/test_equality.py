import unittest

class EqualityTest(unittest.TestCase):
    def test_assert_equal(self):
        lst1 = [1, 2, 3]
        lst2 = [1, 2, 3]
        self.assertEqual(lst1, lst2)   # this test method would pass

    def test_assert_is(self):
        lst1 = [1, 2, 3]
        lst2 = [1, 2, 3]
        self.assertIs(lst1, lst2)      # this test method would fail

if __name__ == '__main__':
    unittest.main()