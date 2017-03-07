#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 20/07/2015

Updated: 07/03/2017

# Description

# Resources

- [Wiki article about Bubble Sort](http://en.wikipedia.org/wiki/Bubble_sort)
- [The Bubble Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html),
article by http://interactivepython.org

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
