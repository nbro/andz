#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Modified: 03/02/16

This file contains some helper functions for sorting algorithms,
and some templates for testing them.
"""

from random import randrange


def is_sorted(ls, rev=False):
    """Checks if a list of numbers is sorted.

    Set `rev=True`, if you want to check ls is sorted in decreasing order.
    Default behaviour, `rev=False`, checks if ls is sorted in increasing order.

    **Time Complexity**: O(n)."""
    for i in range(len(ls) - 1):
        if rev:
            if ls[i + 1] > ls[i]:
                return False
        else:
            if ls[i + 1] < ls[i]:
                return False
    return True


def reverse(ls):
    """Reverses the elements of `ls`.
    Note that you can simply use the reverse function
    of each list object.

    **Time Complexity**: O(n)."""
    for s, e in enumerate(range(len(ls) - 1, len(ls) // 2 - 1, -1)):
        ls[s], ls[e] = ls[e], ls[s]


def get_list(size=10, start=1, end=10):
    """Returns a list of random elements.
    You can specify the size of the list.
    You can also specify the range of numbers in the list."""
    return [randrange(start, end) for x in range(size)]

def run_tests(sorting_algo, in_place=True):
    """Runs some tests for a sorting algorithm `sorting_algo`
    that must return a reference to the list that it should sort."""
    def test_empty():
        ls = get_list(0, -100, 100)
        assert len(ls) == 0
        ls2 = sorting_algo(ls)
        if in_place:
            assert ls == ls2
            assert is_sorted(ls)
        else:
            assert is_sorted(ls2)
        print("test_empty finished.")

    def test1():    
        ls = get_list(1, -100, 100)
        assert len(ls) == 1
        ls2 = sorting_algo(ls)
        if in_place:
            assert ls == ls2
            assert is_sorted(ls)
        else:
            assert is_sorted(ls2)
        print("test1 finished.")

    def test2():    
        ls = get_list(2, -100, 100)
        assert len(ls) == 2
        ls2 = sorting_algo(ls)
        if in_place:
            assert ls == ls2
            assert is_sorted(ls)
        else:
            assert is_sorted(ls2)
        print("test2 finished.")
        
    def test3():
        ls = get_list(1000, -30, 30)
        assert len(ls) == 1000
        ls2 = sorting_algo(ls)
        if in_place:
            assert ls == ls2
            assert is_sorted(ls)
        else:
            assert is_sorted(ls2)
        print("test3 finished.")

    test_empty()
    test1()
    test2()
    test3()

    
if __name__ == "__main__":
    pass
