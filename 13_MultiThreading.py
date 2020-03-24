# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:33:45 2020

@author: rache
"""

from random import randint
from threading import Thread, Lock
from time import time, sleep


# Thread(target, args)
"""
def processing(name):
    print('%s starts process.' % name)
    processTime = randint(5, 10)
    sleep(processTime)
    print('%s finishes process with %d seconds.' % (name, processTime))

def main():
    start = time()
    t1 = Thread(target=processing, args=('Rachel',))
    t1.start()
    t2 = Thread(target=processing, args=('Yeh',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('Total spend %.2f seconds.' % (end - start))
"""


# Inheritance(Thread)
"""
class ProcessTask(Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name
    def run(self):
        print('%s starts processing.' % self._name)
        processTime = randint(5, 10)
        sleep(processTime)
        print('%s finishes processing with %d seconds.' % (self._name, processTime))

def main():
    start = time()
    t1 = ProcessTask('Rachel')
    t1.start()
    t2 = ProcessTask('Yeh')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('Total spend %.2f seconds.' % (end - start))
"""


# Lock()
#"""
class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
        
    def deposit(self, money):
        # A thread enters the critical section by calling the acquire() and exits by release()
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # Create 100 deposit threads to same account
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # Wait until all threads are done
    for t in threads:
        t.join()
    print('Account balance: $%d' % account.balance)
#"""




if __name__ == '__main__':
    main()