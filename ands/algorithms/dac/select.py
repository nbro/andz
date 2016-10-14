#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Find an element x in a list,
such that at most k elements of the list are less than x.
"""


def partition(ls: list, start: int, end: int):
    """Partition algorithm used also by the quick-sort algorithm.
    It basically returns the index i of a number in ls,
    such that all elements on the left of ls[i] are less than ls[i],
    and all elements on the right of ls[i] are greater than ls[i].
    """
    pivot = ls[end]
    p = start

    for i in range(start, end):
        if ls[i] <= pivot:
            ls[p], ls[i] = ls[i], ls[p]
            p += 1

    ls[p], ls[end] = ls[end], ls[p]
    return p


def select(ls: list, k: int):
    """Find an element x in ls,
    such that at most k elements of ls are less than x.
    """
    p = partition(ls, 0, len(ls) - 1)  # p := pivot's index

    if p == k:
        return ls[p]
    elif p > k:
        return select(ls[0:p], k)
    else:  # p < k
        return select(ls[p + 1:], k - p - 1)


if __name__ == "__main__":
    from random import randint

    a = [randint(0, 10) for _ in range(10)]
    print("List:", a)

    print("Selected:", select(a, 4))
