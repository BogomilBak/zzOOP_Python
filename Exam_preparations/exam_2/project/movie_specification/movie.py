import abc

from project.user import User


class Movie(abc.ABC):
    MINIMUM_YEAR = 1888
    AGE_RESTRICTION = 0

    @abc.abstractmethod
    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < Movie.MINIMUM_YEAR:
            raise ValueError(f"Movies weren't made before {Movie.MINIMUM_YEAR}!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError(f"The owner must be an object of type User!")
        if self not in value.movies_owned:
            value.movies_owned.append(self)
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE_RESTRICTION:
            raise ValueError(f"{self.movie_type} movies must be restricted for audience under {self.__class__.AGE_RESTRICTION} years!")
        self.__age_restriction = value

    def details(self):
        return f"{self.movie_type} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    @abc.abstractmethod
    def movie_type(self):
        pass

