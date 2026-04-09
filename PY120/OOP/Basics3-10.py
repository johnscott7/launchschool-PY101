class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

bird1 = Bird('Red')
print(bird1.color)

# For this problem, the MRO will be:
# Bird --> FlyxingMixin --> Animal
# It will stop at Animal and not proceed to object since
# it will find what it needs in Animal.
