class Pet:

    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        print(f'{self.name} says {sound}!')

class Cat(Pet):

    def speak(self):
        super().speak('meow')
    
    def talk(self):
        self.speak()

cheddar = Cat('Cheddar')
cheddar.talk()