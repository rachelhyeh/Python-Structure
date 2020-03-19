# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:55:06 2020

@author: rache
"""

import json


def main():
    mydict = {'name': 'Rachel',
              'age': 26,
              'education': ['UB', 'TAMU'],
              'courses': [
                      {'class': 'MTH', 'grade': 100},
                      {'class': 'ECE', 'grade': 95},
                      {'class': 'CSE', 'grade': 90}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('Finish Saving!')


if __name__ == '__main__':
    main()