"""
# Meta-info

Author: Nelson Brochado

Created: 28/03/2022

Updated: 28/03/2022

# Description

Unit tests for the functions in the andz.algorithms.ds.fibonacci module.
"""

import unittest
from random import randint, random

from andz.algorithms.dp.fibonacci import (
    bottom_up_fibonacci,
    memoized_fibonacci,
    recursive_fibonacci,
)


class TestFibonacci(unittest.TestCase):
    def test_input_is_not_integer(self):
        n = random()
        self.assertRaises(TypeError, recursive_fibonacci, n)
        self.assertRaises(TypeError, memoized_fibonacci, n)
        self.assertRaises(TypeError, bottom_up_fibonacci, n)

    def test_input_is_negative(self):
        n = randint(-1000, -1)
        self.assertRaises(ValueError, recursive_fibonacci, n)
        self.assertRaises(ValueError, memoized_fibonacci, n)
        self.assertRaises(ValueError, bottom_up_fibonacci, n)

    def test_fib_0(self):
        self.assertEqual(recursive_fibonacci(0), 0)
        self.assertEqual(memoized_fibonacci(0), 0)
        self.assertEqual(bottom_up_fibonacci(0), 0)

    def test_fib_1(self):
        self.assertEqual(recursive_fibonacci(1), 1)
        self.assertEqual(memoized_fibonacci(1), 1)
        self.assertEqual(bottom_up_fibonacci(1), 1)

    def test_fib_2(self):
        self.assertEqual(recursive_fibonacci(2), 1)
        self.assertEqual(memoized_fibonacci(2), 1)
        self.assertEqual(bottom_up_fibonacci(2), 1)

    def test_fib_n(self):
        n = randint(3, 30)
        fib_n = recursive_fibonacci(n)
        self.assertEqual(fib_n, memoized_fibonacci(n))
        self.assertEqual(fib_n, bottom_up_fibonacci(n))

    def test_when_return_seq_is_true(self):
        self.assertIsInstance(bottom_up_fibonacci(4, return_seq=True), list)

    def test_when_return_seq_is_true_and_n_is_zero(self):
        self.assertEqual(bottom_up_fibonacci(0, return_seq=True), [0])

    def test_when_return_seq_is_true_and_n_is_one(self):
        self.assertEqual(bottom_up_fibonacci(1, return_seq=True), [0, 1])

    def test_when_return_seq_is_true_and_n_is_two(self):
        self.assertEqual(bottom_up_fibonacci(2, return_seq=True), [0, 1, 1])

    def test_when_return_seq_is_true_and_n_is_three(self):
        self.assertEqual(bottom_up_fibonacci(3, return_seq=True), [0, 1, 1, 2])
