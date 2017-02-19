#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 01/05/2016

Updated: 19/02/2017

# Description

Testing the functions under forward_euler.py
"""

import unittest

from ands.algorithms.ode.forward_euler import *


class TestForwardEuler(unittest.TestCase):
    @staticmethod
    def f(ti, yi):
        return yi

    @staticmethod
    def gen_b(a: float, n: int, h: float) -> float:
        return h * n + a

    def setUp(self):
        # Runs before each test
        self.a = 0  # start of the range [a, b]
        self.n = 7
        self.h = 0.2  # step
        self.b = TestForwardEuler.gen_b(self.a, self.n, self.h)

    def test_forward_euler_parameters_when_are_None(self):
        self.assertRaises(ValueError, forward_euler, None, self.b, self.n, 1, TestForwardEuler.f)
        self.assertRaises(ValueError, forward_euler, self.a, None, self.n, 1, TestForwardEuler.f)
        self.assertRaises(ValueError, forward_euler, self.a, self.b, None, 1, TestForwardEuler.f)
        self.assertRaises(ValueError, forward_euler, self.a, self.b, self.n, None, TestForwardEuler.f)

    def test_forward_euler_approx_parameters_when_are_None(self):
        self.assertRaises(ValueError, forward_euler_approx, None, self.b, self.n, 1, TestForwardEuler.f)
        self.assertRaises(ValueError, forward_euler_approx, self.a, None, self.n, 1, TestForwardEuler.f)
        self.assertRaises(ValueError, forward_euler_approx, self.a, self.b, None, 1, TestForwardEuler.f)
        self.assertRaises(ValueError, forward_euler_approx, self.a, self.b, self.n, None, TestForwardEuler.f)

    def test_forward_euler_b_less_than_a(self):
        self.h = -0.2
        self.b = TestForwardEuler.gen_b(self.a, self.n, self.h)
        self.assertRaises(ValueError, forward_euler, self.a, self.b, self.n, 1, TestForwardEuler.f)

    def test_forward_euler_approx_b_less_than_a(self):
        self.h = -0.2
        self.b = TestForwardEuler.gen_b(self.a, self.n, self.h)
        self.assertRaises(ValueError, forward_euler_approx, self.a, self.b, self.n, 1, TestForwardEuler.f)

    def test_forward_euler_f_is_not_callable(self):
        self.assertRaises(TypeError, forward_euler, self.a, self.b, self.n, 1, None)

    def test_forward_euler_approx_f_is_not_callable(self):
        self.assertRaises(TypeError, forward_euler_approx, self.a, self.b, self.n, 1, None)

    def test_forward_euler_result_is_not_None(self):
        # Consider the problem y' = y, y(0) = 1,
        # the exact solution is y(t) = e^t.
        t, y = forward_euler(self.a, self.b, self.n, 1, TestForwardEuler.f)
        self.assertIsNotNone(t)
        self.assertIsNotNone(y)

    def test_forward_euler_approx_result_is_not_None(self):
        y = forward_euler_approx(self.a, self.b, self.n, 1, TestForwardEuler.f)
        self.assertIsNotNone(y)
