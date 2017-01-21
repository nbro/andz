#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.heap_sort import heap_sort
from tests.algorithms.sorting.base_tests import *


class TestHeapSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="runTest"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, heap_sort, True)
