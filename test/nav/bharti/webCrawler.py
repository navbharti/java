'''
Created on Apr 18, 2014

@author: rajni
'''
import urllib
from bs4 import BeautifulSoup
import urlparse

htmltext = urllib.urlopen("http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/MainMenu.asp")
soup=BeautifulSoup(htmltext)

for tag in soup.findAll('a',href=True):
    raw = tag['href']
   # b1 = urlparse.urlparse(tag['href']).hostname
    b2 = urlparse.urlparse(tag['href']).path
    
    print '"http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/'+str(b2)+'",'
