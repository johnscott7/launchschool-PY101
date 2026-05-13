import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_none(self):
        value = None
        self.assertIsNone(value)

unittest.main()