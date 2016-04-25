#from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
from certificate.my_twitter_api import *
"""
WORKING_DIR/certificate/YOUR_API.py
    consumer_key
    consumer_secret
    access_token
    access_token_secret
"""


import signal
import sys


class MyStreamListener(StreamListener):
    """
    A listener handles tweets that are received from the stream.
    """
    count = 0
    upCount = 0

    def __init__(self, parser):
        super().__init__()
        self.parser = parser # defines what to do on data
        self.open_file()

    def open_file(self):
        self.f = open('foo.txt', 'w')
        signal.signal(signal.SIGINT, self.close_handler)

    def close_handler(self, signal, frame):
        print('Close tweets stream!')
        self.f.close()
        sys.exit(0)

    def on_data(self, data):
        if self.parser(data): # parser parses received data
            ## output valid data to file
            #ref: http://stackoverflow.com/questions/2333872/atomic-writing-to-file-with-python
            self.f.write(data)
            self.f.write('\n')
            self.f.flush()
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

    ## use Singleton. Because when
    #   A client establishes too many connections with the same credentials,
    #   , the oldest connection will be terminated.

    def __init__(self, parser, isOutput = True):
        # can insert more arguments to make auth flexible
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        l = MyStreamListener(parser)
        self.stream = Stream(auth, l)
