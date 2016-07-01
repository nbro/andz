#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.quick_sort import quick_sort
from tests.algorithms.sorting.base_tests import *


class TestQuickSort(unittest.TestCase, SortingAlgoTests):

    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        SortingAlgoTests.__init__(self, quick_sort, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
