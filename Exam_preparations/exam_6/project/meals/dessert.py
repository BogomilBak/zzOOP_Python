# from Exam_preparations.exam_6.project.meals.meal import Meal
from project.meals.meal import Meal


class Dessert(Meal):
    def __init__(self, name, price, quantity=30):
        super().__init__(name, price, quantity)

    @property
    def get_class_by_name(self):
        return "Dessert"
