'''
Created on Nov 19, 2014

@author: rajni
'''
import itertools

comb = itertools.combinations(txt,2)
perm = itertools.permutations('0123456789',2)
print "combination :"
count = 0
for i in comb:
    count = count + 1
    print count, " : ", i

    
print "permutation : "  
count = 0
for i in perm:
    count = count + 1
    print count, " : ", i
    