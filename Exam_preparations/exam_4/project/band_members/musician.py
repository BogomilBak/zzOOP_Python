import abc


class Musician(abc.ABC):
    INVALID_NAME_ERROR_MESSAGE = "Musician name cannot be empty!"
    AGE_BELOW_MINIMUM_ERROR_MESSAGE = "Musicians should be at least 16 years old!"
    MINIMUM_AGE_FOR_MUSICIAN = 16

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError(Musician.INVALID_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < Musician.MINIMUM_AGE_FOR_MUSICIAN:
            raise ValueError(Musician.AGE_BELOW_MINIMUM_ERROR_MESSAGE)
        self.__age = value

    def learn_new_skill(self, new_skill):
        if new_skill not in self.skills_available_to_be_learned:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

    @property
    @abc.abstractmethod
    def skills_available_to_be_learned(self):
        pass

