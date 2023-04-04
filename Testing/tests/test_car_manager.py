from unittest import TestCase

from Testing.car_manager import Car


class TestCar(TestCase):
    MAKE = "Honda"
    MODEL = "Civic"
    FUEL_CONSUMPTION = 7
    FUEL_CAPACITY = 60
    FUEL_AMOUNT = 0

    def test_constructor__happy_case(self):
        car = Car("Honda", "Civic", 7, 60)

        self.assertEqual(self.MAKE, car.make)
        # self.assertEqual(self.MODEL, car.model)
        # self.assertEqual(self.FUEL_CONSUMPTION, car.fuel_consumption)
        # self.assertEqual(self.FUEL_CAPACITY, car.fuel_capacity)
        # self.assertEqual(self.FUEL_AMOUNT, car.fuel_amount)

