class Cat:
    def __init__(self):
        # self._name = name
        pass

    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return 'Name not set!'

    
cat1 = Cat()
print(cat1.get_name())
