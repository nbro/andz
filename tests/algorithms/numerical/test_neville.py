#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 08/10/2017

Updated: 08/10/2017

# Description

Tests for the functions of the module neville.py.
"""

import unittest
from math import isclose, sqrt
from random import uniform
# from scipy import fabs
from scipy.interpolate import barycentric_interpolate

from ands.algorithms.numerical.neville import neville


def f(x: float) -> float:
    """f : [-1, 1] -> R."""
    return 1 / (25 * (x ** 2) + 1)


def g(x: float) -> float:
    return 1 / sqrt(x)


class TestNeville(unittest.TestCase):
    def test_lists_of_different_lengths(self):
        self.assertRaises(ValueError, neville, [1, 2], [3], 0)

    def test_f(self):
        """Interpolation of function f with a polynomial p at the equidistant points
        x[k] = −1 + 2 * (k / n), k = 0, ..., n, using Neville's algorithm."""

        n = 20  # n points, so polynomial would be of degree n - 1.
        xs = [-1 + 2 * (k / n) for k in range(n)]
        ys = [f(x) for x in xs]

        for i in range(20):
            x0 = uniform(-1.0, 1.0)

            y0 = neville(xs, ys, x0)
            bi0 = barycentric_interpolate(xs, ys, x0)

            # f0 = f(x0)
            # e0 = fabs(y0 - f(x0))
            # print("e(%d) = %f\n" % (x0, e0))

            self.assertTrue(isclose(bi0, y0))

    def test_g(self):
        """Example taken from:
        https://en.wikiversity.org/wiki/Numerical_Analysis/Neville%27s_algorithm_examples"""
        xs = [16, 64, 100]
        ys = [g(x) for x in xs]
        x0 = 81

        y0 = neville(xs, ys, x0)
        bi0 = barycentric_interpolate(xs, ys, x0)

        self.assertTrue(isclose(y0, 0.106, rel_tol=1e-02))
        self.assertTrue(isclose(bi0, y0, rel_tol=1e-02))
