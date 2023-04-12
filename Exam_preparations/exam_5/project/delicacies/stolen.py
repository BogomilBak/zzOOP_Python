# from Exam_preparations.exam_5.project.delicacies.delicacy import Delicacy
from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.portion = 250

    @property
    def class_name_getter(self):
        return "Stolen"
