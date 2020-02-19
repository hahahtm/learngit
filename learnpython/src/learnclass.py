#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""author:hahahtm
   date:

"""
class Employee:
    'lei'
    employee=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.employee+=1

    def setname(self,name):
        self.name=name

    def displaypeople(self):
        print ("name:",self.name,self.salary)

emp1=Employee("htm",9500)
emp2=Employee("hc",12000)
emp1.setname("xiaohan")
emp1.displaypeople()
emp1.age=7
emp2.displaypeople()
print(emp1.__dict__)

