class Animal:
    def speak(self, message):
        print(message)

class Dog(Animal):
    def bark(self):
        self.speak('Woof! Woof! Woof!')

class Cat(Animal):
    def meow(self):
        self.speak('meow')

wolfie = Cat()
lucy = Dog()

lucy.bark()
wolfie.meow()