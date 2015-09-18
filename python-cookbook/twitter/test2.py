'''
Created on Nov 8, 2014

@author: rajni
'''
from TwitterAPI import TwitterAPI
api = TwitterAPI('gXuFN93StTAOM7ACHn2etV93N', 'ieG7APGTgPiznPbUhpoSkpfDQ5gL6UlwTq3pF4q04JQK3RpeqU', '262476906-q5sNfau94ywvVsiaYmvh6NabZc4ZGGr9jejnA0tv', 'IewghCAhHolgOvBwFnhdAZTT5pDvsFAOqBsIB4fxh0W73')
r = api.request('search/tweets', {'q':'pizza'})
for item in r:
    print item