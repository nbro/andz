#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ands.algorithms.sorting.bubble_sort import bubble_sort
from tests.algorithms.sorting.base_tests import *


class TestBubbleSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="runTest"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, bubble_sort, True)