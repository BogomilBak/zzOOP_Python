from .formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def sponsors(self):
        first = {
            1: 1500000,
            2: 800000,
        }
        second = {
            8: 20000,
            10: 10000,
        }
        return first, second

    def expenses(self):
        return 250000


