#!/usr/bin/env python

mconv = {"ly" : 9.4605e15, "km" : 1000, "m" : 1, "cm" : 0.01, "mi" : 1609.344, "ft" : 0.3048}

def convert(n = 1, fr = "m", to = "m"):

  pass

print(convert(3.281, "ft", "m"))
print(convert(1000, "m", "km"))
print(convert(0.001, "km", "m"))
print(convert(5280, "ft", "mi"))
print(convert(1, "mi", "ft"))
print(convert(1, "km", "mi"))
print(convert(1, "mi", "km"))

