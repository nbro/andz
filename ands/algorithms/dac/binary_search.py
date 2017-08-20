#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 23/08/2015

Updated: 18/08/2017

# Description

Binary search (or less commonly known as "half-interval search" or "logarithmic search")
is a "divide and conquer" search algorithm that operates on a sorted list.

Binary search compares the target value to the middle element of the list;
if they are unequal, the half in which the target cannot lie is eliminated
and the search continues on the remaining half until it is successful or the remaining half is empty.

## Example

Suppose we have the following sorted list `A` and we want to find the element `k = 3`.

    +-------------------+
    | 3 | 5 | 6 | 7 | 9 |
    +-------------------+

Then the binary-search algorithm proceeds as follows.
We look at the element in the middle of `A`, that is, in our case, it's 6.
We check if `k == 6`. Since `k == 3`, then `k != 6`.
Since the list is sorted, then `k` can only be on the left side of 6,
thus we now check in the left sub-list `A1` of `A`

    +-------+
    | 3 | 5 |
    +-------+

We again look at the middle element of the new list `A1`.
Since this list `A1` contains an even number of elements,
we can decide arbitrarily if the middle is 3 or 5 (in our case).
Let's decide that the middle element is 3.
We compare it with `k` and we find out that it's 3,
thus we have just found what we were looking for.

## Note

Depending on the application, we can decide to return either the index in the list of the target element,
or we can simply return true or false to indicate respectively that the target is or not in our list.
If we decide to return an index, if the target element is not found, we can return (for example) -1.

# Resources

- http://en.wikipedia.org/wiki/Binary_search_algorithm
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
"""

from ands.algorithms.recursion.is_sorted import pythonic_is_sorted, iterative_is_sorted

__all__ = ["linear_search", "binary_search_iteratively", "binary_search_recursively_in_place",
           "binary_search_recursively_not_in_place"]


def linear_search(ls: list, item: object) -> bool:
    """Searches for `item` in the list `ls`.

    It returns the index such that `ls[index] == item`,
    if `item` is in the list `ls`, otherwise it returns -1.

    Time complexity: O(n), where `n` is the size of `ls`."""
    assert pythonic_is_sorted(ls)
    for index, e in enumerate(ls):
        if e == item:
            return index
    return -1


def binary_search_recursively_not_in_place(ls: list, item: object) -> bool:
    """Recursively binary-searches `item` in the list `ls`,
    which is assumed to be sorted in increasing order.

    It returns true if `item` is in `ls`, false otherwise.

    Note: this algorithm uses the slice operator, which creates a sub-lists.
    slicing is an operation that runs in O(k) time."""
    assert pythonic_is_sorted(ls)
    if len(ls) == 0:  # basis
        return False
    else:
        mid = len(ls) // 2
        if ls[mid] == item:
            return True
        elif ls[mid] < item:
            return binary_search_recursively_not_in_place(ls[mid + 1:], item)
        else:
            return binary_search_recursively_not_in_place(ls[0:mid], item)


def _binary_search_recursively_in_place(ls: list, item: object, start: int, end: int) -> bool:
    # <= because if end == start,
    # then it means we're going to search on a list of size 0,
    # and thus item can't be found there.
    if end < start:
        return -1
    else:
        mid = (start + end) // 2
        if ls[mid] == item:
            return mid
        elif ls[mid] < item:
            return _binary_search_recursively_in_place(ls, item, mid + 1, end)
        else:
            return _binary_search_recursively_in_place(ls, item, start, mid - 1)


def binary_search_recursively_in_place(ls: list, item: object) -> bool:
    """Recursively binary-searches `item` in the list `ls`,
    assuming that `ls` is sorted in increasing order.

    It returns the index such that `ls[index] == item`,
    if `item` is in the list `ls`, otherwise it returns -1.

    This algorithm, as opposed to `binary_search_recursively_not_in_place`,
    does not create sub-lists during the recursion process."""
    assert iterative_is_sorted(ls)
    return _binary_search_recursively_in_place(ls, item, 0, len(ls) - 1)


def binary_search_iteratively(ls: list, item: object) -> bool:
    """Iteratively binary-searches for `item` in the `ls`,
    which is assumed to be sorted in increasing order.

    It returns the index such that `ls[index] == item`,
    if `item` is in the list `ls`, otherwise it returns -1.

    Time complexity: O(n * log(n))."""
    assert iterative_is_sorted(ls)

    if len(ls) == 0:
        return -1
    else:
        start = 0
        end = len(ls) - 1

        while start <= end:
            mid = (start + end) // 2

            if ls[mid] == item:
                return mid
            elif ls[mid] < item:  # search on the right
                start = mid + 1
            else:  # search on the left
                end = mid - 1

        return -1
