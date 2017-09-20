#!/usr/bin/env python 

top = 1000000
sieve = [False, False] + [True for i in range(top - 2)]

for i in range(2, top):

  if sieve[i]: # is prime 

    v = i*i
    while v < top:

      if not sieve[v]: print(i, v)
      sieve[v] = False
      v += i

