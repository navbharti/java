'''
Created on Sep 20, 2014

@author: rajni
'''
#openning a file in Read mode
a = open('test', 'w')
a.write('my name is naveen kumar bharti')
#print a
a.close()

a = open('test','r')
print a.read()
#Going 5 bytes forward
a.seek(5)
print a.read()

print a.tell()
print a.readline()
a.close()

