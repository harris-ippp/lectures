#!/usr/bin/env python

import requests, pandas as pd

state_fips= {
  "al" : 1,  "ak" : 2,  "az" : 4,  "ar" : 5,  "ca" : 6,  "co" : 8,  "ct" : 9,  "de" : 10, "fl" : 12, "ga" : 13,
  "hi" : 15, "id" : 16, "il" : 17, "in" : 18, "ia" : 19, "ks" : 20, "ky" : 21, "la" : 22, "me" : 23, "md" : 24, 
  "ma" : 25, "mi" : 26, "mn" : 27, "ms" : 28, "mo" : 29, "mt" : 30, "ne" : 31, "nv" : 32, "nh" : 33, "nj" : 34, 
  "nm" : 35, "ny" : 36, "nc" : 37, "nd" : 38, "oh" : 39, "ok" : 40, "or" : 41, "pa" : 42, "ri" : 44, "sc" : 45, 
  "sd" : 46, "tn" : 47, "tx" : 48, "ut" : 49, "vt" : 50, "va" : 51, "wa" : 53, "wv" : 54, "wi" : 55, "wy" : 56, 
  "dc" : 11, "pr" : 72
} 


def census_table(state, var, sort_abc = False, head = -1):

    base_addr = "http://api.census.gov/data/2015/acs5/profile?"
    var_addr  = "https://api.census.gov/data/2014/acs5/profile/variables/{}.json"

    if state:
      base_addr = base_addr + "for=county:*&in=state:{}&get=NAME,{}"
      addr = base_addr.format(state_fips[state], ",".join(var))
    else:
      base_addr = base_addr + "for=state:*&get=NAME,{}"
      addr = base_addr.format(",".join(var))

    c = requests.get(addr).json()
    df = pd.DataFrame(data = c[1:], columns = c[0])
    df = df[df['state'] != '72']

    for v in var:
      df[v] = pd.to_numeric(df[v], errors = "coerce").fillna(0)

      var_descr = requests.get(var_addr.format(v)).json()
      print(var_descr["name"], var_descr["label"])

        
    pd.set_option('display.max_rows', len(df))
    if sort_abc:
      print(df[['NAME'] + var].to_string(index=False))

    else: 
      print(df[['NAME'] + var].sort_values(by=var[0], ascending = [0])
                              .head(head)
                              .to_string(index=False))

    print("\n")

    return df

census_table("",   ["DP02_0040E"])
# census_table("",   ["DP03_0119PE", "DP02_0066PE", "DP02_0040E"], sort_abc = True)
# census_table("",   ["DP02_0066PE"], sort_abc = True)
# census_table("il", ["DP03_0119PE"], head = 5)
# census_table("pa", ["DP03_0119PE"], head = 5)

