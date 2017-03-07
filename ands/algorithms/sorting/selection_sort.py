#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 09/09/2015

Updated: 07/03/2017

# Description

# Resources

- [Wiki article about Selection Sort](http://en.wikipedia.org/wiki/Selection_sort),
- [The Selection Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html),
article at http://interactivepython.org
"""


def selection_sort(ls: list):
    """In-place sorting algorithm.
    Returns a reference to `ls`.

    **Time Complexity**: O(n<sup>2</sup>)."""
    for i in range(len(ls) - 1):
        k = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[k]:
                ls[k], ls[j] = ls[j], ls[k]
    return ls
