#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 28/06/2015

Updated: 10/03/2017

# Description

Simple primality tests.

# TODO

- Create tests
- Name better the functions
- Document better the functions
- Add complexity analysis
- Organize better the code
"""


def is_prime(n: int) -> bool:
    """Return true if `n` is prime, false otherwise."""
    if n < 2:  # primes are greater than 1
        return False
    if n % 2 == 0:
        return n == 2  # returns True if n == 2 because 2 is a prime
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def _is_prime_r(n: int, i: int) -> bool:
    if i * i <= n:
        if n % i == 0:
            return False
        else:
            return _is_prime_r(n, i + 2)
    return True


def is_prime_r(n: int) -> bool:
    """Return true if `n` is prime, false otherwise.

    This function uses recursion.
    In general, you should prefer an iterative approach,
    because the stack has a limit, and if exceeded an exception is thrown."""
    if n <= 1:  # primes are greater than 1
        return False
    if n % 2 == 0:
        return n == 2
    return _is_prime_r(n, 3)


def is_prime_2(n: int) -> bool:
    """Return true if `n` is prime, false otherwise.

    This algorithm seems to perform better than `is_prime`.

    Time complexity: O(sqrt(n) * O(n % i))."""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
