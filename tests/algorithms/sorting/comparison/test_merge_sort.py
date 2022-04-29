#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 1/01/2017

Updated: 04/08/2018

# Description

Unit tests for the functions in the ands.algorithms.sorting.merge_sort module.
"""

import unittest

from ands.algorithms.sorting.comparison.merge_sort import merge_sort
from tests.algorithms.sorting.base_tests import *


class TestMergeSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, merge_sort, False)
