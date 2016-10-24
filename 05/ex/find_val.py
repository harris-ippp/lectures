#!/usr/bin/env python 


def find_closest_val(l, v):

  l.sort()

  a, b = 0, len(l) - 1

  while b - a > 1:

    h = a + (b - a)//2
    if v < l[h]:
      a, b = a, h
    else:
      a, b = h, b

  if v - l[a] > l[b] - v: 
    return l[b]
  else: return l[a]


from random import randint
l = [randint(0, 1000) for x in range(100)]

# for y in range(100):
#   for x in range(100):
# 
#     r = randint(0, 1000)
#     if find_closest_val(l, r) != min(l, key = lambda x : abs(x - r)):
#       print(l, r)


