#!/usr/bin/env python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def get_prime(cardinal):
    primes = [2]
    prime_factors = []
    n = 3
    num_primes = 1
    while True:
        is_prime = True
        for p in primes:
            # print "n: %d  p: %d" %(n, p)
            if not n % p:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            num_primes += 1
            print("%d is the %d prime" % (n, num_primes))
            if num_primes == cardinal:
                return n
        n += 2
    return n


def get_primes(limit):
    primes = [2]
    prime_factors = []
    n = 3
    new_limit = limit
    while n < limit + 1:
        is_prime = True
        for p in primes:
            # print "n: %d  p: %d" %(n, p)
            if not n % p:
                is_prime = False
                break
        if is_prime:
            # print n, "is prime"
            primes.append(n)
            # print primes
            if not limit % n:
                print("limit:  %d  n: %d" % (limit, n))
                prime_factors.append(n)
                new_limit = limit
                while not new_limit % n:
                    new_limit = new_limit / n
                    print("new limit: %d" % new_limit)
                print(prime_factors)
        limit = new_limit
        n += 2  # only odds can be prime except 2
    return [primes, prime_factors]


if __name__ == '__main__':
    cardinal = 6
    print(get_prime(cardinal))
    cardinal = 10001
    print(get_prime(cardinal))
