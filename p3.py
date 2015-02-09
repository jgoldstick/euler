#!/usr/bin/env python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


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
                print "limit:  %d  n: %d" % (limit, n)
                prime_factors.append(n)
                new_limit = limit
                while not new_limit % n:
                    new_limit = new_limit / n
                    print "new limit: %d" % new_limit
                print prime_factors
        limit = new_limit
        n += 2  # only odds can be prime except 2
    return [primes, prime_factors]

if __name__ == '__main__':
    primes = [2]
    limit = 13195
    limit = 600851475143
    #limit = 15
    primes, prime_factors = get_primes(limit)
    print "All prime numbers less than %d" % limit
    print primes
    print primes[-1], prime_factors
    print "Largest prime factor is %d" % prime_factors[-1]
