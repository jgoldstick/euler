#!/usr/bin/env python

"""
Find the greatest product of five consecutive digits in the 1000-digit number.
"""
candidates = []
f = open("p8.txt")
in_data = f.read(1500)
data_1 = map(int, list("".join(in_data.split())))
data_2 = map(int, list("".join(in_data.split())))


def largest_product(n, data):
    max_candidate = 0
    while len(data) > n:
        candidate = data[:n]
        product = 1
        for d in candidate:
            product *= d

        if product > max_candidate:
            max_candidate = product
            print(candidate, max_candidate, product)
        data.pop(0)
    return max_candidate

print(largest_product(4, data_1))
print(largest_product(13, data_2))
