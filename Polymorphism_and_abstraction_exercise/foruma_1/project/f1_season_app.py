from .formula_teams.mercedes_team import MercedesTeam
from .formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name, budget):
        if team_name not in ['Red Bull', 'Mercedes']:
            raise ValueError("Invalid team name!")
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
        else:
            self.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name, red_bull_pos, mercedes_pos):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")
        best = 'Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes'
        red_bull_message = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_message = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        return f"Red Bull: {red_bull_message}. Mercedes: {mercedes_message}. {best} is ahead at the {race_name} race."
