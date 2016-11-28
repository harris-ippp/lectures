import pandas as pd

sf_url = "https://data.sfgov.org/resource/cuks-n6tp.json?"
query  = "$select=date_trunc_ym(date)%20as%20month,"
query += "%20count(*)&$group=month"

df = pd.read_json(sf_url + query, convert_dates = ["month"])
df.plot(x = "month", y = "count", c = "r")
