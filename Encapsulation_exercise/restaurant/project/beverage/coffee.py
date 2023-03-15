from project.beverage.cold_beverage import ColdBeverage


class Coffee(ColdBeverage):
    PRICE = 3.50
    MILLILITERS = 50

    def __init__(self, name, caffeine):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value
