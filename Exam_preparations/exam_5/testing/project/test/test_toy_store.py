from unittest import TestCase

# from Exam_preparations.exam_5.testing.project.toy_store import ToyStore
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    DEFAULT_SHELF = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
    INVALID_SHELF = "Z"
    VALID_SHELF = "A"
    TOY_NAME_1 = "Gosho"
    TOY_NAME_2 = "Dimitar"

    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_init(self):
        self.assertDictEqual(self.DEFAULT_SHELF, self.toy.toy_shelf)

    def test_add_toy_give_non_existing_shelf_expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy(self.INVALID_SHELF, self.TOY_NAME_1)
        expected_result = "Shelf doesn't exist!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual(self.DEFAULT_SHELF, self.toy.toy_shelf)

    def test__add_toy_give_toy_that_is_already_on_the_shelf_expect_to_raise(self):
        self.toy.add_toy(self.VALID_SHELF, self.TOY_NAME_1)
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy(self.VALID_SHELF, self.TOY_NAME_1)
        expected_result = "Toy is already in shelf!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({
            "A": self.TOY_NAME_1,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        },
            self.toy.toy_shelf
        )

    def test__add_toy_give_different_toy_to_same_shelf_expect_to_raise(self):
        self.toy.add_toy(self.VALID_SHELF, self.TOY_NAME_1)
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy(self.VALID_SHELF, self.TOY_NAME_2)
        expected_result = "Shelf is already taken!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({
            "A": self.TOY_NAME_1,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        },
            self.toy.toy_shelf
        )

    def test__add_toy_happy_case_place_toy_in_the_desired_shelf(self):
        actual_result = self.toy.add_toy(self.VALID_SHELF, self.TOY_NAME_1)
        expected_result = f"Toy:{self.TOY_NAME_1} placed successfully!"
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({
            "A": self.TOY_NAME_1,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        },
            self.toy.toy_shelf
        )

    def test__remove_toy_give_non_existing_shelf_expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy(self.INVALID_SHELF, self.TOY_NAME_1)
        expected_result = "Shelf doesn't exist!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual(self.DEFAULT_SHELF, self.toy.toy_shelf)

    def test__remove_toy_try_to_remove_a_different_toy_from_a_taken_shelf(self):
        self.toy.add_toy(self.VALID_SHELF, self.TOY_NAME_1)
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy(self.VALID_SHELF, self.TOY_NAME_2)
        expected_result = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected_result, str(ex.exception))

    def test__remove_toy_happy_case(self):
        self.toy.add_toy(self.VALID_SHELF, self.TOY_NAME_1)
        actual_result = self.toy.remove_toy(self.VALID_SHELF, self.TOY_NAME_1)
        expected_result = f"Remove toy:{self.TOY_NAME_1} successfully!"
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual(self.DEFAULT_SHELF, self.toy.toy_shelf)


