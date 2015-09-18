'''
Created on Nov 8, 2014
https://github.com/bear/python-twitter
@author: rajni
'''
import twitter
'''
import requests
from requests.auth import HTTPProxyAuth
#set http_proxy=http://proxy.myproxy.com
#set https_proxy=https://proxy.myproxy.com


proxyDict = { 
          'http'  : '10.10.80.13', 
          'https' : '10.10.80.13'
        }
auth = HTTPProxyAuth('r28623', 'Ajit@#angel2012')

r = requests.get("http://www.google.com", proxies=proxyDict, auth=auth)
'''
api = twitter.Api(consumer_key='gXuFN93StTAOM7ACHn2etV93N',
                      consumer_secret='ieG7APGTgPiznPbUhpoSkpfDQ5gL6UlwTq3pF4q04JQK3RpeqU',
                      access_token_key='262476906-q5sNfau94ywvVsiaYmvh6NabZc4ZGGr9jejnA0tv',
                      access_token_secret='IewghCAhHolgOvBwFnhdAZTT5pDvsFAOqBsIB4fxh0W73')
print api
#print api.VerifyCredentials() {"id": 16133, "location": "Philadelphia", "name": "bear"}
#users = api.GetFriends()
#print [u.name for u in users]
#statuses = api.GetPublicTimeline()
users = api.GetFriends()