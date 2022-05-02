#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 29/09/2017

Updated: 30/09/2017

# Description

Tests for the functions in the module ands.algorithms.numerical.horner.
"""

import unittest
from random import randint, uniform

from numpy.polynomial.polynomial import polyval

from ands.algorithms.numerical.horner import horner


class TestHorner(unittest.TestCase):
    def setUp(self):
        self.x0 = uniform(-10.0, -10.0)
        self.degree = randint(0, 30)  # degree of the polynomial

        # We have one more coefficient than the degree of the polynomial.
        self.coefficients = [uniform(-10, 10) for _ in range(self.degree + 1)]

    def test_one(self):
        self.assertAlmostEqual(horner(self.x0, self.coefficients),
                               polyval(self.x0, self.coefficients))
