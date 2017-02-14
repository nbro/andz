#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 05/02/2017

Updated: 05/02/2017

# Description

Tests for the HeapNode class in Heap.py.

"""

import unittest

from ands.ds.Heap import HeapNode


class TestHeapNode(unittest.TestCase):
    def test_creation_argument_None(self):
        self.assertRaises(ValueError, HeapNode, None)

    def test_after_default_creation_same_key_value(self):
        n = HeapNode(26)
        self.assertIsNotNone(n.value)
        self.assertEqual(n.key, n.value)

    def test_creation_with_custom_value(self):
        n = HeapNode(2, "two")
        self.assertIsNotNone(n.value)
        self.assertNotEqual(n.value, n.key)

    def test_heap_node_equal_to_itself(self):
        h = HeapNode(3, "three")
        self.assertEqual(h, h)

    def test_not_equal_when_different_values_but_same_keys(self):
        a = HeapNode("3", 3)
        b = HeapNode("3", "three")
        self.assertNotEqual(a, b)

    def test_not_equal_when_different_keys_but_same_values(self):
        a = HeapNode("1", "x")
        b = HeapNode("3", "x")
        self.assertNotEqual(a, b)

    def test_not_equal_when_different_keys_and_values(self):
        a = HeapNode(2, "x")
        b = HeapNode(3, "y")
        self.assertNotEqual(a, b)

    def test_equal_when_same_key_and_value(self):
        a = HeapNode(2, "two")
        b = HeapNode(2, "two")
        self.assertEqual(a, b)

    def test_less_than_when_key_is_smaller_and_values_equal_to_keys(self):
        a = HeapNode(12)
        b = HeapNode(14)
        self.assertLess(a, b)

    def test_greater_than_when_key_is_greater_and_values_equal_to_keys(self):
        a = HeapNode(12)
        b = HeapNode(14)
        self.assertGreater(b, a)

    def test_less_than_only_key_is_used(self):
        a = HeapNode(3, "three")
        b = HeapNode(5, "zero")
        self.assertLess(a, b)

    def test_greater_than_only_key_is_used(self):
        a = HeapNode(3, 100)
        b = HeapNode(4, "zero")
        self.assertGreater(b, a)

    def test_heap_node_not_greater_than_itself(self):
        a = HeapNode(11)
        b = HeapNode(11, "eleven")
        self.assertFalse(a > a)
        self.assertFalse(b > b)

    def test_heap_node_not_smaller_than_itself(self):
        a = HeapNode(11)
        b = HeapNode(13, "thirteen")
        self.assertFalse(a < a)
        self.assertFalse(b < b)

    def test_heap_node_is_less_than_or_equal_to_itself(self):
        a = HeapNode(2, "two")
        self.assertTrue(a <= a)
        self.assertLessEqual(a, a)

    def test_heap_node_is_greater_than_or_equal_to_itself(self):
        a = HeapNode(2, "two")
        self.assertTrue(a >= a)
        self.assertGreaterEqual(a, a)

    def test_greater_than_or_equal_keys_equal_to_values(self):
        a = HeapNode(13)
        b = HeapNode(17)
        self.assertGreaterEqual(b, a)

    def test_less_than_or_equal_keys_equal_to_values(self):
        a = HeapNode(13)
        b = HeapNode(17)
        self.assertLessEqual(a, b)

    def test_greater_than_or_equal_keys_not_equal_to_values(self):
        a = HeapNode(13, "13")
        b = HeapNode(17, "seventeen")
        self.assertGreaterEqual(b, a)

    def test_less_than_or_equal_keys_not_equal_to_values(self):
        a = HeapNode(13, "one three")
        b = HeapNode(17, "17")
        self.assertLessEqual(a, b)
