#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Employee():
    '''
    Docstring for Employee 1. 
    Docstring for Employee 2.
    '''
    employeecount = 0
    def __init__(self,name,salary):
        """TODO: to be defined1. """
        self.name = name
        self.salary = salary
        Employee.employeecount += 1

    def dispemployeeinfo(self):
        print("name:%s,salary:%d" % (self.name,self.salary))
    def dispemployeecount(self):
        print("Employee count = %d" % Employee.employeecount)

emp1 = Employee("Tom",2000)
emp1.dispemployeeinfo()
emp1.dispemployeecount()

emp2 = Employee("Jack",3000)
emp2.dispemployeeinfo()
emp2.dispemployeecount()

print(Employee.__doc__)
print(Employee.__dict__)
