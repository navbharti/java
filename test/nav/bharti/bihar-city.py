'''
Created on Apr 18, 2014

@author: rajni
'''
from bs4 import BeautifulSoup
import urllib
cityCount=1
textfile = open("C:\\Users\\rajni\\Documents\\bihar-constituency.txt","w")
while(cityCount<39):
    url = "http://elepatdb.cloudapp.net/electorsearch/default.aspx?dist_id="+str(cityCount)
    
    page = urllib.urlopen(url)
    html = page.read()    
    soup=BeautifulSoup(html)
    constituency= soup.find('select',{'id': 'ddcons'})
    options=constituency.findAll('option')
    i=1
    while (i<len(options)):
        print(options[i].text)
        textfile.write(str(options[i].text)+"\n")
        print
        i+=1
    cityCount+=1
textfile.close()