'''
Created on Sep 20, 2014

@author: rajni
'''
tot = 0
#open a file in read mode
file = open("test","r")

#Read a line from the content of the file
fileStr = file.read()

for line in fileStr:
    tot = tot +1

print tot
#Total byttes in the content


