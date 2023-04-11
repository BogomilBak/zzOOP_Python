from unittest import TestCase

# from Exam_preparations.exam_3.testing.project.tennis_player import TennisPlayer
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    NAME = "Djokovic"
    AGE = 30
    POINTS = 900
    MINIMUM_AGE = 18

    def setUp(self) -> None:
        self.player = TennisPlayer(self.NAME, self.AGE, self.POINTS)

    def test_happy_init(self):
        self.assertEqual(self.NAME, self.player.name)
        self.assertEqual(self.AGE, self.player.age)
        self.assertEqual(self.POINTS, self.player.points)
        self.assertListEqual([], self.player.wins)

    def test__name_setter_give_name_less_than_2_symbols__expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "A"

        self.assertEqual(self.NAME, self.player.name)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test__name_setter_give_2_symbols__expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "AD"

        self.assertEqual(self.NAME, self.player.name)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test__age_setter_give_age_less_than_minimum_age__expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 15

        self.assertEqual(self.AGE, self.player.age)
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test__age_setter_give_age_minimum_age__expect_to_succeed(self):
        age = 18
        self.player.age = age
        self.assertEqual(age, self.player.age)

    def test__add_new_win_give_non_existing_win_expect_to_append(self):
        win = "Test1"
        self.player.add_new_win(win)
        self.assertEqual(len(self.player.wins), 1)
        self.assertListEqual([win], self.player.wins)
        win_2 = "Test2"
        self.player.add_new_win(win_2)
        self.assertEqual(len(self.player.wins), 2)
        self.assertListEqual([win, win_2], self.player.wins)

    def test__add_new_win_give_existing_win_expect_to_return_message(self):
        win = "Test1"
        self.player.add_new_win(win)
        actual_result = self.player.add_new_win(win)
        expected_result = f"{win} has been already added to the list of wins!"
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(len(self.player.wins), 1)
        self.assertListEqual([win], self.player.wins)

    def test__lt_give_other_to_be_better_than_our_case(self):
        player_2 = TennisPlayer("Test2", 35, 1500)
        actual_result = self.player < player_2
        expected_result = f'{player_2.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(expected_result, actual_result)

    def test__lt_give_our_case_to_be_better_than_the_other_player(self):
        player_2 = TennisPlayer("Test2", 35, 500)
        actual_result = self.player < player_2
        expected_result = f'{self.player.name} is a better player than {player_2.name}'
        self.assertEqual(expected_result, actual_result)

    def test__str(self):
        self.player.wins = ["Test1", "Asd", "QWE"]
        expected_result = f"Tennis Player: {self.player.name}\n" \
               f"Age: {self.player.age}\n" \
               f"Points: {self.player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.player.wins)}"
        actual_result = str(self.player)
        self.assertEqual(expected_result, actual_result)

