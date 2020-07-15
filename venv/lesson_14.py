

class Animal:
    is_alive: bool = True

    def breeze(self):
        print("I'm breezing")


class Mammal(Animal):
    leg_amount: int
    kid_food_type: str = 'Milk'

    def voice(self):
        raise NotImplementedError

    def do_bad_things(self):
        raise NotImplementedError


class Cat(Mammal):
    def voice(self):
        print('Meow')


class Dog(Mammal):
    def voice(self):
        print('Guf!')
    #pass


class CatDog(Cat, Dog):
    pass


dog = Dog()
cat = Cat()

#cat.voice()
#dog.voice()

catdog = CatDog()
catdog.voice()

#animals = [cat, dog]

#for animal in animals:
  #  animal.voice()

from datetime import datetime

class Human:
    first_name: str
    last_name: str

    def __digest_food(self):
        print("I'm digesting")

    def eat(self):
        self.__digest_food()


    def __init__(self):
        self.first_name = 'Ivan'

    @staticmethod
    def print_current_time():
        print(datetime.now())

    @classmethod
    def get_list_of_attributes(cls):
        return['first name', 'last_name']


h = Human()
h.eat()
# h._Human__digest_food()

print(CatDog.mro())

h.print_current_time()


print(Human.get_list_of_attributes())


print(type(type))

NewHuman = type('NewHuman', (Human,), {'power': 100500, 'can_die': False})

newhuman = NewHuman

print(newhuman.power, newhuman.can_die)


class Configuration:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

config = Configuration()
config2 = Configuration()

print(config2 is config)


from dataclasses import dataclass
from typing import List

@dataclass
class Player:
    full_name: str

@dataclass
class Coach:
    full_name: str



@dataclass
class Team:
    players: List[Player]
    coach: Coach

players = [Player(full_name='Roberto Carlos'), Player(full_name='Roberto Pirlo')]
coach = Coach ('Jurgen Klopp')
dream_team = Team(players=players, coach=oach)


