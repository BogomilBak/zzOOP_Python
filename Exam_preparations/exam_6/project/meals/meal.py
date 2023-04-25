import abc


class Meal(abc.ABC):
    EMPTY_NAME_ERROR_MESSAGE = "Name cannot be an empty string!"
    NEGATIVE_PRICE_ERROR_MESSAGE = "Invalid price!"

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(Meal.EMPTY_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError(Meal.NEGATIVE_PRICE_ERROR_MESSAGE)
        self.__price = value

    @property
    @abc.abstractmethod
    def get_class_by_name(self):
        pass

    def details(self):
        return f"{self.get_class_by_name} {self.name}: {self.price:.2f}lv/piece"
