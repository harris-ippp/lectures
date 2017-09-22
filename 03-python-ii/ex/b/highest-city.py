#!/usr/bin/env python

import json

with open("elevations.json") as f: elevations = json.load(f)
with open("locations.json") as f:  locations = json.load(f)
    
elev = 0
lat, lon = 0, 0
mile_high = 0
for x in elevations["results"]:

    if x["elevation"] > 1609.344: mile_high += 1

    if x["elevation"] < elev: continue
    
    elev = x["elevation"]
    lat, lon = x["location"]["lat"], x["location"]["lng"]

for x in locations:
    if abs(x["results"][0]["geometry"]["location"]["lat"] - lat) < 0.01 and \
       abs(x["results"][0]["geometry"]["location"]["lng"] - lon) < 0.01:
        print(x["results"][0]["formatted_address"], elev)

print("mile high:", mile_high)

