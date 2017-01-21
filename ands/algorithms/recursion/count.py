#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado

Created: 2015

Updated: 21/01/2017

## Description

A very simple example of how to count the number occurrences
of a certain object `o` in a list `ls`.

You should not use recursion in general for doing this task:
for example, in Python the stack limit is quite small: 1000
This is just an example of recursive algorithm!
"""

__all__ = ["count"]


def _count(elem: object, ls, index: int) -> int:
    if index < len(ls):
        if ls[index] == elem:
            return 1 + _count(elem, ls, index + 1)
        else:
            return _count(elem, ls, index + 1)
    return 0


def count(elem: object, ls) -> int:
    """Counts how many times `elem` appears in the list or tuple `ls`."""
    return _count(elem, ls, 0)
