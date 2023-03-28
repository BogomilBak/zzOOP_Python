from .formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def sponsors(self):
        first = {
            1: 1000000,
            3: 500000,
        }
        second = {
            5: 100000,
            7: 50000,
        }
        return first, second

    def expenses(self):
        return 200000
