from unittest import TestCase

from Testing.car_manager import Car


class TestCar(TestCase):
    MAKE = "Honda"
    MODEL = "Civic"
    FUEL_CONSUMPTION = 7
    FUEL_CAPACITY = 60
    FUEL_AMOUNT = 0

    def setUp(self) -> None:
        self.car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

    def test_constructor__happy_case(self):

        self.assertEqual(self.MAKE, self.car.make)
        self.assertEqual(self.MODEL, self.car.model)
        self.assertEqual(self.FUEL_CONSUMPTION, self.car.fuel_consumption)
        self.assertEqual(self.FUEL_CAPACITY, self.car.fuel_capacity)
        self.assertEqual(self.FUEL_AMOUNT, self.car.fuel_amount)

