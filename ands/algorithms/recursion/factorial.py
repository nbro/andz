#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 17/07/2015

Updated: 20/08/2017

# Description

The factorial of a number n is defined recursively as follows:

    fact(n):
        # Assume n is int and n >= 0
        if n == 0 or n == 1:
            return 1
        else:
            return n * fact(n - 1)  # n * (n - 1)!

# Resources

- http://www.math.uah.edu/stat/foundations/Structures.html#com2
"""

__all__ = ["factorial", "iterative_factorial", "smallest_geq", "multiple_factorial"]


def factorial(n: int) -> int:
    """Returns the factorial of `n`, which is calculated recursively,
    as it's usually defined mathematically.

    Assumes that `n >= 0`."""
    assert n >= 0

    if n == 0:
        return 1
    elif n == 1 or n == 2:
        return n
    else:
        return n * factorial(n - 1)


def iterative_factorial(n: int) -> int:
    """Returns the factorial of `n`, which is calculated iteratively.
    This is just for comparison with the recursive implementation.

    Since the "factorial" is a primitive recursive function,
    it can be implemented iteratively.

    Proof that factorial is a primitive recursive function:
    https://proofwiki.org/wiki/Factorial_is_Primitive_Recursive.

    A primitive recursive function is a recursive function which can be implemented with "for" loops.
    See here: http://mathworld.wolfram.com/PrimitiveRecursiveFunction.html"""
    assert n >= 0

    if n == 0 or n == 1:
        return 1

    f = 1
    for i in range(2, n + 1):
        f *= i

    return f


def smallest_geq(x: int) -> int:
    """Returns the smallest number `n` such that `n! >= x`.

    Assumes a non-negative integer `x` as input.

    "geq" stands for greater or equal."""
    assert x >= 0

    n = 0
    while iterative_factorial(n) < x:
        n += 1

    return n


def _multiple_factorial(n: int, i: int, a: list) -> list:
    if i <= n:
        a.append(factorial(i))
        _multiple_factorial(n, i + 1, a)
    return a


def multiple_factorial(n: int) -> list:
    """Returns a list L of factorials from 0 to n, that is:
        L[0] := 0!
        L[1] := 1!
        ...
        L[n] := n!
    If n is a negative number, returns an empty list.

    Assumes n >= 0."""
    assert n >= 0
    return _multiple_factorial(n, 0, [])
