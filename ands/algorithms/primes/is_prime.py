#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 28/06/2015

Updated: 19/09/2017

# Description

Simple primality tests.

# TODO

- Add complexity analysis.
- Add AKS primality test.
"""


def is_prime(n: int) -> bool:
    """Return true if n is prime, false otherwise."""
    if n < 2:  # Primes are greater than 1.
        return False
    if n % 2 == 0:
        return n == 2  # Returns True if n == 2 because 2 is a prime.
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_prime_up_to_square_root(n: int) -> bool:
    """Return true if n is prime, false otherwise.

    Time complexity: O(sqrt(n) * O(n % i))."""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def _recursively_is_prime_aux(n: int, i: int) -> bool:
    if i * i <= n:
        if n % i == 0:
            return False
        else:
            return _recursively_is_prime_aux(n, i + 2)
    return True


def recursively_is_prime(n: int) -> bool:
    """Return true if n is prime, false otherwise.

    In general, you should prefer an iterative approach, because the stack has a
    limit and, if exceeded, an exception is thrown."""
    if n <= 1:  # Primes are greater than 1.
        return False
    if n % 2 == 0:
        return n == 2
    return _recursively_is_prime_aux(n, 3)
