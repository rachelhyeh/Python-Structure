# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:21:46 2020

@author: rache
"""


"""
30 position, 15 Christians, position in a circle
Every 9th person is  tossed
Return safe position where only all Christians stand
"""

def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('Safe' if person else 'Toss', end='')


if __name__ == '__main__':
    main()