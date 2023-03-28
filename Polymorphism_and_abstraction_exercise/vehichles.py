from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER_FUEL_CONS = 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        if self.fuel_quantity > (self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONS) * distance:
            self.fuel_quantity -= (self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONS) * distance

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption


class Truck(Vehicle):
    AIR_CONDITIONER_FUEL_CONS = 1.6

    def drive(self, distance):
        if self.fuel_quantity > (self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONS) * distance:
            self.fuel_quantity -= (self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONS) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

