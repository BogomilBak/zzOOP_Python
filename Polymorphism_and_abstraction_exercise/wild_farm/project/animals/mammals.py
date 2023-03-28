from .animal import *
from abc import ABC, abstractmethod
from ..food import *


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.1
    FOODS = [Vegetable, Fruit]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    WEIGHT_INCREASE = 0.4
    FOODS = [Meat]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    WEIGHT_INCREASE = 0.3
    FOODS = [Vegetable, Meat]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    WEIGHT_INCREASE = 1
    FOODS = [Meat]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
