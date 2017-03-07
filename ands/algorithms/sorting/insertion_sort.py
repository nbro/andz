#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 23/07/2015

Updated: 07/03/2017

# Description

# Resources

- [Wiki articble about Insertion Sort](http://en.wikipedia.org/wiki/Insertion_sort)
- [The Insertion Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html),
article by http://interactivepython.org
"""


def insertion_sort(ls: list):
    """In-place sorting algorithm.
    Returns a reference to `ls`.

    **Time Complexity**: O(n<sup>2</sup>)."""
    for i in range(1, len(ls)):
        n = i
        while n > 0 and ls[n] < ls[n - 1]:
            ls[n], ls[n - 1] = ls[n - 1], ls[n]
            n -= 1
    return ls
