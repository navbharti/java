'''
Created on Sep 19, 2014

@author: rajni
'''
''''A module is a python file that (generally) has only defenitions of variables, functions, and classes.'''
class mathematics:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    def addition(self):
        return (self.a + self.b)
    def subtraction(self):
        return (self.a - self.b)
    def multiplication(self):
        return (self.a * self.b)
    def division(self):
        return (self.a / self.b)
    def reminder(self):
        return (self.a % self.b)
    def setA(self, a):
        self.a = a
    def getA(self):
        return (self.a)
    def setB(self, b):
        self.b = b