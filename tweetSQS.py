#!/usr/bin/env python3

import json
from tweepyStream import TweepyStream
import boto3

# Get the service resource
sqs = boto3.resource('sqs')
# Create/Get the SQS Queue instance
queue = sqs.create_queue(QueueName='test')

trackList = []

def upload_en_tweet_with_geo(json_data):
    meta = json.loads(json_data)
    try:
        if meta["coordinates"] and (meta["lang"] == "en"):

            tweetAttr = {
                "created_at": { # time
                    'StringValue': meta["created_at"],
                    'DataType': 'String'
                },
                "coordinates": {
                    'StringValue': meta["coordinates"].__str__(), # or dump to binary
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
    stream = TweepyStream(upload_en_tweet_with_geo).stream
    trackList = ['concert', 'trip', 'running', 'party']
    print("Enter keywords for tracking followed by a blank line to begin.")
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
