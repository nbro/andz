#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

This file contains some helper functions for sorting algorithms.
"""

from random import randrange


def is_sorted(ls, rev=False):
    """Checks if a list of numbers is sorted.

    Set rev=True, if you want to check ls is sorted in decreasing order.
    Default behaviour, rev=False, checks if ls is sorted in increasing order.

    Time complexity: O(n)"""
    for i in range(len(ls) - 1):
        if rev:
            if ls[i + 1] > ls[i]:
                return False
        else:
            if ls[i + 1] < ls[i]:
                return False
    return True


def reverse(ls):
    """Reverses the elements of ls.
    Note that you can simply use
    the reverse function of each list object.

    Time complexity: O(n)"""
    for s, e in enumerate(range(len(ls) - 1, len(ls) // 2 - 1, -1)):
        ls[s], ls[e] = ls[e], ls[s]


def get_list(size=10, start=1, end=10):
    """Returns a list of random elements.
    You can specify the size of the list.
    You can also specify the range of numbers in the list."""
    return [randrange(start, end) for x in range(size)]
