#!/usr/bin/env python 

depts = {}
for l in open("salaries.csv"):

  # only lines with people
  if not "$" in l: continue

  # split up the lines; 
  # grab departments and salaries.
  sl = l.strip().split(",")
  dept = sl[3].strip()
  sal  = 0 if not sl[7] else float(sl[7][1:])
  
  if dept not in depts: depts[dept] = []
  depts[dept].append(sal)


print("{:25}{:>12}{:>15}{:>11}{:>11}".format("Department", "Employees", "Total Exp.", "Avg. Sal.", "Max Sal."))

for x, l in sorted(depts.items(), key=lambda x: sum(x[1]), reverse = True):
  l = depts[x]
  print("{:2s}{:12d}{:15.2f}{:11.2f}{:11.2f}".format(x, len(l), sum(l), sum(l)/len(l), max(l)))


