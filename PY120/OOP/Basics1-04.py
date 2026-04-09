class Cat:
    def __init__(self):
        print(f"I'm a {self.__class__.__name__.lower()}!")
kitty = Cat()
