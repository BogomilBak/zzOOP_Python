class Jockey:
    EMPTY_NAME_ERROR_MESSAGE = "Name should contain at least one character!"
    MINIMUM_AGE_ERROR_MESSAGE = "Jockeys must be at least 18 to participate in the race!"
    MINIMUM_JOCKEY_AGE = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError(self.EMPTY_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MINIMUM_JOCKEY_AGE:
            raise ValueError(self.MINIMUM_AGE_ERROR_MESSAGE)
        self.__age = value
