#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 20/01/2017

Updated: 04/08/2018

# Description

Unit tests for the functions in the ands.algorithms.recursion.make_decimal
module.
"""

import string
import unittest
from random import choice, randint

from ands.algorithms.recursion.make_decimal import make_decimal


class TestMakeDecimal(unittest.TestCase):
    @staticmethod
    def generate_number(base: int):
        def build_possible_digits(base: int):
            possible_digits = list(string.digits)

            if base < 10:
                possible_digits = possible_digits[0:base]
            elif base > 10:
                possible_digits += list(string.ascii_lowercase)[0 : base - 10]

            return possible_digits

        pd = build_possible_digits(base)

        # Length of the string representing the random number in base `base`.
        length = randint(1, 10)

        return "".join([choice(pd) for _ in range(length)])

    def test_empty_number(self):
        self.assertRaises(ValueError, make_decimal, "", 11)

    def test_none_number(self):
        self.assertRaises(ValueError, make_decimal, None, 13)

    def test_base_1(self):
        self.assertRaises(ValueError, make_decimal, "3", 1)

    def test_base_37(self):
        self.assertRaises(ValueError, make_decimal, "7", 37)

    def test_random_base(self):
        # Testing the implementation of make_decimal against int()
        for _ in range(randint(100, 1000)):
            b = randint(2, 36)
            n = TestMakeDecimal.generate_number(b)
            self.assertEqual(make_decimal(n, b), int(n, b))
