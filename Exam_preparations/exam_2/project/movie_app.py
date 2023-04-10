from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __get_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
        return

    def register_user(self, username, age):
        if self.__get_user_by_username(username):
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        user = self.__get_user_by_username(username)
        if not user:
            raise Exception("This user does not exist!")
        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = self.__get_user_by_username(username)
        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, value in kwargs.items():
            self.__edit_movies_by_values(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def __edit_movies_by_values(self, movie, key, value):
        if key == "title":
            movie.title = value
        elif key == "year":
            movie.year = value
        elif key == "age_restriction":
            movie.age_restriction = value

    def delete_movie(self, username, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = self.__get_user_by_username(username)
        if not movie.owner == user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{user.username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):
        user = self.__get_user_by_username(username)
        if movie.owner == user:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        user = self.__get_user_by_username(username)
        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")
        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_moves = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return '\n'.join(x.details() for x in sorted_moves)

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join([x.username for x in self.users_collection])}\n"
        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join([x.title for x in self.movies_collection])}"
        return result
