#!/usr/bin/env python 

total = 0
for l in open("salaries.csv"):

  sl = l.strip().split(",")

  if "FIRE" in l and "$" in sl[-2]:
    total += float(sl[-2][1:])

print("Total salaries: ${:.2f}".format(total))
