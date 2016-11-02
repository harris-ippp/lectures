#!/usr/bin/env python 

import requests, json
from requests_oauthlib import OAuth1, OAuth1Session

from jamie_keys import consumer_key, consumer_secret, access_token, access_token_secret 

osess = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

stream = osess.get("https://stream.twitter.com/1.1/statuses/filter.json?track=Clinton,Trump", stream=True)
for line in stream.iter_lines():
  if line: 

    j = json.loads(line.decode("utf-8"))

    if 'user' in j and 'text' in j:
      loc = "None"
      if j['place']: 
        loc = j['place']['full_name']
      elif j['user']['location']: 
        loc = j['user']['location']

      print("{:30}\t{:30}\t{}".format(j['user']['name'], loc, j['text'].replace("\n", " // ")))

