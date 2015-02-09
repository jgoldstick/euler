#!/usr/bin/env python

"""
Find the greatest product of five consecutive digits in the 1000-digit number.
"""
candidates = []
f = open("p8.txt")
in_data = f.read(1500)
in_data = map(int, list("".join(in_data.split())))
print in_data

max_candidate = 0
while 1:
    candidate = in_data[:5]
    product = 1
    for d in candidate:
        product *= d
        if product > max_candidate:
            max_candidate = product
            print candidate, max_candidate, product
    in_data.pop(0)
