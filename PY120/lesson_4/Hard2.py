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

class Watercraft(FuelMixin):
    def __init__(self, number_propellers,
                 number_hulls,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

class Catamaran(Watercraft):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity)


class Motorboat(Watercraft):
    def __init__(self,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(1, 1,
                kilometers_per_liter,
                liters_of_fuel_capacity)


auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)
motorboat = Motorboat(3, 800)

print(auto.range())
print(motorcycle.range())
print(catamaran.range())
print(motorboat.range())
print(catamaran.number_propellers, catamaran.number_hulls)
print(motorboat.number_propellers, motorboat.number_hulls)