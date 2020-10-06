#!/usr/bin/env python


"""
a + b + c = 1000
a*a + b*b == c*c
"""

candidates = []
done = False
for a in range(1, 1001):
    if not done:
        for b in range(1, 1001):
            if not done:
                for c in range(1, 1001):
                    if a + b + c == 1000:
                        candidates.append((a, b, c))
                        print(a, b, c, a * a + b * b, c * c)
                        if a * a + b * b == c * c:
                            print(a, b, c, a * b * c)
                            done = True
# print candidates
