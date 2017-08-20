#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 23/07/2015

Updated: 20/08/2017

# Description

It is a simple sorting algorithm which sorts a list by shifting elements one by one.
Following are some of the important characteristics of insertion-sort.

1. It has one of the simplest implementations

2. It is efficient for smaller lists, but inefficient for larger ones (compared to quick-sort, heap-sort or merge-sort).

3. insertion-sort is adaptive, that means it reduces its total number of steps if given a partially sorted list,
hence it increases its efficiency.

4. It is stable, as it does not change the relative order of elements with equal keys.

5. It's better than bubble-sort for almost-ordered lists, even though both have a best-case time complexity of O(n).

# TODO

- Add ASCII animation of a sorting example using insertion-sort!

# References

- http://www.studytonight.com/data-structures/insertion-sorting
- http://en.wikipedia.org/wiki/Insertion_sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
"""

__all__ = ["insertion_sort"]


def insertion_sort(ls: list) -> None:
    """Insertion-sort in-place sorting algorithm.

    Time complexity

    +------+----------+----------+
    | Best |  Average |  Worst   |
    +------+----------+----------+
    | O(n) |  O(n^2)  |  O(n^2)  |
    +------+----------+----------+

    Space complexity: O(1).

    Note: space complexity is O(1), but not considering memory for original list `ls`!"""
    for i in range(1, len(ls)):
        n = i
        while n > 0 and ls[n] < ls[n - 1]:
            ls[n], ls[n - 1] = ls[n - 1], ls[n]
            n -= 1
