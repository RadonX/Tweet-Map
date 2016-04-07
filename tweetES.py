#!/usr/bin/env python3

'''
    1. test ElasticSearch
        open command line that connects to [-r remote] ES
        > python3 -i es.py -r
    2. upload data to ES
        upload [-n nrecord] qualified tweets from [-f filename]
        starting from line [-s start] to ElasticSearch with [-i index]
        > python3 es.py -s 1 -n 500 -f 'place.json' -i 'place'
    3. upload newly fetched data from Twitter
        > python3 es.py -r -i 'place'
'''

from elasticsearch import Elasticsearch, RequestsHttpConnection
import json
from time import sleep

# ----- option -----
import optparse
parser = optparse.OptionParser()
parser.add_option('-r', action='store_true', dest='remote')
parser.add_option('-s', action='store', type='int', dest='start')
parser.add_option('-n', action='store', type='int', dest='nrecord')
parser.add_option('-f', action='store', type='string', dest='filename')
parser.add_option('-i', action='store', type='string', dest='index')
parser.set_default('start', -1) # fetch from Twitter
parser.set_default('nrecord',5000)
opt, args = parser.parse_args()


# ----- Init: connect to ElasticSearch -----

if opt.remote:
    from requests_aws4auth import AWS4Auth
    from certificate.my_AWS_key import * # WORKING_DIR/certificate/YOUR_KEY.py
    REGION = "us-east-1"
    host = 'search-my-es-cluster-3do6mfjfb7daoy7y7xe2n2ly7u.us-east-1.es.amazonaws.com'

    awsauth = AWS4Auth(aws_access_key_id, aws_secret_access_key, REGION, 'es')
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

# -------- end of Init ----------


def upload_tweet_with_geo(json_data):
    meta = json.loads(json_data)
    try:
        if meta["geo"]:
            twitter = {"created_at": meta["created_at"], "text": meta["text"], \
            "user": {"id": meta["user"]["id"], "name": meta["user"]["name"], "location":\
             meta["user"]["location"] }, "geo": meta["geo"], "coordinates": meta["coordinates"],\
             "place": meta["place"] }
            es.index(index = opt.index, doc_type = 'twits', id = meta['id'], body = twitter)
            return True
    except Exception as e:
        print(e, meta)
    return False


def upload_tweet_file(file_name, start, nrecord):
    '''
        upload tweets in local file to ElasticSearch
    '''
    fp = open(file_name)
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

        if upload_tweet_with_geo(line[:-1]):
            num += 1
            if num == nrecord: break
        #sleep(1)



if __name__ == "__main__":
    if opt.start > 0:
        upload_tweet_file(opt.filename, opt.start, opt.nrecord)
    elif opt.start == -1:
        from tweepyStream import TweepyStream
        stream = TweepyStream(upload_tweet_with_geo).stream
        trackList = ['concert', 'trip', 'running', 'party']
        print("Enter keywords to track followed by a blank line.")
        while True:
            keyword = input()
            if keyword == "": break
            trackList.append(keyword)
        print("Start tracking", trackList)
        stream.filter(track = trackList)
        """
Hillary Clinton
Bernie Sanders
Donald Trump
Ted Cruz
John Kasich
Gary Johnson
Jill Stein
        """

