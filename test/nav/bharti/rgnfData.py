'''
Created on Jun 16, 2014

@author: rajni
'''
#from bs4 import BeautifulSoup
#import urllib


#page = urllib.urlopen("http://www.google.co.in/")
#html = page.read() 
#soup=BeautifulSoup(html)
#print soup
#body=soup.find('body')
#import scrapelib
#s = scrapelib.Scraper(requests_per_minute=10, follow_robots=True)

# Grab Google front page
#s.urlopen('https://epayment.canarabank.in/')

# Will raise RobotExclusionError
#s.urlopen('http://google.com/search')

# Will be throttled to 10 HTTP requests per minute
#while True:
 #   s.urlopen('http://example.com')
#f=open("C:\\Users\\rajni\\Desktop\\Crime in India 2012\\TABLES\\Crime Statistics India - 2012 Excel sheet\\3. Crime Against Women\\data for tableau\\district-wise-crimes.txt","r")
#for line in f.readlines():
#    ln=line.strip()
 #   column=ln.split()
  #  col1=column[13]
   # print repr(col1)
#import urllib2
#from OpenSSL import SSL

import json 
import urllib

results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/bx3r91ew?apikey=d82d620771262aa9fd8f7c8342a27143"))
#print results
