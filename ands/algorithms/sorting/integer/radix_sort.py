#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 05/03/2022

Updated: 05/03/2022

# Description

## Short Description

Radix sort is a non-comparison sorting algorithm that uses the stable
counting sort as a subroutine.

## Long Description

Radix-sort assumes that the given list contains integers, each of which has
a w-bit binary representation (for example, w = 32). It sorts the list by
calling w / d times the counting sort algorithm. In the first iteration, it
sorts (with counting sort) the list of integers according to the least
significant d bits of each integer. In the next iteration, it sorts according
to the next least significant d bits. This continues until the last iteration,
where the integers are sorted according to the most significant d bits.

If w / d is not an integer, we can increase w to d⌈w/d⌉, where ⌈⌉ is the
ceiling operation.

## Properties

- Non-comparison (integer) sorting algorithm

## Applications

- Sort records of information that are keyed by multiple fields.
    - Example: sort dates by three keys: year, month, and day.

## TODO

- The code used for counting sort here is really very similar to the standalone
counting sort algorithm in the module counting_sort.py, so we might want to
reuse that code.

# References

- Chapter 8.3, Introduction to Algorithms (3rd edition), by CLRS.
- https://www.youtube.com/watch?v=YXFI4osELGU
- http://www.allisons.org/ll/AlgDS/Sort/Radix/
- Chapter 10, Algorithms in C, R. Sedgewick.
- https://wiki.python.org/moin/BitwiseOperators
"""

__all__ = ["radix_sort"]


def radix_sort(a: list, w: int = 32, d: int = 2) -> list:
    assert isinstance(a, list) and isinstance(w, int) and isinstance(d, int)
    if not all(isinstance(x, int) for x in a):
        raise TypeError("all elements of a should be integers")
    if not all(x >= 0 for x in a):
        raise ValueError("all elements be >= 0")

    # TODO: deal with the case where w is not divisible by d; don't forget the
    #  test cases.

    def index(x: int, p: int) -> int:
        # x is an element of a
        # p is the current iteration number

        # (x >> d * p) & ((1 << d) - 1) is the integer whose binary
        # representation is given by bits
        # (p + 1) * d - 1, ..., p * d of x, where x = a[i].
        #
        # Example
        #
        # Let x = 3, d = 2 and p = 0.
        # Then (x >> d * p) & ((1 << d) - 1) = (3 >> 2 * 0) & ((1 << 2) - 1) =
        # (3 >> 0) & (4 - 1) = 3 & 3 = 3.
        #
        # Let x = 7, d = 2 and p = 1.
        # Then (x >> d * p) & ((1 << d) - 1) = (7 >> 2 * 1) & ((1 << 2) - 1) =
        # (7 >> 2) & (4 - 1) = 1 & 3 = 1.
        return (x >> d * p) & ((1 << d) - 1)

    # w // d of counting sort.
    for p in range(w // d):
        # This block of code is an adaptation of the counting sort algorithm
        # for this radix sort algorithm.

        # The auxiliary counter list of size 1 << d, that is len(c) = 2^p.
        k = 1 << d
        c = [0] * k

        for i in range(len(a)):
            c[index(a[i], p)] += 1

        for i in range(1, k):
            c[i] += c[i - 1]

        # The result list for iteration p.
        b = [None] * len(a)

        for i in range(len(a) - 1, -1, -1):
            c[index(a[i], p)] -= 1
            b[c[index(a[i], p)]] = a[i]

        a = b

    return b


if __name__ == '__main__':
    a: list = []
    b = radix_sort(a)
    print(b)

    a = [2]
    b = radix_sort(a)
    print(b)

    a = [10, 2]
    b = radix_sort(a)
    print(b)

    # a = [10, 2, -3]
    # b = radix_sort(a)
    # print(b)
