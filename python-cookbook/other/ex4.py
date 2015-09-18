'''
Created on Sep 19, 2014

@author: rajni
'''
'''if {conditions to be met}:
    {do this}
    {and this}
    {and this}
{but this happens regardless}
{because it isn't indented}
'''

#EXAMPLE 1
y = 1
if y == 1:
    print "y still equals 1, I was just checking"

#EXAMPLE 2
print "We will show the even numbers up to 20"
n = 1
while n <= 20:
    if n % 2 == 0:
        print n
    n = n + 1
print "there, done."

a = 1
if a > 5:
    print "This shouldn't happen."
else:
    print "This should happen."
    
z = 4
if z > 70:
    print "Something is very wrong"
elif z < 7:
    print "This is normal"
    
'''if {conditions}:
    {run this code}
elif {conditions}:
    {run this code}
elif {conditions}:
    {run this code}
else:
    {run this code}
'''
#You can have as many or as little elif statements as you need
#anywhere from zero to the sky.
#You can have at most one else statement
#and only after all other ifs and elifs.

a = 10
while a > 0:
    print a
    if a > 5:
        print "Big number!"
    elif a % 2 != 0:
        print "This is an odd number"
        print "It isn't greater than five, either"
    else:
        print "this number isn't greater than 5"
        print "nor is it odd"
        print "feeling special?"
    a = a - 1
    print "we just made 'a' one less than what it was!"
    print "and unless a is not greater than 0, we'll do the loop again."
print "well, it seems as if 'a' is now no bigger than 0!"
print "the loop is now over, and without furthur adue, so is this program!"