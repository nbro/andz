#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 20/02/2016

Updated: 23/03/2024

# Description

Unit tests for the classes and functions in the andz.ds.MinMaxHeap module.
"""

import unittest
from random import choice, randint, sample

from andz.ds.MinMaxHeap import MinMaxHeap, is_min_max_heap


class TestMinMaxHeap(unittest.TestCase):
    def test_heap_creation_default(self):
        h = MinMaxHeap()
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size, 0)

    def test_heap_creation_given_list(self):
        a = [12, 14, 28, 6, 7, 10, 18]
        h = MinMaxHeap(a)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, len(a))

    def test_clear_empty_heap(self):
        h = MinMaxHeap()
        self.assertIsNone(h.clear())
        self.assertEqual(h.size, 0)
        self.assertTrue(h.is_empty())

    def test_clear_heap_of_random_size(self):
        h = MinMaxHeap([randint(-100, 100) for _ in range(100)])
        self.assertIsNone(h.clear())
        self.assertEqual(h.size, 0)
        self.assertTrue(h.is_empty())

    def test_add_when_argument_is_None(self):
        h = MinMaxHeap()
        self.assertRaises(ValueError, h.add, None)

    def test_add_add_one(self):
        h = MinMaxHeap()
        self.assertIsNone(h.add(2))
        self.assertEqual(h.size, 1)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.find_max(), 2)
        self.assertEqual(h.find_min(), 2)

    def test_add_multiple_elements(self):
        a = [randint(-100, 100) for _ in range(100)]
        h = MinMaxHeap()

        for i, elem in enumerate(a):
            self.assertIsNone(h.add(elem))
            self.assertEqual(h.size, i + 1)

        self.assertFalse(h.is_empty())
        self.assertEqual(h.find_max(), max(a))
        self.assertEqual(h.find_min(), min(a))

    def test_contains_when_argument_is_None(self):
        h = MinMaxHeap()
        self.assertRaises(ValueError, h.contains, None)

    def test_contains_when_empty_heap(self):
        h = MinMaxHeap()
        self.assertFalse(h.contains(3))

    def test_contains_true(self):
        h = MinMaxHeap([6, 8, 2, 2, 60, 7, 9])
        self.assertTrue(h.contains(2))

    def test_contains_false(self):
        h = MinMaxHeap([6, 8, 2, 60, 7, 9, 3, 67])
        self.assertFalse(h.contains(10))

    def test_delete_when_argument_is_None(self):
        self.assertRaises(ValueError, MinMaxHeap().delete, None)

    def test_delete_when_elem_does_not_exist(self):
        self.assertRaises(LookupError, MinMaxHeap().delete, 3)

    def test_delete_when_elem_is_last(self):
        h = MinMaxHeap([3, 4])
        self.assertIsNone(h.delete(4))
        self.assertTrue(is_min_max_heap(h))
        self.assertEqual(h.size, 1)
        self.assertFalse(h.is_empty())

    def test_delete_all_when_heap_of_random_size(self):
        size = randint(3, 100)
        a = [randint(-100, 100) for _ in range(size)]
        h = MinMaxHeap(a)

        for _ in range(size):
            self.assertIsNone(h.delete(choice(a)))
            self.assertTrue(is_min_max_heap(h))

        self.assertEqual(h.size, 0)
        self.assertTrue(h.is_empty())

    # Testing find_max and remove_max

    def test_find_max_when_empty_heap(self):
        h = MinMaxHeap()
        self.assertIsNone(h.find_max())

    def test_find_max_when_heap_has_size_1(self):
        h = MinMaxHeap([5])
        self.assertEqual(h.find_max(), 5)

    def test_find_max_when_heap_has_size_2(self):
        h = MinMaxHeap([13, 7])
        self.assertEqual(h.find_max(), 13)

    def test_find_max_when_heap_has_random_size(self):
        a = [randint(-100, 100) for _ in range(3, 100)]
        h = MinMaxHeap(a)
        self.assertEqual(h.find_max(), max(a))

    def test_remove_max_when_empty_heap(self):
        h = MinMaxHeap()
        self.assertIsNone(h.remove_max())

    def test_remove_max_when_heap_has_size_1(self):
        h = MinMaxHeap([13])
        self.assertEqual(h.remove_max(), 13)
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size, 0)

    def test_remove_max_when_heap_has_size_2(self):
        h = MinMaxHeap([11, 13])
        self.assertEqual(h.remove_max(), 13)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, 1)

    def test_remove_max_when_heap_has_random_size(self):
        size = randint(3, 100)
        a = [randint(-100, 100) for _ in range(size)]
        h = MinMaxHeap(a)
        m = max(a)
        self.assertEqual(h.remove_max(), m)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, size - 1)

    # Testing find_min and remove_min

    def test_find_min_when_empty_heap(self):
        h = MinMaxHeap()
        self.assertIsNone(h.find_min())

    def test_find_min_when_heap_has_size_1(self):
        h = MinMaxHeap([5])
        self.assertEqual(h.find_min(), 5)

    def test_find_min_when_heap_has_size_2(self):
        h = MinMaxHeap([13, 7])
        self.assertEqual(h.find_min(), 7)

    def test_find_min_when_heap_has_random_size(self):
        a = [randint(-100, 100) for _ in range(3, 100)]
        h = MinMaxHeap(a)
        self.assertEqual(h.find_min(), min(a))

    def test_remove_min_when_empty_heap(self):
        h = MinMaxHeap()
        self.assertIsNone(h.remove_min())

    def test_remove_min_when_heap_has_size_1(self):
        h = MinMaxHeap([13])
        self.assertEqual(h.remove_min(), 13)
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size, 0)

    def test_remove_min_when_heap_has_size_2(self):
        h = MinMaxHeap([11, 13])
        self.assertEqual(h.remove_min(), 11)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, 1)

    def test_remove_min_when_heap_has_random_size(self):
        size = randint(3, 100)
        a = [randint(-100, 100) for _ in range(size)]
        h = MinMaxHeap(a)
        m = min(a)
        self.assertEqual(h.remove_min(), m)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size, size - 1)

    def test_merge_empty_heap_with_empty_heap(self):
        a = MinMaxHeap()
        b = MinMaxHeap()
        self.assertIsNone(a.merge(b))

    def test_merge_empty_heap_with_non_empty_heap(self):
        a = MinMaxHeap()
        ls = [-3, 5, 7, 9, 1, 5, 2]
        b = MinMaxHeap(ls)
        self.assertIsNone(a.merge(b))
        self.assertEqual(a.size, len(ls))
        self.assertEqual(b.size, len(ls))

    def test_merge_non_empty_heap_with_empty_heap(self):
        ls = [-3, 5, 7, 9, 1, 5, 2]
        a = MinMaxHeap(ls)
        b = MinMaxHeap()
        self.assertIsNone(a.merge(b))
        self.assertEqual(a.size, len(ls))
        self.assertEqual(b.size, 0)
        self.assertTrue(b.is_empty())

    def test_merge_non_empty_heap_with_non_empty_heap(self):
        ls = [-3, 5, 7, 9, 1, 5, 2]
        size = len(ls)
        a = MinMaxHeap(ls)
        b = MinMaxHeap(sample(ls, size))
        self.assertIsNone(a.merge(b))
        self.assertEqual(a.size, size * 2)
        self.assertEqual(b.size, size)
