'''
Created on Apr 18, 2014

@author: rajni
'''

import urllib
import re
urls = ["http://google.com","http://www.jcheminf.com/","http://www.pondiuni.edu.in/","http://ceobihar.nic.in/Search/Name_Search.html"]

i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i < len(urls):
    htmlfile = urllib.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern, htmltext)
    print(titles)
    i+=1
