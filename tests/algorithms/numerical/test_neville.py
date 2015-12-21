#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 08/10/2017

Updated: 08/10/2017

# Description

Unit tests for the functions in the ands.algorithms.numerical.neville module.
"""

import unittest

from ands.algorithms.numerical.neville import neville
from tests.algorithms.numerical.polynomial_interpolation_tests import *


class TestNeville(unittest.TestCase, PolynomialInterpolationTests):
    def __init__(self, method_name="__init__"):
        unittest.TestCase.__init__(self, method_name)
        PolynomialInterpolationTests.__init__(self, neville)
