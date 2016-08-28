#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

A very simple example of how to count the number occurrences
of a certain number `n` in a list `ls`.
You should not use recursion in general for doing this task,
at least in Python, because the stack limit is quite small: 1000
This is just an example of recursion!
"""


def _count(n, ls, index):
    if index < len(ls):
        if ls[index] == n:
            return 1 + _count(n, ls, index + 1)
        else:
            return _count(n, ls, index + 1)
    return 0


def count(n, ls):
    """Counts how many times `n` appears in the list or tuple `ls`."""
    return _count(n, ls, 0)


def test1():
    from random import randint
    import sys

    RECURSION_LIMIT = sys.getrecursionlimit()

    # Keep this number smaller than RECURSION_LIMIT
    LIST_SIZE = RECURSION_LIMIT - 100

    for _ in range(10):
        ls = [randint(0, 10) for _ in range(LIST_SIZE)]
        r = randint(0, 10)
        c = count(r, ls)

        if c != ls.count(r):
            raise Exception(
                "Something is wrong with the implementation of count...!")


if __name__ == "__main__":
    test1()
