class Animal:
    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Animal):
    def fetch(self):
        return 'fetching!'
    
    def speak(self):
        return 'bark!'
    
class Cat(Animal):
    def speak(self):
        return 'meow!'
    

dave = Dog()

kitty = Cat()
print(kitty.run())            # running!
print(kitty.speak())          # meow!

try:
    kitty.fetch()
except AttributeError as exception:
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError 'Cat' object has no attribute 'fetch'