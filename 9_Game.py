# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:40:29 2020

@author: rache
"""

from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Person(object, metaclass=ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        :param name 
        :param hp: healing points
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, enemy):
        pass


class Player(Person):
    
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """
        :param name
        :param hp: healing point
        :param mp: magic point
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, enemy):
        """Attack enemy HP between 10 and 30"""
        enemy.hp -= randint(10, 25)

    def double_attack(self, enemy):
        """ 
        Attack enemy 50HP or at least half of HP
        :param enemy
        :return: True for success otherwise false
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = enemy.hp * 2 // 1
            injury = injury if injury >= 50 else 50
            enemy.hp -= injury
            return True
        else:
            self.attack(enemy)
            return False

    def magic_attack(self, others):
        """
        :param enemy
        :return: True for success otherwise false
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """Resume MP radomly between 1 and 20"""
        incMP = randint(1, 20)
        self._mp += incMP
        return incMP

    def __str__(self):
        return '%sPlayer\n' % self._name + 'HP: %d\n' % self._hp + 'MP: %d\n' % self._mp


class Monster(Person):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return 'Monster %s\n' % self._name + 'HP: %d\n' % self._hp


def is_any_alive(monsters):
    """Whether monster is alive or not"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """Random select one of the monster which is alive to attack"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(player, monsters):
    """Display information of player and monsters"""
    print(player)
    for monster in monsters:
        print(monster, end='')


def main():
    player = Player('Rachel', 1000, 120)
    m1 = Monster('A', 75)
    m2 = Monster('B', 150)
    m3 = Monster('C', 300)
    m4 = Monster('D', 600)
    m5 = Monster('E', 1200)
    ms = [m1, m2, m3, m4, m5]
    fight_round = 1
    while player.alive and is_any_alive(ms):
        print('========Round %02d========' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)   #Random select which method to attack
        if skill <= 6:  #60% uses normal attack
            print('%s uses normal attack to %s.' % (player.name, m.name))
            player.attack(m)
            print('%s resumes %dMP.' % (player.name, player.resume()))
        elif skill <= 9:  #30% uses magic attack (if no MP then normal attack)
            if player.magic_attack(ms):
                print('%s uses magic attack.' % player.name)
            else:
                print('%s fails to use magic attack.' % player.name)
        else:  #10% uese double attack (if no MP then normal attack)
            if player.double_attack(m):
                print('%s uses double attack to %s.' % (player.name, m.name))
            else:
                print('%s uses normal attack to %s.' % (player.name, m.name))
                print('%s resumes %dMP.' % (player.name, player.resume()))
        #if m.alive > 0:  #Monster attack player if still alives
        #    print('%s attacks %s.' % (m.name, u.name))
        #    m.attack(u)
        for i in range(len(ms)):
            if ms[i].alive==True:
                print('%s attacks %s.' % (ms[i].name, player.name))
                ms[i].attack(player)
        display_info(player, ms)  #Display information for all in each round
        fight_round += 1
    print('\n========Game Over!========\n')
    if player.alive > 0:
        print('Player %s Victory!' % player.name)
    else:
        print('Monster Victory!')


if __name__ == '__main__':
    main()