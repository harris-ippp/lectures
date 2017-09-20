import requests, pandas as pd

state_fips= {
  "al" : 1,  "ak" : 2,  "az" : 4,  "ar" : 5,  "ca" : 6,  "co" : 8,  "ct" : 9,  "de" : 10, "fl" : 12, "ga" : 13,
  "hi" : 15, "id" : 16, "il" : 17, "in" : 18, "ia" : 19, "ks" : 20, "ky" : 21, "la" : 22, "me" : 23, "md" : 24, 
  "ma" : 25, "mi" : 26, "mn" : 27, "ms" : 28, "mo" : 29, "mt" : 30, "ne" : 31, "nv" : 32, "nh" : 33, "nj" : 34, 
  "nm" : 35, "ny" : 36, "nc" : 37, "nd" : 38, "oh" : 39, "ok" : 40, "or" : 41, "pa" : 42, "ri" : 44, "sc" : 45, 
  "sd" : 46, "tn" : 47, "tx" : 48, "ut" : 49, "vt" : 50, "va" : 51, "wa" : 53, "wv" : 54, "wi" : 55, "wy" : 56, 
  "dc" : 11, "pr" : 72
} 

pct = "Percent "

def census_table(state, name, num, den, sort_abc = False, head = -1):

    base_addr = "http://api.census.gov/data/2014/acs5?"

    if state:
      base_addr = base_addr + "for=county:*&in=state:{}&get=NAME,{}"
      addr = base_addr.format(state_fips[state], ",".join([num, den]))
    else:
      base_addr = base_addr + "for=state:*&get=NAME,{}"
      addr = base_addr.format(",".join([num, den]))

    print(addr)
    
    c = requests.get(addr).json()
    a = [{c[0][xi]:x for xi, x in enumerate(v)} for v in c[1:]]

    df = pd.io.json.json_normalize(a)
    df = df[df['state'] != '72']

    for v in [num, den]: 
      df[v] = df[v].astype(int)
        
    df[pct + name] = df[num] / df[den]
    pd.set_option('display.max_rows', len(df))
    if sort_abc:
      print(df[['NAME', pct + name]])
      print(df[['NAME', pct + name]].to_string(index=False))

    else: 
      print(df[['NAME', pct + name]].sort_values(by=[pct + name], ascending = [0])
                                    .head(head)
                                    .to_string(index=False))

    return a

# census_table("",   "Poverty",      "B06012_002E", "B06012_001E", head = 5)
# census_table("",   "Poverty",      "B06012_002E", "B06012_001E", sort_abc = True)
# census_table("il", "Poverty",      "B06012_002E", "B06012_001E", head = 5)
# census_table("il", "Teen Births",  "B13016_003E", "B13016_002E", 5)
# census_table("pa", "BA or Higher", "B16010_041E", "B16010_001E", 5)

