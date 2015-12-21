#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 18/01/2017

Updated: 04/08/2018

# Description

Unit tests for the functions in the ands.algorithms.recursion.ackermann module.
"""

import unittest

from ands.algorithms.recursion.ackermann import ackermann


class TestAckermann(unittest.TestCase):
    # m is the first parameter to the Ackermann function
    # whereas n is the second one.

    def test_m0_n0(self):
        self.assertEqual(ackermann(0, 0), 1)

    def test_m0_n1(self):
        self.assertEqual(ackermann(0, 1), 2)

    def test_m0_n2(self):
        self.assertEqual(ackermann(0, 2), 3)

    def test_m1_n0(self):
        self.assertEqual(ackermann(1, 0), 2)

    def test_m1_n1(self):
        self.assertEqual(ackermann(1, 1), 3)

    def test_m1_n2(self):
        self.assertEqual(ackermann(1, 2), 4)

    def test_m2_n0(self):
        self.assertEqual(ackermann(2, 0), 3)

    def test_m2_n1(self):
        self.assertEqual(ackermann(2, 1), 5)

    def test_m2_n2(self):
        self.assertEqual(ackermann(2, 2), 7)
