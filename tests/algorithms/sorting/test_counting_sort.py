#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 03/03/2022

Updated: 03/03/2022

# Description

Unit tests for the functions in the ands.algorithms.sorting.counting_sort
module.
"""

import unittest

from ands.algorithms.sorting.counting_sort import counting_sort
from tests.algorithms.sorting.base_tests import *


class TestCountingSort(unittest.TestCase, SortingAlgorithmTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        SortingAlgorithmTests.__init__(self, counting_sort,
                                       in_place=False,
                                       start=0,
                                       end=10000)
