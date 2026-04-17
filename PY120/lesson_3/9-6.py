class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self._name = name

student1 = Student('Craig')
student2 = Student('David')

print(student1._name)
print(student1.__class__.school_name)

print(student2._name)
print(student2.__class__.school_name)