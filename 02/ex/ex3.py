#!/usr/bin/env python 

def is_prime(n):

  pass


N = 100
prime = []
for x in range(N):
  prime = []
  if is_prime(x):
    print(x, "is prime!")
    prime.append(x)

print("my primes up to", N, "are:", prime)
  

