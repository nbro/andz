#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 08/10/2017

Updated: 08/10/2017

# Description

Tests for the functions of the module ands.algorithms.numerical.barycentric.
"""

import unittest

from ands.algorithms.numerical.barycentric import barycentric
from tests.algorithms.numerical.polynomial_interpolation_tests import *


class TestBarycentric(unittest.TestCase, PolynomialInterpolationTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        PolynomialInterpolationTests.__init__(self, barycentric)
