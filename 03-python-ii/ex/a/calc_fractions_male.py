#!/usr/bin/env python

genders = {}

for l in open("dist.female.first"):
  sl = l.strip().split()
  genders[sl[0]] = [0, float(sl[1])]

for l in open("dist.male.first"):
  sl = l.strip().split()
  if sl[0] in genders:
    genders[sl[0]][0] = float(sl[1])
  else:
    genders[sl[0]] = [float(sl[1]), 0]

with open("gender_frac_male", "w") as out:
  for n, c in genders.items():

    s = sum(c)
    genders[n] = [c[0]/s, c[1]/s]
    out.write(n + " " + str(c[0]/s) + "\n")
