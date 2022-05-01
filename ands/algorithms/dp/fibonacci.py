#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 20/07/2015

Updated: 07/03/2018

# Description

In this file you can find some functions that return the nth fibonacci number,
but they do it in different ways, which has also an impact on the performance
and asymptotic complexity of the same algorithms.

The Fibonacci numbers is an infinite sequence of numbers, where the next element
of the sequence is constructed by summing the previous two elements of the same.

The first two elements are usually 0 and 1, so the next element is 1, so the
sequence is now {0, 1, 1}. We then add 1 + 1 = 2 two obtain the 4th element of
the sequence, which is now {0, 1, 1, 2}, and so on.
"""

__all__ = ["recursive_fibonacci", "memoized_fibonacci", "bottom_up_fibonacci"]


def recursive_fibonacci(n: int) -> int:
    """Returns the nth fibonacci number using a recursive approach.

    Time complexity: O(2ⁿ)."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def _memoized_fibonacci_aux(n: int, memo: dict) -> int:
    """Auxiliary function of memoized_fibonacci."""
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = _memoized_fibonacci_aux(n - 1, memo) + \
                  _memoized_fibonacci_aux(n - 2, memo)
    return memo[n]


def memoized_fibonacci(n: int) -> int:
    """Returns the nth fibonacci number using recursion and a technique called
    "memoization".

    Time complexity: O(n)."""
    memo = {}
    return _memoized_fibonacci_aux(n, memo)


def bottom_up_fibonacci(n: int, return_ith: bool = False) -> object:
    """Returns the nth fibonacci number if return_ith=False, else it returns a
    list containing all the ith fibonacci numbers, for i=0, ... , n.

    For example, suppose return_ith == True and n == 5, then this function
    returns [0, 1, 1, 2, 3, 5]. If return_ith == False, it returns simply 5.

    Note: indices start from 0 (not from 1).

    This function uses a dynamic programing "bottom up" approach: we start by
    finding the optimal solution to smaller sub-problems, and from there, we
    build the optimal solution to the initial problem.

    Time complexity: O(n)."""
    if n == 0:
        return n if not return_ith else [n]
    if n == 1:
        return n if not return_ith else [0, n]

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[-1] if not return_ith else fib


if __name__ == "__main__":
    for f in range(10):
        print(recursive_fibonacci(f))
        print(memoized_fibonacci(f))
        print(bottom_up_fibonacci(f, True))
