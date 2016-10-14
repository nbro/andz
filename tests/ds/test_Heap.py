#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 14/02/16

Last update: 06/09/16

Tests for the abstract class Heap.
"""

import unittest

from ands.ds.Heap import Heap, HeapNode


class TestHeap(unittest.TestCase):
    def test_heap_creation(self):
        self.assertRaises(NotImplementedError, Heap, [12, 14, 28])
        self.assertIsNotNone(Heap())
        self.assertEqual(Heap().heap, [])
        self.assertEqual(Heap([]).heap, [])


class TestHeapNode(unittest.TestCase):
    def test_None(self):
        self.assertRaises(ValueError, HeapNode, None)

    def test_creation_key_value_same(self):
        n = HeapNode(26)
        self.assertIsNotNone(n.value)
        self.assertEqual(n.key, n.value)

    def test_creation_key_value_different(self):
        n = HeapNode(2, "two")
        self.assertIsNotNone(n.value)
        self.assertNotEqual(n.value, n.key)

    def test_less_and_greater_than(self):
        h = HeapNode(12)
        h2 = HeapNode(14)
        h3 = HeapNode(12, "Twelve")

        self.assertLess(h, h2)
        self.assertGreater(h2, h)
        self.assertLess(h3, h2)
        self.assertGreater(h2, h3)
        self.assertFalse(h < h)
        self.assertFalse(h > h)
        self.assertFalse(h2 < h2)
        self.assertFalse(h2 > h2)
        self.assertFalse(h3 < h3)
        self.assertFalse(h3 > h3)

    def test_equal_not_equal(self):
        h = HeapNode(12)
        h2 = HeapNode(14)
        h3 = HeapNode(12)
        h4 = HeapNode(14, "fourteen")

        self.assertEqual(h, h)
        self.assertEqual(h4, h4)
        self.assertEqual(h, h3)
        self.assertNotEqual(h, h2)
        self.assertNotEqual(h3, h2)
        self.assertNotEqual(h2, h4)
        self.assertEqual(h4, HeapNode(14, "fourteen"))
        self.assertNotEqual(h4, HeapNode("fourteen", 14))

    def test_less_and_greater_or_equal(self):
        h = HeapNode(12)
        h2 = HeapNode(14)
        h3 = HeapNode(12, "Twelve")

        self.assertLessEqual(h, h3)
        self.assertLessEqual(h3, h)
        self.assertGreaterEqual(h, h3)
        self.assertGreaterEqual(h3, h)
        self.assertLessEqual(h3, h3)
        self.assertLessEqual(h2, h2)
        self.assertLessEqual(h, h)


if __name__ == "__main__":
    unittest.main(verbosity=2)
