import abc


class Horse(abc.ABC):
    MINIMUM_HORSE_NAME_LENGTH = 4
    SPEED_ABOVE_MAXIMUM_ERROR_MESSAGE = "Horse speed is too high!"

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < self.MINIMUM_HORSE_NAME_LENGTH:
            raise ValueError(f"Horse name {value} is less than {self.MINIMUM_HORSE_NAME_LENGTH} symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.breed_maximum_speed:
            raise ValueError(self.SPEED_ABOVE_MAXIMUM_ERROR_MESSAGE)
        self.__speed = value

    def train(self):
        if self.speed + self.speed_increased_from_training > self.breed_maximum_speed:
            self.speed = self.breed_maximum_speed
        else:
            self.speed += self.speed_increased_from_training

    @property
    @abc.abstractmethod
    def speed_increased_from_training(self):
        pass

    @property
    @abc.abstractmethod
    def breed_maximum_speed(self):
        pass

