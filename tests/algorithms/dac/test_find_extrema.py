#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 19/02/2017

Updated: 19/02/2017

# Description

Unit tests for the functions in the ands.algorithms.dac.find_extrema module.
"""

import unittest
from random import randint

from ands.algorithms.dac.find_extrema import *


class TestFindExtrema(unittest.TestCase):
    def test_list_empty(self):
        self.assertIsNone(find_max([]))
        self.assertIsNone(find_min([]))

    def test_list_size_1(self):
        self.assertEqual(find_max([13]), 13)
        self.assertEqual(find_min([13]), 13)

    def test_list_size_2_max_is_first_min_is_second(self):
        self.assertEqual(find_max([13, 11]), 13)
        self.assertEqual(find_min([13, 11]), 11)

    def test_list_size_2_max_is_second_min_is_first(self):
        self.assertEqual(find_max([13, 19]), 19)
        self.assertEqual(find_min([13, 19]), 13)

    def test_list_random_size_max_is_first_min_is_last(self):
        ls = list(range(randint(3, 1000), -1, -1))
        self.assertEqual(find_max(ls), ls[0])
        self.assertEqual(find_min(ls), ls[-1])

    def test_list_random_size_max_is_last_min_is_first(self):
        ls = list(range(randint(3, 1000)))
        self.assertEqual(find_max(ls), ls[-1])
        self.assertEqual(find_min(ls), ls[0])

    def test_list_random_size_max_and_min_are_somewhere(self):
        ls = [randint(-100, 100) for _ in range(3, 1000)]
        self.assertEqual(find_max(ls), max(ls))
        self.assertEqual(find_min(ls), min(ls))
