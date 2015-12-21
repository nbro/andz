#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Want to know more about selection sort?

- http://en.wikipedia.org/wiki/Selection_sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
"""


def selection_sort(ls: list):
    """In-place sorting algorithm.

    Time complexity: O(n^2)"""

    for i in range(len(ls) - 1):
        k = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[k]:
                ls[k], ls[j] = ls[j], ls[k]
    return ls
