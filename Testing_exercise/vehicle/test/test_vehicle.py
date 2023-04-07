import unittest
from unittest import TestCase

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle_init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__raise_expected(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100000)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive__happy_case(self):
        distance = 1
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        self.vehicle.drive(distance)
        self.assertEqual(self.FUEL - fuel_needed, self.vehicle.fuel)

    def test__drive_reduces_fuel_with_maximum_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test__refuel_give_more_than_the_capacity_expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test__refuel_happy_case(self):
        amount = 1
        self.vehicle.drive(amount)
        expected_result = self.vehicle.fuel + amount
        self.vehicle.refuel(1)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test__str_vehicle(self):
        actual_result = str(self.vehicle)
        expected = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected, actual_result)

