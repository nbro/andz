#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Want to know more about insertion sort?

- http://en.wikipedia.org/wiki/Insertion_sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
"""


def insertion_sort(ls: list):
    """In-place sorting algorithm.

    Time complexity: O(n^2)"""
    for i in range(1, len(ls)):
        n = i
        while n > 0 and ls[n] < ls[n - 1]:
            ls[n], ls[n - 1] = ls[n - 1], ls[n]
            n -= 1
    return ls
