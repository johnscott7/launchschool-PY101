class Person:
    def __init__(self, name):
        self.name = name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'
    
    @name.setter
    def name(self, name):
        names = name.split()
        self._first_name = names[0]
        if len(names) > 1:
            self._last_name = names[1]
        else:
            self._last_name = ''

    def __str__(self):
        return self.name
    

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams
bob = Person('Robert Smith')
print(f"The person's name is: {bob}")