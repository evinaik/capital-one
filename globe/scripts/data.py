#!/usr/bin/env python
import twitter

CONSUMER_KEY = 'VTiKXADVTl6WR1r0d3I28VD4y'
CONSUMER_SECRET = 'owYftIYKzxdYvSUEdEWkM88emP4SMay61AsXhEnroKRY8NlvsC'
ACCESS_KEY = '786003535733194752-ZA7oCmdpKxVuTWM9yPZGvKwmiRzpkZ9'
ACCESS_SECRET = 'YZbwWkV6pRHEfO7dQ8HtOJFw5ZNdy3WV1uCp0r6Kkwma1'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_KEY,
                  access_token_secret=ACCESS_SECRET)
results = api.GetSearch(raw_query="q=%3A)")

print results