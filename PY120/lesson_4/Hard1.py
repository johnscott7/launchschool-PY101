class FuelMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    
    @property
    def fuel_efficiency(self):
        return self._fuel_efficiency
    
    @fuel_efficiency.setter
    def fuel_efficiency(self, kilometers_per_liter):
        self._fuel_efficiency = kilometers_per_liter

    @property
    def fuel_capacity(self):
        return self._fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, liters_of_fuel_capacity):
        self._fuel_capacity = liters_of_fuel_capacity


class WheeledVehicle(FuelMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity


auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print("Auto tires:", auto.tires)
print("Auto range:", auto.range())
print("Auto tire 0 pressure:", auto.tire_pressure(0))
auto.inflate_tire(0, 35)
print("Auto tire 0 pressure after inflate:", auto.tire_pressure(0))

print()

print("Motorcycle tires:", motorcycle.tires)
print("Motorcycle range:", motorcycle.range())
print("Motorcycle tire 0 pressure:", motorcycle.tire_pressure(0))
motorcycle.inflate_tire(0, 25)
print("Motorcycle tire 0 pressure after inflate:", motorcycle.tire_pressure(0))

print()

print("Catamaran propellers:", catamaran.number_propellers)
print("Catamaran hulls:", catamaran.number_hulls)
print("Catamaran range:", catamaran.range())
print("Catamaran fuel efficiency:", catamaran.fuel_efficiency)
print("Catamaran fuel capacity:", catamaran.fuel_capacity)