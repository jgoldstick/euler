#!/usr/bin/env python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


if __name__ == '__main__':
    number_range = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    number_range = (6, 7, 8, 9, 10)
    number_range = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    number_range = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    #number_range = (6,7,8,9,10)
    candidate = 20
    not_found = True
    while not_found:
        for i in (number_range):
            print i, candidate
            if candidate % i:
                candidate += number_range[-1]
                break
        else:
            print "Range is ", number_range
            print "smallest number divisible by all in range is %d" % candidate
            not_found = False
