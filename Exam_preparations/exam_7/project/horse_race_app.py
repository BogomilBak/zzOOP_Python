# from Exam_preparations.exam_7.project.horse_race import HorseRace
# from Exam_preparations.exam_7.project.horse_specification.appaloosa import Appaloosa
# from Exam_preparations.exam_7.project.horse_specification.thoroughbred import Thoroughbred
# from Exam_preparations.exam_7.project.jockey import Jockey

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_BREEDS = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }
    MINIMUM_HORSE_RACE_PARTICIPANTS = 2

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        self.__validate_horse_already_exists(horse_name)
        if horse_type not in self.VALID_HORSE_BREEDS:
            return
        horse = self.VALID_HORSE_BREEDS[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        self.__validate_jockey_already_exists(jockey_name)
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        self.__validate_horse_race_season_taken(race_type)
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        jockey = self.__validate_jockey_does_not_exist(jockey_name)
        horse = self.__validate_horse_is_available(horse_type)
        if jockey.horse:
            return f"Jockey {jockey.name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        race = self.__validate_horse_race_exists(race_type)
        jockey = self.__validate_jockey_does_not_exist(jockey_name)
        self.__validate_jockey_has_a_horse(jockey)
        if jockey in race.jockeys:
            return f"Jockey {jockey.name} has been already added to the {race.race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        race = self.__validate_horse_race_exists(race_type)
        self.__validate_horse_race_minimum_participants(race)
        winner = self.__get_winner_from_race(race)
        winner_horse = winner.horse.name
        winner_horse_speed = winner.horse.speed
        return f"The winner of the {race_type} race, with a speed of {winner_horse_speed}km/h is {winner.name}! Winner's horse: {winner_horse}."

    def __validate_horse_already_exists(self, horse_name):
        horse = [x for x in self.horses if x.name == horse_name]
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

    def __validate_jockey_already_exists(self, jockey_name):
        jockey = [x for x in self.jockeys if x.name == jockey_name]
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

    def __validate_horse_race_season_taken(self, race_type):
        race = [x for x in self.horse_races if x.race_type == race_type]
        if race:
            raise Exception(f"Race {race_type} has been already created!")

    def __validate_jockey_does_not_exist(self, jockey_name):
        jockey = [x for x in self.jockeys if x.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        return jockey[0]

    def __validate_horse_is_available(self, horse_type):
        for index in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[index]
            if not horse.is_taken and horse.__class__.__name__ == horse_type:
                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __validate_horse_race_exists(self, race_type):
        race = [x for x in self.horse_races if x.race_type == race_type]
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        return race[0]

    @staticmethod
    def __validate_jockey_has_a_horse(jockey):
        if not jockey.horse:
            raise Exception(f"Jockey {jockey.name} cannot race without a horse!")

    def __validate_horse_race_minimum_participants(self, race):
        if len(race.jockeys) < self.MINIMUM_HORSE_RACE_PARTICIPANTS:
            raise Exception(f"Horse race {race.race_type} needs at least two participants!")

    @staticmethod
    def __get_winner_from_race(race):
        horse_top_speed = 0
        jockey = None
        for current_jockey in race.jockeys:
            if current_jockey.horse.speed > horse_top_speed:
                horse_top_speed = current_jockey.horse.speed
                jockey = current_jockey
        return jockey

