#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Modified: 01/07/16

### Resources

- [Selection Sort](http://en.wikipedia.org/wiki/Selection_sort), Wiki's article

- [The Selection Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html),
article at [http://interactivepython.org](http://interactivepython.org)
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
