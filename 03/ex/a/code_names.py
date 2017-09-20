#!/usr/bin/env python

code = {}
for l in open("gender_code", "r"):
  sl = l.strip().split()
  code[sl[1]] = sl[0]


for l in open("salaries.csv"):

  l = l.strip()
  l = l.replace("\"", "")

  if "POLICE OFFICER" in l:
    n = l.split(",")[1].strip()
    n = n.split()[0]
    if n not in code:
      code[n] = None


r = sum(not c for n, c in code.items())

for n, c in code.items():

  if c: continue

  while c not in ["M", "F", "A", "?"]:
    c = input("{}  --  {} [M/F/A/?] :: ".format(r, n)).upper()

  with open("gender_code", "a") as out:
    out.write(c + " " + n + "\n")

  r -= 1


