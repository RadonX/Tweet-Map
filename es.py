#!/usr/bin/env python3

'''
    1. test ElasticSearch
        open command line that connects to [-r remote] ES
        > python3 -i es.py -r
    2. upload data to ES
        upload [-n nrecord] qualified tweets from [-f filename]
        starting from line [-s] to ElasticSearch with [-i index]
        > python3 es.py -s 1 -n 500 -f 'place.json' -i 'place'
    3. upload newly fetched data from Twitter
        > python3 es.py -s -r -1 -i 'place_'
'''

from elasticsearch import Elasticsearch, RequestsHttpConnection
import json
from time import sleep

# ----- opt -----
import optparse
parser = optparse.OptionParser()
parser.add_option('-r', action='store_true', dest='remote')
parser.add_option('-s', action='store', type='int', dest='start')
parser.add_option('-n', action='store', type='int', dest='nrecord')
parser.add_option('-f', action='store', type='string', dest='filename')
parser.add_option('-i', action='store', type='string', dest='index')
parser.set_default('start', 0)
parser.set_default('nrecord',5000)
opt, args = parser.parse_args()

# ----- Init: BEGIN -----
if opt.remote:
    from requests_aws4auth import AWS4Auth
    from certificate.my_AWS_key import * # WORKING_DIR/certificate/YOUR_KEY.py
    REGION = "us-east-1"
    host = 'search-my-es-cluster-3do6mfjfb7daoy7y7xe2n2ly7u.us-east-1.es.amazonaws.com'

    awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')
    es = Elasticsearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    #print(es.info())
else:
    es = Elasticsearch()

# es.indices.delete(index = opt.index)
# ----- Init: END -----

def parse_json(json_data):
    meta = json.loads(json_data)
    try:
        # since the proportion of data with 'geo' is small, 1%
        # and this web app only cares about this field
        if meta["geo"]:
            twitter = {"created_at": meta["created_at"], "text": meta["text"], \
            "user": {"id": meta["user"]["id"], "name": meta["user"]["name"], "location":\
             meta["user"]["location"] }, "geo": meta["geo"], "coordinates": meta["coordinates"],\
             "place": meta["place"] }
            es.index(index = opt.index, doc_type = 'twits', id = meta['id'], body = twitter)
            return True

    except Exception as e:
        print('parse_json')
        print(meta)
        print(e)

    return False


def import_twits(file_name, start, nrecord):
    # ref: https://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/
    # if file is large,
    # use [Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/docs-bulk.html)
    fp = open(file_name)
    line = "foobar"
    count = 0
    num = 0
    while True:
        line = fp.readline()
        if not line: break
        if len(line) == 1: continue #"\n"
        count += 1
        print('#%d (%d)' %(count,num) )
        if count < start: continue
        print('line:',len(line))

        if parse_json(line[:-1]):
            num += 1
            if num == nrecord: break
        #sleep(1)


#from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from certificate.my_twitter_api import * # WORKING_DIR/certificate/YOUR_API.py

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    count = 0
    upCount = 0
    def on_data(self, data):
        if parse_json(data):
            self.upCount += 1
            if self.upCount % 10 == 0:
                print(str(self.count) + "(" + str(self.upCount) +")")
        self.count += 1
        return True

    def on_error(self, status):
        print('on_error')
        print(status)


if __name__ == "__main__":
    if opt.start > 0:
        import_twits(opt.filename, opt.start, opt.nrecord)
    elif opt.start == -1:
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=['concert','trip','running','party'])


