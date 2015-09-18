'''
Created on Sep 19, 2014

@author: rajni
'''
input = open('data', 'r')
print input
#input.close()

output = open('data', 'w')
output.write('this is written by porgram')
while True:
    line = input.readline()
    if not line: break
    print line