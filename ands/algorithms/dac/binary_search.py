#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Binary search is a "divide and conquer" search algorithm
that operates on a sorted list.

If you want to know more about binary search:

- http://en.wikipedia.org/wiki/Binary_search_algorithm
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html

Note that no serious tests have been made on this algorihm.
"""


def linear_search(ls, item):
    """Searches for item in ls

    Time complexity: O(n),
    where n is the size of ls.
    """
    for i in ls:
        if i == item:
            return True
    return False


def binary_search_r(ls, value):
    """Recursive binary search.

    Note that this algorithm uses the slice operator,
    which creates a sub-lists.
    slides is an operation that runs in O(k) time...
    To repair this, we can pass the indices,
    instead of creating a new sub-list using the slice operator"""
    if len(ls) == 0:  # basis
        return False
    else:
        mid = len(ls) // 2
        if ls[mid] == value:
            return True
        elif ls[mid] < value:
            return binary_search_r(ls[mid + 1:], value)
        else:
            return binary_search_r(ls[0:mid], value)


def binary_search_i(ls, value):
    """Iterative binary search algorithm.

    Time complexity: O(n*log_2(n))
    """
    if len(ls) == 0:
        return False
    else:
        start = 0
        end = len(ls) - 1
        while start <= end:
            mid = (start + end) // 2

            if ls[mid] == value:
                return True

            elif ls[mid] < value:  # search on the right
                start = mid + 1

            else:  # search on the left
                end = mid - 1
        return False
