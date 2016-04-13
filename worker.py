#!/usr/bin/env python3

import boto3
from time import sleep
import json
from alchemyapi import AlchemyAPI
from certificate.my_api_key import *

sqs = boto3.resource('sqs')
# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')
alchemyapi = AlchemyAPI(alchemy_api_key)

for message in queue.receive_messages(MessageAttributeNames=['All'], VisibilityTimeout=30, MaxNumberOfMessages=5):
    #sleep(1)

    print(message.body)
    response = alchemyapi.sentiment("text", message.body)
    if response['status'] == 'OK':
        result = response["docSentiment"]
        '''
        "docSentiment": {
            "type": "SENTIMENT_LABEL",
            "score": "DOCUMENT_SENTIMENT",
            "mixed": "SENTIMENT_MIXED"
        }
        '''
        print(json.dumps(result, indent=4))
        #if 'score' in response['docSentiment']:
    else:
        print('Error in sentiment analysis call: ', response['statusInfo'])

    if message.message_attributes is not None:
        geoinfo = message.message_attributes.get('coordinates').get('StringValue') or ''
        print(geoinfo)

    # Let the queue know that the message is processed
    # message.delete()
