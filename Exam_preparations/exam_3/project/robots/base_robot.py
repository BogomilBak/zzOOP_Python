import abc


class BaseRobot(abc.ABC):
    ROBOT_EMPTY_NAME_ERROR_MESSAGE = "Robot name cannot be empty!"
    ROBOT_EMPTY_KIND_ERROR_MESSAGE = "Robot kind cannot be empty!"
    ROBOT_EMPTY_PRICE_ERROR_MESSAGE = "Robot price cannot be less than or equal to 0.0!"

    def __init__(self, name, kind, price: float, weight):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace() or not isinstance(value, str):
            raise ValueError(BaseRobot.ROBOT_EMPTY_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if not value or value.isspace() or not isinstance(value, str):
            raise ValueError(BaseRobot.ROBOT_EMPTY_KIND_ERROR_MESSAGE)
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0 or not isinstance(value, float):
            raise ValueError(BaseRobot.ROBOT_EMPTY_PRICE_ERROR_MESSAGE)
        self.__price = value

    @property
    @abc.abstractmethod
    def weight_increment(self):
        pass

    def eating(self):
        self.weight += self.weight_increment

