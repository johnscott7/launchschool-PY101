class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

print(vars(Fruit('orange')))
print(vars(Pizza('pepperoni')))