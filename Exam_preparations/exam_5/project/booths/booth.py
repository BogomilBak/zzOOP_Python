import abc


class Booth(abc.ABC):
    INVALID_CAPACITY_ERROR_MESSAGE = "Capacity cannot be a negative number!"

    def __init__(self, booth_number, capacity):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError(Booth.INVALID_CAPACITY_ERROR_MESSAGE)
        self.__capacity = value

    @property
    @abc.abstractmethod
    def get_class_name(self):
        pass

    @property
    @abc.abstractmethod
    def price_per_boot_type(self):
        pass

    def reserve(self, number_of_people):
        self.price_for_reservation = self.price_per_boot_type * number_of_people
        self.is_reserved = True

