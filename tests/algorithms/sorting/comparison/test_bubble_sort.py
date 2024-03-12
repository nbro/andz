#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 1/01/2017

Updated: 04/08/2018

# Description

Unit tests for the functions in the
andz.algorithms.sorting.comparison.bubble_sort module.
"""

import unittest

from andz.algorithms.sorting.comparison.bubble_sort import bubble_sort
from tests.algorithms.sorting.base_tests import *


class TestBubbleSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, bubble_sort)
