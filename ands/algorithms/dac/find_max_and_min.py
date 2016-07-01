#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Finding the minimum and the maximum
of a list of numbers using the "Divide and Conquer" strategy.
"""


def find_max(ls):
    """Divide and Conquer not in-place algorithm
    to find the maximum element of a list or tuple"""

    if len(ls) == 1:
        return ls[0]
    elif len(ls) == 2:
        return ls[0] if ls[0] > ls[1] else ls[1]
    else:
        mid = len(ls) // 2
        m1 = find_max(ls[0:mid])
        m2 = find_max(ls[mid:])
        return m1 if m1 > m2 else m2


def find_min(ls):
    """'Divide and Conquer' not in-place algorithm
    to find the minimum element of a list or tuple."""

    if len(ls) == 1:
        return ls[0]
    elif len(ls) == 2:
        return ls[0] if ls[0] < ls[1] else ls[1]
    else:
        mid = len(ls) // 2
        m1 = find_min(ls[0:mid])
        m2 = find_min(ls[mid:])
        return m1 if m1 < m2 else m2


if __name__ == "__main__":
    from random import randint

    a = [randint(0, 10) for _ in range(10)]
    print("List:", a)

    print("Min:", find_min(a))
    print("Max:", find_max(a))
