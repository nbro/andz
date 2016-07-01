#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.merge_sort import merge_sort
from tests.algorithms.sorting.base_tests import *


class TestMergeSort(unittest.TestCase, SortingAlgoTests):

    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        SortingAlgoTests.__init__(self, merge_sort, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
