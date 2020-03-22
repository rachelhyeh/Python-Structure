# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:44:35 2020

@author: rache
"""

import re

##### Valid Username and ID
"""
def main():
    username = input('Create your username: ')
    userID = input('Create your user ID: ')
    
    m1 = re.match(r'^[0-9a-zA-Z_]{1,20}$', username)
    if not m1:
        print('Invalid name. Only upper letter, lower letter and numbers are allowed with length under 20.')
    m2 = re.match(r'^[1-9]\d{4,11}$', userID)
    if not m2:
        print('Invalid ID. Only numbers are allowed with lenth between 4 and 11.')
    if m1 and m2:
        print('Success!')
"""



##### Find Number in String
"""
def main():
    # Create a compile to find all classes
    pattern = re.compile(r'\D{3}\d{3}(?=\D)')
    sentence = '''
    The cources I took: ENG101MTH142PHY107CGE101MTH241PHY108ECE202ECE278MTH306ECE205PHY207ECE305ECE310ECE324ECE352
    '''
    print(sentence)
    
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('----------------')

    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('----------------')

    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())
"""



##### Change Words in String
"""
def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)
"""



##### Separate Words in String
"""
def main():
    anthem = 'Oh, say can you see, \
            By the dawn\'s early light, \
            What so proudly we hailed, \
            At the twilight\'s last gleaming? \
            Whose broad stripes and bright stars, \
            Through the perilous fight, \
            O\'er the ramparts we watched, \
            Were so gallantly streaming. \
            And the rocket\'s red glare, \
            The bombs bursting in air, \
            Gave proof through the night, \
            That our flag was still there. \
            Oh say does that star spangled banner yet wave, \
            For the land of the free, and the home of the brave.'
    sentence_list = re.split(r'[，。, .]', anthem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  
"""



if __name__ == '__main__':
    main()