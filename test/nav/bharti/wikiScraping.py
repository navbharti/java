'''
Created on Jun 13, 2014

@author: rajni
'''
from bs4 import BeautifulSoup
import urllib

page = urllib.urlopen("http://en.wikipedia.org/wiki/Srinivasa_Ramanujan")
html = page.read() 
soup=BeautifulSoup(html)

body=soup.find('body')
#print body
heading= body.find('h1',{'id':'firstHeading'})
print heading.text
