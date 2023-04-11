class Concert:
    GENRE_TYPES = [
        "Metal",
        "Rock",
        "Jazz"
    ]
    MINIMUM_CONCERT_AUDIENCE = 1
    MINIMUM_PLACE_STRING_LENGTH = 2
    AUDIENCE_BELOW_MINIMUM_ERROR_MESSAGE = "At least one person should attend the concert!"
    PLACE_BELOW_MINIMUM_ERROR_MESSAGE = f"Place must contain at least {MINIMUM_PLACE_STRING_LENGTH} chars. It cannot be empty!"
    MINIMUM_TICKET_PRICE_ERROR_MESSAGE = "Ticket price must be at least 1.00$!"
    MINIMUM_EXPENSES_ERROR_MESSAGE = "Expenses cannot be a negative number!"

    def __init__(self, genre, audience, ticket_price, expenses, place):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in self.GENRE_TYPES:
            raise ValueError(f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        if value < Concert.MINIMUM_CONCERT_AUDIENCE:
            raise ValueError(Concert.AUDIENCE_BELOW_MINIMUM_ERROR_MESSAGE)
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        if value < 1.0:
            raise ValueError(Concert.MINIMUM_TICKET_PRICE_ERROR_MESSAGE)
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0.00:
            raise ValueError(Concert.MINIMUM_EXPENSES_ERROR_MESSAGE)
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if len(value) < Concert.MINIMUM_PLACE_STRING_LENGTH or value.isspace():
            raise ValueError(self.PLACE_BELOW_MINIMUM_ERROR_MESSAGE)
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
