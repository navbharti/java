'''
Created on Nov 10, 2014

@author: rajni
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

'''
consumer_key='gXuFN93StTAOM7ACHn2etV93N',
                      consumer_secret='ieG7APGTgPiznPbUhpoSkpfDQ5gL6UlwTq3pF4q04JQK3RpeqU',
                      access_token_key='262476906-q5sNfau94ywvVsiaYmvh6NabZc4ZGGr9jejnA0tv',
                      access_token_secret='IewghCAhHolgOvBwFnhdAZTT5pDvsFAOqBsIB4fxh0W73'
                      '''

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="gXuFN93StTAOM7ACHn2etV93N"
consumer_secret="ieG7APGTgPiznPbUhpoSkpfDQ5gL6UlwTq3pF4q04JQK3RpeqU"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="262476906-q5sNfau94ywvVsiaYmvh6NabZc4ZGGr9jejnA0tv"
access_token_secret="IewghCAhHolgOvBwFnhdAZTT5pDvsFAOqBsIB4fxh0W73"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])

