import requests, pandas as pd

addr =  "http://api.census.gov/data/2014/acs5/"
addr += "profile?get=DP02_0037PE,NAME&for=state:*"
j = requests.get(addr).json()

df = pd.DataFrame(j[1:], columns = j[0])
print(df)
