#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 29/09/2017

Updated: 29/09/2017

# Description

Tests for the functions in the module ands.algorithms.numerical.newton.
"""

import unittest
from math import isclose

from ands.algorithms.numerical.newton import *


class TestNewton(unittest.TestCase):
    def test_f_not_callable(self):
        self.assertRaises(TypeError, newton, 3, 2, max)

    def test_df_not_callable(self):
        self.assertRaises(TypeError, newton, 3, max, 2)

    def test_find_square_root(self):
        a = 9  # We want to find the square root of a.
        x0 = 5
        f = lambda x: x * x - a
        df = lambda x: 2 * x
        self.assertTrue(isclose(newton(x0, f, df), 3.0,
                                rel_tol=1e-6,
                                abs_tol=0.0))

    def test_find_reciprocal(self):
        a = 2  # We want to find the reciprocal of a, i.e. 1 / a.
        x0 = 0.3
        f = lambda x: a - (1 / x)
        df = lambda x: 1 / (x * x)
        # We could also use the iteration: x_next = x * (2 - x * a).
        self.assertTrue(isclose(newton(x0, f, df), 1 / 2,
                                rel_tol=1e-6,
                                abs_tol=0.0))
