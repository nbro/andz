#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 15/08/2015

Updated: 07/03/2018

# Description

Finds a peak in a list`A of comparable objects. A peak A[i] satisfies the
following condition:

    A[i - 1] <= A[i] >= A[i + 1]

for i=1...len(A) - 2. In other words, A[i] is a peak if it is not smaller than
its neighbors.

The two algorithms to find the peak below can return different correct answers,
because they operate differently. find_peak_linearly proceeds linearly through
the input list ls, whereas find_peak uses a divide and conquer strategy.

# TODO

- Complexity analysis of find_peak.

# References

- https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&spfreload=10
"""

__all__ = ["find_peak", "find_peak_linearly"]


def find_peak_linearly(ls: list) -> int:
    """Finds the index of the first peak in ls.

    If there's no peak or the list is empty, -1 is returned.

    Time complexity: O(n), where len(ls) == n."""
    for i in range(1, len(ls) - 1):
        if ls[i - 1] <= ls[i] >= ls[i + 1]:
            return i
    return -1


def _find_peak(ls: list, i: int, j: int) -> int:
    """Auxiliary in-place algorithm to find_peak."""
    m = (i + j) // 2

    if 0 < m < len(ls) - 1:

        if ls[m - 1] <= ls[m] >= ls[m + 1]:
            return m

        elif ls[m - 1] > ls[m]:
            return _find_peak(ls, i, m - 1)

        elif ls[m] < ls[m + 1]:
            return _find_peak(ls, m + 1, j)
    else:
        return -1


def find_peak(ls: list) -> int:
    """Returns the index of a peak in ls, using the divide-and-conquer strategy.

    If there's no peak or the list is empty, -1 is returned."""
    return _find_peak(ls, 0, len(ls) - 1)
