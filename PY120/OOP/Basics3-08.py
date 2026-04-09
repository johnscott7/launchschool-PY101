class Animal:
    def __init__(self, color):
        self._color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.get_color())

# For this problem, the MRO will be
# Cat --> Animal --> object
# It will never search Bird
