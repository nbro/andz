#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 20/01/2017

# Description

Testing the recursive palindrome function.
"""

import string
import unittest
from random import choice, randint

from ands.algorithms.recursion.palindrome import is_palindrome


class TestRecursivePalindrome(unittest.TestCase):
    @staticmethod
    def generate_palindrome(n: int):
        """Generates a palindrome of size `n`"""
        assert n > 0
        if n == 1:
            return choice(string.ascii_letters)

        p = []
        for _ in range(n - 1):
            char = choice(string.ascii_letters)
            p.insert(len(p) // 2, char)
            p.insert(len(p) // 2, char)
        return "".join(p)

    def test_empty_str(self):
        self.assertTrue(is_palindrome(""))

    def test_size_1(self):
        self.assertTrue(
            is_palindrome(TestRecursivePalindrome.generate_palindrome(1)))

    def test_size_2(self):
        self.assertTrue(
            is_palindrome(TestRecursivePalindrome.generate_palindrome(2)))

    def test_size_2_not(self):
        self.assertFalse(is_palindrome("xy"))

    def test_random_size(self):
        n = randint(3, 100)
        self.assertTrue(
            is_palindrome(TestRecursivePalindrome.generate_palindrome(n)))
