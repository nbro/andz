#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Reverse the elements of a list using recursion.
This method can also be applied to strings
and other iterables with some modifications.
"""

def _reverse(ls, i, j):
    if (j - i) >= 1:
        ls[j], ls[i] = ls[i], ls[j]
        _reverse(ls, i + 1, j - 1)
    return ls

def reverse(ls):
    """Returns the reverse of the list `ls` using recursion."""
    if len(ls) < 2:
        return ls
    else:
        return _reverse(ls, 0, len(ls) - 1)


if __name__ == "__main__":
    print(reverse([1, 2, 3]))
    
    import string
    import random
    from collections import Counter
    
    for i in range(10000):
        ls = [random.randint(0, 100) for _ in range(100)]
        # print("List:", ls)

        r = reverse(ls)
        # print("Reversed:", r)
        ls.reverse()

        # the elements of the list passed to Counter must be hashable
        if Counter(ls) != Counter(r):
            raise Exception("Something wrong with the implementation of 'reverse'")
