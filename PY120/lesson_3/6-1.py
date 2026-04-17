class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        
        self._name = name

jack = Person('Jack')
print(jack.name)


jack.name = 'John'
print(jack.name)

jack.name = 50