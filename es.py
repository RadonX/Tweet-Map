#!/usr/bin/env python3

'''
    1. test elasticsearch
    2. import data
'''

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import json
from time import sleep

REMOTE = False
# ----- Init -----
if REMOTE:
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

'''
todo: delete index
query = {"query" : {"exists" : { "field" : "geo" }}}
res = es.search(index='twit3', body=query)
es.get(index='posts', doc_type='blog', id=1)
es.search(index='posts', q='author:"Benjamin Pollack" python')
'''


def import_twits(file_name, index):
    # ref: https://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/
    # if file is large,
    # use [Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/docs-bulk.html)
    fp = open(file_name)
    line = "foobar"
    count = 0
    start = 817
    while True:
        line = fp.readline()
        if not line: break
        if len(line) == 1: continue
        count += 1
        if count < start: continue
        print('line:',len(line))
        meta = json.loads(line[:-1])
        try:
            twitter = {"created_at": meta["created_at"], "text": meta["text"], \
            "user": {"id": meta["user"]["id"], "name": meta["user"]["name"], "location":\
             meta["user"]["location"] }, "geo": meta["geo"], "coordinates": meta["coordinates"],\
             "place": meta["place"] }
            es.index(index = index, doc_type = 'twits', id = meta['id'], body = twitter)
        except Exception as e:
            print(line)
            print(e)
        #sleep(1)
        print('#',count)

import_twits('tweetMessi.json', 'trip, travel, journey')
