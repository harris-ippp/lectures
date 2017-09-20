#!/usr/bin/env python

frac_male = {}
for l in open("data/gender_frac_male"):

  sl = l.strip().split()
  n, v = sl[0], float(sl[1])

  frac_male[n] = v

not_found = set()
counts = {"M":0, "F":0}
for l in open("salaries.csv"):

  l = l.strip()
  l = l.replace("\"", "")

  if "POLICE OFFICER" in l:

    n = l.split(",")[1].strip()
    n = n.split()[0]

    if n in frac_male:
      counts["M"] += frac_male[n]
      counts["F"] += 1 - frac_male[n]
    else: 
      not_found.add(n)

print(not_found)
print()

print(counts)
print(len(not_found), "names not found")


