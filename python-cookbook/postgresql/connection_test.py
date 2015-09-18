'''
Created on Oct 18, 2014

@author: rajni
'''
#source: http://www.tutorialspoint.com/postgresql/postgresql_python.htm
#Connecting To Database
'''Following Python code shows how to connect to an existing database. 
If database does not exist, then it will be created and finally a database 
object will be returned.'''
import psycopg2

conn = psycopg2.connect(database="navbharti", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")

print "Opened database successfully"