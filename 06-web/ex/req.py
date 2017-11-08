#!/usr/bin/env python 

import requests

addr = "https://harris-ippp.github.io/lectures/"

resp = requests.get(addr) # this is it!!
# pt = requests.put('addr', data = {'key':'value'})
# ... and options, delete, etc.

s = resp.status_code
t = resp.text
# j = resp.json()
print(s, t)

