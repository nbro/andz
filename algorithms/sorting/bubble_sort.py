#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Want to know more about bubble sort?

- http://en.wikipedia.org/wiki/Bubble_sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
"""


def bubble_sort(ls: list):
    """In-place sorting algorithm.

    Time complexity: O(n^2)"""
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls