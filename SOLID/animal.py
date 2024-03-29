from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species
    @abstractmethod
    def animal_sound(self):
        pass


class Dog(Animal):

    def animal_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def animal_sound(self):
        return 'meow'


class Chicken(Animal):
    def animal_sound(self):
        return 'cluck'


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')
        elif animal.species == "chicken":
            print('cluck')


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
animal_sound(animals)

