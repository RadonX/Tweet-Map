#!/usr/bin/env python3

'''
Usage:
> python worker.py
'''
arn = 'arn:aws:sns:us-east-1:664206762806:entertainment'
queueName = 'test'
NEW_THREAD_INTERVAL = 10
WORKING_INTERVAL = 15

from time import sleep


import boto3
import json
from alchemyapi import AlchemyAPI
from certificate.my_api_key import *

sqs = boto3.resource('sqs')
# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName=queueName)
alchemyapi = AlchemyAPI(alchemy_api_key)
sns = boto3.resource('sns')
platform_endpoint = sns.PlatformEndpoint(arn)
count = 0

def parse_tweet():
    global queue, platform_endpoint, alchemyapi, count, WORKING_INTERVAL

    count += 1
    print(count)

    sleep(WORKING_INTERVAL)

    for message in queue.receive_messages(MessageAttributeNames=['All'], VisibilityTimeout=30, MaxNumberOfMessages=1):
        if message.message_attributes is not None:
            snsMsg = {}
            ## geo
            coordinates = message.message_attributes.get('coordinates').get('StringValue')
            if coordinates:
                snsMsg['geo'] = json.loads(coordinates.replace("'",'"'))
                # {'coordinates': [-83.0247498, 40.0194511], 'type': 'Point'}

                ## sentiment
                response = alchemyapi.sentiment("text", message.body)
                if response['status'] == 'OK':
                    sentimentResult = response["docSentiment"]
                    '''
                    {
                        ["score": "DOCUMENT_SENTIMENT",]
                        ["mixed": "SENTIMENT_MIXED",]
                        "type": "SENTIMENT_LABEL",
                    }
                    '''
                    snsMsg['sentiment'] = sentimentResult
                    snsMsg['tweet'] = message.body
                    snsMsg['user'] = message.message_attributes.get('user_name').get('StringValue')

                    ## dump snsMsg and send message to SNS
                    snsMessage = json.dumps(snsMsg)
                    response = platform_endpoint.publish(
                        Message=snsMessage,
                        Subject='Tweet'
                    )
                    #print(snsMessage)
                    '''
                    {
                        "sentiment": {"score": "0.303898", "type": "positive"},
                        "tweet": "neck deep was so awesome\n#neckdeep #poppunk #concert #zurich #werk21 #dynamo #music #live @\u2026 https://t.co/29kt7MiqOG",
                        "geo": {"coordinates": [8.5396694, 47.3831786], "type": "Point"},
                        "user": "Marco Studer"}
                    '''
                else:
                    print('Error in sentiment analysis call: ', response['statusInfo'])

        # Let the queue know that the message is processed
        message.delete()



from concurrent.futures import ThreadPoolExecutor

def main():
    executor = ThreadPoolExecutor(max_workers=10)
    while True:
        executor.submit(parse_tweet)
        sleep(NEW_THREAD_INTERVAL)

if __name__ == '__main__':
    main()
