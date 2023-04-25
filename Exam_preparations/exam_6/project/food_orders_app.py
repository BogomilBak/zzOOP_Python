# from Exam_preparations.exam_6.project.meals.meal import Meal
# from Exam_preparations.exam_6.project.client import Client

from project.meals.meal import Meal
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    CURRENT_RECEIPT_ID = 0
    VALID_MEALS = [
        "Starter",
        "Main Dish",
        "Dessert",
        "MainDish"
    ]

    CLIENT_ALREADY_EXISTS_ERROR_MESSAGE = "The client has already been registered!"
    MINIMUM_MENU_LENGTH = 5
    MINIMUM_MENU_LENGTH_ERROR_MESSAGE = "The menu is not ready!"

    def __init__(self):
        self.menu = []
        self.client_list = []

    def register_client(self, client_phone_number):
        self.__validate_if_client_already_exists(client_phone_number)
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ not in self.VALID_MEALS:
                continue
            self.menu.append(meal)

    def show_menu(self):
        menu = self.__menu_message_builder()
        return menu

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        self.__check_if_there_are_enough_meals()
        client = self.__find_or_generate_client(client_phone_number)
        self.__validate_if_all_meals_exist(meal_names_and_quantities)
        self.__validate_if_there_is_enough_quantity(meal_names_and_quantities)
        self.__add_meals_to_client_cart(client, meal_names_and_quantities)
        # total_bill = sum(x.price for x in client.shopping_cart)
        meals = ', '.join(x.name for x in client.shopping_cart)
        return f"Client {client_phone_number} successfully ordered {meals} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.__find_or_generate_client(client_phone_number)
        self.__check_if_there_are_meals_in_clients_list(client)
        self.__increases_meal_quantities_back(client)
        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.__find_or_generate_client(client_phone_number)
        self.__check_if_there_are_meals_in_clients_list(client)
        bill = client.bill
        client.bill = 0
        client.shopping_cart = []
        receipt_number = self.__generate_receipt_number()
        return f"Receipt #{receipt_number} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __validate_if_client_already_exists(self, client_phone_number):
        client = [x for x in self.clients_list if x.phone_number == client_phone_number]
        if client:
            raise Exception(self.CLIENT_ALREADY_EXISTS_ERROR_MESSAGE)

    def __menu_message_builder(self):
        if len(self.menu) < self.MINIMUM_MENU_LENGTH:
            raise Exception(self.MINIMUM_MENU_LENGTH_ERROR_MESSAGE)
        return '\n'.join(x.details() for x in self.menu).strip()

    def __check_if_there_are_enough_meals(self):
        if len(self.menu) < self.MINIMUM_MENU_LENGTH:
            raise Exception(self.MINIMUM_MENU_LENGTH_ERROR_MESSAGE)

    def __find_or_generate_client(self, client_phone_number):
        client = [x for x in self.clients_list if x.phone_number == client_phone_number]
        if client:
            return client[0]
        self.register_client(client_phone_number)
        client = self.__find_or_generate_client(client_phone_number)
        return client

    def __validate_if_all_meals_exist(self, meal_names_and_quantities):
        for meal in meal_names_and_quantities:
            for meal_obj in self.menu:
                if meal == meal_obj.name:
                    break
            else:
                raise Exception(f"{meal} is not on the menu!")

    def __validate_if_there_is_enough_quantity(self, meal_names_and_quantities):
        for name, quantity in meal_names_and_quantities.items():
            for meal_obj in self.menu:
                if meal_obj.name == name:
                    if quantity > meal_obj.quantity:
                        raise Exception(f"Not enough quantity of {meal_obj.__class__.__name__}: {name}!")

    def __get_meal_by_name(self, name):
        meal = [x for x in self.menu if x.name == name]
        return meal[0]

    def __add_meals_to_client_cart(self, client, meal_names_and_quantities):
        for meal, quantity in meal_names_and_quantities.items():
            meal_obj = self.__get_meal_by_name(meal)
            client.shopping_cart.append(meal_obj)
            price = meal_obj.price * quantity
            client.bill += price
            meal_obj.quantity -= quantity
            if meal not in client.last_quantity_ordered:
                client.last_quantity_ordered[meal] = 0
            client.last_quantity_ordered[meal] += quantity

    @staticmethod
    def __check_if_there_are_meals_in_clients_list(client):
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

    @staticmethod
    def __increases_meal_quantities_back(client):
        for meal_obj in client.shopping_cart:
            for meal, quantity in client.last_quantity_ordered.items():
                if meal_obj.name == meal:
                    quantity_ordered = client.last_quantity_ordered[meal]
                    meal_obj.quantity += quantity_ordered
                    client.last_quantity_ordered[meal] = 0
                    break

    def __generate_receipt_number(self):
        self.CURRENT_RECEIPT_ID += 1
        return self.CURRENT_RECEIPT_ID


