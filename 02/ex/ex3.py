#!/usr/bin/env python 

# THIS IS A TERRIBLE ALGORITHM.
def is_prime(n):

  for v in range(2, n):

    # if the remainder is 0...
    if not (n % v):
      # the number is not prime.
      return False

  return True


N = 100
prime = []
for x in range(N):
  if is_prime(x):
    print(x, "is prime!")
    prime.append(x)

print("my primes up to", N, "are:", prime)
  

