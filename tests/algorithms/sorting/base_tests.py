#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 20/03/2016

Updated: 04/08/2018

# Description

Common unit tests for the functions to sort sequences.
"""

from random import randint

from ands.algorithms.recursion.is_sorted import iterative_is_sorted


def build_random_list(size=10, start=-10, end=10):
    """Returns a list of random elements.
    You can specify the size of the list.
    You can also specify the range of numbers in the list."""
    return [randint(start, end) for _ in range(size)]


class SortingAlgorithmTests:
    def __init__(self, sorting_algorithm, in_place):
        self.sorting_algorithm = sorting_algorithm
        self.in_place = in_place

    def assert_commonalities(self, a):
        b = self.sorting_algorithm(a)

        if self.in_place:
            self.assertIsNone(b)
            self.assertTrue(iterative_is_sorted(a))
        else:  # In-place sorting algorithms return all None
            self.assertTrue(iterative_is_sorted(b))

    def test_empty(self):
        self.assert_commonalities([])

    def test_size_1(self):
        a = build_random_list(1)
        self.assert_commonalities(a)

    def test_size_2(self):
        a = build_random_list(2)
        self.assert_commonalities(a)

    def test_random_size(self):
        size = randint(3, 1113)
        a = build_random_list(size, -432, 1233)
        self.assert_commonalities(a)
