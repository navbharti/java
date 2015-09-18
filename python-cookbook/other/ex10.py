'''
Created on Sep 19, 2014

@author: rajni
'''
import ex12
# Defining a class
'''class class_name:
    [statement 1]
    [statement 2]
    [statement 3]
    [etc]
    '''
#An example of a class
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale
        
a = Shape(4, 6)
print a.area()
a.authorName("naveen")
a.describe("This is a class description!!!")  
print a.perimeter()
print a.author

class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x
        
b = Square(4)
print b.area()

a = ex12.mathematics(2, 3)
print a.addition()