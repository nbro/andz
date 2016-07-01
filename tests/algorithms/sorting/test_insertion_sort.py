#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.insertion_sort import insertion_sort
from tests.algorithms.sorting.base_tests import *


class TestInsertionSort(unittest.TestCase, SortingAlgoTests):

    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        SortingAlgoTests.__init__(self, insertion_sort, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
