# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:11:35 2020

@author: rache
"""

"""
from math import sqrt

def is_prime(n):
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('Prime100.txt', 'Prime1000.txt', 'Prime10000.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('Error!')
    finally:
        for fs in fs_list:
            fs.close()
    print('Finish!')
"""

def PascalsTriangle(rows, file):
    pt = [[]] * rows
    for row in range(len(pt)):
        pt[row] = [None] * (row + 1)
        for col in range(len(pt[row])):
            if col == 0 or col == row:
                pt[row][col] = 1
            else:
                pt[row][col] = pt[row - 1][col] + pt[row - 1][col - 1]
            file.write(str(pt[row][col]) + '\t')
        file.write('\n')


def main():
    filenames = ('PascalsTriangle5.txt', 'PascalsTriangle10.txt', 'PascalsTriangle15.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 15):
            if number < 5:
                PascalsTriangle(number, fs_list[0])
            elif number < 10:
                PascalsTriangle(number, fs_list[1])
            else:
                PascalsTriangle(number, fs_list[2])
    except IOError as ex:
        print(ex)
        print('Error!')
    finally:
        for fs in fs_list:
            fs.close()
    print('Finish!')
    
if __name__ == '__main__':
    main()