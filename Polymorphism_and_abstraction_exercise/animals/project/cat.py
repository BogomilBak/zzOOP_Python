from .animal import Animal


class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        