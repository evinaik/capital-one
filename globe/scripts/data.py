#!/usr/bin/env python
# import twitter

# from TwitterSearch import *
# tweets = []
# kwords = ['obama']
# try:
#     ts = TwitterSearch(
#             consumer_key = 'VTiKXADVTl6WR1r0d3I28VD4y',
#             consumer_secret = 'owYftIYKzxdYvSUEdEWkM88emP4SMay61AsXhEnroKRY8NlvsC',
#             access_token = '786003535733194752-ZA7oCmdpKxVuTWM9yPZGvKwmiRzpkZ9',
#             access_token_secret = 'YZbwWkV6pRHEfO7dQ8HtOJFw5ZNdy3WV1uCp0r6Kkwma1'
#             )
#     abc = '-1'
#     for i in xrange(0, 5):
#         tso = TwitterSearchOrder() # create a TwitterSearchOrder object
#         tso.set_keywords(kwords, True) # let's define all words we would like to have a look for
#         # tso.set_positive_attitude_filter()
#         tso.set_language('en') # we want to see German tweets only
#         tso.set_include_entities(False) # and don't give us all those entity information
#         # tso.set_geocode(180, 90, 10000)
#         if abc != '-1':
#             tso.set_max_id(long(abc))

#         for tweet in ts.search_tweets_iterable(tso):
#             if tweet['geo']:
#                 tweets.append(tweet['geo']['coordinates'])
#                 id = tweet['id']
# except TwitterSearchException as e: # take care of all those ugly errors if there are some
#     print(e)


# for tweet in tweets:
#     print tweet

from twython import TwythonStreamer

class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
        # print data
        if 'geo' in data:
            print data['geo']
        elif 'user' in data and 'location' in data['user']:
            print data['user']['location']

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

consumer_key = 'VTiKXADVTl6WR1r0d3I28VD4y'
consumer_secret = 'owYftIYKzxdYvSUEdEWkM88emP4SMay61AsXhEnroKRY8NlvsC'
access_token = '786003535733194752-ZA7oCmdpKxVuTWM9yPZGvKwmiRzpkZ9'
access_token_secret = 'YZbwWkV6pRHEfO7dQ8HtOJFw5ZNdy3WV1uCp0r6Kkwma1'

streamer = TweetStreamer(consumer_key, consumer_secret,
                         access_token, access_token_secret)

streamer.statuses.filter(track = 'the')