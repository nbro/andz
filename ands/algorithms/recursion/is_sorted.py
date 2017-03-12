#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 21/01/2017

Updated: 11/03/2017

# Description

`is_sorted` check if a list or tuple contains elements in sorted order by using recursion.
This algorithm can potentially be modified to work with other collections.
The other versions are here just for comparison.

"""

import operator

__all__ = ["is_sorted", "iterative_is_sorted", "pythonic_is_sorted"]


def _is_sorted(a, i: int, op) -> bool:
    """`i` is used to index the two adjacent elements of `a`.

    op can either be >, if `a` should be in ascending order,
    or <, if `a` should be in descending order."""
    if i == len(a) - 1:  # If i is the last index, there's nothing more to check, thus the list is sorted.
        return True
    if op(a[i], a[i + 1]):
        return False
    else:
        return _is_sorted(a, i + 1, op)


def is_sorted(a, rev=False) -> bool:
    """Checks recursively if `a` is sorted.

    If `rev` is `True`, this function checks if `a` is sorted in descending order,
    else if it's sorted in ascending order."""
    if len(a) < 2:
        return True

    op = operator.gt
    if rev:
        op = operator.lt

    return _is_sorted(a, 0, op)


def iterative_is_sorted(a, rev=False) -> bool:
    """Iterative alternative to `is_sorted`.

    **Time complexity**: O(n)."""
    if len(a) < 2:
        return True

    op = operator.gt
    if rev:
        op = operator.lt

    for i in range(len(a) - 1):
        if op(a[i], a[i + 1]):
            return False

    return True


def pythonic_is_sorted(a, rev=False) -> bool:
    """Checking if a is sorted in a shorter way by using the `all` function."""
    op = operator.le
    if rev:
        op = operator.ge
    return all(op(a[i], a[i + 1]) for i in range(len(a) - 1))
