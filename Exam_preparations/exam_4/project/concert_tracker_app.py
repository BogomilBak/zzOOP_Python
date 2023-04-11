# from Exam_preparations.exam_4.project.band import Band
# from Exam_preparations.exam_4.project.band_members.drummer import Drummer
# from Exam_preparations.exam_4.project.band_members.guitarist import Guitarist
# from Exam_preparations.exam_4.project.band_members.singer import Singer
# from Exam_preparations.exam_4.project.concert import Concert

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }
    MUSICIAN_NAMES = {}
    BAND_NAMES = {}
    CONCERT_PLACES = {}

    INVALID_MUSICIAN_TYPE_ERROR_MESSAGE = "Invalid musician type!"

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        self.__validate_musician_type(musician_type)
        self.__validate_musician_name_exists(name)
        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.MUSICIAN_NAMES[name] = musician
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        self.__validate_band_name_exists(name)
        band = Band(name)
        self.BAND_NAMES[name] = band
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        self.__validate_concert_exists_by_place(place)
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.CONCERT_PLACES[place] = concert
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        self.__validate_musician_name_does_not_exist(musician_name)
        self.__validate_band_name_does_not_exist(band_name)
        musician = self.MUSICIAN_NAMES[musician_name]
        band = self.BAND_NAMES[band_name]
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        self.__validate_band_name_does_not_exist(band_name)
        band = self.BAND_NAMES[band_name]
        self.__validate_musician_is_a_member_of_band(band, musician_name)
        musician = self.MUSICIAN_NAMES[musician_name]
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        concert = self.CONCERT_PLACES[concert_place]
        band = self.BAND_NAMES[band_name]
        self.__validate_band_members_are_of_all_types(band)
        check_if_all_members_can_do_their_part = self.__validate_band_can_play_at_concert(concert.genre, band)
        if not check_if_all_members_can_do_their_part:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = self.__calculate_profit(concert)
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def __validate_musician_type(self, musician_type):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError(self.INVALID_MUSICIAN_TYPE_ERROR_MESSAGE)

    def __validate_musician_name_exists(self, name):
        if name in self.MUSICIAN_NAMES:
            raise Exception(f"{name} is already a musician!")

    def __validate_band_name_exists(self, name):
        if name in self.BAND_NAMES:
            raise Exception(f"{name} band is already created!")

    def __validate_concert_exists_by_place(self, place):
        if place in self.CONCERT_PLACES:
            raise Exception(f"{place} is already registered for {self.CONCERT_PLACES[place].genre} concert!")

    def __validate_musician_name_does_not_exist(self, musician_name):
        if musician_name not in self.MUSICIAN_NAMES:
            raise Exception(f"{musician_name} isn't a musician!")

    def __validate_band_name_does_not_exist(self, band_name):
        if band_name not in self.BAND_NAMES:
            raise Exception(f"{band_name} isn't a band!")

    def __validate_band_members_are_of_all_types(self, band):
        check_if_all_types_are_present = set()
        [check_if_all_types_are_present.add(x.get_class_name_by_type()) for x in band.members if x.get_class_name_by_type() in self.VALID_MUSICIAN_TYPES]
        if len(check_if_all_types_are_present) < 3:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

    @staticmethod
    def __get_band_members(band):
        drummers = [x for x in band.members if x.get_class_name_by_type() == "Drummer"]
        singers = [x for x in band.members if x.get_class_name_by_type() == "Singer"]
        guitarists = [x for x in band.members if x.get_class_name_by_type() == "Guitarist"]
        if not drummers or not singers or not guitarists:
            return False
        return drummers, singers, guitarists

    def __validate_band_can_play_at_concert(self, genre, band):
        drummers, singers, guitarists = self.__get_band_members(band)
        if genre == "Rock":
            return self.__validate_band_play_rock(drummers, singers, guitarists)
        elif genre == "Metal":
            return self.__validate_band_play_metal(drummers, singers, guitarists)
        elif genre == "Jazz":
            return self.__validate_band_play_jazz(drummers, singers, guitarists)

    @staticmethod
    def __validate_band_play_rock(drummers, singers, guitarists):
        drummers_check = [x for x in drummers if "play the drums with drumsticks" in x.skills]
        singers_check = [x for x in singers if "sing high pitch notes" in x.skills]
        guitarists_check = [x for x in guitarists if "play rock" in x.skills]
        if drummers_check and singers_check and guitarists_check:
            return True
        return False

    @staticmethod
    def __validate_band_play_metal(drummers, singers, guitarists):
        drummers_check = [x for x in drummers if "play the drums with drumsticks" in x.skills]
        singers_check = [x for x in singers if "sing low pitch notes" in x.skills]
        guitarists_check = [x for x in guitarists if "play metal" in x.skills]
        if drummers_check and singers_check and guitarists_check:
            return True
        return False

    @staticmethod
    def __validate_band_play_jazz(drummers, singers, guitarists):
        drummers_check = [x for x in drummers if "play the drums with drum brushes" in x.skills]
        singers_check = [x for x in singers if "sing low pitch notes" and "sing low pitch notes" in x.skills]
        guitarists_check = [x for x in guitarists if "play jazz" in x.skills]
        if drummers_check and singers_check and guitarists_check:
            return True
        return False

    @staticmethod
    def __calculate_profit(concert):
        amount = (concert.audience * concert.ticket_price) - concert.expenses
        return amount

    @staticmethod
    def __validate_musician_is_a_member_of_band(band, musician_name):
        musician = [x for x in band.members if x.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band.name}!")



