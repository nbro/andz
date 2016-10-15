#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 17/02/16

Last update: 15/10/16

Tests for the MaxHeap class.
"""

import unittest
from random import randint

from ands.ds.MaxHeap import MaxHeap, is_max_heap, HeapNode


class TestMaxHeap(unittest.TestCase):
    def test_empty_heap_creation(self):
        h = MaxHeap()
        self.assertTrue(is_max_heap(h))
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size(), 0)

    def test_non_empty_heap_creation(self):
        ls = [12, 14, 28, 6, 7, 10, 18]
        h = MaxHeap(ls)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_max_heap(h))

    def test_build_max_heap(self):
        h = MaxHeap([12])

        self.assertEqual(h.search_by_value(12), 0)
        self.assertTrue(h.contains(12))
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), 1)
        self.assertEqual(h.find_max(), HeapNode(12))

        self.assertTrue(is_max_heap(h))
        self.assertEqual(h.remove_max(), HeapNode(12))
        self.assertTrue(is_max_heap(h))
        self.assertTrue(h.is_empty())

        h = MaxHeap([28, 14, 12, 10, 7, 6, 18])
        self.assertEqual(h.search_by_value(28), 0)
        self.assertTrue(h.contains(6))
        self.assertTrue(h.contains(10))
        self.assertEqual(h.size(), 7)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.find_max(), HeapNode(28))

        self.assertTrue(is_max_heap(h))

        self.assertEqual(h.remove_max(), HeapNode(28))
        self.assertEqual(h.find_max(), HeapNode(18))
        self.assertEqual(h.search_by_value(28), -1)
        self.assertFalse(h.contains(28))
        self.assertTrue(h.contains(7))
        self.assertEqual(h.size(), 6)
        self.assertFalse(h.is_empty())

        self.assertTrue(is_max_heap(h))

    def test_push_down(self):
        h = MaxHeap([28, 14, 12, 10, 7, 6, 18])
        h.heap[0] = HeapNode(2)
        h.push_down(0)
        self.assertTrue(is_max_heap(h))

    def test_push_up(self):
        h = MaxHeap([28, 14, 12, 10, 7, 6, 18])
        h.heap[h.size() - 1] = HeapNode(99)
        h.push_up(h.size() - 1)
        self.assertTrue(is_max_heap(h))

    def test_add(self):
        h = MaxHeap()

        self.assertRaises(ValueError, h.add, None)

        h.add(12)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), 1)
        self.assertEqual(h.find_max(), HeapNode(12))
        self.assertEqual(h.heap[0], h.find_max())

        self.assertTrue(is_max_heap(h))
        self.assertEqual(h.remove_max(), HeapNode(12))
        self.assertTrue(h.is_empty())

        ls = []
        t = 100
        for i in range(t):
            ls.append(randint(-100, 100))
            h.add(ls[-1])
            self.assertEqual(h.size(), (i + 1))
            self.assertTrue(h.contains(HeapNode(ls[-1])))
            self.assertTrue(is_max_heap(h))

        c = 0
        while not h.is_empty():
            n = h.remove_max()
            self.assertIsNotNone(n)
            self.assertIn(n.key, ls)
            c += 1
            self.assertTrue(is_max_heap(h))

        self.assertEqual(c, t)
        self.assertTrue(h.is_empty())

        s = h.size()
        h.add(HeapNode(1024))
        self.assertEqual(h.size(), (s + 1))
        self.assertNotEqual(h.search(HeapNode(1024)), -1)

        self.assertTrue(is_max_heap(h))

        s = h.size()
        h.add(HeapNode(2048, "2^11"))
        self.assertEqual(h.size(), (s + 1))
        self.assertTrue(h.contains(HeapNode(2048, "2^11")))
        self.assertTrue(is_max_heap(h))

    def test_delete(self):

        h = MaxHeap([12, 14, 28, 7, 6, 18])

        # asserting it raises exceptions for bad indices
        self.assertRaises(TypeError, h.delete, "0")
        self.assertRaises(TypeError, h.delete, 2.72)
        self.assertRaises(TypeError, h.delete, None)
        self.assertRaises(IndexError, h.delete, -1)
        self.assertRaises(IndexError, h.delete, 6)

        self.assertTrue(is_max_heap(h))

        while not h.is_empty():
            r = randint(0, h.size() - 1)
            n = h.delete(r)
            self.assertIsNotNone(n)
            self.assertTrue(is_max_heap(h))

        self.assertTrue(h.is_empty())

    def test_find_max(self):
        h = MaxHeap([28, 14, 12, 10])
        self.assertEqual(h.size(), 4)

        m = h.find_max()
        self.assertEqual(m, h.remove_max())
        self.assertEqual(m, HeapNode(28))
        self.assertEqual(h.size(), 3)
        self.assertTrue(is_max_heap(h))

        m = h.find_max()
        self.assertEqual(m, h.remove_max())
        self.assertEqual(HeapNode(14), m)
        self.assertEqual(h.size(), 2)
        self.assertTrue(is_max_heap(h))

        m = h.find_max()
        self.assertEqual(m, h.remove_max())
        self.assertEqual(HeapNode(12), m)
        self.assertEqual(h.size(), 1)
        self.assertTrue(is_max_heap(h))

        m = h.find_max()
        self.assertEqual(m, h.remove_max())
        self.assertEqual(HeapNode(10), m)
        self.assertEqual(h.size(), 0)
        self.assertIsNone(h.find_max())
        self.assertTrue(is_max_heap(h))

    def test_remove_max(self):
        ls = [28, 14, 12, 10, 7, 6, 18]
        h = MaxHeap(ls)
        c = len(ls)

        while not h.is_empty():
            m = h.remove_max()

            for e in h.heap:
                self.assertGreaterEqual(m.key, e.key)

            self.assertIsNotNone(m)
            self.assertIn(m.key, ls)
            self.assertEqual(h.size(), (c - 1))

            c -= 1

            self.assertTrue(is_max_heap(h))

        self.assertEqual(c, 0)
        self.assertIsNone(h.remove_max())
        self.assertTrue(is_max_heap(h))

    def test_search(self):
        ls = [28, 14, 12, 10, 7, 6, 18]
        h = MaxHeap(ls)

        v = h.search(12)
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_max_heap(h))

        v = h.search(HeapNode(14))
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_max_heap(h))

        v = h.search(HeapNode(12, "Noi"))
        self.assertEqual(v, -1)
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_max_heap(h))

        self.assertRaises(ValueError, h.search, None)
        self.assertTrue(is_max_heap(h))

    def test_search_by_value(self):
        ls = [28, 14, 12]
        h = MaxHeap(ls)

        self.assertRaises(Exception, h.search_by_value, HeapNode(14))
        self.assertRaises(ValueError, h.search_by_value, None)

        self.assertTrue(is_max_heap(h))

        v = h.search_by_value(14)
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))
        self.assertTrue(is_max_heap(h))

        ls = [(12, "Noi"), (14, "Tu")]
        h = MaxHeap(ls)
        v = h.search_by_value("Tu")
        self.assertIn(v, range(0, len(ls)))
        self.assertEqual(h.size(), len(ls))

        self.assertTrue(is_max_heap(h))

    def test_contains(self):
        ls = [28, 14, 12]
        h = MaxHeap(ls)
        self.assertTrue(h.contains(28))
        self.assertTrue(h.contains(14))
        self.assertTrue(h.contains(12))
        self.assertFalse(h.contains(200))
        self.assertFalse(h.contains(7))
        self.assertRaises(ValueError, h.contains, None)
        self.assertTrue(is_max_heap(h))

    def test_merge(self):
        h = MaxHeap([12, 14, 28])
        self.assertTrue(is_max_heap(h))
        self.assertEqual(h.size(), 3)

        h2 = MaxHeap([(30, "15x2"), (1, "1")])
        self.assertEqual(h2.size(), 2)
        self.assertTrue(is_max_heap(h))

        h.merge(h2)
        self.assertEqual(h.size(), 5)
        self.assertEqual(h.find_max(), HeapNode(30, "15x2"))
        self.assertTrue(is_max_heap(h))

    def test_replace(self):
        h = MaxHeap([28, 12, 14, 7])

        p = h.replace(0, 1)
        self.assertEqual(p, HeapNode(28))
        self.assertEqual(h.size(), 4)
        self.assertTrue(is_max_heap(h))

        p = h.replace(3, 99)
        self.assertEqual(p, HeapNode(7))
        self.assertEqual(h.size(), 4)
        self.assertTrue(is_max_heap(h))

        p = h.replace(0, HeapNode(0))
        self.assertEqual(p, HeapNode(99))
        self.assertEqual(h.size(), 4)
        self.assertTrue(is_max_heap(h))
        self.assertRaises(ValueError, h.replace, 0, None)
        self.assertRaises(IndexError, h.replace, -1, 3)

    def test_clear(self):
        h = MaxHeap([12, 14])
        self.assertEqual(h.size(), 2)
        h.clear()
        self.assertEqual(h.size(), 0)

    def test_swap(self):
        h = MaxHeap([12, 14, 28])

        h.swap(0, 2)
        self.assertFalse(is_max_heap(h))

        h.swap(0, 2)
        self.assertTrue(is_max_heap(h))
        self.assertRaises(IndexError, h.swap, 0, 3)
        self.assertRaises(IndexError, h.swap, -3, 2)

    def test_is_good_index(self):
        h = MaxHeap([12, 14, 28])

        self.assertRaises(TypeError, h.is_good_index, 3.14159)
        self.assertRaises(TypeError, h.is_good_index, "a nightmare of nightmares")
        self.assertRaises(TypeError, h.is_good_index, None)
        self.assertRaises(TypeError, h.is_good_index, h.swap)

        self.assertTrue(h.is_good_index(0))
        self.assertTrue(h.is_good_index(1))
        self.assertTrue(h.is_good_index(2))
        self.assertFalse(h.is_good_index(-1))
        self.assertFalse(h.is_good_index(3))

    def test_parent_index(self):
        h = MaxHeap([12, 14, 28])

        self.assertRaises(IndexError, h.parent_index, -1)
        self.assertRaises(IndexError, h.parent_index, 3)

        self.assertEqual(h.parent_index(0), -1)
        self.assertEqual(h.parent_index(1), 0)
        self.assertEqual(h.parent_index(2), 0)

    def test_grandparent_index(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.grandparent_index, -1)
        self.assertRaises(IndexError, h.grandparent_index, 5)

        self.assertEqual(h.grandparent_index(0), -1)
        self.assertEqual(h.grandparent_index(1), -1)
        self.assertEqual(h.grandparent_index(2), -1)
        self.assertEqual(h.grandparent_index(3), 0)
        self.assertEqual(h.grandparent_index(4), 0)

    def test_left_index(self):
        h = MaxHeap([12, 14, 28])
        self.assertRaises(IndexError, h.left_index, -1)
        self.assertRaises(IndexError, h.left_index, 3)
        self.assertEqual(h.left_index(0), 1)
        self.assertEqual(h.left_index(1), -1)
        self.assertEqual(h.left_index(2), -1)

    def test_right_index(self):
        h = MaxHeap([12, 14, 28, 6])

        self.assertRaises(IndexError, h.right_index, -1)
        self.assertRaises(IndexError, h.right_index, 4)

        self.assertEqual(h.right_index(0), 2)
        self.assertEqual(h.right_index(1), -1)
        self.assertEqual(h.right_index(2), -1)
        self.assertEqual(h.right_index(3), -1)
        self.assertEqual(h.left_index(1), 3)

    def test_has_children(self):
        h = MaxHeap([12, 14, 28, 6])
        self.assertRaises(IndexError, h.has_children, -1)
        self.assertTrue(h.has_children(0))
        self.assertTrue(h.has_children(1))
        self.assertFalse(h.has_children(2))
        self.assertFalse(h.has_children(3))

    def test_is_child(self):
        h = MaxHeap([12, 14, 28, 6])

        self.assertRaises(IndexError, h.is_child, -1, 3)
        self.assertRaises(IndexError, h.is_child, 0, 4)

        self.assertFalse(h.is_child(0, 0))
        self.assertFalse(h.is_child(1, 1))
        self.assertFalse(h.is_child(2, 2))
        self.assertFalse(h.is_child(3, 3))

        self.assertTrue(h.is_child(3, 1))
        self.assertTrue(h.is_child(2, 0))
        self.assertTrue(h.is_child(1, 0))

        self.assertFalse(h.is_child(3, 0))
        self.assertFalse(h.is_child(3, 2))

    def test_is_grandchild(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.is_grandchild, -1, 3)
        self.assertRaises(IndexError, h.is_grandchild, 0, 6)

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

    def test_is_parent(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.is_parent, -1, 3)
        self.assertRaises(IndexError, h.is_parent, 0, 6)

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

    def test_is_grandparent(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.is_grandparent, -1, 3)
        self.assertRaises(IndexError, h.is_grandparent, 0, 6)

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

    def test_is_on_even_level(self):
        h = MaxHeap([12, 14, 28, 6, 7, 18, 10, 3, 1])

        self.assertRaises(IndexError, h.is_on_even_level, -1)

        self.assertTrue(h.is_on_even_level(0))
        self.assertFalse(h.is_on_even_level(1))
        self.assertFalse(h.is_on_even_level(2))
        self.assertTrue(h.is_on_even_level(3))
        self.assertTrue(h.is_on_even_level(4))
        self.assertTrue(h.is_on_even_level(5))
        self.assertTrue(h.is_on_even_level(6))
        self.assertFalse(h.is_on_even_level(7))
        self.assertFalse(h.is_on_even_level(8))

    def test_is_on_odd_level(self):
        h = MaxHeap([12, 14, 28, 6, 7, 18, 10, 3, 1])

        self.assertRaises(IndexError, h.is_on_odd_level, 10)

        self.assertFalse(h.is_on_odd_level(0))
        self.assertTrue(h.is_on_odd_level(1))
        self.assertTrue(h.is_on_odd_level(2))
        self.assertFalse(h.is_on_odd_level(3))
        self.assertFalse(h.is_on_odd_level(4))
        self.assertFalse(h.is_on_odd_level(5))
        self.assertFalse(h.is_on_odd_level(6))
        self.assertTrue(h.is_on_odd_level(7))
        self.assertTrue(h.is_on_odd_level(8))


if __name__ == "__main__":
    unittest.main(verbosity=2)
