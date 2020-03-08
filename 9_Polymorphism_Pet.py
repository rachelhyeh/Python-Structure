# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:51:13 2020

@author: rache
"""

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print('%s: Woof!' % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s: Meow~' % self._nickname)


def main():
    pets = [Dog('Doggy'), Cat('Kitten'), Dog('Puppy')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()