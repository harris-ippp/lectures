#!/usr/bin/env python 

yum = ["pineapple", "watermelon", "blueberry", "apricot", "chirimoya", "grapefruit", "blackberry", "guava", "avocado", "raspberry", "coconut", "pomegranate", "lucuma", "strawberry", "plums", "cranberry", "gooseberry", "lingonberry", "currant", "goji", "persimmon", "avocado", "banana", "apple", "durian", "huckleberry", "lychee", "passionfruit", "tomato"]

#################################
#################################

print(":: 1 :: alphabetically")
yum.sort()
for y in yum:

  print(y)

#################################
#################################

print(":: 2 :: only the berries")
for y in yum:

  if "berry" in y:
    print(y)


