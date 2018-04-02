#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 18/01/2017

# Description

Testing hanoi function.
"""

import unittest

from ands.algorithms.recursion.hanoi import hanoi


class TestRecursiveHanoi(unittest.TestCase):
    def test_n0(self):
        self.assertEqual(hanoi(0), [])

    def test_n1(self):
        self.assertEqual(hanoi(1), [(1, 'A', 'C')])

    def test_n2(self):
        self.assertEqual(hanoi(2),
                         [(1, 'A', 'B'), (2, 'A', 'C'), (1, 'B', 'C')])

    def test_n3(self):
        self.assertEqual(hanoi(3), [(1, 'A', 'C'),
                                    (2, 'A', 'B'),
                                    (1, 'C', 'B'),
                                    (3, 'A', 'C'),
                                    (1, 'B', 'A'),
                                    (2, 'B', 'C'),
                                    (1, 'A', 'C')])
