'''
Created on Apr 9, 2014

@author: rajni
'''
import fibo, sys
from nav.bharti.fibo import fib
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333))
print(a.count(66.25))
print(a.count( 'x'))

print(a.insert(2, -1))
print(a)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

fib(100)
dir(fibo)
dir(sys)
dir()