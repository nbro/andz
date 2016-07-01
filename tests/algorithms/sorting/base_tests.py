#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randrange, randint


def get_list(size=10, start=1, end=10):
    """Returns a list of random elements.
    You can specify the size of the list.
    You can also specify the range of numbers in the list."""
    return [randrange(start, end) for x in range(size)]


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


class SortingAlgoTests:

    def __init__(self, sorting_algo, in_place):
        self.sorting_algo = sorting_algo
        self.in_place = in_place

    def assert_commonalities(self, ls):
        ls2 = self.sorting_algo(ls)

        if self.in_place:
            self.assertIs(ls, ls2)

        self.assertTrue(is_sorted(ls2))

    def test_empty(self):
        ls = get_list(0, -100, 100)
        self.assertEqual(len(ls), 0)
        self.assert_commonalities(ls)

    def test_when_size_1(self):
        ls = get_list(1, -100, 100)
        self.assertEqual(len(ls), 1)
        self.assert_commonalities(ls)

    def test_when_size_2(self):
        ls = get_list(2, -100, 100)
        self.assertEqual(len(ls), 2)
        self.assert_commonalities(ls)

    def test_when_size_1000(self):
        ls = get_list(1000, -30, 30)
        self.assertEqual(len(ls), 1000)
        self.assert_commonalities(ls)

    def test_when_random_size(self):
        for i in range(10):
            n = randint(0, 1000)
            ls = get_list(n, -100, 100)
            self.assertEqual(len(ls), n)
            self.assert_commonalities(ls)
