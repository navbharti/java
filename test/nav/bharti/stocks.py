'''
Created on Apr 18, 2014

@author: rajni
'''
import urllib
import re

symbolslist = ["aapl","spy","goog","nflx"]

i=0
'''http://finance.yahoo.com/q;_ylt=AiUB6ConppEx4WxSkZ5oYucnv7gF?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s=appl'''
while i<len(symbolslist):
    url = "http://finance.yahoo.com/q;_ylt=AiUB6ConppEx4WxSkZ5oYucnv7gF?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s=" + symbolslist[i]
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_184_' + symbolslist[i] + '">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print(price)
    i+=1