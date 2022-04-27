#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 23/07/2015

Updated: 09/03/2022

# Description

It is a simple sorting algorithm which sorts a list by shifting elements one by
one.

## Properties

- comparison-based sorting algorithm
- stable
- in-place
- efficient for "small" lists
- adaptive (reduces the number of comparison if the list is already sorted)
- Better than bubble-sort for almost-ordered lists, even though both have
a best-case time complexity of O(n).
- Online (can sort a list as it receives it)

# TODO

- Add ASCII animation of a sorting example using insertion-sort!
- Add key parameter to sort by key

# References

- http://en.wikipedia.org/wiki/Insertion_sort
- https://runestone.academy/ns/books/published/pythonds/SortSearch/TheInsertionSort.html
- http://www.studytonight.com/data-structures/insertion-sorting
"""

__all__ = ["insertion_sort"]


def insertion_sort(ls: list) -> None:
    """Insertion-sort in-place sorting algorithm.

    Time complexity

    +------+----------+----------+
    | Best |  Average |  Worst   |
    +------+----------+----------+
    | O(n) |   O(n²)  |   O(n²)  |
    +------+----------+----------+

    Space complexity: O(1)."""
    for i in range(1, len(ls)):
        n = i
        while n > 0 and ls[n] < ls[n - 1]:
            ls[n], ls[n - 1] = ls[n - 1], ls[n]
            n -= 1
