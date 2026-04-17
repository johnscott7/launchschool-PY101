class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name == other.name
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name != other.name
    
lucy = 18
rosie = Cat('rosie')
indo = Cat('rosie')

print(rosie == indo)
print(rosie == rosie)
print(lucy == rosie)
print(rosie == lucy)
