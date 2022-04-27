#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 22/07/2015

Updated: 15/03/2022

# Description

Reverses in-place the elements of a list using recursion.

This method could also be adapted to work with other mutable collections.

# TODO

- Implement the iterative versions with slicing, i.e. s[::-1], and without it.
"""

__all__ = ["reverse"]


def _reverse_aux(ls: list, i: int, j: int) -> list:
    if (j - i) >= 1:
        ls[j], ls[i] = ls[i], ls[j]
        _reverse_aux(ls, i + 1, j - 1)
    return ls


def reverse(ls: list) -> list:
    """Returns the reverse of the list ls using recursion."""
    if len(ls) < 2:
        return ls
    else:
        return _reverse_aux(ls, 0, len(ls) - 1)
