#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 18/08/2015

Updated: 10/03/2017

# Description

Find an element x in a list, such that at most k elements of the list are less than or equal to x.

# TODO

- Consider to move algorithm `partition` to its own file, since it's used here and by quick-sort.
- Add complexity analysis
- Add _select_in_place
"""

from ands.algorithms.sorting.quick_sort import partition

__all__ = ["select"]


def _select_not_in_place(ls: list, k: int) -> object:
    """Find an element `x` in `ls`, such that at most `k` elements of `ls` are less than `x`."""
    p = partition(ls, 0, len(ls) - 1)  # p := pivot's index

    if p == k:
        return ls[p]
    elif p > k:
        return _select_not_in_place(ls[0:p], k)
    else:  # p < k
        return _select_not_in_place(ls[p + 1:], k - p - 1)


def select(ls: list, k: int) -> object:
    """Returns an element `x` from `ls` such that at most `k` from `ls` are less than `x`.

    Assumes `ls` is a valid list and k is an int.

    If k >= len(ls) or k < 0, ValueError is raised.
    If the list `ls` is empty, None is returned.
    If k == 0, it means that `x` is the smallest element in `ls`.

    The reason why if `k == len(ls)` it raises a ValueError
    it's because we have len(ls) - 1 elements in `ls` which aren't x."""
    if k < 0 or k >= len(ls):
        raise ValueError("k < 0 or k >= len(ls)")
    return _select_not_in_place(ls, k)
