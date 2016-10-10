#!/usr/bin/env python 

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# Your code goes here.
# Should be < 3 lines.

number = str(2 ** 865)
for n in number:
  solution += int(n)

# Check for the correct answer.
print("#7 : 2^865 ::", "Correct." if solution == 1181 else ("Wrong: " + str(solution)))

