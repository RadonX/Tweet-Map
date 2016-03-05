#!/usr/bin/env python3
from elasticsearch import Elasticsearch, exceptions
from time import sleep

from setting import *
#es = Elasticsearch(host=HOST)
es = Elasticsearch()

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('log_tweetSearch.txt')
#fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
logger.addHandler(fh)
logger.addHandler(ch)

'''
def test_es():
    resp = {}
    try:
        msg = es.cat.indices()
        resp["msg"] = msg
        resp["status"] = "success"
    except:
        resp["status"] = "failure"
        resp["msg"] = "Unable to reach ES"
    #return jsonify(resp)

res = es.search(
        index="sfdata",
        body={
            "query": {"match": {"fooditems": key}},
            "size": 750 # max document size
      })

'''

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
        #vendors = set([x["_source"]["applicant"] for x in hits)


    def parse_coord_data(self, srclist):
        coord = {"geo": []}
        for src in srclist:
            try:
                coord['geo'].append(src['_source']['coordinates'])#['coordinates'])
                #~ ['geo']
            except Exception as e:
                #print(e)
                continue
        return coord

    # --------------------------
    def load_data_in_es(self):
        """ creates an index in elasticsearch """
        #r = requests.get(url)
        data = r.json()
        for id, truck in enumerate(data):
            res = es.index(index="sfdata", doc_type="truck", id=id, body=truck)
        print("Total trucks loaded: ", len(data) )
