class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
            
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')

emp_1 = Employee('John', 'Scott', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.first = 'Jim'

print(emp_1)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)