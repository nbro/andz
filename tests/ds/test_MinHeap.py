#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 14/02/2016

Updated: 12/03/2017

# Description

Unit tests for the classes and functions in the ands.ds.MinHeap module.
"""

import unittest
from random import choice, randint, sample

from ands.ds.MinHeap import MinHeap, is_min_heap


class TestMinHeap(unittest.TestCase):
    def test_heap_creation_default(self):
        h = MinHeap()
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size, 0)

    def test_heap_creation_given_list(self):
        a = [12, 14, 28, 6, 7, 10, 18]
        h = MinHeap(a)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, len(a))

    def test_clear_empty_heap(self):
        h = MinHeap()
        self.assertIsNone(h.clear())
        self.assertEqual(h.size, 0)
        self.assertTrue(h.is_empty())

    def test_clear_heap_of_random_size(self):
        h = MinHeap([randint(-100, 100) for _ in range(100)])
        self.assertIsNone(h.clear())
        self.assertEqual(h.size, 0)
        self.assertTrue(h.is_empty())

    def test_add_when_argument_is_None(self):
        h = MinHeap()
        self.assertRaises(ValueError, h.add, None)

    def test_add_add_one(self):
        h = MinHeap()
        self.assertIsNone(h.add(2))
        self.assertEqual(h.size, 1)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.find_min(), 2)

    def test_add_multiple_elements(self):
        a = [randint(-100, 100) for _ in range(100)]
        h = MinHeap()

        for i, elem in enumerate(a):
            self.assertIsNone(h.add(elem))
            self.assertEqual(h.size, i + 1)

        self.assertFalse(h.is_empty())
        self.assertEqual(h.find_min(), min(a))

    def test_contains_when_argument_is_None(self):
        h = MinHeap()
        self.assertRaises(ValueError, h.contains, None)

    def test_contains_when_empty_heap(self):
        h = MinHeap()
        self.assertFalse(h.contains(3))

    def test_contains_true(self):
        h = MinHeap([6, 8, 2, 2, 60, 7, 9])
        self.assertTrue(h.contains(2))

    def test_contains_false(self):
        h = MinHeap([6, 8, 2, 60, 7, 9, 3, 67])
        self.assertFalse(h.contains(10))

    def test_delete_when_argument_is_None(self):
        self.assertRaises(ValueError, MinHeap().delete, None)

    def test_delete_when_elem_does_not_exist(self):
        self.assertRaises(LookupError, MinHeap().delete, 3)

    def test_delete_when_elem_is_last(self):
        h = MinHeap([3, 4])
        self.assertIsNone(h.delete(4))
        self.assertTrue(is_min_heap(h))
        self.assertEqual(h.size, 1)
        self.assertFalse(h.is_empty())

    def test_delete_all_when_heap_of_random_size(self):
        size = randint(3, 100)
        a = [randint(-100, 100) for _ in range(size)]
        h = MinHeap(a)

        for _ in range(size):
            self.assertIsNone(h.delete(choice(a)))
            self.assertTrue(is_min_heap(h))

        self.assertEqual(h.size, 0)
        self.assertTrue(h.is_empty())

    def test_find_min_when_empty_heap(self):
        h = MinHeap()
        self.assertIsNone(h.find_min())

    def test_find_min_when_heap_has_size_1(self):
        h = MinHeap([5])
        self.assertEqual(h.find_min(), 5)

    def test_find_min_when_heap_has_size_2(self):
        h = MinHeap([13, 7])
        self.assertEqual(h.find_min(), 7)

    def test_find_min_when_heap_has_random_size(self):
        a = [randint(-100, 100) for _ in range(3, 100)]
        h = MinHeap(a)
        self.assertEqual(h.find_min(), min(a))

    def test_remove_min_when_empty_heap(self):
        h = MinHeap()
        self.assertIsNone(h.remove_min())

    def test_remove_min_when_heap_has_size_1(self):
        h = MinHeap([13])
        self.assertEqual(h.remove_min(), 13)
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size, 0)

    def test_remove_min_when_heap_has_size_2(self):
        h = MinHeap([11, 13])
        self.assertEqual(h.remove_min(), 11)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, 1)

    def test_remove_min_when_heap_has_random_size(self):
        size = randint(3, 100)
        a = [randint(-100, 100) for _ in range(size)]
        h = MinHeap(a)
        m = min(a)
        self.assertEqual(h.remove_min(), m)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, size - 1)

    def test_merge_empty_heap_with_empty_heap(self):
        a = MinHeap()
        b = MinHeap()
        self.assertIsNone(a.merge(b))

    def test_merge_empty_heap_with_non_empty_heap(self):
        a = MinHeap()
        ls = [-3, 5, 7, 9, 1, 5, 2]
        b = MinHeap(ls)
        self.assertIsNone(a.merge(b))
        self.assertEqual(a.size, len(ls))
        self.assertEqual(b.size, len(ls))

    def test_merge_non_empty_heap_with_empty_heap(self):
        ls = [-3, 5, 7, 9, 1, 5, 2]
        a = MinHeap(ls)
        b = MinHeap()
        self.assertIsNone(a.merge(b))
        self.assertEqual(a.size, len(ls))
        self.assertEqual(b.size, 0)
        self.assertTrue(b.is_empty())

    def test_merge_non_empty_heap_with_non_empty_heap(self):
        ls = [-3, 5, 7, 9, 1, 5, 2]
        size = len(ls)
        a = MinHeap(ls)
        b = MinHeap(sample(ls, size))
        self.assertIsNone(a.merge(b))
        self.assertEqual(a.size, size * 2)
        self.assertEqual(b.size, size)
