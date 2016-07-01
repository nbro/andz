#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Modified: 01/07/16


### Parts of the quicksort algorithm

1. **Partition**

    All elements smaller than a number  usually called "pivot"
    are put to the left of the pivot.

    In this quick sort algorithm, the pivot is chosen to be
    the last element of the range [`start`, `end`],
    but it could also have been choosen, e.g., to be the middle element.

    We keep searching for elements less than the pivot,
    from the left to the right of the range [`start`, `end`[,
    and we insert them at the position tracked by the variable `p_index`.

    So, `p_index` keeps track of the position (or index)
    in the range [`start`, `end`[, where all elements to the left of `p_index` are smaller than the pivot.
    Before returning this position (`p_index`), the pivot is inserted in that position.
    Note that doing this, the pivot will be already in its final sorted position.

2. **Recursive Calls**

    `quick_sort` is called recursively
    on the left of the pivot and on the right until `start >= end`.


## Resources
- [Quicksort](http://en.wikipedia.org/wiki/Quicksort), Wiki's article
- [The Quick Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html),
section of online book on searching and sorting by
[http://interactivepython.org](http://interactivepython.org)
"""


def partition(ls: list, start: int, end: int):
    """Shifts all elements in `ls` that are less than the pivot
    to the left of the position `p_index`, which is at the end returned.

    **Time Complexity:** O(k), where k is the size of `ls`."""
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
    and then calls itself recursively on the left and right
    sides of the pivot index (`p_index`)."""
    if start < end:
        # Returns the pivot index after partition.
        p_index = partition(ls, start, end)

        # Calling _quick_sort_aux on the left side of the pivot.
        _quick_sort_aux(ls, start, p_index - 1)

        # Calling quick_sort on the right side of the pivot.
        _quick_sort_aux(ls, p_index + 1, end)


def quick_sort(ls: list):
    """In-place sorting algorithm.
    Returns a reference to `ls`.

    **Time Complexity**

    - Worst Case: O(n<sup>2</sup>)

    - Average Case: O(n*log<sub>2</sub>(n))"""
    _quick_sort_aux(ls, 0, len(ls) - 1)
    return ls
