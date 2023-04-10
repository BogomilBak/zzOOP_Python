from Exam_preparations.exam_2.project.movie_app import MovieApp
from Exam_preparations.exam_2.project.movie_specification.action import Action
from Exam_preparations.exam_2.project.movie_specification.fantasy import Fantasy
from Exam_preparations.exam_2.project.movie_specification.movie import Movie
from Exam_preparations.exam_2.project.movie_specification.thriller import Thriller
from Exam_preparations.exam_2.project.user import User


movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)


# app = MovieApp()
# # print(app.register_user("Gosho", 30))
# print(app.register_user("Pesho", 30))
# user1 = app.users_collection[0]
# # user2 = app.users_collection[1]
# # action1 = Fantasy("The matrix", 1900, user1, 15)
# # action2 = Fantasy("The banq", 1900, user2, 15)
# # print(app.upload_movie("Gosho", action1))
# # print(app.upload_movie("Pesho", action2))
# # # print(app.edit_movie("Gosho", action1, title="Free Guy 2", year=1900, age_restriction=30))
# # # print(action1.title)
# # # print(action1.year)
# # # print(action1.age_restriction)
# # print(app.like_movie("Gosho", action2))
# # print(app.dislike_movie("Gosho", action2))
#
# movie1 = Movie("Test", 1900, user1, 55)
# print(movie1.details())

# app = MovieApp()
# print(str(app))