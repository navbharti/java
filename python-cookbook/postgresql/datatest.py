'''
Created on Oct 27, 2014

@author: rajni
'''
import dataset
import psycopg2

def table(table_name):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("select * from " + table_name)
    rows = cur.fetchall()
    return rows

db = dataset.connect('sqlite:///:memory:')
table1 = db['sometable']
data = table('all_merged_inmeter')
for d in data:
    table1.insert(dict(id=d[1], type=d[3], cluster=d[6], transaction=d[8]))
    
#table.insert(dict(name='john Doe', age=37))

#john = table.find_one(name='john Doe')
rows = table1.all()
for row in rows:
    print row['id'], "\t", row['type']
    
rows = table1    