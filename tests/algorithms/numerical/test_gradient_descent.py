#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 26/10/2017

Updated: 26/10/2017

# Description

Unittests for the functions inside ands.algorithms.numerical.gradient_descent.py.
"""

import unittest

from ands.algorithms.numerical.gradient_descent import *

'''
def f(x: float) -> float:
    return x ** 4 - 3 * x ** 3 + 2
'''


def df(x: float) -> float:
    """Derivative of f."""
    return 4 * x ** 3 - 9 * x ** 2


class TestGradientDescent(unittest.TestCase):
    def test_type_error_when_df_not_callable(self):
        self.assertRaises(TypeError, gradient_descent, 0.3, 5)

    def test_find_local_min_of_f(self):
        self.assertAlmostEqual(gradient_descent(6, df), 2.24674, 5)
