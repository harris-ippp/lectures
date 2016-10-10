#!/usr/bin/env python 

yum = ["pineapple", "watermelon", "blueberry", 
       "apricot", "chirimoya", "grapefruit"]

with open("output.txt", "w") as output:
  for y in yum: output.write(y + "\n")

