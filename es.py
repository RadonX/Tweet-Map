#!/usr/bin/env python3

'''
    1. test elasticsearch
        > python3 -i es.py
    2. import data
        > python3 es.py -s 1 -n 500 -f 'place.json' -i 'place'
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

def import_twits(file_name, index, start, nrecord):
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
        if len(line) == 1: continue
        count += 1
        print('#%d (%d)' %(count,num) )
        if count < start: continue
        print('line:',len(line))
        meta = json.loads(line[:-1])
        try:
            # since the proportion of data with 'geo' is small, 1%
            # and this web app only cares about this field
            if meta["geo"]:
                twitter = {"created_at": meta["created_at"], "text": meta["text"], \
                "user": {"id": meta["user"]["id"], "name": meta["user"]["name"], "location":\
                 meta["user"]["location"] }, "geo": meta["geo"], "coordinates": meta["coordinates"],\
                 "place": meta["place"] }
                es.index(index = index, doc_type = 'twits', id = meta['id'], body = twitter)
                num += 1
                if num == nrecord: break
        except Exception as e:
            print(line)
            print(e)
        #sleep(1)


if __name__ == "__main__":
    if opt.start > 0:
        import_twits(opt.filename, opt.index, opt.start, opt.nrecord)
