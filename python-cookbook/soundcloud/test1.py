'''
Created on Nov 7, 2014

@author: rajni
'''
import soundcloud

client = soundcloud.Client(client_id = 'b0d5791113277104bcdcd445b15df6c5' )
tracks = client.get('/tracks', limit = 15)
#for track in tracks:
    #print track.id, "\t", track.created_at, "\t", track.user_id, "\t", track.user['username'], "\t", track.title, "\t", track.permalink, "\t", track.permalink_url, "\t", track.uri
    #users = track.user
    #for user in users:
    #   print user
    #print track.id
    #print track.id
    #print track.created_at
    #print track.user_id
    #print track.user['username']
    #print track.title
    #print track.permalink
    #print track.permalink_url
    #print track.uri
    #print track.sharing
    #print track.embeddable_by
    #print track.purchase_url
    #print track.artwork_url
    #print track.label['username']
    #print track.duration
    #print track.genre
    #print track.tag_list
    #print track.id

users = client.get('/users')
for user in users:
    print user.id, "\t", user.country, "\t", user.city, "\t", user.online
 
#connections = client.get('/connect')
#for connection in connections:
    #print connection.client_id, "\t", connection.redirect_uri, "\t", connection.response_type, "\t", connection.scope, "\t", connection.display, "\t", connection.state 
    #print connection.client_id