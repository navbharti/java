'''
Created on Apr 18, 2014

@author: rajni
'''

from bs4 import BeautifulSoup
import urllib
universityId=1

#textfile = open("C:\\Users\\rajni\\Documents\\bihar-constituency.txt","w")
url = "http://www.ugc.ac.in"
page = urllib.urlopen(url)
html = page.read()
soup=BeautifulSoup(html)
links = soup.find_all('a')
i=0
while (i<len(links)):
    print(links[i])
    i+=1
