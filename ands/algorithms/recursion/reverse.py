#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Created: 2015

Last update: 16/01/2017

Reverses in-place the elements of a list using recursion.
This method could also be adapted to work with other mutable collections.
"""

__all__ = ["reverse"]


def _reverse(ls: list, i: int, j: int) -> list:
    if (j - i) >= 1:
        ls[j], ls[i] = ls[i], ls[j]
        _reverse(ls, i + 1, j - 1)
    return ls


def reverse(ls: list) -> list:
    """Returns the reverse of the list `ls` using recursion."""
    if len(ls) < 2:
        return ls
    else:
        return _reverse(ls, 0, len(ls) - 1)
