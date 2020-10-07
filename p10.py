#!/usr/bin/env python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def get_primes(limit):
    """
    generate prime numbers below value of limit
    """
    primes = [2]
    yield 2
    n = 3
    while n < limit:
        is_prime = True
        for p in primes:
            # print "n: %d  p: %d" %(n, p)
            if not n % p:
                is_prime = False
                break
        if is_prime:
            print(n, "is prime")
            primes.append(n)
            yield n
        n += 2  # only odds can be prime except 2

    return


if __name__ == '__main__':

    limit = 2000000
    #limit = 20
    primes = [p for p in get_primes(limit)]
    print(primes, sum(primes))
