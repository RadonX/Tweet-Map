#!/usr/bin/env python
from flask import Flask, jsonify, request, render_template
import sys

INDEX = 'place'
from tweetSearch import tweetSearch
tweetsearch = tweetSearch()
tweetsearch.safe_check_index(INDEX)

application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html', field = '_all')

@application.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if not keyword:
        keyword = '_all'
    return render_template('index.html', field = keyword)

@application.route('/json', methods=['GET'])
def json():
    keyword = request.args.get('keyword')
    if (keyword == '_all') or (not keyword):
        #query = {"query": {"exists": {"field": "geo"}}, "size": 500}
        query = {"query": {"match_all": {}}, "size": 500}
    else:
        query = {"query": {"match_phrase": {"text": keyword}}, "size": 500}
    result = tweetsearch.query_data(index = INDEX, query = query)
    return jsonify(result)


if __name__ == "__main__":
    application.run(debug=True) # for dev
    #application.run(host='0.0.0.0', port=5000) # for prod
