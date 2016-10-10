#!/usr/bin/env python 

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# Your code goes here.
# Should be about 10 lines.

f1, f2 = 1, 1
while f1 < 1e9:

  if not (f1 % 17):
    solution += f1

  s  = f1 + f2
  f1 = f2
  f2 = s

# Check for the correct answer.
print("#2 : Fibonacci ::", "Correct." if solution == 15129388 else ("Wrong: " + str(solution)))

