'''
Created on Jul 18, 2014

@author: rajni
'''
from bs4 import BeautifulSoup
import urllib

page = urllib.urlopen("http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_join")
html = page.read()    
soup=BeautifulSoup(html)
div=soup.find('table',{'class':'reference notranslate'})
print div