#!/usr/bin/env python

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
s = 0
f = open("p13.txt")
for n in f:
    s += int(n)
print s, str(s)[:10]
