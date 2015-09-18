'''
Created on Nov 9, 2014

@author: rajni
'''
import soundcloud

# create a client object with access token
client = soundcloud.Client(access_token='https://api.soundcloud.com/oauth2/token')

# print out the user's username
print client.get('/me').username

# update the user's profile description
user = client.post('/me', description='I am using the SoundCloud API!')
print user.description