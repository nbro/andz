#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Primality Tests
"""

def is_prime(n):
    """Returns True if n is a prime, False otherwise."""
    if n <= 1:  # primes are greater than 1
        return False
    if n == 2:  # 2 is a prime
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n: 
        if n % i == 0:
            return False
        i += 2
    return True


def _is_prime_r(n, i):
    if i * i <= n:
        if n % i == 0:
            return False
        else:
            return _is_prime_r(n, i + 2)
    return True

# do not use this function, because the stack has a limit,
# and if exceeded an exception is thrown.
def is_prime_r(n):
    if n <= 1:  # primes are greater than 1
        return False
    if n == 2:  # 2 is a prime
        return True
    if n % 2 == 0:
        return False
    return _is_prime_r(n, 3)


def test1():
    for i in range(100000):
        assert is_prime(i) == is_prime_r(i)
    print("Finished test 1.")

    
if __name__ == "__main__":
    test1()
