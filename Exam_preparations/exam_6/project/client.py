class Client:
    PHONE_NUMBER_LENGTH = 10
    INVALID_PHONE_NUMBER_ERROR_MESSAGE = "Invalid phone number!"

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.last_quantity_ordered = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.startswith("0") or not len(value) == Client.PHONE_NUMBER_LENGTH or not value.isdigit():
            raise ValueError(Client.INVALID_PHONE_NUMBER_ERROR_MESSAGE)
        self.__phone_number = value


