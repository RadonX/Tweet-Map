#!/usr/bin/env python3

'''
> python tweetSQS.py

`tweetSQS.py` uses tweepyStream filters Twitter Stream and feeds data to `upload_tweet_with_geo()`,
    which is a handler that uploads qualified tweets to Amazon SQS.
'''

queueName = 'test'


import json
from tweepyStream import TweepyStream
import boto3

# Get the service resource
sqs = boto3.resource('sqs')
# Create/Get the SQS Queue instance
queue = sqs.create_queue(QueueName=queueName)


def upload_tweet_with_geo(json_data):
    meta = json.loads(json_data)
    try:
        if meta["coordinates"]:
            if  (meta["lang"] != "en"):
                print(meta['lang'])
                return False

            tweetAttr = {
                "created_at": { # time
                    'StringValue': meta["created_at"],
                    'DataType': 'String'
                },
                "coordinates": {
                    'StringValue': json.dumps(meta["coordinates"]),
                    'DataType': 'String'
                }, # "place": meta["place"]
                "user_id": {
                    'StringValue': meta["user"]["id"].__str__(),
                    'DataType': 'Number'
                },
                "user_name": {
                    'StringValue': meta["user"]["name"],
                    'DataType': 'String'
                },
                "location": {
                    'StringValue': meta["user"]["location"] or " ",
                    'DataType': 'String'
                },
            }

            queue.send_message(MessageBody= meta["text"], MessageAttributes=tweetAttr)
            print(meta["user"]["name"])

            return True
    except Exception as e:
        print(e)
    return False


if __name__ == "__main__":
    stream = TweepyStream(upload_tweet_with_geo).stream
    trackList = []
    print("Enter keywords for tracking followed by a newline to begin. \
            You will use the default track list if no keyword is entered. ")
    while True:
        keyword = input()
        if keyword == "": break
        trackList.append(keyword)
    if len(trackList) == 0:
        trackList = ['concert', 'trip', 'running', 'party']
    print("Start tracking", trackList)
    #ref: https://dev.twitter.com/streaming/overview/request-parameters
    stream.filter(track = trackList, languages = ['en'])
    """
Hillary Clinton
Bernie Sanders
Donald Trump
Ted Cruz
John Kasich
Gary Johnson
Jill Stein
    """
