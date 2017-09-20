#!/usr/bin/env python

import json

with open('salaries.json') as json_data:
  d = json.load(json_data)
  print(d)


