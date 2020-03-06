# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:56:13 2020

@author: rache
"""

import time

class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
        
    def run(self):
        """
        Counting time
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
                    
    def display(self):
        """
        Display time
        """
        print('%02d:%02d:%02d' %(self._hour, self._minute, self._second))


def main():
    #clock = Clock()
    clock = Clock(23, 59, 30)
    while True:
        clock.display()
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()