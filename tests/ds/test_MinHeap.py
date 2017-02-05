#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado
Created: 14/02/2016
Updated: 05/02/2017

# Description

Tests for the MinHeap class.
"""

import unittest
from random import randint

from ands.ds.MinHeap import MinHeap, is_min_heap, HeapNode


class TestMinHeap(unittest.TestCase):
    def test_empty_heap_creation(self):
        h = MinHeap()
        self.assertTrue(is_min_heap(h))
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size(), 0)

    def test_non_empty_heap_creation(self):
        ls = [12, 14, 28, 6, 7, 10, 18]
        h = MinHeap(ls)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_min_heap(h))

    def test_build_min_heap_one(self):
        h = MinHeap([12])

        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), 1)
        self.assertTrue(h.contains(12))
        self.assertEqual(h.search_by_value(12), 0)
        self.assertEqual(h.find_min(), HeapNode(12))
        self.assertTrue(is_min_heap(h))

        self.assertEqual(h.remove_min(), HeapNode(12))
        self.assertTrue(h.is_empty())
        self.assertTrue(is_min_heap(h))

    def test_build_min_heap_many(self):
        ls = [28, 14, 12, 10, 7, 6, 18]
        h = MinHeap(ls)

        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), 7)
        self.assertEqual(h.search_by_value(6), 0)
        self.assertEqual(h.find_min(), HeapNode(6))
        self.assertTrue(is_min_heap(h))

        for e in ls:
            self.assertTrue(h.contains(e))

        m = h.remove_min()
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), 6)
        self.assertEqual(m, HeapNode(6))
        self.assertEqual(h.find_min(), HeapNode(7))
        self.assertEqual(h.search_by_value(6), -1)
        self.assertFalse(h.contains(6))
        self.assertTrue(is_min_heap(h))

    def test_push_down(self):
        h = MinHeap([28, 14, 12, 10, 7, 6, 18])
        h.heap[0] = HeapNode(94)
        h.push_down(0)
        self.assertTrue(is_min_heap(h))

    def test_push_up(self):
        h = MinHeap([28, 14, 12, 10, 7, 6, 18])
        h.heap[h.size() - 1] = HeapNode(3)
        h.push_up(h.size() - 1)
        self.assertTrue(is_min_heap(h))

    def test_add_none(self):
        h = MinHeap()
        self.assertRaises(ValueError, h.add, None)

    def test_add_one(self):
        h = MinHeap()
        h.add(12)

        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), 1)
        self.assertEqual(h.find_min(), HeapNode(12))
        self.assertEqual(h.heap[0], h.find_min())
        self.assertTrue(is_min_heap(h))

        self.assertEqual(h.remove_min(), HeapNode(12))
        self.assertTrue(h.is_empty())

    def test_add_many(self):
        h = MinHeap()
        ls = []
        t = 100
        for i in range(t):
            ls.append(randint(-100, 100))
            h.add(ls[-1])
            self.assertEqual(h.size(), i + 1)
            self.assertTrue(h.contains(HeapNode(ls[-1])))
            self.assertTrue(is_min_heap(h))

        c = 0
        while not h.is_empty():
            n = h.remove_min()
            self.assertIsNotNone(n)
            self.assertTrue(n.key in ls)
            c += 1
            self.assertTrue(is_min_heap(h))

        self.assertEqual(c, t)
        self.assertTrue(h.is_empty())

    # TODO: test_add_many_with_value
    def test_add_one_with_value(self):
        h = MinHeap()
        h.add(HeapNode(2048, "2^11"))
        self.assertEqual(h.size(), 1)
        self.assertTrue(h.contains(HeapNode(2048, "2^11")))
        self.assertTrue(is_min_heap(h))

    def test_delete_bad_index(self):
        h = MinHeap([18, 6, 7, 28, 14, 12])

        self.assertRaises(IndexError, h.delete, -1)
        self.assertRaises(IndexError, h.delete, 6)
        self.assertRaises(TypeError, h.delete, 3.14159)
        self.assertRaises(TypeError, h.delete, None)
        self.assertRaises(TypeError, h.delete, "0")
        self.assertTrue(is_min_heap(h))

    def test_delete(self):
        h = MinHeap([12, 14, 28, 7, 6, 18])

        while not h.is_empty():
            p = randint(0, h.size() - 1)
            n = h.delete(p)
            self.assertIsNotNone(n)
            self.assertTrue(is_min_heap(h))

        self.assertTrue(h.is_empty())

    def test_find_min(self):
        ls = [28, 14, 12, 10]
        h = MinHeap(ls)

        n = len(ls)
        for _ in range(n):
            self.assertEqual(HeapNode(min(ls)), h.find_min())
            self.assertEqual(h.find_min(), h.remove_min())
            self.assertEqual(h.size(), len(ls) - 1)
            ls.remove(min(ls))
            self.assertTrue(is_min_heap(h))

        self.assertEqual(len(ls), 0)
        self.assertTrue(h.is_empty())

    def test_remove_min(self):
        ls = [28, 14, 12, 10, 7, 6, 18]
        h = MinHeap(ls)
        c = len(ls)

        while not h.is_empty():
            m = h.remove_min()

            self.assertIsNotNone(m)
            self.assertIn(m.key, ls)
            self.assertEqual(h.size(), c - 1)

            for e in h.heap:
                self.assertLessEqual(m.key, e.key)

            c -= 1
            self.assertTrue(is_min_heap(h))

        self.assertEqual(c, 0)
        self.assertIsNone(h.remove_min())
        self.assertTrue(is_min_heap(h))

    def test_search_when_exists(self):
        ls = [28, 14, 12, 10, 7, 6, 18]
        h = MinHeap(ls)

        v = h.search(12)
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_min_heap(h))

        v = h.search(HeapNode(14))
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_min_heap(h))

    def test_search_when_not_exists(self):
        ls = [28, 12, 14]
        h = MinHeap(ls)

        v = h.search(HeapNode(12, "twelve"))
        self.assertEqual(v, -1)
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_min_heap(h))

        self.assertRaises(ValueError, h.search, None)
        self.assertTrue(is_min_heap(h))

    def test_search_by_value_bad(self):
        ls = [11, 12, 13, 14]
        h = MinHeap(ls)

        self.assertRaises(Exception, h.search_by_value, HeapNode(13))
        self.assertTrue(is_min_heap(h))

    def test_search_by_value_default(self):
        ls = [28, 14, 12]
        h = MinHeap(ls)

        v = h.search_by_value(14)
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_min_heap(h))

    def test_search_by_value_custom(self):
        ls = [(12, "twelve"), (14, "fourteen")]
        h = MinHeap(ls)

        v = h.search_by_value("fourteen")
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_min_heap(h))

    def test_contains(self):
        ls = [28, 14, 12]
        h = MinHeap(ls)

        for e in ls:
            self.assertTrue(h.contains(e))

        self.assertFalse(h.contains(3))
        self.assertTrue(is_min_heap(h))

    def test_contains_none(self):
        ls = [99, 31]
        h = MinHeap(ls)
        self.assertRaises(ValueError, h.contains, None)
        self.assertTrue(is_min_heap(h))

    def test_merge(self):
        h = MinHeap([0, -1, 2])
        h2 = MinHeap([(30, "thirty"), (1, "one")])

        h.merge(h2)

        self.assertEqual(h.size(), 5)
        self.assertEqual(h.find_min(), HeapNode(-1))

        self.assertEqual(h2.size(), 2)
        self.assertEqual(h2.find_min(), HeapNode(1, "one"))

        self.assertTrue(is_min_heap(h))
        self.assertTrue(is_min_heap(h2))

    def test_replace(self):
        h = MinHeap([28, 12, 14, 7])

        p = h.replace(0, 3)

        self.assertEqual(p, HeapNode(7))
        self.assertEqual(h.size(), 4)
        self.assertTrue(is_min_heap(h))

        p = h.replace(3, 1)
        self.assertEqual(p, HeapNode(28))
        self.assertEqual(h.size(), 4)
        self.assertTrue(is_min_heap(h))

        p = h.replace(0, HeapNode(1))
        self.assertEqual(p, HeapNode(1))
        self.assertEqual(h.size(), 4)
        self.assertTrue(is_min_heap(h))

    def test_replace_bad(self):
        h = MinHeap([7, 3, 2, 5])
        self.assertRaises(ValueError, h.replace, 0, None)
        self.assertRaises(IndexError, h.replace, -1, 3)

    def test_clear(self):
        h = MinHeap()

        h.clear()
        self.assertTrue(h.is_empty())

        h.add(13)
        h.clear()
        self.assertTrue(h.is_empty())

    def test_swap(self):
        h = MinHeap([12, 14, 28])

        h.swap(0, 2)
        self.assertFalse(is_min_heap(h))

        h.swap(0, 2)
        self.assertTrue(is_min_heap(h))

    def test_swap_bad(self):
        h = MinHeap([29, 31, 99])
        self.assertRaises(IndexError, h.swap, 0, 3)
        self.assertRaises(IndexError, h.swap, -3, 2)
        self.assertTrue(is_min_heap(h))

    def test_is_good_index_bad(self):
        h = MinHeap([97, 101, 103])

        self.assertRaises(TypeError, h.is_good_index, 3.14159)
        self.assertRaises(TypeError, h.is_good_index, "quelli che benpensano")
        self.assertRaises(TypeError, h.is_good_index, None)
        self.assertRaises(TypeError, h.is_good_index, h.swap)

    def test_is_good_index(self):
        h = MinHeap([1001, 11, 17])

        self.assertTrue(h.is_good_index(0))
        self.assertTrue(h.is_good_index(1))
        self.assertTrue(h.is_good_index(2))
        self.assertFalse(h.is_good_index(-1))
        self.assertFalse(h.is_good_index(3))

    def test_parent_index_bad(self):
        h = MinHeap([23, 27, 29])

        self.assertRaises(IndexError, h.parent_index, -1)
        self.assertRaises(IndexError, h.parent_index, 3)

    def test_parent_index(self):
        h = MinHeap([41, 43])

        self.assertEqual(h.parent_index(0), -1)
        self.assertEqual(h.parent_index(1), 0)

    def test_grandparent_index_bad(self):
        h = MinHeap([1, 2, 3, 4, 5])

        self.assertRaises(IndexError, h.parent_index, -1)
        self.assertRaises(IndexError, h.parent_index, 5)

    def test_grandparent_index(self):
        h = MinHeap([1, 2, 3, 4, 5])

        self.assertEqual(h.grandparent_index(0), -1)
        self.assertEqual(h.grandparent_index(1), -1)
        self.assertEqual(h.grandparent_index(2), -1)
        self.assertEqual(h.grandparent_index(3), 0)
        self.assertEqual(h.grandparent_index(4), 0)

    def test_left_index_bad(self):
        h = MinHeap([2, 3, 5])

        self.assertRaises(IndexError, h.left_index, -1)
        self.assertRaises(IndexError, h.left_index, 3)

    def test_left_index(self):
        h = MinHeap([2, 3, 5])

        self.assertEqual(h.left_index(0), 1)
        self.assertEqual(h.left_index(1), -1)
        self.assertEqual(h.left_index(2), -1)

    def test_right_index_bad(self):
        h = MinHeap([9, 8, 7, 6])

        self.assertRaises(IndexError, h.right_index, -1)
        self.assertRaises(IndexError, h.right_index, 4)

    def test_right_index(self):
        h = MinHeap([9, 8, 7, 6])

        self.assertEqual(h.right_index(0), 2)
        self.assertEqual(h.right_index(1), -1)
        self.assertEqual(h.right_index(2), -1)
        self.assertEqual(h.right_index(3), -1)

    def test_has_children_bad(self):
        h = MinHeap([11, 12, 13, 14])

        self.assertRaises(IndexError, h.has_children, -1)
        self.assertRaises(IndexError, h.has_children, 4)

    def test_has_children(self):
        h = MinHeap([11, 12, 13, 14])

        self.assertTrue(h.has_children(0))
        self.assertTrue(h.has_children(1))
        self.assertFalse(h.has_children(2))
        self.assertFalse(h.has_children(3))

    def test_is_child_bad(self):
        h = MinHeap([12, 14, 28, 6])

        self.assertRaises(IndexError, h.is_child, -1, 3)
        self.assertRaises(IndexError, h.is_child, 0, 4)

    def test_is_child(self):
        h = MinHeap([12, 14, 28, 6])

        self.assertFalse(h.is_child(0, 0))
        self.assertFalse(h.is_child(1, 1))
        self.assertFalse(h.is_child(2, 2))
        self.assertFalse(h.is_child(3, 3))

        self.assertTrue(h.is_child(3, 1))
        self.assertTrue(h.is_child(2, 0))
        self.assertTrue(h.is_child(1, 0))

        self.assertFalse(h.is_child(3, 0))
        self.assertFalse(h.is_child(3, 2))

    def test_is_grandchild_bad(self):
        h = MinHeap([31, 33, 37, 39, 41])

        self.assertRaises(IndexError, h.is_grandchild, -1, 3)
        self.assertRaises(IndexError, h.is_grandchild, 0, 6)

    def test_is_grandchild(self):
        h = MinHeap([31, 33, 37, 39, 41])

        self.assertFalse(h.is_grandchild(0, 0))
        self.assertFalse(h.is_grandchild(1, 1))
        self.assertFalse(h.is_grandchild(2, 2))
        self.assertFalse(h.is_grandchild(3, 3))
        self.assertFalse(h.is_grandchild(4, 4))

        self.assertTrue(h.is_grandchild(3, 0))
        self.assertFalse(h.is_grandchild(3, 1))
        self.assertFalse(h.is_grandchild(3, 2))
        self.assertFalse(h.is_grandchild(3, 4))

        self.assertTrue(h.is_grandchild(4, 0))
        self.assertFalse(h.is_grandchild(4, 1))
        self.assertFalse(h.is_grandchild(4, 2))
        self.assertFalse(h.is_grandchild(4, 3))

        self.assertFalse(h.is_grandchild(1, 0))
        self.assertFalse(h.is_grandchild(1, 2))
        self.assertFalse(h.is_grandchild(1, 3))
        self.assertFalse(h.is_grandchild(1, 4))

        self.assertFalse(h.is_grandchild(2, 0))
        self.assertFalse(h.is_grandchild(2, 1))
        self.assertFalse(h.is_grandchild(2, 3))
        self.assertFalse(h.is_grandchild(2, 4))

    def test_is_parent_bad(self):
        h = MinHeap([-1, -2, -3, -4])

        self.assertRaises(IndexError, h.is_parent, -1, 3)
        self.assertRaises(IndexError, h.is_parent, 0, 6)

    def test_is_parent(self):
        h = MinHeap([-1, -2, -3, -4, -5])

        self.assertFalse(h.is_parent(0, 0))
        self.assertFalse(h.is_parent(1, 1))
        self.assertFalse(h.is_parent(2, 2))
        self.assertFalse(h.is_parent(3, 3))
        self.assertFalse(h.is_parent(4, 4))

        self.assertTrue(h.is_parent(0, 1))
        self.assertTrue(h.is_parent(0, 2))
        self.assertFalse(h.is_parent(0, 3))
        self.assertFalse(h.is_parent(0, 4))

        self.assertTrue(h.is_parent(1, 3))
        self.assertTrue(h.is_parent(1, 4))
        self.assertFalse(h.is_parent(1, 2))
        self.assertFalse(h.is_parent(1, 0))

        self.assertFalse(h.is_parent(2, 0))
        self.assertFalse(h.is_parent(2, 1))
        self.assertFalse(h.is_parent(2, 3))
        self.assertFalse(h.is_parent(2, 4))

        self.assertFalse(h.is_parent(3, 0))
        self.assertFalse(h.is_parent(3, 1))
        self.assertFalse(h.is_parent(3, 2))
        self.assertFalse(h.is_parent(3, 4))

        self.assertFalse(h.is_parent(4, 0))
        self.assertFalse(h.is_parent(4, 1))
        self.assertFalse(h.is_parent(4, 2))
        self.assertFalse(h.is_parent(4, 3))

    def test_is_grandparent_bad(self):
        h = MinHeap([9, 99, 999, 9999, 99999])

        self.assertRaises(IndexError, h.is_grandparent, -1, 3)
        self.assertRaises(IndexError, h.is_grandparent, 0, 6)

    def test_is_grandparent(self):
        h = MinHeap([9, 99, 999, 9999, 99999])

        self.assertFalse(h.is_grandparent(0, 0))
        self.assertFalse(h.is_grandparent(1, 1))
        self.assertFalse(h.is_grandparent(2, 2))
        self.assertFalse(h.is_grandparent(3, 3))
        self.assertFalse(h.is_grandparent(4, 4))

        self.assertFalse(h.is_grandparent(0, 1))
        self.assertFalse(h.is_grandparent(0, 2))
        self.assertTrue(h.is_grandparent(0, 3))
        self.assertTrue(h.is_grandparent(0, 4))

        self.assertFalse(h.is_grandparent(1, 0))
        self.assertFalse(h.is_grandparent(1, 2))
        self.assertFalse(h.is_grandparent(1, 3))
        self.assertFalse(h.is_grandparent(1, 4))

        self.assertFalse(h.is_grandparent(2, 0))
        self.assertFalse(h.is_grandparent(2, 1))
        self.assertFalse(h.is_grandparent(2, 3))
        self.assertFalse(h.is_grandparent(2, 4))

        self.assertFalse(h.is_grandparent(3, 0))
        self.assertFalse(h.is_grandparent(3, 1))
        self.assertFalse(h.is_grandparent(3, 2))
        self.assertFalse(h.is_grandparent(3, 4))

        self.assertFalse(h.is_grandparent(4, 0))
        self.assertFalse(h.is_grandparent(4, 1))
        self.assertFalse(h.is_grandparent(4, 2))
        self.assertFalse(h.is_grandparent(4, 3))

    def test_is_on_even_level_bad(self):
        ls = [12, 14, 28, 6, 7, 18, 10, 3, 1]
        h = MinHeap(ls)

        self.assertRaises(IndexError, h.is_on_even_level, -1)
        self.assertRaises(IndexError, h.is_on_even_level, len(ls))

    def test_is_on_even_level(self):
        ls = [12, 14, 28, 6, 7, 18, 10, 3, 1]
        h = MinHeap(ls)

        self.assertTrue(h.is_on_even_level(0))

        self.assertFalse(h.is_on_even_level(1))
        self.assertFalse(h.is_on_even_level(2))

        self.assertTrue(h.is_on_even_level(3))
        self.assertTrue(h.is_on_even_level(4))
        self.assertTrue(h.is_on_even_level(5))
        self.assertTrue(h.is_on_even_level(6))

        self.assertFalse(h.is_on_even_level(7))
        self.assertFalse(h.is_on_even_level(8))

    def test_is_on_odd_level_bad(self):
        ls = [12, 14, 28, 6, 7, 18, 10, 3, 1]
        h = MinHeap(ls)

        self.assertRaises(IndexError, h.is_on_odd_level, -1)
        self.assertRaises(IndexError, h.is_on_odd_level, len(ls))

    def test_is_on_odd_level(self):
        ls = [12, 14, 28, 6, 7, 18, 10, 3, 1]
        h = MinHeap(ls)

        self.assertFalse(h.is_on_odd_level(0))
        self.assertTrue(h.is_on_odd_level(1))
        self.assertTrue(h.is_on_odd_level(2))
        self.assertFalse(h.is_on_odd_level(3))
        self.assertFalse(h.is_on_odd_level(4))
        self.assertFalse(h.is_on_odd_level(5))
        self.assertFalse(h.is_on_odd_level(6))
        self.assertTrue(h.is_on_odd_level(7))
        self.assertTrue(h.is_on_odd_level(8))
