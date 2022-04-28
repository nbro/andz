#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 03/03/2022

Updated: 03/03/2022

# Description

Unit tests for the functions in the
ands.algorithms.sorting.integer.counting_sort module.
"""

import unittest

from ands.algorithms.sorting.integer.counting_sort import counting_sort
from tests.algorithms.sorting.base_tests import SortingAlgorithmTests


class TestCountingSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, counting_sort,
                                       in_place=False,
                                       start=0,
                                       end=10000)

    def test_raises_when_not_all_int(self):
        self.assertRaises(TypeError, self.sorting_algorithm, [1, "1"])

    def test_raises_when_k_is_not_non_negative(self):
        self.assertRaises(ValueError, self.sorting_algorithm, [1], -1)

    def test_raises_when_not_all_elements_are_less_than_k(self):
        self.assertRaises(ValueError, self.sorting_algorithm, [10, 1], 3)

    def test_raises_when_not_all_elements_are_non_negative(self):
        self.assertRaises(ValueError, self.sorting_algorithm, [10, -1])
