from unittest import TestCase

from project.plantation import Plantation


class TestPlantation(TestCase):
    SIZE = 5
    PLANT_1 = "A"
    PLANT_2 = "B"
    PLANT_3 = "CD"
    WORKER_1 = "Pesho"
    WORKER_2 = "Gosho"
    SIZE_ERROR_MESSAGE = "Size must be positive number!"
    WORKER_HIRED_ALREADAY_ERROR_MESSAGE = "Worker already hired!"
    PLANTATION_FULL_ERROR_MESSAGE = "The plantation is full!"

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test__init(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertFalse(self.plantation.plants)
        self.assertFalse(self.plantation.workers)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test__size__expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            plantation = Plantation(-1)

        self.assertEqual(self.SIZE_ERROR_MESSAGE, str(ex.exception))

    def test__hire_worker__happy_case(self):
        actual_result = self.plantation.hire_worker(self.WORKER_1)
        expected_result = f"{self.WORKER_1} successfully hired."
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.WORKER_1 in self.plantation.workers)

    def test__hire_worker__expect_to_raise(self):
        self.plantation.hire_worker(self.WORKER_1)
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker(self.WORKER_1)

        self.assertEqual(1, len(self.plantation.workers))
        self.assertEqual(self.WORKER_HIRED_ALREADAY_ERROR_MESSAGE, str(ex.exception))

    def test__hire_two_workers(self):
        self.plantation.hire_worker(self.WORKER_1)
        self.plantation.hire_worker(self.WORKER_2)
        self.assertEqual(2, len(self.plantation.workers))

    def test__len__(self):
        self.assertEqual(0, len(self.plantation))
        self.plantation.plants = {1: "a", 3: "a"}
        self.assertEqual(2, len(self.plantation))

    def test__planting_give_non_existing_worker(self):
        self.plantation.workers = [self.WORKER_1]
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting(self.WORKER_2, self.PLANT_1)
        error_message = f"Worker with name {self.WORKER_2} is not hired!"
        self.assertEqual(error_message, str(ex.exception))
        self.assertFalse(self.plantation.plants)

    def test__planting_above_maximum_capacity(self):
        self.plantation.workers = [self.WORKER_1]
        self.plantation.size = 0
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting(self.WORKER_1, "ASDASDASD")

        self.assertFalse(self.plantation.plants)
        self.assertEqual(self.PLANTATION_FULL_ERROR_MESSAGE, str(ex.exception))

    def test__planting_first_time_for_worker(self):
        self.plantation.workers = [self.WORKER_1]
        actual_result = self.plantation.planting(self.WORKER_1, self.PLANT_1)
        expected_result = f"{self.WORKER_1} planted it's first {self.PLANT_1}."
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.WORKER_1 in self.plantation.plants.keys())
        self.assertTrue([self.PLANT_1] == self.plantation.plants[self.WORKER_1])
        self.assertTrue(len(self.plantation) == 1)

    def test__planting_second_time_wokrer_adds_plant(self):
        self.plantation.workers = [self.WORKER_1]
        self.plantation.planting(self.WORKER_1, self.PLANT_1)
        actual_result = self.plantation.planting(self.WORKER_1, self.PLANT_1)
        expected_result = f"{self.WORKER_1} planted {self.PLANT_1}."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(1, len(self.plantation.plants.keys()))
        self.assertTrue([self.PLANT_1, self.PLANT_1] == self.plantation.plants[self.WORKER_1])
        self.assertTrue(len(self.plantation) == 2)

    def test__planting_first_time_for_second_while_first_already_exists(self):
        self.plantation.workers = [self.WORKER_1, self.WORKER_2]
        self.plantation.planting(self.WORKER_1, self.PLANT_1)
        actual_result = self.plantation.planting(self.WORKER_2, self.PLANT_3)
        expected_result = f"{self.WORKER_2} planted it's first {self.PLANT_3}."
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.WORKER_2 in self.plantation.plants.keys())
        self.assertTrue([self.PLANT_3] == self.plantation.plants[self.WORKER_2])
        self.assertTrue(len(self.plantation) == 2)

    def test__str_(self):
        self.plantation.workers = [self.WORKER_1, self.WORKER_2]
        self.plantation.plants = {
            self.WORKER_1: [self.PLANT_1, self.PLANT_2],
            self.WORKER_2: [self.PLANT_3, self.PLANT_1]
        }
        actual_result = str(self.plantation)
        expected_result = [f"Plantation size: {self.plantation.size}"]
        expected_result.append(f'{", ".join(self.plantation.workers)}')
        for worker, plants in self.plantation.plants.items():
            expected_result.append(f"{worker} planted: {', '.join(plants)}")
        expected_result = '\n'.join(expected_result)
        self.assertEqual(expected_result, actual_result)

    def test__repr(self):
        self.plantation.workers = [self.WORKER_1, self.WORKER_2]
        actual_result = repr(self.plantation)
        expected_result = f'Size: {self.plantation.size}\n' + f'Workers: {", ".join(self.plantation.workers)}'
        self.assertEqual(expected_result, actual_result)





