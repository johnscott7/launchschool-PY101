class Cat:
    COLOR = 'purple'
    
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self._name} and I'm a {self.COLOR} cat!")

sophie = Cat('Sophie')
sophie.greet()
