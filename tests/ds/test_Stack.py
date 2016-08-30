#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 01/07/16

Last Update: 01/07/16

Testing the Stack class,
using just integers as elements,
since the behaviour of adding and removing from this stack
is the same as adding and removing from a list.
"""

import unittest

from ands.ds.Stack import Stack


class TestStack(unittest.TestCase):

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())

        s.push(12)
        self.assertFalse(s.is_empty())

        top = s.pop()
        self.assertIsNotNone(top)
        self.assertEqual(top, 12)
        self.assertTrue(s.is_empty())

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)

        for i in range(100):
            s.push(i)
            self.assertEqual(s.size(), i + 1)

        size = s.size()
        while not s.is_empty():
            self.assertIsNotNone(s.pop())
            size -= 1
            self.assertEqual(s.size(), size)

        self.assertEqual(s.size(), 0)
        self.assertTrue(s.is_empty())

    def test_top(self):
        s = Stack()

        self.assertTrue(s.is_empty())
        self.assertIsNone(s.top())
        self.assertEqual(s.size(), 0)

        for i in range(-10, 1):
            s.push(i)

        size = s.size()

        for _ in range(10):
            self.assertEqual(s.top(), 0)

        self.assertFalse(s.is_empty())
        self.assertEqual(s.size(), size)

        n = 0

        while not s.is_empty():
            self.assertEqual(s.top(), n)
            n -= 1
            self.assertIsNotNone(s.pop())

        self.assertEqual(s.size(), 0)

    def test_push(self):
        s = Stack()

        s.push(None)
        self.assertEqual(s.size(), 1)
        self.assertIs(s.pop(), None)
        self.assertEqual(s.size(), 0)

        for i in range(100):
            s.push(i)
            self.assertEqual(s.top(), i)
            self.assertEqual(s.size(), i + 1)

        size = s.size()
        while not s.is_empty():
            self.assertEqual(s.size(), size)
            self.assertIsNotNone(s.pop())
            size -= 1
            self.assertEqual(s.size(), size)

        self.assertEqual(s.size(), 0)

    def test_pop(self):
        s = Stack()

        self.assertIsNone(s.pop())

        s.push(None)
        self.assertEqual(s.size(), 1)
        self.assertIsNone(s.pop())
        self.assertEqual(s.size(), 0)

        for i in range(100):
            s.push(i)

        for i in range(99, -1, -1):
            p = s.pop()
            self.assertIsNotNone(p)
            self.assertEqual(p, i)

        self.assertEqual(s.size(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
