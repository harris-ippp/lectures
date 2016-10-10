#!/usr/bin/env python 

import requests, json, pprint

# retrieving from the internet
# we'll cover this in a few weeks.
response = requests.get("http://plenar.io/v1/api/detail/?dataset_name=crimes_2001_to_present&obs_date__ge=2016-5-1&crimes_2001_to_present__filter={%22op%22:%20%22eq%22,%20%22col%22:%20%22primary_type%22,%20%22val%22:%20%22NARCOTICS%22}")
j = response.json()

# writing to a file
with open("narcotics.json", "w") as out: out.write(json.dumps(j, indent=2, sort_keys=True))

# reading from a file
with open("narcotics.json") as data: narcotics = json.load(data)

pprint.pprint(narcotics)

