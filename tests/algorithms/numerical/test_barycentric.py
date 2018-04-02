#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 08/10/2017

Updated: 02/04/2018

# Description

Tests for the functions of the module ands.algorithms.numerical.barycentric.
"""

import unittest

from ands.algorithms.numerical.barycentric import barycentric, compute_weights
from tests.algorithms.numerical.polynomial_interpolation_tests import *


class TestBarycentric(unittest.TestCase, PolynomialInterpolationTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        PolynomialInterpolationTests.__init__(self, barycentric)

    def test_when_weights_are_provided(self):
        # n points, so polynomial would be of degree n - 1.
        xs = [8, 16, 64]
        n = len(xs)

        # Given that we want to call barycentric multiple times with different y
        # values and different points of evaluation of the polynomial, i.e.
        # different x0's, then we pre-compute the weights and pass them to the
        # function barycentric.
        ws = compute_weights(xs)

        # f and g are functions.
        for h in [f, g]:
            ys = [h(x) for x in xs]  # Evaluate the function at all xs points.

            for x0 in [-2, 2]:
                y0 = barycentric(xs, ys, x0, ws)
                bi0 = barycentric_interpolate(xs, ys, x0)

                self.assertAlmostEqual(bi0, np.array(y0))
