from .player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args: Player):
        result = []
        for player in args:
            if player not in self.players:
                result.append(player)
                self.players.append(player)
        return f"Successfully added: {', '.join([x.name for x in result])}"

    def add_supply(self, *args):
        [self.supplies.append(x) for x in args]

    def __find_player(self, player_name):
        for x in self.players:
            if x.name == player_name:
                return x
        return

    def __find_supply_by_type(self, type):
        for index in range(len(self.supplies)-1, -1, -1):
            supply = self.supplies[index]
            if supply.__class__.__name__ == type:
                return supply, index
        return -1, None

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player(player_name)
        if not player:
            return
        if sustenance_type not in ['Food', 'Drink']:
            return
        if not [x for x in self.supplies if x.__class__.__name__.lower() == sustenance_type.lower()]:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        sustenance, index = self.__find_supply_by_type(sustenance_type)
        player.stamina = min(player.stamina + sustenance.energy, 100)
        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {sustenance.name}."

    def duel(self, first_player_name, second_player_name):
        first = self.__find_player(first_player_name)
        second = self.__find_player(second_player_name)
        if first.stamina == 0 and second.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\nPlayer {second_player_name} does not have enough stamina."
        if first.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if second.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."
        lower = first if first.stamina < second.stamina else second
        bigger = first if lower == second else second
        bigger.stamina = max(bigger.stamina - (lower.stamina / 2), 0)
        if bigger.stamina <= 0:
            return f"Winner: {lower.name}"
        lower.stamina = max(lower.stamina - (bigger.stamina / 2), 0)
        if lower.stamina <= 0:
            return f"Winner: {bigger.name}"
        winner = lower if lower.stamina > bigger.stamina else bigger
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + "\n"
        for supply in self.supplies:
            result += supply.details() + "\n"
        return result.strip()




