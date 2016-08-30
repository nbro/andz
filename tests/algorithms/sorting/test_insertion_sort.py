#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.insertion_sort import insertion_sort
from tests.algorithms.sorting.base_tests import *


class TestInsertionSort(unittest.TestCase, SortingAlgorithmTests):

    def __init__(self, method_name="runTest"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, insertion_sort, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
