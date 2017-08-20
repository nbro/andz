#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 09/08/2015

Updated: 20/08/2017

# Description

## Parts of the quick-sort algorithm

1. **Partition**

    All elements smaller than a number  usually called "pivot" are put to the left of the pivot.

    In this partition algorithm, the pivot is chosen to be the last element of the range [`start`, `end`],
    but it could also have been chosen, e.g., to be the middle element.

    We keep searching for elements less than the pivot,
    from the left to the right of the range [`start`, `end`[,
    and we insert them at the position tracked by the variable `p`.

    So, `p` keeps track of the position (or index) in the range [`start`, `end`[,
    where all elements to the left of `p` are smaller than the pivot.
    Before returning this position (`p`), the pivot is inserted in that position.
    Note that doing this, the pivot will be already in its final sorted position.

2. **Recursive Calls**

    `quick_sort` is called recursively on the left of the pivot and on the right until `start >= end`.

# TODO

- Add ASCII animation of a sorting example using quick-sort!
- Improve efficiency of best case time complexity and space complexity.

# References

- http://en.wikipedia.org/wiki/Quicksort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
- http://algs4.cs.princeton.edu/23quicksort/
"""

__all__ = ["quick_sort", "partition"]


def partition(ls: list, start: int, end: int) -> int:
    """Shifts all elements in `ls` that are less than the pivot
    to the left of the position `p`, which is at the end returned.

    Time complexity: O(k), where k is the size of `ls`."""
    pivot = ls[end]  # Take last element as pivot.
    p = start  # pivot's index

    for i in range(start, end):
        if ls[i] <= pivot:
            ls[p], ls[i] = ls[i], ls[p]
            p += 1

    # Insert the pivot at index p (the pivot's index).
    ls[p], ls[end] = ls[end], ls[p]
    return p


def _quick_sort_aux(ls: list, start: int, end: int) -> None:
    """Keeps calling partition to find the pivot index `p`,
    and then calls itself recursively on the left and right sides of the pivot index.

    This is an auxiliary method for `quick_sort` and thus is considered private,
    and therefore should not be used by clients of this module."""
    if start < end:
        # Returns the pivot index after partition.
        p = partition(ls, start, end)

        # Calling _quick_sort_aux on the left side of the pivot.
        _quick_sort_aux(ls, start, p - 1)

        # Calling quick_sort on the right side of the pivot.
        _quick_sort_aux(ls, p + 1, end)


def quick_sort(ls: list) -> None:
    """Quick-sort in-place sorting algorithm.

    Time complexity

    +-------------+-------------+----------+
    |    Best     |   Average   |   Worst  |
    +-------------+-------------+----------+
    | O(n*log(n)) | O(n*log(n)) |  O(n^2)  |
    +-------------+-------------+----------+

    Note: the best case can be improved to O(n) if a 3-way partition is used and we have equal keys.

    Space complexity: O(n).

    Note: the space complexity can be improved to O(log(n))."""
    _quick_sort_aux(ls, 0, len(ls) - 1)
