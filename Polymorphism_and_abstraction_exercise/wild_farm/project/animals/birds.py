from .animal import *
from abc import ABC, abstractmethod
from ..food import *


class Owl(Bird):
    WEIGHT_INCREASE = 0.25
    FOODS = [Meat]

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    WEIGHT_INCREASE = 0.35
    FOODS = [Vegetable, Fruit, Meat, Seed]

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"


