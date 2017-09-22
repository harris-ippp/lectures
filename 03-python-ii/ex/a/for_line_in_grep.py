#!/usr/bin/env python

for line in open("salaries.csv", "r"):

  if "$" not in line: continue
  line = line.replace("$", "").strip()

  # split the line into a list
  spline = line.split(",")

  # pull off the salary, as a float
  if not spline[-2]: continue
  if float(spline[-2]) > 200000: print(line)

