#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Quick-Sort

Parts of the algorithm:

1. Partition
All elements smaller than a pivot are put to the left of the pivot:

In this quick sort algorithm,  
the pivot is chosen to be the last element of the range [start, end].

We keep searching for elements less than the pivot ,
from the left to the right of the range(start, end).

A variable called "p_index" keeps track of the position or index in the range(start, end),
where all elements to the left of "p_index" are smaller than the pivot.

Before returning this position ("p_index"), the pivot is inserted in that position.
Note that doing this, the pivot will be already in its final sorted position...

2. Recursive calls
Call "quick_sort" recursively on the left of the pivot and on the right
until start >= end


Want to know more about quick sort?

- http://en.wikipedia.org/wiki/Quicksort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
"""


def partition(ls: list, start: int, end: int):
    """Shifts all elements in A that are <= pivot 
    to the left of the future pivot position "p_index",
    and returns the position of the pivot, that I called "p_index" """

    pivot = ls[end]  # Take last element as pivot.
    p_index = start

    for i in range(start, end):
        if ls[i] <= pivot:
            ls[p_index], ls[i] = ls[i], ls[p_index]
            p_index += 1

    # Insert the pivot at index p_index (the pivot's index).
    ls[p_index], ls[end] = ls[end], ls[p_index]

    return p_index


def _quick_sort_aux(ls: list, start: int, end: int):
    """Keeps calling partition to find the pivot index,
    and then calls itself recursively
    on the left and right sides of the pivot index (p_index)"""
    if start < end:
        # Returns the pivot index after partition.
        p_index = partition(ls, start, end)

        # Calling _quick_sort_aux on the left side of the pivot.
        _quick_sort_aux(ls, start, p_index - 1)

        # Calling quick_sort on the right side of the pivot.
        _quick_sort_aux(ls, p_index + 1, end)


def quick_sort(ls: list):
    """In-place sorting algorithm.

    Time complexity:
    O(n^2) (in the worst case) and
    O(n*log_2(n)) (in the average case)."""
    _quick_sort_aux(ls, 0, len(ls) - 1)


if __name__ == '__main__':
    a = [12, 14, 10, 9, 8, 100, 10, 12, 7, 28]
    quick_sort(a)
    print(a)
