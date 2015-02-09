#!/usr/bin/env python
"""
Project Euler problem 1


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""


def f(limit):
    sum = 0
    for n in range(limit):
        if n % 3 and n % 5:
            pass
        else:
            sum += n
    return sum


if __name__ == '__main__':
    print f(10)
    print f(1000)
