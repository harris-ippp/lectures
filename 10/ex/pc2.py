#!/usr/bin/env python 

i = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a = "abcdefghijklmnopqrstuvwxyzab"

u = "http://www.pythonchallenge.com/pc/def/map.html"

o = ""
for l in i:
  if l in a: o += a[a.index(l) + 2]
  else: o += l

print(o)

o = ""
for l in i: 
  if l.isalpha():
    o += chr(ord(l)+2)
  else: o += l
print(o)


