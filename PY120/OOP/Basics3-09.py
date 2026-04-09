class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color

# For this problem, the MRO will be :
# # Cat --> Animal --> object
# It will never search Bird