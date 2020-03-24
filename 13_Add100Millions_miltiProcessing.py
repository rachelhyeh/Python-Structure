# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:43:03 2020

@author: rache
"""

from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, queue):
    total = 0
    for number in curr_list:
        total += number
    queue.put(total)

"""
def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))
"""


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    queue = Queue()
    index = 0
    # Separate into 8 process for calculation
    for _ in range(8):
        p = Process(target=task_handler,args=(number_list[index:index + 12500000], queue))
        index += 12500000
        processes.append(p)
        p.start()
    # Start the processes and count time
    start = time()
    for p in processes:
        p.join()
    # Combine the processes and results
    total = 0
    while not queue.empty():
        total += queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()