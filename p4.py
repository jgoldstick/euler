#!/usr/bin/env python

"""

find the largest palindrome made from the product of 2 3 digit numbers
"""
candidates = []
for i in range(100, 1000):
    for j in range(100, 1000):
        candidate = i * j
        # print i, j, str(candidate), str(candidate)[::-1]
        if str(candidate) == str(candidate)[::-1]:
            print candidate
            candidates.append(candidate)

print candidates
print max(candidates)

"""
revisited
"""

candidate = 999 * 999
while True:
    if str(candidate) == str(candidate)[::-1]:
        break
    candidate -= 1

print candidate
