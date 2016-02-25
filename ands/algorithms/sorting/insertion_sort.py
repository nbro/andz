#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Modified: 03/02/16

### Resources

- [Insertion Sort](http://en.wikipedia.org/wiki/Insertion_sort), Wiki's article

- [The Insertion Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html),
article by [http://interactivepython.org](http://interactivepython.org)
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


if __name__ == "__main__":
    from util import run_tests
    run_tests(insertion_sort)
