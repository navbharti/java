'''
Created on Sep 19, 2014

@author: rajni
'''
a = 0
while a < 10:
    a = a + 1
    print a
    
'''while {condition that the loop continues}:
    {what to do in the loop}
    {have it indented, usually four spaces}
{the code here is not looped}
{because it isn't indented} 
'''

#EXAMPLE
#Type this in, see what it does
x = 10
while x != 0:
    print x
    x = x - 1
    print "wow, we've counted x down, and now it equals", x
print "And now the loop has ended."