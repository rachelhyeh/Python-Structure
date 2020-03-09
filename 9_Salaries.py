# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:46:43 2020

@author: rache
"""

"""
Salary for each month
Manager: $7500
Engineer: $50/hr
Sales: $60000+ 5% commissions
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass
    
    @abstractmethod
    def get_title(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 7500.0
    def get_title(self):
        return "Manager"


class Engineer(Employee):
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 50.0 * self._working_hour
    
    def get_title(self):
        return "Engineer"


class Sales(Employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 5000.0 + self._sales * 0.05
    
    def get_title(self):
        return "Sales"


def main():
    '''
    emps = [
        Manager('A'), Engineer('B'),
        Manager('C'), Sales('D'),
        Sales('E'), Engineer('F'),
        Engineer('G')
    ]
    for emp in emps:
        print('=====Employee %s as the %s=====' % (emp.name, emp.get_title()))
        if isinstance(emp, Engineer):
            emp.working_hour = int(input('Working hours for last month: '))
        elif isinstance(emp, Sales):
            emp.sales = float(input('Commissions for last month: '))
        print('Salary for last month is $%s \n' %emp.get_salary())
    '''
    
    Employee.name = input('Please enter name: ')
    Employee.get_title = input('Please enter position as Manager or Engineer or Sales: ')
    if Employee.get_title == 'Manager':
        emp = Manager(str(Employee.name))
    elif Employee.get_title == 'Engineer':
        emp = Engineer(str(Employee.name))
        emp.working_hour = int(input('Working hours for last month: '))
    elif Employee.get_title == 'Sales':
        emp = Sales(str(Employee.name))
        emp.sales = float(input('Commissions for last month: '))
    print('Salary for last month is $%s \n' %emp.get_salary())
            
if __name__ == '__main__':
    main()