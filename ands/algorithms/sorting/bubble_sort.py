#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Modified: 01/07/16

### Resources
- [Bubble Sort](http://en.wikipedia.org/wiki/Bubble_sort), Wiki's article

- [The Bubble Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html),
article by [http://interactivepython.org](http://interactivepython.org)
"""


def bubble_sort(ls: list):
    """In-place sorting algorithm.
    Returns a reference to `ls`.

    **Time Complexity:** O(n<sup>2</sup>)."""
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls
