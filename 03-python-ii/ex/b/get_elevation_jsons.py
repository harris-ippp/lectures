#!/usr/bin/env python 

import json, requests

from pprint import pprint

from netrc import netrc
_, _, loc_passwd = netrc().authenticators("google-location")
_, _, ele_passwd = netrc().authenticators("google-elevation")

loc_query = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=" + loc_passwd
ele_query = "https://maps.googleapis.com/maps/api/elevation/json?locations={}&key=" + ele_passwd

cities = ["New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Phoenix, AZ", "Philadelphia, PA", "San Antonio, TX", "San Diego, CA", "Dallas, TX", "San Jose, CA", "Austin, TX", "Jacksonville, FL", "San Francisco, CA", "Columbus, OH", "Indianapolis, IN", "Fort Worth, TX", "Charlotte, NC", "Seattle, WA", "Denver, CO", "El Paso, TX", "Washington, DC", "Boston, MA", "Detroit, MI", "Nashville, TN", "Memphis, TN", "Portland, OR", "Oklahoma City, OK", "Las Vegas, NV", "Louisville, KY", "Baltimore, MD", "Milwaukee, WI", "Albuquerque, NM", "Tucson, AZ", "Fresno, CA", "Sacramento, CA", "Mesa, AZ", "Kansas City, MO", "Atlanta, GA", "Long Beach, CA", "CO Springs, CO", "Raleigh, NC", "Miami, FL", "VA Beach, VA", "Omaha, NE", "Oakland, CA", "Minneapolis, MN", "Tulsa, OK", "Arlington, TX", "New Orleans, LA", "Wichita, KS", "Cleveland, OH", "Tampa, FL", "Bakersfield, CA", "Aurora, CO", "Honolulu, HI", "Anaheim, CA", "Santa Ana, CA", "Corpus Christi, TX", "Riverside, CA", "Lexington, KY", "St. Louis, MO", "Stockton, CA", "Pittsburgh, PA", "Saint Paul, MN", "Cincinnati, OH", "Anchorage, AK", "Henderson, NV", "Greensboro, NC", "Plano, TX", "Newark, NJ", "Lincoln, NE", "Toledo, OH", "Orlando, FL", "Chula Vista, CA", "Irvine, CA", "Fort Wayne, IN", "Jersey City, NJ", "Durham, NC", "St. Petersburg, FL", "Laredo, TX", "Buffalo, NY", "Madison, WI", "Lubbock, TX", "Chandler, AZ", "Scottsdale, AZ", "Glendale, AZ", "Reno, NV", "Norfolk, VA", "Winston–Salem, NC", "North Las Vegas, NV", "Irving, TX", "Chesapeake, VA", "Gilbert, AZ", "Hialeah, FL", "Garland, TX", "Fremont, CA", "Baton Rouge, LA", "Richmond, VA", "Boise, ID", "San Bernardino, CA"]
cities = []

locations = []
for c in cities:
    print(c)
    resp = requests.get(loc_query.format(c))
    print(resp.json())
    locations.append(resp.json())

if locations:
    with open('locations.json', 'w') as outfile:
        json.dump(locations, outfile, indent = 2)

with open("locations.json") as f: locations = json.load(f)
pprint(locations)

points = "|".join(["{}".format(l["status"]) for l in locations])
print(points)

points = "|".join(["{0[lat]},{0[lng]}".format(l["results"][0]["geometry"]["location"]) for l in locations])
print(ele_query.format(points))
resp = requests.get(ele_query.format(points))
with open('elevations.json', 'w') as outfile: json.dump(resp.json(), outfile, indent = 2)

with open("elevations.json") as f: elevations = json.load(f)

with open("locations.json") as f: locations = json.load(f)

pprint(locations)
pprint(elevations)


