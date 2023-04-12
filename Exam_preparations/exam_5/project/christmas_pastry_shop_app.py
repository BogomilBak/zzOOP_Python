# from Exam_preparations.exam_5.project.booths.open_booth import OpenBooth
# from Exam_preparations.exam_5.project.booths.private_booth import PrivateBooth
# from Exam_preparations.exam_5.project.delicacies.gingerbread import Gingerbread
# from Exam_preparations.exam_5.project.delicacies.stolen import Stolen

from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }
    VALID_BOOTHS = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy, name, price):
        self.__validate_delicacy_already_exists_with_given_name(name)
        self.__validate_delicacy_type(type_delicacy)
        delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        self.__validate_booth_already_exists_with_given_name(booth_number)
        self.__validate_booth_type(type_booth)
        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number, delicacy_name):
        booth = self.__get_booth_by_booth_number(booth_number)
        delicacy = self.__get_delicacy_by_delicacy_name(delicacy_name)
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number):
        booth = self.__get_booth_by_booth_number(booth_number)
        calculate_bill = self.__calculate_bill_for_booth(booth)
        self.income += calculate_bill
        self.__clearing_booth_finalization(booth)
        return self.__leave_booth_return_message_builder(booth_number, calculate_bill)

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __validate_delicacy_already_exists_with_given_name(self, name):
        delicacy = [x for x in self.delicacies if x.name == name]
        if delicacy:
            raise Exception(f"{name} already exists!")

    def __validate_delicacy_type(self, type_delicacy):
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

    def __validate_booth_already_exists_with_given_name(self, booth_number):
        booth = [x for x in self.booths if x.booth_number == booth_number]
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

    def __validate_booth_type(self, type_booth):
        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

    def __get_booth_by_booth_number(self, booth_number):
        booth = [x for x in self.booths if x.booth_number == booth_number]
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        return booth[0]

    def __get_delicacy_by_delicacy_name(self, delicacy_name):
        delicacy = [x for x in self.delicacies if x.name == delicacy_name]
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        return delicacy[0]

    @staticmethod
    def __calculate_bill_for_booth(booth):
        amount = booth.price_for_reservation
        amount += sum([x.price for x in booth.delicacy_orders])
        return amount

    @staticmethod
    def __clearing_booth_finalization(booth):
        booth.is_reserved = False
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0

    @staticmethod
    def __leave_booth_return_message_builder(booth_number, calculate_bill):
        message = f"Booth {booth_number}:\n"
        message += f"Bill: {calculate_bill:.2f}lv."
        return message




