# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:18:17 2020

@author: rache
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


# Without multiprocessing
"""
def processing(name):
    print('%s starts process.' % name)
    processTime = randint(5, 10)
    sleep(processTime)
    print('%s finished process with %d seconds.' % (name, processTime))

def main():
    start = time()
    processing('Rachel')
    processing('Yeh')
    end = time()
    print('Total spend %.2f seconds.' % (end - start))
"""


# With multiprocessing
"""
def processing(name):
    print('%s starts process with PID %d.' % (name, getpid()))
    processTime = randint(5, 10)
    sleep(processTime)
    print('%s finishes process with %d seconds.' % (name, processTime))

def main():
    start = time()
    p1 = Process(target=processing, args=('Rachel', ))
    p1.start()
    p2 = Process(target=processing, args=('Yeh', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Total spend %.2f seconds.' % (end - start))
"""


# With multiprocessing
"""
counter = 0
def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.1)
        
def main():
    Process(target=sub_task, args=('Rachel', )).start()
    Process(target=sub_task, args=('Yeh', )).start()
"""


if __name__ == '__main__':
    main()