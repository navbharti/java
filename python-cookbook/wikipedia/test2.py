'''
Created on Nov 10, 2014

@author: rajni
'''
import json
import speech
import wikipedia


query = speech.input("say something")
print query
print wikipedia.summary(query, sentences=2)
speech.say(wikipedia.summary(query, sentences=2))