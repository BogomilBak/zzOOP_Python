from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_poss):
        revenue = self.caulculate_sponsors(race_poss) - self.expenses()
        self.__budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.__budget}$"

    @abstractmethod
    def sponsors(self):
        pass

    @abstractmethod
    def expenses(self):
        pass

    def caulculate_sponsors(self, pos):
        money = 0
        for dic in self.sponsors():
            if pos <= min(dic.keys()):
                money += dic[min(dic.keys())]
                continue
            if pos <= max(dic.keys()):
                money += dic[max(dic.keys())]
        return money

