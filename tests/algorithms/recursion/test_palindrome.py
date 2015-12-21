#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 20/01/2017

Updated: 15/03/2022

# Description

Unit tests for the functions in the ands.algorithms.recursion.palindrome
module.
"""

import string
import unittest
from random import choice, randint

from ands.algorithms.recursion.palindrome import is_palindrome, iterative_is_palindrome


def make_test(func: callable):
    class TestIsPalindrome(unittest.TestCase):
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
            self.assertTrue(func(""))

        def test_size_1(self):
            self.assertTrue(func(TestIsPalindrome.generate_palindrome(1)))

        def test_size_2(self):
            self.assertTrue(func(TestIsPalindrome.generate_palindrome(2)))

        def test_size_2_not(self):
            self.assertFalse(func("xy"))

        def test_random_size(self):
            n = randint(3, 100)
            self.assertTrue(func(TestIsPalindrome.generate_palindrome(n)))

    return TestIsPalindrome


test_is_palindrome_recursively = make_test(is_palindrome)
test_is_palindrome_iteratively = make_test(iterative_is_palindrome)

if __name__ == "__main__":
    unittest.main()
