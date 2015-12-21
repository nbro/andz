#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 18/08/2015

Updated: 10/03/2017

# Description

Find an element x in a list, such that at most k elements of the list are less
than or equal to x.

# TODO

- Add complexity analysis
- Add _select_in_place
"""

from ands.algorithms.sorting.comparison.quick_sort import partition

__all__ = ["select"]


def _select_not_in_place(ls: list, k: int) -> object:
    """Find an element x in ls, such that at most k elements of ls are less than
    x."""
    p = partition(ls, 0, len(ls) - 1)  # p := pivot's index
    if p == k:
        return ls[p]
    if p > k:
        return _select_not_in_place(ls[0:p], k)
    return _select_not_in_place(ls[p + 1 :], k - p - 1)  # p < k


def select(ls: list, k: int) -> object:
    """Returns an element x from ls such that at most k from ls are less than x.

    If k >= len(ls) or k < 0, ValueError is raised.
    If the list ls is empty, None is returned.
    If k == 0, it means that x is the smallest element in ls."""
    if k < 0 or k >= len(ls):
        raise ValueError("k < 0 or k >= len(ls)")
    return _select_not_in_place(ls, k)
