# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:36:03 2020

@author: rache
"""

import pyperclip
from io import StringIO

"""
# Escape Character
print('My name is \'0123\'')
# Raw String
print(r'My name is \'0123\'')

str = 'MyNameIs0123'
print('My' in str)
print('Mys' in str)
# contain only letters
print(str.isalpha())
# contain only letters and numbers
print(str.isalnum())
# contain only numbers
print(str.isdecimal())

print(str[0:8].isalpha())
print(str[8:12].isdecimal())

list = ['Oh, say can you see', 'By the dawn\'s early light']
print('--'.join(list))
words_list = list[0].split()
print(words_list)
email = '     rachelyeh1007@gmail.com          '
print(email)
print(email.strip())
print(email.lstrip())

pyperclip.copy(list[0])
print(pyperclip.paste())
"""


def reverse_str1(str):
    return str[::-1]

def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]

def reverse_str3(str):
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len - 1, -1, -1):
        rstr.write(str[index])
    return rstr.getvalue()

def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))

def reverse_str5(str):
    str_list = list(str)
    str_len = len(str)
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]

    return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(str)
    print(reverse_str1(str))
    print(reverse_str2(str))
    print(reverse_str3(str))
    print(reverse_str4(str))
    print(reverse_str5(str))
