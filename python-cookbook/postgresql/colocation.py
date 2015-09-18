'''
Created on Oct 19, 2014

@author: rajni
'''
import psycopg2

conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("SELECT gid, type, 'Cluster', grid_id from all_merged_inmeter order by grid_id")
rows = cur.fetchall()
print "Gid\ttype\tcluster"
next_r = 0
next_c = 0

cur = conn.cursor()
cur.execute("select grid_id, count(grid_id)::integer from  all_merged_inmeter    group by grid_id order by grid_id")
rows = cur.fetchall()
index = 0
print len(rows)
feature_type = {'vehicle accident': 1, 'vehicle lost': 2, 'unidentified body':3, 'missing male':4, 'missing female': 5 }
feature_summary = [[-1 for x in xrange(7)] for x in xrange(300)]
for row in rows:
    index = index + 1
    feature_summary[index][0] = row[0]
    feature_summary[index][1] = row[1]
    print feature_summary[index][0], "\t", feature_summary[index][1]
    #print row

cur = conn.cursor()

cur.execute("SELECT gid, type, 'Cluster', grid_id from all_merged_inmeter order by grid_id")
rows = cur.fetchall()
index = 0
for row in rows:
    for i in range(feature_summary[index][1]):
        if feature_summary[index][0] == row[3] and row[1] == feature_type['vehicle accident']:
            feature_summary[index][2] += 1
        if feature_summary[index][0] == row[3] and row[1] == feature_type['vehicle lost']:
            feature_summary[index][2] += 1
        if feature_summary[index][0] == row[3] and row[1] == feature_type['unidentified body']:
            feature_summary[index][2] += 1
        if feature_summary[index][0] == row[3] and row[1] == feature_type['missing male']:
            feature_summary[index][2] += 1
        if feature_summary[index][0] == row[3] and row[1] == feature_type['missing female']:
            feature_summary[index][2] += 1
        index = index + 1
    
print "feature_summary"
for j in range(130):
    print feature_summary[j]
        
    
# Creates a list containing 5 lists initialized to 0
transaction_table = [[-1 for x in xrange(50)] for x in xrange(300)] 
#transaction_table = [300][50]
'''
for i in range(len(rows)):
   #print row[0],"\t", row[1],"\t",row[2],"\t", row[3], "\n"
    #print rows[i][3]
    if(rows[i][3]!=rows[i-1][3]):
        next_c = 0
        next_r = next_r + 1
        transaction_table[next_r][next_c] = rows[i][3]
        next_c = next_c + 1
        print
        print rows[i][3],"rows: ",next_r
    transaction_table[next_r][next_c] = rows[i][0]    
    next_c = next_c + 1
    print rows[i][0], "Column: ", next_c
    
  # next_c = next_c + 1
print "Operation done successfully";

'''
'''
for t in transaction_table:
    print t
    
'''
print "now fetch some more!!!"


cur = conn.cursor()
cur.execute("SELECT gid, grid_id FROM all_merged_inmeter where type = '''vehicle lost''' order by gid")
t1 = cur.fetchall()
for t in t1:
    print t[0]

cur = conn.cursor()    
cur.execute("select gid, grid_id from all_merged_inmeter where type = '''missing male''' order by gid")
t2 = cur.fetchall()
for t in t2:
    print t[0]
    
cur = conn.cursor()
cur.execute("select gid, grid_id from all_merged_inmeter where type = '''missing female''' order by gid")
t3 = cur.fetchall()
for t in t3:
    print t[0]
    
cur = conn.cursor()
cur.execute("select gid, grid_id from all_merged_inmeter where type = '''vehicle accident''' order by gid")
t4 = cur.fetchall()
for t in t4:
    print t[0]
    
cur = conn.cursor()
cur.execute("select gid, grid_id from all_merged_inmeter where type = '''unidentified body''' order by gid")
t5 = cur.fetchall()
for t in t5:
    print t[0]
    
for i in range(len(t1)):
    if t1[1] == t2[1]:
        print t1[0], "\t", t2[0], "\t", t2[1]    

for i in range(len(t1)):
    if t1[1] == t2[1]:
        print t1[0], "\t", t3[0], "\t", t3[1] 
        
conn.close()