# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:07:15 2020

@author: rache
"""

from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """
        Orinigal coordinate of x- and y-axis
        :param x: x-axis
        :param y: y-axis
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        New coordinate for x- and y-axis
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        Distance of movement
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        Counting the distance with another coordinate
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    p1.move_by(-1, 2)
    p2.move_to(-1, 2)
    print(p1)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()