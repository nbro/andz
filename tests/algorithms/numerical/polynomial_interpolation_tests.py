#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 12/10/2017

Updated: 02/04/2018

# Description

Common units tests for the algorithms to perform polynomial interpolation.
"""

from math import sqrt
from random import uniform

import numpy as np
from scipy.interpolate import barycentric_interpolate


def f(x: float) -> float:
    """f : [-1, 1] -> R."""
    return 1 / (25 * (x**2) + 1)


def g(x: float) -> float:
    return 1 / sqrt(x)


class PolynomialInterpolationTests:
    def __init__(self, polynomial_interpolation_algorithm):
        self.algorithm = polynomial_interpolation_algorithm

    def test_lists_of_different_lengths(self):
        self.assertRaises(ValueError, self.algorithm, [1, 2], [3], 0)

    def test_f(self):
        """Interpolation of function f with a polynomial p at the equidistant
        points x[k] = −1 + 2 * (k / n), k = 0, ..., n."""

        n = 20  # n points, so polynomial would be of degree n - 1.
        xs = [-1 + 2 * (k / n) for k in range(n)]
        ys = [f(x) for x in xs]

        for i in range(20):
            x0 = uniform(-1.0, 1.0)

            y0 = self.algorithm(xs, ys, x0)
            bi0 = barycentric_interpolate(xs, ys, x0)

            self.assertAlmostEqual(bi0, np.array(y0), 4)

    def test_g(self):
        """Example taken from:
        https://en.wikiversity.org/wiki/Numerical_Analysis/Neville%27s_algorithm_examples"""
        xs = [16, 64, 100]
        ys = [g(x) for x in xs]
        x0 = 81

        y0 = self.algorithm(xs, ys, x0)
        bi0 = barycentric_interpolate(xs, ys, x0)

        self.assertAlmostEqual(bi0, np.array(y0), 4)
