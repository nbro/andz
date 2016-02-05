#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: June, 2015

In this file you can find some functions
that return the nth fibonacci number,
but they do it in different ways,
which has also an impact on the performance (Big-O complexity)
of the same algorithms.

The dynamic programming versions run in O(n) time.
"""


def recursive_fib(n):
    """Returns the nth fibonacci number.

    Running time complexity: O(2^n).

    :type n : int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)


def _memoized_fib_aux(n, memo):
    """Returns the nth fibonacci number.

    This function uses recursion and memoisation
    to calculate the n fibonacci number.

    Running time complexity: O(n).

    :type n : int
    :type memo : dict
    """
    if n == 0 or n == 1:
        return n
    if n not in memo.keys():
        memo[n] = _memoized_fib_aux(n - 1, memo) + _memoized_fib_aux(n - 2, memo)
    return memo[n]


def memoized_fib(n):
    """Returns the nth fibonacci number using memoisation."""
    memo = {}
    return _memoized_fib_aux(n, memo)


def bottom_up_fib(n, ls=False):
    """Returns the nth fibonacci number if ls=False,
    else it returns a list containing
    all the ith fibonacci numbers, for i=0, ... , n

    This function uses a dynamic programing bottom up approach,
    because we start by finding the optimal solution
    to smaller sub-problems, and from there,
    we build the optimal solution to the initial problem.

    :type n : int
    :type ls : bool
    """
    if n == 0:
        return n if not ls else [n]
    if n == 1:
        return n if not ls else [0, n]

    fib = [0]*(n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[-1] if not ls else fib


if __name__ == "__main__":
    for f in range(10):
        print(recursive_fib(f))
        print(memoized_fib(f))
        print(bottom_up_fib(f, ls=True))
