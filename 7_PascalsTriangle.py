# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:58:56 2020

@author: rache
"""

def main():
    num = int(input('Number of rows: '))
    pt = [[]] * num
    for row in range(len(pt)):
        pt[row] = [None] * (row + 1)
        for col in range(len(pt[row])):
            if col == 0 or col == row:
                pt[row][col] = 1
            else:
                pt[row][col] = pt[row - 1][col] + pt[row - 1][col - 1]
            print(pt[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()