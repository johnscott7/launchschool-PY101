class MoveMixin:
    def walk(self):
        return f"{self.full_name} {self.gait()} forward"

class Noble(MoveMixin):
    def __init__(self, name, title):
        self._name = name
        self.title = title
    
    def gait(self):
        return "struts"
    
    @property
    def full_name(self):
        return self.title + ' ' + self._name
    
    @property
    def name(self):
        return self._name
    
class Person(MoveMixin):
    def __init__(self, name):
        self._name = name

    def gait(self):
        return "strolls"

    @property
    def full_name(self):
        return self._name
    
class Cat(MoveMixin):
    def __init__(self, name):
        self._name = name

    def gait(self):
        return "saunters"
    
    @property
    def full_name(self):
        return self._name

class Cheetah(MoveMixin):
    def __init__(self, name):
        self._name = name

    def gait(self):
        return "runs"
    
    @property
    def full_name(self):
        return self._name
    
byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"