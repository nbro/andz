#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 10/03/2017

Updated: 10/03/2017

# Description

Unit tests for the functions in the andz.algorithms.dac.select module.
"""

import unittest
from random import randint, randrange, sample

from andz.algorithms.dac.select import select


class TestSelect(unittest.TestCase):
    def test_when_empty_list(self):
        # No matter which value for k, with an empty list ValueError is always raised.
        self.assertRaises(ValueError, select, [], 2)

    def test_when_list_size_1_invalid_k(self):
        self.assertRaises(ValueError, select, [3], 1)
        self.assertRaises(ValueError, select, [3], -1)

    def test_when_list_size_2_invalid_k(self):
        self.assertRaises(ValueError, select, [3, 5], 2)
        self.assertRaises(ValueError, select, [3, 5], -1)

    def test_when_list_size_1_k_is_zero(self):
        self.assertEqual(select([7], 0), 7)

    def test_when_list_size_2_k_is_zero(self):
        self.assertEqual(select([7, 5], 0), 5)
        self.assertEqual(select([5, 7], 0), 5)

    def test_when_list_random_size_k_is_zero(self):
        a = [randint(-100, 100) for _ in range(randint(3, 100))]
        self.assertEqual(select(a, 0), min(a))

    def test_when_list_random_size_all_elements_equal(self):
        x = randint(-100, 100)
        a = [x] * randint(1, 100)
        self.assertEqual(select(a, randint(0, len(a) - 1)), x)

    def test_when_list_random_size_random_k(self):
        a = sample(range(100), 100)
        self.assertIn(select(a, randrange(0, len(a))), a)
