#!/usr/bin/env python 

import requests, json
import os, sys

from time import sleep
import datetime as dt

# from netrc import netrc
# user, acct, passwd = netrc().authenticators("weather")

# REAL ENDPOINT :: endpoint = "http://api.wunderground.com/api/{}/history_{}/q/K{}.json"

endpoint = "https://raw.githubusercontent.com/harris-ippp/lectures/master/09-weather/data/wu/history_{}/q/K{}.json"
dirname  = os.path.dirname(os.path.realpath(__file__))

for city in ["MDW"]: 

    cdir = dirname + "/" + city + "/"
    os.makedirs(cdir, exist_ok = True)
    
    for year in [2015]:
        
        nyd = dt.date(int(year), 1, 1)
        print(city, year)

        if os.path.isfile(cdir + str(nyd + dt.timedelta(2)) + ".csv"): continue
        
        for n in range(366):

            date = str(nyd + dt.timedelta(n))

            print(date)
            data = requests.get(endpoint.format(date.replace("-", ""), city)).json()

            with open(cdir + date + ".json", "w") as out:
                json.dump(data, out)
                
            with open(cdir + date + ".csv", "w") as out:
                for obs in data["history"]["observations"]:
                    t = float(obs["tempi"])
                    precip = float(obs["precipi"])
                    if precip < 0: precip = 0
                    datetime = "{year}-{mon}-{mday}T{hour}:{min}:00Z".format(**obs["utcdate"])

                    out.write(",".join([datetime, str(t), str(precip)]) + "\n")
                    
            sleep(7)
            
        sys.exit()


