class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def turn_on(self):
        print("Engine engaged.")

    def accelerate(self):
        print(f"Vroom vroom. {self.model} is accelerating.")
        self.speed += 20

    def brake(self):
        print("Woahhh nelly, slow down there.")
        self.speed -= 20

    def turn_off(self):
        if self.speed > 0:
            print("Cannot disengage engine. Slow down first.")
        print("Engine disengaged. Car is off.")

    def speed_check(self):
        print(f"Your speed is {self.speed}.")

my_car = Car('Honda Fit', 2005, 'black')
my_car.turn_on()
my_car.accelerate()
my_car.accelerate()
my_car.speed_check()
my_car.brake()
my_car.turn_off()
my_car.brake()
my_car.turn_off()