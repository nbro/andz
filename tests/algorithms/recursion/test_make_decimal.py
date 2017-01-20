#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Created: 20/01/2017
"""

import string
import unittest
from random import randint, choice

from ands.algorithms.recursion.make_decimal import make_decimal


class TestMakeDecimal(unittest.TestCase):
    def generate_number(self, base: int):

        def build_possible_digits(base: int):
            possible_digits = list(string.digits)

            if base < 10:
                possible_digits = possible_digits[0:base]
            elif base > 10:
                possible_digits += list(string.ascii_lowercase)[0:base - 10]

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
        for i in range(randint(100, 1000)):
            b = randint(2, 36)
            n = self.generate_number(b)
            self.assertEqual(make_decimal(n, b), int(n, b))
