#!/usr/bin/env python 

import pprint

import argparse

import requests, json
from requests_oauthlib import OAuth1

from jamie_keys import consumer_key, consumer_secret, access_token, access_token_secret 

def go(addr):

  oauth = OAuth1(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
  j = requests.get(url=addr, auth=oauth).json()

  print(pprint.pformat(j))
  return j


if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument('address')
  print(parser.parse_args().address)
  go(parser.parse_args().address)


