#!/usr/bin/env python 

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# You coulduse here the square root function, sqrt.
# It returns a floating point value
# sqrt(9) -> 3.0 but sqrt(10) -> 3.162...
# But... you don't need it!
from math import sqrt

# Your code goes here.
# Should be < 10 lines.
for a in range(1, 1000):
  for b in range(a, 1000):
    c = sqrt(a * a + b * b)
    if a + b + c == 1000:
      solution = int(a * b * c)
      break
  if solution: break

# Check for the correct answer.
print("#5 : Pythagorean Triplet ::", "Correct." if solution == 31875000 else ("Wrong: " + str(solution)))

