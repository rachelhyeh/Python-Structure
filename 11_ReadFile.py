# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:01:32 2020

@author: rache
"""

import time

"""
def main():
    f = None
    try:
        #f = open('NationalAnthem.txt', 'r', encoding='utf-8')
        f = open('11_NationalAnthem.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('File not found error!')
    except LookupError:
        print('Look up error!')
    except UnicodeDecodeError:
        print('Unicode decode error!')
    finally:
        if f:
            f.close()
"""
"""
def main():
    try:
        with open('11_NationalAnthem.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('File not found error!')
    except LookupError:
        print('Look up error!')
    except UnicodeDecodeError:
        print('Unicode decode error!')
"""        

def main():
    
    #read the whole file at once
    with open('11_NationalAnthem.txt', 'r', encoding='utf-8') as f:
        print(f.read())
        print()
    
    
    #use for-in loop to read
    with open('11_NationalAnthem.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
        print()
    
    # Read by lines
    with open('11_NationalAnthem.txt') as f:
        lines = f.readlines()
    print(lines)

        
if __name__ == '__main__':
    main()