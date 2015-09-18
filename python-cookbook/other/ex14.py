'''
Created on Sep 20, 2014
http://www.sthurlow.com/python/lesson11/
@author: rajni
'''
### pickletest.py
### PICKLE AN OBJECT

# import the pickle module
import pickle

# lets create something to be pickled
# How about a list?
picklelist = ['one',2,'three','four',5,'can you count?']

# now create a file
# replace filename with the file you want to create
file = open('filename', 'w')

# now let's pickle picklelist
pickle.dump(picklelist,file)

# close the file, and your pickling is complete
file.close()


# now open a file for reading
# replace filename with the path to the file you created in pickletest.py
unpicklefile = open('filename', 'r')

# now load the list that we pickled into a new object
unpickledlist = pickle.load(unpicklefile)

# close the file, just for safety
unpicklefile.close()

# Try out using the list
for item in unpickledlist:
    print item