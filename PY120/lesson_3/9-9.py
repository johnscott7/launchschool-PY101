class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

my_bird = Sparrow('sparrow')
print(my_bird.species)