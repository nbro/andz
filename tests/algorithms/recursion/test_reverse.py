#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Created: 16/01/2017

Testing the recursive implementation of reversing a list.
"""

import unittest
from random import randint

from ands.algorithms.recursion.reverse import reverse


class TestRecursiveReverse(unittest.TestCase):
    def test_empty(self):
        l = []
        rev = reverse(l)
        self.assertIs(rev, l)
        self.assertEqual(rev, [])

    def test_size_one(self):
        l = [97]
        rev = reverse(l)
        self.assertIs(rev, l)
        self.assertEqual(rev, [97])

    def test_size_two(self):
        l = [101, 67]
        rev = reverse(l)
        self.assertIs(rev, l)
        self.assertEqual(rev, [67, 101])

    def test_greater_than_two(self):
        l = [randint(0, 100) for _ in range(100)]
        copy = l[:]  # shallow copy is ok in this case.
        rev = reverse(l)
        copy.reverse()
        self.assertIs(rev, l)
        self.assertEqual(rev, copy)


if __name__ == "__main__":
    unittest.main(verbosity=2)
