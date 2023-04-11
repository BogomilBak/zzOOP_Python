class Band:
    INVALID_BAND_NAME_ERROR_MESSAGE = "Band name should contain at least one character!"

    def __init__(self, name):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(Band.INVALID_BAND_NAME_ERROR_MESSAGE)
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
