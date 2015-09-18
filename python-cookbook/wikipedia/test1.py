'''
Created on Nov 8, 2014

@author: rajni
'''
import wikipedia
#print wikipedia.summary("pondicherry").encode("iso-8859-15", "xmlcharrefreplace")
#print wikipedia.search("Barack")
ny = wikipedia.page("pondicherry")
print ny.title
print ny.url
#print ny.content.encode("iso-8859-15", "xmlcharrefreplace")
#print ny.links[0]
#print wikipedia.summary("Facebook")

'''

wikipedia.search(query, results=10, suggestion=False)
Do a Wikipedia search for query.

Keyword arguments:

results - the maxmimum number of results returned
suggestion - if True, return results and suggestion (if any) in a tuple
'''
queries = wikipedia.search('Facebook',results = 51, suggestion = True)
#print query
print queries
#print len(queries)
for query in queries:
    print query
print wikipedia.suggest('Facebook')
print wikipedia.summary('Facebook', sentences=2, chars=10, auto_suggest=True, redirect=True)
print wikipedia.page(title="Facebook", pageid=None, auto_suggest=True, redirect=True, preload=False)

print wikipedia.geosearch(72.0, 12.0 , title='Facebook', results=10, radius=1000)

wikipage = wikipedia.WikipediaPage(title='Facebook', pageid=None, redirect=True, preload=False, original_title=u'')
print wikipage