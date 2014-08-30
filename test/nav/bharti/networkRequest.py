'''
Created on Apr 18, 2014

@author: rajni
'''
from bs4 import BeautifulSoup
import urllib
urls=["http://www.ugc.ac.in/centralniversitylist.aspx?id=1&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=2&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=3&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=4&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=5&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=7&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=8&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=9&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=10&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=11&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=12&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=13&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=20&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=21&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=22&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=23&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=24&Unitype=1",
      #"http://www.ugc.ac.in/centralniversitylist.aspx?id=25&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=26&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=27&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=28&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=29&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=30&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=31&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=32&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=33&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=34&Unitype=1",
      "http://www.ugc.ac.in/centralniversitylist.aspx?id=35&Unitype=1"]
i =0
print len(urls)
while (i<len(urls)):
    url = urls[i]
    page = urllib.urlopen(url)
    html = page.read()    
    soup=BeautifulSoup(html)
    table = soup.find('table')
    divs=table.find_all('div',{'class':'box720'})
    for div in divs:
        print(str(i)+div.find('b').text+ "\t"+ div.find('a').text)   
    i+=1

#main

        