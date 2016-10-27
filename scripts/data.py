#!/usr/bin/env python

from twython import TwythonStreamer
from geopy.geocoders import Nominatim
from senti_classifier import senti_classifier
from time import sleep
import datetime
import nltk

nltk.data.path.append('../nltk_data/')

# normally hide these values, but this is a new account made solely for this
# purpose so security is not a key feature at this point in development
consumer_key = 'wOq8bUAoKkgDTC0XHOQvU0eY1'
consumer_secret = 'Pc9zJokOo9ciyDpSpwbicqYQhIySTyzZJ76JY2euByogLXLWPF'
access_token = '786003535733194752-wFxrt7OD1sCbba0Y3mtLsZcZmHqaRGR'
access_token_secret = '7tuK1HM0gxe8LrGjJRPMUPFqZjfJif32ekXAemOjMODVP'
sleepTime = 5

class TweetStreamer(TwythonStreamer):

    allData = []

    def __init__(self, *args, **kwargs):
        super(TweetStreamer, self).__init__(*args, **kwargs)
        self.geo = Nominatim()
    def on_success(self, data):
        if 'geo' in data and data['geo']:
            self.write(str(data['geo']['coordinates'][0]), str(data['geo']['coordinates'][0]), data['user']['followers_count'], data['text'])
        elif 'user' in data and 'location' in data['user'] and data['user']['location']:
            try:
                loc = self.geo.geocode(data['user']['location'])
            except:
                return
            if loc:
                self.write(str(loc.latitude), str(loc.longitude), data['user']['followers_count'], data['text'])

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

    def write(self, lat, lon, size, text):
        pos_score, neg_score = senti_classifier.polarity_scores([text])
        self.allData.extend([lat, lon, size/(size+5000.0), 1 if pos_score >= neg_score else 0, datetime.datetime.now()])
        temp = ''
        curr = datetime.datetime.now()
        while len(self.allData) > 4 and (curr - self.allData[4]).total_seconds() >= 600:
            self.allData = self.allData[5:]
        for i in self.allData:
            if not isinstance(i, datetime.datetime):
                temp += str(i) + ","
        with open('../data/clowns.txt', 'w+') as f:
            f.write(temp)

def call(streamer):
    try:
        streamer = TweetStreamer(consumer_key, consumer_secret,
                                 access_token, access_token_secret)
        streamer.statuses.filter(track = 'clown,trump,clinton')
    except:
        print TweetStreamer.allData
        print 'Sleeping for ' + str(sleepTime) + ' seconds'
        for i in xrange(0, sleepTime, 5):
            sleep(5)
            print str(i + 5) + '...'
        call(streamer)

if __name__ == '__main__':
    streamer = TweetStreamer(consumer_key, consumer_secret,
                                 access_token, access_token_secret)
    call(streamer)