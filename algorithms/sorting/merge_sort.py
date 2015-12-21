#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Want to know more about merge sort?

- http://en.wikipedia.org/wiki/Merge_sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
"""


def merge(left: list, right: list):
    """Merges 2 sorted list in 1 single list,
    which is returned at the end.

    Time complexity: O(m),
    where m=len(left) + len(right)."""

    mid = []

    i = 0  # Used to index the left list.
    j = 0  # Used to index the right list.

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mid.append(left[i])
            i += 1
        else:
            mid.append(right[j])
            j += 1

    while i < len(left):
        mid.append(left[i])
        i += 1

    while j < len(right):
        mid.append(right[j])
        j += 1

    return mid


def merge_r(left: list, right: list):
    """Equivalent to merge, but using recursion
    and creating new sub-lists at each recursion call.

    You should use merge instead of this function,
    because the space complexity of this algorithm is higher
    than the space complexity of merge.
    """
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    elif left[0] < right[0]:
        return [left[0]] + merge_r(left[1:], right)
    else:
        return [right[0]] + merge_r(left, right[1:])


def _merge_sort_aux(ls: list):
    """Not-in-place sorting algorithm.

    Splits the original list ls
    until we have many sub-lists of one element,
    which is by the way the base case.
    
    Note that a list of 1 element is sorted by definition.
    
    Using the merge algorithm,
    we can easily merge two sorted lists of size 1,
    to obtain a merged sorted list of size 2.

    We keep merging greater sorted lists,
    until we obtain the final sorted list.

    Time complexity: O(n*log_2(n))"""

    # Base case, where "ls" contains either 1 or 0 items,
    # and it is by definition sorted.
    if len(ls) < 2:
        return ls

    # Calls merge_sort on the left half part of ls.
    left = merge_sort(ls[0:len(ls) // 2])

    # Calls merge_sort on the right half part of ls.
    right = merge_sort(ls[len(ls) // 2:])

    # Note that in the previous 2 statements,
    # we are creating new sub-lists using ls[0:len(ls)//2],
    # for the first case, for example.

    # Returns a new sorted list composed of the items in left and right.
    return merge(left, right)


def merge_sort(ls: list):
    """Not-in-place sorting algorithm.

    Time complexity: O(n*log_2(n))"""
    ls = _merge_sort_aux(ls)
    return ls