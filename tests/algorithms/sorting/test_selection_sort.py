#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.selection_sort import selection_sort
from tests.algorithms.sorting.base_tests import *


class TestSelectionSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="runTest"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, selection_sort, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
