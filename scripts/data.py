#!/usr/bin/env python

from twython import TwythonStreamer
from geopy.geocoders import Nominatim
from senti_classifier import senti_classifier
from time import sleep
import numpy
import datetime
import nltk
import json

nltk.data.path.append('../nltk_data/')

# normally hide these values, but this is a new account made solely for this
# purpose so security is not a key feature at this point in development
consumer_key = 'wOq8bUAoKkgDTC0XHOQvU0eY1'
consumer_secret = 'Pc9zJokOo9ciyDpSpwbicqYQhIySTyzZJ76JY2euByogLXLWPF'
access_token = '786003535733194752-wFxrt7OD1sCbba0Y3mtLsZcZmHqaRGR'
access_token_secret = '7tuK1HM0gxe8LrGjJRPMUPFqZjfJif32ekXAemOjMODVP'
sleepTime = 5

class TweetStreamer(TwythonStreamer):

    clownData = []
    trumpData = []
    clintonData = []

    def __init__(self, *args, **kwargs):
        super(TweetStreamer, self).__init__(*args, **kwargs)
        self.geo = Nominatim()
    def on_success(self, data):
        if 'geo' in data and data['geo']:
            self.write(data['geo']['coordinates'][0], data['geo']['coordinates'][0], data['user']['followers_count'], data['text'])
        elif 'user' in data and 'location' in data['user'] and data['user']['location']:
            try:
                loc = self.geo.geocode(data['user']['location'])
            except:
                return
            if loc:
                self.write(loc.latitude, loc.longitude, data['user']['followers_count'], data['text'])

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

    def write(self, lat, lon, size, text):
        self.sendToList(lat, lon, size, text, ['clinton' in text.lower() or 'hillary' in text.lower(), 'trump' in text.lower() or 'donald' in text.lower()])
        temp = json.dumps(self.sendToFile())
        with open('../data.json', 'w+') as f:
            f.write(temp)

    def sendToList(self, lat, lon, size, text, word):
        pos_score, neg_score = senti_classifier.polarity_scores([text])
        temp = [lat, lon, size, 1 if pos_score >= neg_score else 0, datetime.datetime.now()]
        if word[0]:
            self.clintonData.extend(temp)
        if word[1]:
            self.trumpData.extend(temp)
        if word[0] is not word[1]:
            n = [0, 0, 0, 0, temp[4]]
            if word[0]:
                self.clintonData.extend(n)
            else:
                self.trumpData.extend(n)

    def sendToFile(self):
        curr = datetime.datetime.now()
        temp = [[], []]

        self.appendData(temp[0], self.clintonData, curr, 'clinton')
        self.appendData(temp[1], self.trumpData, curr, 'trump')

        return temp

    def appendData(self, l, d, c, name):
        while len(d) > 4 and (c - d[4]).total_seconds() >= 600:
            d = d[5:]
        l.append(name)
        l.append([])
        if not d:
            return
        tr = [d[i + 2] for i in xrange(0, len(d), 5)]
        iqr = numpy.subtract(*numpy.percentile(numpy.array(tr), [75, 25]))
        med = numpy.median(iqr)
        tr = [i for i in tr if i > med - iqr and i < med + iqr]
        if not tr:
            return
        r = max(tr) - min(tr)
        if r == 0:
            r = 1
        for i in xrange(0, len(d), 5):
            size = float(d[i + 2] - min(tr))/ r
            if size > 1:
                size = 1
            l[1].extend([d[i], d[i + 1], size, d[i + 3]])

def call(streamer):
    try:
        streamer.statuses.filter(track = 'trump,clinton,donald trump,hillary clinton')
    except:
        for i in xrange(0, sleepTime):
            print sleepTime - i
            sleep(1)
        call(TweetStreamer(consumer_key, consumer_secret,
                                 access_token, access_token_secret))

if __name__ == '__main__':
    streamer = TweetStreamer(consumer_key, consumer_secret,
                                 access_token, access_token_secret)
    call(streamer)