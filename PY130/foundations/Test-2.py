import unittest

class TestSomething(unittest.TestCase):
    def test_value_lower_is_xyz(self):
        value = 'XYZ'
        self.assertEqual('xyz', value.lower())

unittest.main()