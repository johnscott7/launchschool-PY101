class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self._name = name

    @classmethod
    def get_school(cls):
        return cls.school_name
    
print(Student.get_school())
print(Student.school_name)
