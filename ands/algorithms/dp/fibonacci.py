#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 20/07/2015

Updated: 29/03/2022

# Description

In this file, you can find some functions that return the nth fibonacci number,
but they do it in different ways, which has also an impact on the performance
and asymptotic complexity of the same algorithms.

The Fibonacci numbers is an infinite sequence of numbers, where the next
element of the sequence is constructed by summing the previous two elements of
the same.

The first two elements are (usually) 0 and 1, so the next element is 1, so the
sequence is now {0, 1, 1}. We then add 1 + 1 = 2 to obtain the 4th element of
the sequence, which is now {0, 1, 1, 2}, and so on.

The nth Fibonacci number can thus be computed in a recursive way. First, the
base cases are when n = 0 and n = 1, so fib(0) = 0 and fib(1) = 1. The
inductive case is fib(n) = fib(n - 1) + fib(n - 2).

It turns out that, if we compute the nth Fibonacci number in this way, we would
repeat some computations. For example, to compute fib(5), you would need to
compute fib(4) and fib(3). To compute fib(4), we would need to compute fib(3)
and fib(2). So, we would compute fib(3) twice.

To solve this problem, once we compute fib(3), we can solve the result. This is
called memoization.

The time complexity of memoized_fibonacci (below) is linear because we need
to solve all fib(i), from i=0 to i=n, and each of these sub-problems takes
constant time.

## References

- "Lecture 19: Dynamic Programming I: Fibonacci, Shortest Paths"
(https://www.youtube.com/watch?v=OQ5jsbhAv_M&ab_channel=MITOpenCourseWare)
- https://www.youtube.com/watch?v=P8Xa2BitN3I&ab_channel=HackerRank

## TODO

- Write a Fibonacci function for negative numbers.
"""

from typing import Union

__all__ = ["recursive_fibonacci", "memoized_fibonacci", "bottom_up_fibonacci"]


def _check_input(n: int):
    if not isinstance(n, int):
        raise TypeError("n should be an int")
    if n < 0:
        raise ValueError("n should be >= 0")


def recursive_fibonacci(n: int) -> int:
    """Returns the nth fibonacci number using a recursive approach.

    Time complexity: O(2ⁿ)."""
    _check_input(n)
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
        memo[n] = _memoized_fibonacci_aux(n - 1, memo) + _memoized_fibonacci_aux(
            n - 2, memo
        )
    return memo[n]


def memoized_fibonacci(n: int) -> int:
    """Returns the nth fibonacci number using recursion and a technique called
    "memoization".

    Time complexity: O(n)."""
    _check_input(n)
    memo = {}
    return _memoized_fibonacci_aux(n, memo)


def bottom_up_fibonacci(n: int, return_seq: bool = False) -> Union[int, list]:
    """Returns the nth fibonacci number if return_seq=False, else it returns a
    list containing the sequence of Fibonacci numbers from i=0 to i=n.

    For example, suppose return_seq == True and n == 5, then this function
    returns [0, 1, 1, 2, 3, 5]. If return_seq == False, it returns simply 5.

    Note: indices start from 0 (not from 1).

    This function uses a dynamic programing "bottom up" approach: we start by
    finding the optimal solution to smaller sub-problems, and from there, we
    build the optimal solution to the initial problem.

    Time complexity: O(n)."""
    _check_input(n)
    assert isinstance(return_seq, bool)
    if n == 0:
        return n if not return_seq else [n]
    if n == 1:
        return n if not return_seq else [0, n]

    # If we don't need to return the list of numbers, we only need to save the
    # last 2 values, so that would be constant space.
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[-1] if not return_seq else fib


if __name__ == "__main__":
    for f in range(10):
        print(recursive_fibonacci(f))
        print(memoized_fibonacci(f))
        print(bottom_up_fibonacci(f, True))
