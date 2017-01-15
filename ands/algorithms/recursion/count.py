#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

A very simple example of how to count the number occurrences
of a certain object `o` in a list `ls`.

You should not use recursion in general for doing this task:
for example, in Python the stack limit is quite small: 1000
This is just an example of recursive algorithm!
"""


def _count(o: object, ls, index: int) -> int:
    if index < len(ls):
        if ls[index] == o:
            return 1 + _count(o, ls, index + 1)
        else:
            return _count(o, ls, index + 1)
    return 0


def count(o: object, ls):
    """Counts how many times `o` appears in the list or tuple `ls`."""
    return _count(o, ls, 0)
