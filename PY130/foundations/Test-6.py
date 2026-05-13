class NoExperienceError(Exception):
    pass

class Employee:
    def __init__(self, experience):
        self.experience = experience
        self.hired = False

    def hire(self):
        if self.experience < 3:
            raise NoExperienceError
        else:
            self.hired = True


import unittest

class TestEmployee(unittest.TestCase):
    def test_hire_exception_with_low_experience(self):
        employee = Employee(2)
        with self.assertRaises(NoExperienceError):
            employee.hire()

unittest.main()