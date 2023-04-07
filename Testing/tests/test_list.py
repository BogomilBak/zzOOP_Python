from unittest import TestCase

from Testing.list import IntegerList


class TestIntegerList(TestCase):
    DEFAULT = 2, 4, 6

    def setUp(self) -> None:
        self.list = IntegerList(self.DEFAULT)

    def test_add__an_element_different_from_int__expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.list.add("Gosho")

        self.assertIsNotNone(ex)

    def test_add__integer_element__expect_to_succeed(self):
        self.list.add(1)
        self.assertEqual(self.list.get_data()[-1], 1)

    def test_remove_index_out_of_range_element__expect_to_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(5)

        self.assertIsNotNone(ex)

    def test_remove_index__expect_to_succeed(self):
        tt = IntegerList(1, 2, 3)
        tt.remove_index(0)
        self.assertEqual(len(tt.get_data()), 2)

    def test_constructor_give_not_integers__expect_to_be_empty(self):
        tt = IntegerList("asd", [1, 2], {2, 3}, 2.5)
        self.assertEqual(len(tt.get_data()), 0)

    def test_constructor_give_integers_expect_to_not_be_empty(self):
        tt = IntegerList(1, 2, "gosho")
        self.assertEqual(len(tt.get_data()), 2)

    def test_get__give_element_that_is_inside_expect_to_succeed(self):
        tt = IntegerList(1, 2, "gosho")
        result = tt.get(0)
        self.assertEqual(result, 1)

    def test_get__give_element_that_does_not_exist_expect_to_raise(self):
        tt = IntegerList(1, 2, "gosho")
        with self.assertRaises(IndexError) as ex:
            tt.get(5)

        self.assertIsNotNone(ex)

    def test_insert__give_out_of_range_index_expect_to_raise_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.list.insert(5, 2)

        self.assertIsNotNone(ex)

    def test_insert__give_not_an_integer__expect_to_raise_value_error(self):
        tt = IntegerList(1, 2, "gosho")
        with self.assertRaises(ValueError) as ex:
            tt.insert(0, "pesho")

        self.assertIsNotNone(ex)

    def test_get_biggest__happy_case_expect_to_succeed(self):
        tt = IntegerList(1, 2, "gosho")
        result = tt.get_biggest()
        self.assertEqual(result, 2)

    def test_get_index__happy_case(self):
        tt = IntegerList(1, 2, "gosho")
        result = tt.get_index(1)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()