#!/usr/bin/env python

from twython import TwythonStreamer
from geopy.geocoders import Nominatim

# normally hide these values, but this is a new account made solely for this
# purpose so security is not a key feature at this point in development
consumer_key = 'VTiKXADVTl6WR1r0d3I28VD4y'
consumer_secret = 'owYftIYKzxdYvSUEdEWkM88emP4SMay61AsXhEnroKRY8NlvsC'
access_token = '786003535733194752-ZA7oCmdpKxVuTWM9yPZGvKwmiRzpkZ9'
access_token_secret = 'YZbwWkV6pRHEfO7dQ8HtOJFw5ZNdy3WV1uCp0r6Kkwma1'

class TweetStreamer(TwythonStreamer):
    def __init__(self, *args, **kwargs):
        super(TweetStreamer, self).__init__(*args, **kwargs)
        self.geo = Nominatim()
    def on_success(self, data):
        # print data
        if 'geo' in data and data['geo']:
            print data['geo']['coordinates'], data['user']['followers_count']
        elif 'user' in data and 'location' in data['user'] and data['user']['location']:
            try:
                loc = self.geo.geocode(data['user']['location'])
            except:
                return
            if loc:
                temp = [loc.latitude, loc.longitude]
                print temp, data['user']['followers_count']

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

if __name__ == '__main__':
    streamer = TweetStreamer(consumer_key, consumer_secret,
                             access_token, access_token_secret)

    streamer.statuses.filter(track = 'clown')