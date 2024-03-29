class HorseRace:
    VALID_RACE_TYPES = [
        'Winter',
        'Spring',
        'Autumn',
        'Summer',
    ]
    INVALID_RACE_TYPE_ERROR_MESSAGE = "Race type does not exist!"

    def __init__(self, race_type):
        self.race_type = race_type
        self.jockeys = []
    
    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value not in self.VALID_RACE_TYPES:
            raise ValueError(self.INVALID_RACE_TYPE_ERROR_MESSAGE)
        self.__race_type = value
