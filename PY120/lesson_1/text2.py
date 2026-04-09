class Cat:
    def __init__(self, name):
        self.name = name


dog = Cat('horse')
horse = Cat('horse')

print(dog == horse)