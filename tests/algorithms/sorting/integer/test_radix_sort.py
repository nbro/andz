#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 05/03/2022

Updated: 05/03/2022

# Description

Unit tests for the functions in the andz.algorithms.sorting.integer.radix_sort
module.
"""

import unittest

from andz.algorithms.sorting.integer.radix_sort import radix_sort
from tests.algorithms.sorting.base_tests import SortingAlgorithmTests


class TestRadixSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(
            self, radix_sort, in_place=False, start=0, end=10000
        )

    def test_raises_when_not_all_int(self):
        self.assertRaises(TypeError, self.sorting_algorithm, [1, "1"])

    def test_raises_when_not_all_elements_are_non_negative(self):
        self.assertRaises(ValueError, self.sorting_algorithm, [10, -1])


if __name__ == "__main__":
    unittest.main()
