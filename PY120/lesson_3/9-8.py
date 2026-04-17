class Car:
    manufacturer = 'Toyota'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f"Class manufacturer: {Car.manufacturer}")
        print(f"Instance manufacturer: {self.manufacturer}")

car1 = Car('Cadillac')
car1.show_manufacturer()
