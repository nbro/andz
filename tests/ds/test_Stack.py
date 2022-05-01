#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado
Created: 01/07/16
Updated: 04/02/2017

# Description

Tests for the Stack data structure.
"""

import unittest
from random import randint

from ands.ds.Stack import Stack


class TestStack(unittest.TestCase):
    def test_creation_default(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        self.assertTrue(s.is_empty())

    def test_creation_good_list(self):
        s = Stack(["first", 2, 3.14])
        self.assertEqual(s.size(), 3)
        self.assertFalse(s.is_empty())

    def test_creation_list_with_None(self):
        self.assertRaises(ValueError, Stack, ["first", 2, None, 3.14, None])

    def test_creation_argument_not_iterable(self):
        self.assertRaises(TypeError, Stack, 2.72)

    def test_top_empty_stack(self):
        s = Stack()
        self.assertIsNone(s.top())

    def test_push_None(self):
        s = Stack()
        self.assertRaises(ValueError, s.push, None)

    def test_push_one(self):
        s = Stack()
        s.push(3)
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.top(), 3)

    def test_push_many(self):
        s = Stack()

        for i in range(randint(2, 100)):
            s.push(i)
            self.assertEqual(s.size(), i + 1)
            self.assertFalse(s.is_empty())
            self.assertEqual(s.top(), i)

    def test_pop_empty_stack(self):
        s = Stack()
        self.assertIsNone(s.pop())

    def test_pop_last(self):
        s = Stack([7])
        self.assertEqual(s.pop(), 7)
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)

    def test_pop_until_empty(self):
        ls = [randint(-10, 10) for _ in range(randint(1, 100))]
        s = Stack(ls)

        for i, e in enumerate(reversed(ls)):
            elem = s.pop()
            self.assertEqual(elem, e)
            self.assertEqual(s.size(), len(ls) - (i + 1))

        self.assertTrue(s.is_empty())

    def test_print_stack(self):
        print("\n", repr(Stack([11, 2, 3])), sep="")
