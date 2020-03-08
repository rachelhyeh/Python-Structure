# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:37:36 2020

@author: rache
"""

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('% is playing.' % self._name)

    def drink(self):
        if self._age >= 21:
            print('%s is %s and can drink beer.' % (self._name, self._age))
        else:
            print('%s is not 18 and can only drink juice.' % self._name)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s is studing %s in %s.' % (self._name, course, self._grade))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %s is teaching %s.' % (self._title, self._name, course))


def main():
    stu = Student('Rachel', 18, 'Graduate')
    stu.study('Math')
    stu.drink()
    stu.age = 24
    stu.drink()
    t = Teacher('Yeh', 38, 'Dr.')
    t.teach('Python programming')
    t.drink()


if __name__ == '__main__':
    main()