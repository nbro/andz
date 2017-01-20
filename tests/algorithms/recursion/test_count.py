#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Created: 15/01/2017

Testing the method `count` from `ands.algorithms.recursion.count`.
"""

import unittest
from random import randint

from ands.algorithms.recursion.count import count


class TestRecursiveCount(unittest.TestCase):
    def test_empty_list(self):
        ls = []
        self.assertEqual(count(7, ls), 0)

    def test_size_1(self):
        ls = [3]
        self.assertEqual(count(3, ls), 1)
        self.assertEqual(count(11, ls), 0)

    def test_size_greater_than_1(self):
        ls = [5, 2, 11, 2, 17, 29, 37, 41, 2, 5]
        self.assertEqual(count(2, ls), 3)
        self.assertEqual(count(13, ls), 0)

    def test_random_size(self):
        ls = [randint(-10, 10) for _ in range(randint(5, 15))]
        self.assertEqual(count(-11, ls), 0)
