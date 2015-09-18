'''
Created on Sep 19, 2014

@author: rajni
'''
def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mult(a, b):
    return (a * b)
    
def div(a, b):
    return (a / b)

def modulo(a, b):
    return (a % b)

def pow(a, b):
    return (a ** b)

# Below is the function
def hello():
    print "hello"
    return 1234

# And here is the function being used
a = hello()
print add(11,22)
print sub(11, 22)
print mult(4, 5)
print div(40, 5)
print modulo(123, 10)
print pow(2, 3)

