#!/usr/bin/env python 

yum = ["pineapple", "watermelon", "blueberry", 
       "apricot", "chirimoya", "grapefruit",]

output = open("output.txt", "w")
for y in yum: output.write(y + "\n")
output.close()


