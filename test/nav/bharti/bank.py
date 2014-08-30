'''
Created on Jul 15, 2014

@author: rajni
'''
from bs4 import BeautifulSoup
import urllib
page = urllib.urlopen("http://www.banklocations.in/bank_specific_details.jsp?bank_main_id=3&city=Kerala")
html = page.read()    
soup=BeautifulSoup(html)
link=soup.find('div',{'id':'banks_search_subpage_container'})
rows=link.find_all('div',{'class':'city_search_bank_row'})
print len(rows)
for row in rows:
    print row.a