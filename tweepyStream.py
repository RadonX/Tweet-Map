#from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from certificate.my_twitter_api import *
"""
WORKING_DIR/certificate/YOUR_API.py
    consumer_key
    consumer_secret
    access_token
    access_token_secret
"""


class MyStreamListener(StreamListener):
    """
    A listener handles tweets that are received from the stream.
    """
    count = 0
    upCount = 0

    def __init__(self, parser):
        super().__init__()
        self.parser = parser # defines what to do on data

    def on_data(self, data):
        if self.parser(data): # push valid data to ES
            self.upCount += 1
            if self.upCount % 10 == 0:
                print(str(self.count) + "(" + str(self.upCount) +")")
        self.count += 1
        return True

    def on_error(self, status):
        print('on_error')
        print(status)


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python2
#class MyClass(BaseClass):
#    __metaclass__ = Singleton

#Python3
class TweepyStream(metaclass=Singleton):

    # use Singleton because every auth can start only one stream.

    def __init__(self, parser):
        # can insert more arguments to make auth flexible
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        l = MyStreamListener(parser)
        self.stream = Stream(auth, l)


