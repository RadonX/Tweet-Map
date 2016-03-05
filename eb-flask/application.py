#!/usr/bin/env python
from flask import Flask, jsonify, request, render_template
import sys

INDEX = 'twit3'
from tweetSearch import tweetSearch
tweetsearch = tweetSearch()
tweetsearch.safe_check_index(INDEX)

application = Flask(__name__)

'''
sys.exit(1)
x.strip().lower()
'''

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/search')
def search():
    key = request.args.get('q')
    if not key:
        return jsonify({
            "status": "failure",
            "msg": "Please provide a query"
        })
    return 'search'

@application.route('/alltweet')
def alltweet():
    query = {"query" : {"exists" : { "field" : "geo" }}}
    #query = {"query" : { "match_all": {} }} #4
    result = tweetsearch.query_data(index = INDEX, query = query)
    return jsonify(result)


if __name__ == "__main__":
    application.run(debug=True) # for dev
    #application.run(host='0.0.0.0', port=5000) # for prod
