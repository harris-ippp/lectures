#!/usr/bin/env python 

import requests

url = 'http://geocoding.geo.census.gov/geocoder/geographies/addressbatch'
payload = {'benchmark':'Public_AR_Current','vintage':'ACS2013_Current', 'format':'json'}
files = {'addressFile': ('short.csv', open('short.csv', 'rb'), 'text/csv')}
r = requests.post(url, files=files, data = payload)
print(r.text)

