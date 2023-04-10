import os


class User:
    MINIMUM_AGE = 6

    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MINIMUM_AGE:
            raise ValueError(f"Users under the age of {self.MINIMUM_AGE} are not allowed!")
        self.__age = value

    def __str__(self):
        # result = f"Username: {self.username}, Age: {self.age}\n" + f"Liked movies:\n"
        # if self.movies_liked:
        #     result += '\n'.join(x.details() for x in self.movies_liked) + '\n'
        # else:
        #     result += "No movies liked.\n"
        # result += "Owned movies:\n"
        # if self.movies_owned:
        #     result += '\n'.join(x.details() for x in self.movies_owned)
        # else:
        #     result += "No movies owned."
        # return result
        movies_liked_str = 'No movies liked.'
        if self.movies_liked:
            movies_liked_str = os.linesep.join(x.details() for x in self.movies_liked)
        movies_owned_str = 'No movies owned.'
        if self.movies_owned:
            movies_owned_str = os.linesep.join(x.details() for x in self.movies_owned)

        return f'''Username: {self.username}, Age: {self.age}
Liked movies:
{movies_liked_str}
Owned movies:
{movies_owned_str}'''


