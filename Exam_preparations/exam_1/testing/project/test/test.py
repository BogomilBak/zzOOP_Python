from unittest import TestCase

from project.movie import Movie


class TestMovie(TestCase):
    TEST_NAME = "The Matrix"
    TEST_YEAR = 2000
    TEST_RATING = 9.5

    def setUp(self) -> None:
        self.movie = Movie(self.TEST_NAME, self.TEST_YEAR, self.TEST_RATING)

    def test__init_provide_accurate_data_expect_to_succeed(self):
        self.assertEqual(self.TEST_NAME, self.movie.name)
        self.assertEqual(self.TEST_YEAR, self.movie.year)
        self.assertEqual(self.TEST_RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__name_provide_empty_string_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test__year_provide_invalid_value_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1800

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test__add_actor_append_actor_and_check_if_actor_is_in_list__expect_to_succeed(self):
        self.movie.add_actor("Keanu")
        self.assertTrue("Keanu" in self.movie.actors)

    def test__add_multiple_actors_and_check_if_they_are_in_list__expect_to_succeed(self):
        self.movie.add_actor("Test1")
        self.movie.add_actor("Test2")
        self.movie.add_actor("Test3")
        self.assertTrue("Test1" in self.movie.actors)
        self.assertTrue("Test2" in self.movie.actors)
        self.assertTrue("Test3" in self.movie.actors)

    def test__add_actor_append_same_actor_twice__expect_to_raise(self):
        self.movie.add_actor("Keanu")
        result = self.movie.add_actor("Keanu")
        self.assertEqual("Keanu is already added in the list of actors!", result)

    def test__gt_provide_weaker_movie_expect_the_matrix_to_be_better(self):
        titanic = Movie("Titanic", 1990, 5.5)
        result = self.movie > titanic
        self.assertEqual('"The Matrix" is better than "Titanic"', result)

    def test__gt_provide_better_movie_expect_titanic_to_be_better(self):
        titanic = Movie("Titanic", 1990, 10.5)
        result = self.movie > titanic
        self.assertEqual('"Titanic" is better than "The Matrix"', result)

    def test__repr__expect_to_give_accurate_info(self):
        self.movie.actors = ['Keanu', 'Trinity']
        actual_result = repr(self.movie)
        expected_result = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected_result, actual_result)
