import requests

addr =  "http://api.census.gov/data/2014/acs5/profile?"
addr += "for=tract:*&in=state:42+county:*"
addr += "&get=NAME,DP02_0058E,DP02_0058M"

resp = requests.get(addr) # this is it!!
# pt = requests.put('addr', data = {'key':'value'})
# ... and options, delete, etc.

s = resp.status_code
t = resp.text
c = resp.content
j = resp.json()

