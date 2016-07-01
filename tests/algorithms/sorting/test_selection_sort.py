#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.selection_sort import selection_sort
from tests.algorithms.sorting.base_tests import *


class TestSelectionSort(unittest.TestCase, SortingAlgoTests):

    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        SortingAlgoTests.__init__(self, selection_sort, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
