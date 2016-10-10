#!/usr/bin/env python 

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# Your code goes here.
# Should be about 10 lines.

count = 0
while count < 9:

  # step by primes, without further thought.
  solution += 1
  if any([solution % v for v in [4, 13, 14, 26, 50]]):
    continue

  count += 1

    
# Check for the correct answer.
print("#1 : 9th Multiple ::", "Correct." if solution == 81900 else ("Wrong: " + str(solution)))


