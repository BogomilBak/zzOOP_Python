import unittest
from unittest import TestCase

from project.hero import Hero


class TestHero(TestCase):
    USERNAME = "Gosho"
    LEVEL = 1
    HEALTH = 10
    DAMAGE = 1

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        self.default_enemy = Hero("Pesho", 1, 1, 1)

    def test_init(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test_battle_with_same_names_expect_raise(self):
        self.default_enemy.username = self.USERNAME
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.default_enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test__battle_health_is_zero_before_start__expect_raise(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.default_enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test__battle_enemy_health_is_zero_before_start__expect_raise(self):
        self.default_enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.default_enemy)
        self.assertEqual(f"You cannot fight {self.default_enemy.username}. He needs to rest", str(ex.exception))

    def test__battle_draw_should_return_proper_message_draw(self):
        first = Hero("asd", 2, 1, 2)
        second = Hero("dsa", 2, 1, 2)

        actual_result = first.battle(second)
        self.assertEqual("Draw", actual_result)

    def test__battle_win_for_the_attacking_player_should_return_you_win(self):
        first = Hero("asd", 20, 100, 2)
        second = Hero("dsa", 2, 1, 2)

        expected_level = first.level + 1
        expected_health = first.health + 5 - (second.damage * second.level)
        expected_damage = first.damage + 5

        actual_result = first.battle(second)
        self.assertEqual("You win", actual_result)
        self.assertEqual(expected_level, first.level)
        self.assertEqual(expected_health, first.health)
        self.assertEqual(expected_damage, first.damage)

    def test__battle_lose_for_the_attacking_player_should_return_you_lose(self):
        second = Hero("asd", 20, 100, 2)
        first = Hero("dsa", 2, 1, 2)

        expected_level = second.level + 1
        expected_health = second.health + 5 - (first.damage * first.level)
        expected_damage = second.damage + 5

        actual_result = first.battle(second)
        self.assertEqual("You lose", actual_result)
        self.assertEqual(expected_level, second.level)
        self.assertEqual(expected_health, second.health)
        self.assertEqual(expected_damage, second.damage)

    def test__str__expected_happy_message(self):
        actual_result = str(self.hero)
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n"

        self.assertEqual(expected_result, actual_result)

