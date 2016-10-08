#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
"""

import unittest
from ands.algorithms.ode.forward_euler import *
from pprint import pprint


class TestForwardEuler(unittest.TestCase):

    def __init__(self, method_name="runTest"):
        unittest.TestCase.__init__(self, method_name)

    def f(self, ti, yi):
        return yi

    def get_b(self, a, n, h):
        return h * n + a

    def test_parameters_not_none(self):
        a = 0
        n = 7
        h = 0.2
        b = self.get_b(a, n, h)
        self.assertRaises(ValueError, forward_euler, None, b, n, 1, self.f)
        self.assertRaises(ValueError, forward_euler, a, None, n, 1, self.f)
        self.assertRaises(ValueError, forward_euler, a, b, None, 1, self.f)
        self.assertRaises(ValueError, forward_euler, a, b, n, None, self.f)

    def test_b_less_than_a(self):
        a = 0
        n = 7
        h = -0.2
        b = self.get_b(a, n, h)
        self.assertRaises(ValueError, forward_euler, a, b, n, 1, self.f)

    def test_f_is_callable(self):
        a = 0
        n = 7
        h = 0.2
        b = self.get_b(a, n, h)
        self.assertRaises(TypeError, forward_euler, a, b, n, 1, None)

    def test_1(self):
        # consider the problem y' = y, y(0) = 1
        # the exact solution is y(t) = e^t.

        # should in this case mean that the step is going to be like 0.2
        a = 0
        n = 7
        h = 0.2
        b = self.get_b(a, n, h)

        t, y = forward_euler(a, b, n, 1, self.f)

        self.assertIsNotNone(t)
        self.assertIsNotNone(y)


if __name__ == "__main__":
    unittest.main(verbosity=2)