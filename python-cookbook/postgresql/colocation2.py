'''
Created on Oct 20, 2014

@author: rajni
'''
import psycopg2
import itertools
from itertools import combinations
import copy
from sets import Set
import dataset 

#fetched the data from the given table
def table(table_name):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("select id, type, cluster, transaction from " + table_name)
    rows = cur.fetchall()
    return rows

#fetch attribute from the table in the order by
def get_attribute(table_name, attr):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("select distinct "+attr+" from "+table_name+" order by "+ attr)
    rows = cur.fetchall()
    return rows

#fetched the points belogs to the given grid_id
def point_in_grid(grid_id):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('select gid from all_merged_inmeter where grid_id = ' + str(grid_id) + 'order by gid')
    rows = cur.fetchall()
    return rows

#returns the features type in the given grid_id
def type_in_grid(grid_id):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('select distinct type from all_merged_inmeter where grid_id = ' + str(grid_id))
    rows = cur.fetchall()
    return rows

#check for feature type if present or not
def type_present(grid_id, type):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('select True from all_merged_inmeter where grid_id = '+ str(grid_id)+ ' and "type" = '+ str("'" + type+ "'"))
    rows = cur.fetchall()
    if rows:
        return True
    return False

#returns the featrues count in the given grid_id
def type_count_in_grid(grid_id, type):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('select gid from all_merged_inmeter where grid_id = ' + str(grid_id) + ' and "type" = ' + str("'" + type+ "'"))
    rows = cur.fetchall()
    return len(rows)

