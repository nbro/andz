#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 23/08/2015

Updated: 19/02/2017

# Description

Finding the maximum (or minimum) of a list of numbers using the "divide and conquer" strategy.

"""

__all__ = ["find_extremum_not_in_place", "find_extremum_in_place", "find_max", "find_min"]


def find_extremum_not_in_place(ls: list, _find_max: bool = True) -> object:
    """Finds (not in place) the maximum (or minimum) element in `ls`, which is assumed to be a list.

    It finds the maximum if `_find_max` is set to `True`, it finds the minimum otherwise."""
    if len(ls) == 0:
        return
    if len(ls) == 1:
        return ls[0]
    elif len(ls) == 2:
        if _find_max:
            return ls[0] if ls[0] > ls[1] else ls[1]
        else:
            return ls[0] if ls[0] < ls[1] else ls[1]
    else:
        mid = len(ls) // 2

        m1 = find_extremum_not_in_place(ls[0:mid], _find_max)
        m2 = find_extremum_not_in_place(ls[mid:], _find_max)

        if _find_max:
            return m1 if m1 > m2 else m2
        else:
            return m1 if m1 < m2 else m2


def _find_extremum_in_place(ls: list, start: int, end: int, _find_max: bool = True) -> object:
    if (end - start) < 0:
        return
    if (end - start) == 0:
        return ls[start]
    elif (end - start) == 1:
        if _find_max:
            return ls[start] if ls[start] > ls[end] else ls[end]
        else:  # find min
            return ls[start] if ls[start] < ls[end] else ls[end]
    else:
        mid = (start + end) // 2

        assert start <= mid <= end

        m1 = _find_extremum_in_place(ls, start, mid - 1, _find_max)
        m2 = _find_extremum_in_place(ls, mid, end, _find_max)

        if _find_max:
            return m1 if m1 > m2 else m2
        else:  # find min
            return m1 if m1 < m2 else m2


def find_extremum_in_place(ls: list, find_max: bool = True) -> object:
    """Finds (in place) the maximum (or minimum) element in `ls`, which is assumed to be a list.

    It finds the maximum if `find_max` is set to `True`, it finds the minimum otherwise."""
    return _find_extremum_in_place(ls, 0, len(ls) - 1, find_max)


def find_max(ls: list) -> object:
    m = find_extremum_in_place(ls)
    assert m == find_extremum_not_in_place(ls)
    return m


def find_min(ls: list) -> object:
    m = find_extremum_in_place(ls, False)
    assert m == find_extremum_not_in_place(ls, False)
    return m
