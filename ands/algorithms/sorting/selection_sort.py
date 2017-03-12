#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 09/09/2015

Updated: 10/03/2017

# Description

Selection sorting is conceptually probably the most simplest sorting algorithm.

This algorithm first finds the smallest element in the list and exchanges it with the element in the first position,
then find the second smallest element and exchange it with the element in the second position,
and continues in this way until the entire list is sorted.

# References

- [http://www.studytonight.com/data-structures/selection-sorting](http://www.studytonight.com/data-structures/selection-sorting)
- [Wiki article about Selection Sort](http://en.wikipedia.org/wiki/Selection_sort),
- [The Selection Sort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html),
article at http://interactivepython.org

"""

__all__ = ["selection_sort"]


def selection_sort(ls: list) -> None:
    """Selection-sort in-place sorting algorithm.
    Returns a reference to ls.

    **Time complexity**

    +--------+----------+----------+
    |  Best  |  Average |  Worst   |
    +--------+----------+----------+
    | O(n^2) |  O(n^2)  |  O(n^2)  |
    +--------+----------+----------+

    **Space complexity**: O(n)."""
    for i in range(len(ls) - 1):
        k = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[k]:
                ls[k], ls[j] = ls[j], ls[k]
