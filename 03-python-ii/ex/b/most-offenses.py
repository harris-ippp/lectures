#!/usr/bin/env python 

import json

with open("narcotics.json") as data: narcotics = json.load(data)
offenses = {x['description'] for x in narcotics['objects']}

for o in offenses: 
  print(len([i for i in narcotics['objects'] if i['description'] == o]), o)
