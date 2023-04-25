from unittest import TestCase

# from Exam_preparations.exam_6.testing.project.shopping_cart import ShoppingCart
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    NAME = "Billa"
    NAME_2 = "Kaufland"
    BUDGET = 200
    BUDGET_2 = 400
    VALID_NAME = "Milk"
    VALID_NAME_2 = "Meat"
    VALID_PRICE = 1
    VALID_PRICE_2 = 2
    INVALID_PRICE = 300

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart(self.NAME, self.BUDGET)

    def test__init(self):
        self.assertEqual(self.NAME, self.shopping_cart.shop_name)
        self.assertEqual(self.BUDGET, self.shopping_cart.budget)
        self.assertDictEqual({}, self.shopping_cart.products)

    def test_name_give_low_case_name(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = "billa"

        expected_result = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(self.NAME, self.shopping_cart.shop_name)

    def test_name_give_numbers_name(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = "1230"

        expected_result = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(self.NAME, self.shopping_cart.shop_name)

    def test_name_give_mixed_incorrect_value(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = "123123aA"

        expected_result = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(self.NAME, self.shopping_cart.shop_name)

    def test_add_to_cart_happy_case(self):
        actual_result = self.shopping_cart.add_to_cart(self.VALID_NAME, self.VALID_PRICE)
        expected_result = f"{self.VALID_NAME} product was successfully added to the cart!"
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({self.VALID_NAME: self.VALID_PRICE}, self.shopping_cart.products)

    def test_give_too_expensive_item_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart(self.VALID_NAME, self.INVALID_PRICE)
        expected_result = f"Product {self.VALID_NAME} cost too much!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({}, self.shopping_cart.products)

    def test_give_item_exactly_on_the_verge_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart(self.VALID_NAME, 100)
        expected_result = f"Product {self.VALID_NAME} cost too much!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({}, self.shopping_cart.products)


    def test_remove_from_cart_happy_case(self):
        self.shopping_cart.add_to_cart(self.VALID_NAME, self.VALID_PRICE)
        actual_result = self.shopping_cart.remove_from_cart(self.VALID_NAME)
        expected_result = f"Product {self.VALID_NAME} was successfully removed from the cart!"
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({}, self.shopping_cart.products)

    def test_remove_from_cart_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.remove_from_cart(self.VALID_NAME)
        expected_result = f"No product with name {self.VALID_NAME} in the cart!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({}, self.shopping_cart.products)

    def test_add(self):
        test_shopping_cart = ShoppingCart(self.NAME_2, self.BUDGET_2)
        self.shopping_cart.products = {self.VALID_NAME : self.VALID_PRICE}
        test_shopping_cart.products = {self.VALID_NAME_2: self.VALID_PRICE_2}
        new_instance = self.shopping_cart + test_shopping_cart
        expected_budget_result = self.shopping_cart.budget + test_shopping_cart.budget
        expected_name_result = f"{self.shopping_cart.shop_name}{test_shopping_cart.shop_name}"
        expected_products_result = {self.VALID_NAME: self.VALID_PRICE, self.VALID_NAME_2: self.VALID_PRICE_2}
        self.assertEqual(expected_budget_result, new_instance.budget)
        self.assertEqual(expected_name_result, new_instance.shop_name)
        self.assertDictEqual(expected_products_result, new_instance.products)

    def test_buy_products(self):
        self.shopping_cart.add_to_cart(self.VALID_NAME, self.VALID_PRICE)
        actual_result = self.shopping_cart.buy_products()
        expected_result = f'Products were successfully bought! Total cost: {self.VALID_PRICE:.2f}lv.'
        self.assertEqual(expected_result, actual_result)

    def test_buy_products_expect_to_raise(self):
        self.shopping_cart.budget = 1
        self.shopping_cart.add_to_cart(self.VALID_NAME, self.VALID_PRICE_2)
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.buy_products()
        expected_result = f"Not enough money to buy the products! Over budget with {1:.2f}lv!"
        self.assertEqual(expected_result, str(ex.exception))
