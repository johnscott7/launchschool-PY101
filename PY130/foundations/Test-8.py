import unittest

class MyList:
    def process(self):
        return self

class TestMyList(unittest.TestCase):
    def test_process_returns_same_object(self):
        lst = MyList()
        self.assertIs(lst, lst.process())

unittest.main()



# cat.py
# --------------------------
class Cat:
    def __init__(self, name):
        self.name = name

    def miaow(self):
        return f"{self.name} is miaowing."


# test_cat.py
# --------------------------
import unittest
from cat import Cat

class CatTests(unittest.TestCase):

    def setUp(self):
        self.kitty = Cat('Kitty')

    def test_is_cat(self):
        pass

    def test_name(self):
        pass

    def test_miaow(self):
        pass

    def test_raises_error(self):
        pass

if __name__ == '__main__':
    unittest.main()