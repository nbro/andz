#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 29/09/2017

Updated: 29/09/2017

# Description

Unit tests for the functions in the ands.algorithms.matching.gale_shapley
module.
"""

import unittest

from ands.algorithms.matching.gale_shapley import gale_shapley


class TestGaleShapley(unittest.TestCase):
    def test_when_preferences_lists_are_empty(self):
        self.assertEqual(gale_shapley([], []), ([], []))

    def test_when_preferences_lists_sizes_mismatch(self):
        self.assertRaises(ValueError, gale_shapley, [[]], [])
        self.assertRaises(ValueError, gale_shapley, [], [[]])
        self.assertRaises(ValueError, gale_shapley, [[0, 1]], [[0]])
        self.assertRaises(ValueError, gale_shapley, [[0]], [[0, 1]])

    def test_when_preferences_lists_have_duplicates(self):
        gs = gale_shapley
        self.assertRaises(ValueError, gs, [[0, 0], [1, 0]], [[0, 1], [1, 0]])
        self.assertRaises(ValueError, gs, [[1, 0], [0, 0]], [[0, 1], [1, 0]])
        self.assertRaises(ValueError, gs, [[1, 0], [0, 1]], [[0, 0], [1, 0]])
        self.assertRaises(ValueError, gs, [[1, 0], [0, 1]], [[1, 0], [0, 0]])

    def test_when_preferences_lists_contains_out_of_range_values(self):
        gs = gale_shapley
        self.assertRaises(ValueError, gs, [[2, 0], [1, 0]], [[0, 1], [1, 0]])
        self.assertRaises(ValueError, gs, [[1, 0], [-4, 0]], [[0, 1], [1, 0]])
        self.assertRaises(ValueError, gs, [[1, 0], [0, 1]], [[10, 0], [1, 0]])
        self.assertRaises(ValueError, gs, [[1, 0], [0, 1]], [[1, 0], [-1, 0]])

    def test_when_one_man_and_woman(self):
        self.assertEqual(gale_shapley([[0]], [[0]]), ([0], [0]))

    def test_when_two_men_and_women(self):
        self.assertEqual(gale_shapley([[0, 1], [0, 1]], [[1, 0], [0, 1]]),
                         ([1, 0], [1, 0]))

    def test_when_three_men_and_women(self):
        self.assertEqual(gale_shapley([[2, 0, 1], [0, 2, 1], [0, 1, 2]],
                                      [[0, 2, 1], [2, 0, 1], [0, 1, 2]]),
                         ([2, 1, 0], [2, 1, 0]))
