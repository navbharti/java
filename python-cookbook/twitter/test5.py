'''
Created on Nov 10, 2014

@author: rajni
'''
import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY='gXuFN93StTAOM7ACHn2etV93N',
CONSUMER_SECRET='ieG7APGTgPiznPbUhpoSkpfDQ5gL6UlwTq3pF4q04JQK3RpeqU',
OAUTH_TOKEN='262476906-q5sNfau94ywvVsiaYmvh6NabZc4ZGGr9jejnA0tv',
OAUTH_TOKEN_SECRET='IewghCAhHolgOvBwFnhdAZTT5pDvsFAOqBsIB4fxh0W73'


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print twitter_api