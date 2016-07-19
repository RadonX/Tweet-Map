This repository includes two course assignment of mine. The twitter streaming part is under the root directory and is shared between both assignment. `eb-flask` is a Flask application for assignment one, and `eb-rails` is an RoR application for assignment two. 

Check [Cloud Computing | Trello](https://trello.com/b/3ggCBiei/cloud-computing) for more resources regarding the assignments. 

#### Assignment 1 - Tweet Map

The goal of this assignment is to provide you experience in developing and deploying a web application using AWS Cloud services. Your web application would collect Twitts and do some processing and represent the Twitts on GoogleMaps. Following are the required steps:  

1. Use [Twitter Streaming API](https://dev.twitter.com/streaming/overview) to fetch tweets from the twitter hose in real-time.

2. Use [ElasticSearch](https://www.elastic.co/products/elasticsearch)([elastic/elasticsearch: Open Source, Distributed, RESTful Search Engine](https://github.com/elastic/elasticsearch)) or [AWS CloudSearch](https://aws.amazon.com/cloudsearch/) to store the tweets on the backend

3. Create a web UI that allows users to search for a few keywords (via a dropdown). The keywords (up to 10) can be of your choosing.

3. Use [Google Maps API](https://developers.google.com/maps/documentation/javascript/) to render these filtered tweets in the map in whatever manner you want.

4. Deploy your application on [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) in an auto-scaling environment.


#### Assignment 2 - SQS and SNS

- Use the [Amazon SQS service](https://aws.amazon.com/sqs/) to create a processing queue for the Tweets that are delivered by the Twitter Streaming API. 
- Use [Amazon SNS service](https://aws.amazon.com/sns/) to update the status processing on each tweet so the UI can refresh.
- Integrate a third party cloud service API into the Tweet processing flow.

- Architecture Diagram
 ![](http://i.imgur.com/ouIDUJT.png)
