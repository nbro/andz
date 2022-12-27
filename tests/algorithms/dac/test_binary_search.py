#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 18/02/2017

Updated: 18/02/2017

# Description

Tests for the functions in the module ands.algorithms.dac.binary_search.py

"""

import unittest
from random import randint, choice

from ands.algorithms.dac.binary_search import *


class TestBinarySearch(unittest.TestCase):
    def test_list_empty(self):
        self.assertEqual(linear_search([], 3), -1)
        self.assertEqual(binary_search_iteratively([], 3), -1)
        self.assertEqual(binary_search_recursively_in_place([], 3), -1)
        self.assertFalse(binary_search_recursively_not_in_place([], 3))

    def test_list_size_1_exists(self):
        self.assertEqual(linear_search([3], 3), 0)
        self.assertEqual(binary_search_iteratively([3], 3), 0)
        self.assertEqual(binary_search_recursively_in_place([3], 3), 0)
        self.assertTrue(binary_search_recursively_not_in_place([3], 3))

    def test_list_size_1_does_not_exist(self):
        self.assertEqual(linear_search([3], 5), -1)
        self.assertEqual(binary_search_iteratively([3], 5), -1)
        self.assertEqual(binary_search_recursively_in_place([3], 5), -1)
        self.assertFalse(binary_search_recursively_not_in_place([3], 5))

    def test_list_size_2_exists_first_place(self):
        self.assertEqual(linear_search([3, 5], 3), 0)
        self.assertEqual(binary_search_iteratively([3, 5], 3), 0)
        self.assertEqual(binary_search_recursively_in_place([3, 5], 3), 0)
        self.assertTrue(binary_search_recursively_not_in_place([3, 5], 3))

    def test_list_size_2_exists_second_place(self):
        self.assertEqual(linear_search([3, 5], 5), 1)
        self.assertEqual(binary_search_iteratively([3, 5], 5), 1)
        self.assertEqual(binary_search_recursively_in_place([3, 5], 5), 1)
        self.assertTrue(binary_search_recursively_not_in_place([3, 5], 5))

    def test_list_size_2_does_not_exist(self):
        self.assertEqual(linear_search([3, 5], 7), -1)
        self.assertEqual(binary_search_iteratively([3, 5], 7), -1)
        self.assertEqual(binary_search_recursively_in_place([3, 5], 7), -1)
        self.assertFalse(binary_search_recursively_not_in_place([3, 5], 7))

    def test_list_random_size_exists(self):
        ls = list(range(randint(3, 10000)))
        item = choice(ls)
        index = ls.index(item)

        self.assertEqual(linear_search(ls, item), index)
        self.assertEqual(binary_search_iteratively(ls, item), index)
        self.assertEqual(binary_search_recursively_in_place(ls, item), index)
        self.assertTrue(binary_search_recursively_not_in_place(ls, item))

    def test_list_random_size_does_not_exist_upper(self):
        upper = 10000
        ls = list(range(randint(3, upper)))
        self.assertEqual(linear_search(ls, upper), -1)
        self.assertEqual(binary_search_iteratively(ls, upper), -1)
        self.assertEqual(binary_search_recursively_in_place(ls, upper), -1)
        self.assertFalse(binary_search_recursively_not_in_place(ls, upper))

    def test_list_random_size_does_not_exist_lower(self):
        ls = list(range(randint(3, 10000)))
        self.assertEqual(linear_search(ls, -1), -1)
        self.assertEqual(binary_search_iteratively(ls, -1), -1)
        self.assertEqual(binary_search_recursively_in_place(ls, -1), -1)
        self.assertFalse(binary_search_recursively_not_in_place(ls, -1))
