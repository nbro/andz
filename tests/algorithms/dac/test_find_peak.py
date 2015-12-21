#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 10/03/2017

Updated: 10/03/2017

# Description

Unit tests for the functions in the ands.algorithms.dac.find_peak module.
"""

import unittest
from random import randint

from ands.algorithms.dac.find_peak import find_peak, find_peak_linearly


class TestFindPeak(unittest.TestCase):
    def test_find_peak_empty_list(self):
        self.assertEqual(find_peak([]), -1)
        self.assertEqual(find_peak_linearly([]), -1)

    def test_find_peak_size_1(self):
        self.assertEqual(find_peak([47]), -1)
        self.assertEqual(find_peak_linearly([47]), -1)

    def test_find_peak_size_2(self):
        self.assertEqual(find_peak([47, 59]), -1)
        self.assertEqual(find_peak_linearly([47, 59]), -1)

    def test_find_peak_size_3_no_peak(self):
        self.assertEqual(find_peak([47, 59, 71]), -1)
        self.assertEqual(find_peak_linearly([47, 59, 71]), -1)

    def test_find_peak_size_3(self):
        self.assertEqual(find_peak([47, 71, 71]), 1)
        self.assertEqual(find_peak_linearly([47, 71, 71]), 1)

    def test_find_peak_sorted_list(self):
        self.assertEqual(find_peak(list(range(100))), -1)
        self.assertEqual(find_peak_linearly(list(range(100))), -1)
        self.assertEqual(find_peak(list(range(100, -1, -1))), -1)
        self.assertEqual(find_peak_linearly(list(range(100, -1, -1))), -1)

    def test_find_peak_all_elements_are_equal(self):
        a = [randint(-100, 100)] * 10
        self.assertNotEqual(find_peak(a), -1)
        self.assertNotEqual(find_peak_linearly(a), -1)

    def test_find_peak_specific_case(self):
        a = [7, 4, 5, 6, 7, 6]
        self.assertEqual(find_peak(a), 4)
        self.assertEqual(find_peak_linearly(a), 4)
