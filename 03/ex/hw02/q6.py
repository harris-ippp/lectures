#!/usr/bin/env python 

# The 'solution' variable should hold the
# solution when the script is done.

from hw1_support import list_of_integers

solution = 0

# Your code goes here.
# Should be about 1 line

solution = sum(list_of_integers)

# Check for the correct answer.
print("#6 : Big Sum ::", "Correct." if solution == 4392062850662655421630916471493739822967788497424482 else ("Wrong: " + str(solution)))


