#!/usr/bin/env python 

import sys
import requests, json, pandas as pd

from netrc import netrc
if not netrc().authenticators("bls"):
  print("You must download your own bls api key.")
  sys.exit()

user, acct, bls_key = netrc().authenticators("bls")

import datetime
last_year = datetime.date.today().year

# https://www.bls.gov/help/hlpforma.htm#LA

state_fips= {
  "al" : 1,  "ak" : 2,  "az" : 4,  "ar" : 5,  "ca" : 6,  "co" : 8,  "ct" : 9,  "de" : 10, "fl" : 12, "ga" : 13,
  "hi" : 15, "id" : 16, "il" : 17, "in" : 18, "ia" : 19, "ks" : 20, "ky" : 21, "la" : 22, "me" : 23, "md" : 24,
  "ma" : 25, "mi" : 26, "mn" : 27, "ms" : 28, "mo" : 29, "mt" : 30, "ne" : 31, "nv" : 32, "nh" : 33, "nj" : 34,
  "nm" : 35, "ny" : 36, "nc" : 37, "nd" : 38, "oh" : 39, "ok" : 40, "or" : 41, "pa" : 42, "ri" : 44, "sc" : 45,
  "sd" : 46, "tn" : 47, "tx" : 48, "ut" : 49, "vt" : 50, "va" : 51, "wa" : 53, "wv" : 54, "wi" : 55, "wy" : 56,
  # "dc" : 11, "pr" : 72
}

series = ['LASST{:02d}0000000000006'.format(v) for k, v in state_fips.items()]
reverse_names = {'LASST{:02d}0000000000006'.format(v) : k.upper() for k, v in state_fips.items()}

reverse_names = {'LAUCT171400000000003' : "Chicago",
                 'LAUCT426000000000003' : 'Philadelphia',
                 'LAUCT365100000000003' : 'New York',
                 'LAUCT064400000000003' : "Los Angeles",
                 "LAUCT483500000000003" : "Houston"}


if True: # Get from scratch
    
    headers = {'Content-type': 'application/json'}

    for y in range(1980, 2016, 5):

      ye = y + 4
      if ye > last_year: ye = last_year

      data = json.dumps({"seriesid": list(reverse_names.keys()), "startyear": y, "endyear": ye, 
                         "registrationKey" : bls_key})
      p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
      print(p)
      print(p.text)
      j = p.json()

      with open("bls_{}.json".format(y), "w") as out: out.write(json.dumps(j, indent=2))


df = None
for y in range(1980, 2016, 5):
        
  with open("bls_{}.json".format(y)) as data: j = json.load(data)
  print("bls_{}.json".format(y))
  
  series_list = []
  for series in j["Results"]['series']:
      
      values, dates = [], []
      for obs in series['data']:
          values.append(obs['value'])
          dates.append(obs['year'] + obs['period'][1:] + "01")
      s = pd.Series(data = values, index = pd.DatetimeIndex(dates, format='%Y%m%d'), name = series['seriesID'])
      series_list.append(s)
  
  if df is not None: 
    df = df.append(pd.concat(series_list, axis=1))
  else:  df = pd.concat(series_list, axis=1)

df.index.rename("Date", inplace=False)
df.sort_index(inplace = True)
df.rename(columns = reverse_names, inplace = True)
df.to_csv("bls.csv", index_label = "Date")


