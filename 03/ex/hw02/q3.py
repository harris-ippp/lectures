#!/usr/bin/env python 

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0
number   = 175832868806

# First create a list of prime numbers to 300.
primes = []
for n in range(2, 300):
  is_prime = True
  for p in primes:
    if not(n%p):
      is_prime = False
      break
  if is_prime:
    primes.append(n)

# Now which of these are factors of 175832868806
nfactors = 0
for p in primes:
  if not number % p:
    nfactors += 1

solution = nfactors

# Check for the correct answer.
print("#3 : Count Prime Factors ::", "Correct." if solution == 6 else ("Wrong: " + str(solution)))