#returns total points in the given grid_id
def pointcount_in_grid(grid_id):
    conn = psycopg2.connect(database="postgis_21_sample", user="postgres", password="postgresql123#", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('select gid from all_merged_inmeter where grid_id = ' + str(grid_id))
    rows = cur.fetchall()
    return len(rows)

#returns the feature probability of the given type in the grid_id
def f_prob_in_grid(grid_id, type):
    return float(type_count_in_grid(grid_id, type))/float(pointcount_in_grid(grid_id))

#returns the colocation in a grid of given numbers of feature patterns
def pattern_in_trans(grid_id,num):
    types = type_in_grid(84)
    combination = combinations(types,num)
    return list(combination)

#returns the probability of a pattern in transaction
def p_brob_in_grid(grid_id, pattern):
    prob = 1
    if len(pattern) <= 0:
        return float(0)
    for p in pattern:
        if type_present(grid_id,p):
            prob *= f_prob_in_grid(grid_id, p)
    return float(prob)

#returns the expected support for pattern 
def p_expsup(pattern):
    expsup = 1
    transactions = get_attribute('all_merged_inmeter','grid_id')
    if len(pattern) <= 0:
        return float(0)
    for transaction in transactions:
        expsup += p_brob_in_grid(int(transaction[0]), pattern)
    return float (expsup)

#returns the support of colocations pattern1 and pattern2 after calculating union
def expsup(pattern1, pattern2):
    pattern1 = Set(pattern1)
    pattern2 = Set(pattern2)
    pattern1 = pattern1 | pattern2
    return float(p_expsup(pattern1))
    
#returns the confidence to the colocation rules (X->Y) using (X U Y) as addition 
def expconf(pattern1, pattern2):
    temp_expsup = expsup(pattern1, pattern2)
    temp_p_expsup = p_expsup(pattern1)
    return temp_expsup / temp_p_expsup

#returns the confidence of the colocation rules (X->Y) as (X U Y) as union
def expconf1(pattern1, pattern2):
    return expsup(pattern1, pattern2)/p_expsup(pattern1)
    
def trim_colocation(pattern):
    for i in range(len(list(pattern))):
        pattern[i] = str(str(pattern[i]).replace("(","").replace(")","").replace("'","").replace(",",""))
    return pattern

#generates colocations and calculates the support of colocations
def colocation_sup():
    features = get_attribute("all_merged_inmeter","type")
    output = sum([map(list, combinations(features, i)) for i in range(len(features) + 1)], [])
    print "Colocations\tSupport"
    for feature in output:
        feature = trim_colocation(feature)
        print feature, "\t", p_expsup(feature) 
 
def colocation_rules():
    features = get_attribute("all_merged_inmeter","type")
    output = sum([map(list, combinations(features, i)) for i in range(len(features) + 1)], [])
    for feature1 in output:
        for feature2 in output:
            if (len(Set(feature1)) !=0 and len(Set(feature2)) != 0) and len(Set(feature1) & Set(feature2)) == 0:
                feature1 = trim_colocation(feature1)
                feature2 = trim_colocation(feature2)
                print feature1, "-->", feature2, "\tConf: ",expconf(feature1, feature2)
                #print trim_colocation(feature1), "-->", trim_colocation(feature2), "\t\t", Set(feature1) | Set(feature2)
                #print feature1, "-->", feature2
                
# First of all generate all the colocation from the features
#colocation_rules()




data = ['missing female']
data1 = ['missing female', 'missing male', 'unidentified body']
data2 = []
print len(Set(data))
print len(Set(data1))
print len(Set(data2))
print len(Set(data) & Set(data1))
print Set(data) & Set(data1)
if len(Set(data) & Set(data1)) == 0:
    print Set(data) | Set(data1)
if (len(Set(data)) !=0 and len(Set(data1)) != 0) and len(Set(data) & Set(data1)) == 0:
                feature1 = trim_colocation(data)
                feature2 = trim_colocation(data1) 
                print feature1
                print feature2

#colocation_rules()
colocation_sup()

'''
                
print len(Set(data) & Set(data1)) != 0
if len(Set(data) | Set(data1)) != 0:
                print data, "-->", data1, "\tConf: ",expconf(data, data1) '''
    #if len(feature) != 0:
     #   print p_expsup(feature
     
#colocation_sup()  
''' 
data = ['vehicle lost', 'vehicle accident']
data1 = ['missing male','missing female']
print "Patter: ", data, "\tExpSup: ", p_expsup(data)
print "Patter: ", data1, "\tExpSup: ", p_expsup(data1)
print "Patter: ", (Set(data) | Set(data1)), "\tExpSup: ", expsup(data,data1)
print expconf(data,data1)   
'''
#Output: 
#Patter:  ['vehicle lost', 'vehicle accident']     ExpSup:  55.4021682501
#Patter:  ['missing male', 'missing female']     ExpSup:  72.3065605776
#Patter:  Set(['missing male', 'vehicle accident', 'missing female', 'vehicle lost'])     ExpSup:  40.6033701454
#0.732884134826

'''print type_in_grid(84)
p = pattern_in_trans(84,1)  
print p
p = trim_colocation(p)
print p  
print p_expsup(p)
for pi in p:
    print pi '''
 
'''
    
print "---------------------------------------------------------"
data = ['vehicle lost', 'vehicle accident']
data1 = ['missing male','missing female']
#data = Set(data)
#data1 = Set(data1)
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
temp = engineers | programmers | managers
for row in temp:
    print row
print len(data) 


#print p_expsup(data)
#print p_expsup(data1)
#expsup = p_expsup(data) + p_expsup(data1)
#print "expsup::", expsup
#expconf = expsup/p_expsup(data)
#print "expconf::", expconf
#print expconf(data, data1)
#print expsup(data, data1)/p_expsup(data)
        
print "combine"
data = ('vehicle lost', 'vehicle accident')
print len(data)
output = sum([map(list, combinations(data, i)) for i in range(len(data) + 1)], [])
for row in output:
    print row, "\t", len(row), "\t", p_brob_in_grid(84, row)
print "one feature pattern in grid"        
one_colocation = pattern_in_trans(84,1)
for row in one_colocation:
    print row
#print p_brob_in_grid(84, )
print "two feature pattern in grid"        
two_colocation = pattern_in_trans(84,2)
print "three feature pattern in grid"        
three_colocaiton = pattern_in_trans(84,3)
#print p_brob_in_grid(84,three_colocaiton )
types = type_in_grid(84)
print 
print 
print
pattern = {'vehicle lost', 'vehicle accident'}
print pattern
print "probability of pattern::"
print p_brob_in_grid(84,pattern )
print "probability of ffeature "
print f_prob_in_grid(84,'vehicle lost')
print type_count_in_grid(84,'vehicle lost')
print str("'missing male'")

rows = table('all_merged_inmeter')
for row in rows:
    print row
            
print type_present(84,'missing male')
print type_count_in_grid(84,'vehicle lost')
print type_count_in_grid(84,'missing male')
print pointcount_in_grid(84)
print f_prob_in_grid(84,'vehicle lost')


rows = type_in_grid(84)
for row in rows:
    print row

    
rows = point_in_grid(84)
for row in rows:
    print row

t = table("SELECT gid, type, 'cluster', grid_id from all_merged_inmeter order by grid_id")
for i in t: 
    print i
    
t = grid_id("select distinct grid_id from all_merged_inmeter")
for i in t:
    print i
    
    '''