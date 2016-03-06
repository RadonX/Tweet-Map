#!/usr/bin/env python3
from elasticsearch import Elasticsearch, exceptions, RequestsHttpConnection
from time import sleep

from setting import *
from requests_aws4auth import AWS4Auth
REGION = "us-east-1"
awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')
es = Elasticsearch(
    hosts=[{'host': HOST, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
#es = Elasticsearch()

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.DEBUG)
#ch = logging.StreamHandler()
logger.addHandler(fh)
#logger.addHandler(ch)


class tweetSearch(object):
    """docstring for tweetSearch"""

    def __init__(self):
        pass

    def safe_check_index(self, index, retry=3):
        """ connect to ES with retry """
        while retry > 0:
            retry -= 1
            try:
                status = es.indices.exists(index)
                return status
            except exceptions.ConnectionError as e:
                print("Unable to connect to ES. Retying in 5 secs...")
                sleep(5)

    def query_data(self, index, query, datatype = 1):
        if not self.safe_check_index(index):
            print("Index not found...")
        esdata = es.search(index = index, body = query)
        # es.get(index='posts', doc_type='blog', id=1)
        # es.search(index='posts', q='author:"Benjamin Pollack" python')
        logger.debug(str(esdata))
        try:
            hits = esdata['hits']['hits']
            print('fetch', len(hits), 'hits' )
        except Exception:
            print("there is no hits")

        # ----- 1: get coordinates -----
        if datatype == 1: #~~
            return self.parse_coord_data(hits)

        #exp
        # filtering results
        #res = set(x["_source"]["key"] for x in hits)


    def parse_coord_data(self, srclist):
        coord = {"geo": []}
        for src in srclist:
            try:
                coord['geo'].append(src['_source']['coordinates'])#['coordinates'])
            except Exception as e:
                #print(e)
                continue
        return coord
