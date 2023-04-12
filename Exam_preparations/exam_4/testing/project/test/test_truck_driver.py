from unittest import TestCase

# from Exam_preparations.exam_4.testing.project.truck_driver import TruckDriver
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    NAME = "Gosho"
    MONEY_PER_MILE = 10
    CARGO_LOCATION = "Aitos"
    CARGO_LOCATION_2 = "Karnobat"
    CARGO_MILES = 50
    CARGO_MILES_2 = 80
    EATING_DECREMENT = 20
    EATING_CHECKPOINT = 250
    SLEEPING_DECREMENT = 45
    SLEEPING_CHECKPOINT = 1000
    PUMP_GAS_DECREMENT = 500
    PUMP_GAS_CHECKPOINT = 1500
    REPAIR_CHECKPOINT = 10000
    REPAIR_TRUCK_DECREMENT = 7500

    def setUp(self) -> None:
        self.driver = TruckDriver(self.NAME, self.MONEY_PER_MILE)

    def test_init_happy_case(self):
        self.assertEqual(self.NAME, self.driver.name)
        self.assertEqual(self.MONEY_PER_MILE, self.driver.money_per_mile)
        self.assertDictEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -50
        expected_message = f"{self.driver.name} went bankrupt."
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 50
        self.assertEqual(50, self.driver.earned_money)

    def test_add_cargo_happy_case(self):
        actual_result = self.driver.add_cargo_offer(self.CARGO_LOCATION, self.CARGO_MILES)
        expected_result = f"Cargo for {self.CARGO_MILES} to {self.CARGO_LOCATION} was added as an offer."
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({self.CARGO_LOCATION: self.CARGO_MILES}, self.driver.available_cargos)
        self.driver.add_cargo_offer(self.CARGO_LOCATION_2, self.CARGO_MILES_2)
        self.assertDictEqual({self.CARGO_LOCATION: self.CARGO_MILES, self.CARGO_LOCATION_2: self.CARGO_MILES_2}, self.driver.available_cargos)

    def test_add_cargo_expect_to_raise(self):
        self.driver.add_cargo_offer(self.CARGO_LOCATION, self.CARGO_MILES)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer(self.CARGO_LOCATION, self.CARGO_MILES)
        expected_result = "Cargo offer is already added."
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({self.CARGO_LOCATION: self.CARGO_MILES}, self.driver.available_cargos)

    def test_drive_best_cargo_offer(self):
        self.driver.available_cargos = {self.CARGO_LOCATION: self.CARGO_MILES, self.CARGO_LOCATION_2: self.CARGO_MILES_2}
        actual_result = self.driver.drive_best_cargo_offer()
        self.assertDictEqual({self.CARGO_LOCATION: self.CARGO_MILES, self.CARGO_LOCATION_2: self.CARGO_MILES_2}, self.driver.available_cargos)
        expected_money = self.CARGO_MILES_2 * self.driver.money_per_mile
        expected_miles = self.CARGO_MILES_2
        self.assertEqual(expected_miles, self.driver.miles)
        self.assertEqual(expected_money, self.driver.earned_money)
        expected_result = f"{self.driver.name} is driving {self.CARGO_MILES_2} to {self.CARGO_LOCATION_2}."
        self.assertEqual(expected_result, actual_result)

    def test_drive_best_cargo_offer_expect_to_raise(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_eating_happy_case(self):
        LOCATION_1, MILES_1 = "Karnobat", 50
        LOCATION_2, MILES_2 = "Daleche", 300
        self.driver.available_cargos = {
            LOCATION_1: MILES_1,
            LOCATION_2: MILES_2
        }
        actual_result = self.driver.drive_best_cargo_offer()
        expected_money = (MILES_2 * self.driver.money_per_mile) - self.EATING_DECREMENT
        expected_miles = MILES_2
        expected_result = f"{self.driver.name} is driving {MILES_2} to {LOCATION_2}."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_money, self.driver.earned_money)
        self.assertEqual(expected_miles, self.driver.miles)

    def test_sleeping_happy_case(self):
        LOCATION_1, MILES_1 = "Karnobat", 50
        LOCATION_2, MILES_2 = "Daleche", 1100
        self.driver.available_cargos = {
            LOCATION_1: MILES_1,
            LOCATION_2: MILES_2
        }
        actual_result = self.driver.drive_best_cargo_offer()
        eating_money_loss = (MILES_2 // self.EATING_CHECKPOINT) * self.EATING_DECREMENT
        sleeping_money_loss = (MILES_2 // self.SLEEPING_CHECKPOINT) * self.SLEEPING_DECREMENT
        expected_money = (MILES_2 * self.driver.money_per_mile) - eating_money_loss - sleeping_money_loss
        expected_miles = MILES_2
        expected_result = f"{self.driver.name} is driving {MILES_2} to {LOCATION_2}."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_money, self.driver.earned_money)
        self.assertEqual(expected_miles, self.driver.miles)

    def test_pumping_gas_happy_case(self):
        LOCATION_1, MILES_1 = "Karnobat", 50
        LOCATION_2, MILES_2 = "Daleche", 1800
        self.driver.available_cargos = {
            LOCATION_1: MILES_1,
            LOCATION_2: MILES_2
        }
        actual_result = self.driver.drive_best_cargo_offer()
        eating_money_loss = (MILES_2 // self.EATING_CHECKPOINT) * self.EATING_DECREMENT
        sleeping_money_loss = (MILES_2 // self.SLEEPING_CHECKPOINT) * self.SLEEPING_DECREMENT
        pumping_gas_money_loss = (MILES_2 // self.PUMP_GAS_CHECKPOINT) * self.PUMP_GAS_DECREMENT
        expected_money = (MILES_2 * self.driver.money_per_mile) - eating_money_loss - sleeping_money_loss - pumping_gas_money_loss
        expected_miles = MILES_2
        expected_result = f"{self.driver.name} is driving {MILES_2} to {LOCATION_2}."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_money, self.driver.earned_money)
        self.assertEqual(expected_miles, self.driver.miles)

    def test_repairing_happy_case(self):
        LOCATION_1, MILES_1 = "Karnobat", 50
        LOCATION_2, MILES_2 = "Daleche", 12000
        self.driver.available_cargos = {
            LOCATION_1: MILES_1,
            LOCATION_2: MILES_2
        }
        actual_result = self.driver.drive_best_cargo_offer()
        eating_money_loss = (MILES_2 // self.EATING_CHECKPOINT) * self.EATING_DECREMENT
        sleeping_money_loss = (MILES_2 // self.SLEEPING_CHECKPOINT) * self.SLEEPING_DECREMENT
        pumping_gas_money_loss = (MILES_2 // self.PUMP_GAS_CHECKPOINT) * self.PUMP_GAS_DECREMENT
        repairing_money_loss = (MILES_2 // self.REPAIR_CHECKPOINT) * self.REPAIR_TRUCK_DECREMENT
        expected_money = (MILES_2 * self.driver.money_per_mile) - eating_money_loss - sleeping_money_loss - pumping_gas_money_loss - repairing_money_loss
        expected_miles = MILES_2
        expected_result = f"{self.driver.name} is driving {MILES_2} to {LOCATION_2}."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_money, self.driver.earned_money)
        self.assertEqual(expected_miles, self.driver.miles)

    def test_repr_(self):
        self.driver.miles = 500
        expected_result = f"{self.driver.name} has {self.driver.miles} miles behind his back."
        actual_result = repr(self.driver)
        self.assertEqual(expected_result, actual_result)





