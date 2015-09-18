'''
Created on Nov 9, 2014

@author: rajni
'''
import soundcloud

# create client object with app and user credentials
client = soundcloud.Client(client_id='b0d5791113277104bcdcd445b15df6c5',
                           client_secret='43849b5d768bc76154cf5e23ab1c1ae9',
                           username='navbharti',
                           password='soundcloud123#')

# print authenticated user's username
print "id: ", client.get('/me').id
print "permalink: ", client.get('/me').permalink
print "username: ", client.get('/me').username
print "uri: ", client.get('/me').uri
print "avatar_url: ", client.get('/me').avatar_url
print "country: ", client.get('/me').country
print "full_name: ", client.get('/me').full_name
print "city: ", client.get('/me').city
print "description: ", client.get('/me').description
print "discogs_name: ", client.get('/me').discogs_name
print "myspace_name: ", client.get('/me').myspace_name
print "website: ", client.get('/me').website
print "website_title: ", client.get('/me').website_title
print "online: ", client.get('/me').online
print "track_count: ", client.get('/me').track_count
print "playlist_count: ", client.get('/me').playlist_count
print "followers_count: ", client.get('/me').followers_count
print "followings_count: ", client.get('/me').followings_count
print "public_favorites_count: ", client.get('/me').public_favorites_count
print "plan: ", client.get('/me').plan
print "private_tracks_count: ", client.get('/me').private_tracks_count
print "private_playlists_count: ", client.get('/me').private_playlists_count
print "primary_email_confirmed: ", client.get('/me').primary_email_confirmed
'''
{
  "id": 3207,
  "permalink": "jwagener",
  "username": "Johannes Wagener",
  "uri": "https://api.soundcloud.com/users/3207",
  "permalink_url": "http://soundcloud.com/jwagener",
  "avatar_url": "http://i1.sndcdn.com/avatars-000001552142-pbw8yd-large.jpg?142a848",
  "country": "Germany",
  "full_name": "Johannes Wagener",
  "city": "Berlin",
  "description": "<b>Hacker at SoundCloud</b>\r\n\r\nSome of my recent Hacks:\r\n\r\nsoundiverse.com \r\nbrowse recordings with the FiRe app by artwork\r\n\r\ntopbillin.com \r\nfind people to follow on SoundCloud\r\n\r\nchatter.fm \r\nget your account hooked up with a voicebox\r\n\r\nrecbutton.com \r\nrecord straight to your soundcloud account",
  "discogs_name": null,
  "myspace_name": null,
  "website": "http://johannes.wagener.cc",
  "website_title": "johannes.wagener.cc",
  "online": true,
  "track_count": 12,
  "playlist_count": 1,
  "followers_count": 416,
  "followings_count": 174,
  "public_favorites_count": 26,
  "plan": "Pro Plus",
  "private_tracks_count": 63,
  "private_playlists_count": 3,
  "primary_email_confirmed": true
}
'''