#!/usr/bin/env python 

a = [1, 2, 3, 5, 6, 0, 3, 5]
b = [1, 3, 5, 7, 9, 11, 13]
l = [x for x in a if x in b]
print(l)

