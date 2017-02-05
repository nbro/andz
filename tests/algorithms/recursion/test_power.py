#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado
Created: 18/01/2017

# Description

Testing the recursive power function.
"""

import unittest
from random import randint

from ands.algorithms.recursion.power import power


class TestRecursivePower(unittest.TestCase):
    # Testing raising to power of 0.

    def test_base_0_power_0(self):
        self.assertEqual(power(0, 0), 1)

    def test_base_minus_1_power_0(self):
        self.assertEqual(power(-1, 0), 1)

    def test_base_1_power_0(self):
        self.assertEqual(power(1, 0), 1)

    def test_base_random_base_power_0(self):
        self.assertEqual(power(randint(2, 100), 0), 1)
        self.assertEqual(power(randint(-100, -2), 0), 1)

    def test_base_0_power_1(self):
        self.assertEqual(power(0, 1), 0)

    def test_base_1_power_1(self):
        self.assertEqual(power(1, 1), 1)

    def test_base_minus_1_power_1(self):
        self.assertEqual(power(-1, 1), -1)

    def test_random_base_power_1(self):
        a = randint(2, 100)
        b = randint(-100, -2)
        self.assertEqual(power(a, 1), a)
        self.assertEqual(power(b, 1), b)

    def test_random_base_random_positive_power(self):
        b = randint(-100, 100)
        p = randint(2, 100)
        self.assertEqual(power(b, p), b ** p)
