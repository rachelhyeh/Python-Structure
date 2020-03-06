# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:06:09 2020

@author: rache
"""

from random import randrange, randint, sample


def display(balls):
    """
    Display numbers of balls in the list
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    Random select one set of numbers
    """
    regular_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(regular_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    """
    Six selects of regular balls(1-34) and one select of red ball(1-16)
    Random select without repeats
    """
    n = int(input('Number of sets: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()