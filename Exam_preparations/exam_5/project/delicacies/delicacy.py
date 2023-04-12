import abc


class Delicacy(abc.ABC):
    INVALID_NAME_ERROR_MESSAGE = "Name cannot be null or whitespace!"
    INVALID_PRICE_ERROR_MESSAGE = "Price cannot be less or equal to zero!"

    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError(Delicacy.INVALID_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError(Delicacy.INVALID_PRICE_ERROR_MESSAGE)
        self.__price = value

    def details(self):
        return f"{self.class_name_getter} {self.name}: {self.portion}g - {self.price:.2f}lv."

    @property
    @abc.abstractmethod
    def class_name_getter(self):
        pass

