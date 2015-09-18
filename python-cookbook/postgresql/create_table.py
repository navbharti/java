'''
Created on Oct 18, 2014

@author: rajni
'''
import psycopg2

conn = psycopg2.connect(database="navbharti", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")

print "Opened database successfully"
#source: http://www.tutorialspoint.com/postgresql/postgresql_python.htm
#Create a Table
'''Following Python program will be used to create a table in previously created database:'''


cur = conn.cursor()
cur.execute('''CREATE OR REPLACE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully"

#INSERT Operation
'''Following Python program shows how we can create records in our COMPANY table created in above example:'''
conn.commit()
conn.close()