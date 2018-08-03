#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 21/01/2017

Updated: 04/08/2018

# Description

Unit tests for the functions in the ands.algorithms.recursion.is_sorted module.
"""

import unittest
from random import randint

from ands.algorithms.recursion.is_sorted import *


class TestIsSorted(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(is_sorted([]))
        self.assertTrue(is_sorted([], True))

        self.assertTrue(iterative_is_sorted([]))
        self.assertTrue(iterative_is_sorted([], True))

        self.assertTrue(pythonic_is_sorted([]))
        self.assertTrue(pythonic_is_sorted([], True))

    def test_empty_tuple(self):
        self.assertTrue(is_sorted(()))
        self.assertTrue(is_sorted((), True))

        self.assertTrue(iterative_is_sorted(()))
        self.assertTrue(iterative_is_sorted((), True))

        self.assertTrue(pythonic_is_sorted(()))
        self.assertTrue(pythonic_is_sorted((), True))

    def test_size_1_list(self):
        r = randint(-10, 10)
        self.assertTrue(is_sorted([r]))
        self.assertTrue(is_sorted([r], True))

        self.assertTrue(iterative_is_sorted([r]))
        self.assertTrue(iterative_is_sorted([r], True))

        self.assertTrue(pythonic_is_sorted([r]))
        self.assertTrue(pythonic_is_sorted([r], True))

    def test_size_1_tuple(self):
        r = randint(-10, 10)
        self.assertTrue(is_sorted((r,)))
        self.assertTrue(is_sorted((r,), True))

        self.assertTrue(iterative_is_sorted((r,)))
        self.assertTrue(iterative_is_sorted((r,), True))

        self.assertTrue(pythonic_is_sorted((r,)))
        self.assertTrue(pythonic_is_sorted((r,), True))

    def test_size_2_list_sorted(self):
        ls = [13, 19]

        self.assertTrue(is_sorted(ls))
        self.assertFalse(is_sorted(ls, True))

        self.assertTrue(iterative_is_sorted(ls))
        self.assertFalse(iterative_is_sorted(ls, True))

        self.assertTrue(pythonic_is_sorted(ls))
        self.assertFalse(pythonic_is_sorted(ls, True))

    def test_size_2_list_rev(self):
        ls = [23, 11]

        self.assertFalse(is_sorted(ls))
        self.assertTrue(is_sorted(ls, True))

        self.assertFalse(iterative_is_sorted(ls))
        self.assertTrue(iterative_is_sorted(ls, True))

        self.assertFalse(pythonic_is_sorted(ls))
        self.assertTrue(pythonic_is_sorted(ls, True))

    def test_size_2_tuple_sorted(self):
        tup = (13, 19)

        self.assertTrue(is_sorted(tup))
        self.assertFalse(is_sorted(tup, True))

        self.assertTrue(iterative_is_sorted(tup))
        self.assertFalse(iterative_is_sorted(tup, True))

        self.assertTrue(pythonic_is_sorted(tup))
        self.assertFalse(pythonic_is_sorted(tup, True))

    def test_size_2_tuple_rev(self):
        tup = (23, 11)

        self.assertFalse(is_sorted(tup))
        self.assertTrue(is_sorted(tup, True))

        self.assertFalse(iterative_is_sorted(tup))
        self.assertTrue(iterative_is_sorted(tup, True))

        self.assertFalse(pythonic_is_sorted(tup))
        self.assertTrue(pythonic_is_sorted(tup, True))

    def test_random_size_list_sorted(self):
        ls = [randint(-100, 100) for _ in range(randint(3, 300))]
        ls.sort()
        self.assertTrue(is_sorted(ls))
        self.assertTrue(iterative_is_sorted(ls))
        self.assertTrue(pythonic_is_sorted(ls))

    def test_random_size_list_rev(self):
        ls = [randint(-100, 100) for _ in range(randint(3, 300))]
        ls.sort(reverse=True)
        self.assertTrue(is_sorted(ls, True))
        self.assertTrue(iterative_is_sorted(ls, True))
        self.assertTrue(pythonic_is_sorted(ls, True))

    def test_random_size_tuple_sorted(self):
        tup = [randint(-100, 100) for _ in range(randint(3, 300))]
        tup.sort()
        tup = tuple(tup)

        self.assertTrue(is_sorted(tup))
        self.assertTrue(iterative_is_sorted(tup))
        self.assertTrue(pythonic_is_sorted(tup))

    def test_random_size_tuple_rev(self):
        tup = [randint(-100, 100) for _ in range(randint(3, 300))]
        tup.sort(reverse=True)
        tup = tuple(tup)

        self.assertTrue(is_sorted(tup, True))
        self.assertTrue(iterative_is_sorted(tup, True))
        self.assertTrue(pythonic_is_sorted(tup, True))
