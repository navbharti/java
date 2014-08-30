'''
Created on Apr 18, 2014
This code is written for fetching table 
tried web site http://ceobihar.nic.in/Search/Name_Search.html
@author: rajni
'''
from bs4 import BeautifulSoup
import urllib
url = "http://ceobihar.nic.in/Search/Name_Search.html"
page = urllib.urlopen(url)
html = page.read()    
soup=BeautifulSoup(html)
table=soup.find('div',{'id': 'inner_middle'})

'''td = table.findAll('div', {'class':'content_box_text'})'''
links=table.findAll('a')
textfile=open("C:\\Users\\rajni\\Documents\\bihar-links.txt","w")
i=0
while (i<len(links)):
    print(links[i].text)
    textfile.write(str(links[i])+"\n")
    i+=1
textfile.close()
