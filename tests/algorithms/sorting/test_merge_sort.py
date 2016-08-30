#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.merge_sort import merge_sort
from tests.algorithms.sorting.base_tests import *


class TestMergeSort(unittest.TestCase, SortingAlgorithmTests):

    def __init__(self, method_name="runTest"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, merge_sort, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
