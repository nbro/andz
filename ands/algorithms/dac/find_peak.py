#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

The two algorithms to find the peak below
can return different correct answers,
because they operate differently.

Resources:
- https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&spfreload=10
"""


def find_peak_brute_force(ls):
    """Finds the first peak in ls.
    If there's no peak, None is returned.

    A peak ls[i] satisfies the following condition:
    ls[i - 1] <= ls[i] >= ls[i + 1]
    for i=1...len(ls) - 2.
    In other words, A[i] is a peak
    if it is not smaller than its neighbors,

    Time complexity: O(n),
    where n is the size of ls."""
    for i in range(1, len(ls) - 1):
        if ls[i - 1] <= ls[i] >= ls[i + 1]:
            return i


def _find_peak_aux(ls, i, j):
    """Using Divide-and-Conquer paradigm."""
    m = (i + j) // 2

    if 0 < m < len(ls) - 1:

        if ls[m - 1] <= ls[m] >= ls[m + 1]:
            return m

        elif ls[m - 1] > ls[m]:
            return _find_peak_aux(ls, i, m - 1)

        elif ls[m] < ls[m + 1]:
            return _find_peak_aux(ls, m + 1, j)
    else:
        return -1


def find_peak(ls):
    """Returns the index of a peak in ls.
    If there's no peak, -1 is returned."""
    return _find_peak_aux(ls, 0, len(ls) - 1)


if __name__ == "__main__":
    from random import randint

    a = [randint(0, 10) for _ in range(10)]
    print("List:", a)

    print(find_peak_brute_force(a))
    print(find_peak(a))
