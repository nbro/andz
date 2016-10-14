#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 17/02/16

Last update: 28/08/16

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
        assert h.search_by_value(28) == 0
        assert h.contains(6)
        assert h.contains(10)
        assert h.size() == 7
        assert not h.is_empty()
        assert h.find_max() == HeapNode(28)
        self.assertTrue(is_max_heap(h))

        assert h.remove_max() == HeapNode(28)
        assert h.find_max() == HeapNode(18)
        assert h.search_by_value(28) == -1
        assert not h.contains(28)
        assert h.contains(7)
        assert h.size() == 6
        assert not h.is_empty()
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
        assert not h.is_empty()
        assert h.size() == 1

        assert h.find_max() == HeapNode(12)
        assert h.heap[0] == h.find_max()

        self.assertTrue(is_max_heap(h))
        assert h.remove_max() == HeapNode(12)
        assert h.is_empty()

        ls = []
        t = 100
        for i in range(t):
            ls.append(randint(-100, 100))
            h.add(ls[-1])
            assert h.size() == (i + 1)
            assert h.contains(HeapNode(ls[-1]))
            self.assertTrue(is_max_heap(h))

        c = 0
        while not h.is_empty():
            n = h.remove_max()
            assert n and n.key in ls
            c += 1
            self.assertTrue(is_max_heap(h))

        assert c == t
        assert h.is_empty()

        s = h.size()
        h.add(HeapNode(1024))
        assert h.size() == (s + 1)
        assert h.search(HeapNode(1024)) != -1
        self.assertTrue(is_max_heap(h))

        s = h.size()
        h.add(HeapNode(2048, "2^11"))
        assert h.size() == (s + 1)
        assert h.contains(HeapNode(2048, "2^11"))
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
            assert n
            self.assertTrue(is_max_heap(h))

        assert h.is_empty()

    def test_find_max(self):
        h = MaxHeap([28, 14, 12, 10])
        assert h.size() == 4

        m = h.find_max()
        assert m == h.remove_max() == HeapNode(28)
        assert h.size() == 3
        self.assertTrue(is_max_heap(h))

        m = h.find_max()
        assert m == h.remove_max() == HeapNode(14)
        assert h.size() == 2
        self.assertTrue(is_max_heap(h))

        m = h.find_max()
        assert m == h.remove_max() == HeapNode(12)
        assert h.size() == 1
        self.assertTrue(is_max_heap(h))

        m = h.find_max()
        assert m == h.remove_max() == HeapNode(10)
        assert h.size() == 0
        assert not h.find_max()
        self.assertTrue(is_max_heap(h))

    def test_remove_max(self):
        ls = [28, 14, 12, 10, 7, 6, 18]
        h = MaxHeap(ls)
        c = len(ls)

        while not h.is_empty():
            m = h.remove_max()
            for e in h.heap:
                assert m.key >= e.key
            assert m
            assert m.key in ls
            assert h.size() == (c - 1)
            c -= 1
            self.assertTrue(is_max_heap(h))

        assert c == 0
        assert not h.remove_max()
        self.assertTrue(is_max_heap(h))

    def test_search(self):
        ls = [28, 14, 12, 10, 7, 6, 18]
        h = MaxHeap(ls)

        v = h.search(12)
        assert v in range(0, len(ls))
        assert h.size() == len(ls)
        self.assertTrue(is_max_heap(h))

        v = h.search(HeapNode(14))
        assert v in range(0, len(ls))
        assert h.size() == len(ls)
        self.assertTrue(is_max_heap(h))

        v = h.search(HeapNode(12, "Noi"))
        assert v == -1
        assert h.size() == len(ls)
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
        assert v in range(0, len(ls))
        assert h.size() == len(ls)
        self.assertTrue(is_max_heap(h))

        ls = [(12, "Noi"), (14, "Tu")]
        h = MaxHeap(ls)
        v = h.search_by_value("Tu")
        assert v in range(0, len(ls))
        assert h.size() == len(ls)

        self.assertTrue(is_max_heap(h))

    def test_contains(self):
        ls = [28, 14, 12]
        h = MaxHeap(ls)
        assert h.contains(28) and h.contains(14) and h.contains(12)
        assert not h.contains(200) and not h.contains(7)
        self.assertRaises(ValueError, h.contains, None)
        self.assertTrue(is_max_heap(h))

    def test_merge(self):
        h = MaxHeap([12, 14, 28])
        self.assertTrue(is_max_heap(h))
        assert h.size() == 3

        h2 = MaxHeap([(30, "15x2"), (1, "1")])
        assert h2.size() == 2
        self.assertTrue(is_max_heap(h))

        h.merge(h2)
        assert h.size() == 5
        assert h.find_max() == HeapNode(30, "15x2")
        assert h2.size() == 2
        self.assertTrue(is_max_heap(h))

    def test_replace(self):
        h = MaxHeap([28, 12, 14, 7])

        p = h.replace(0, 1)
        assert p == HeapNode(28)
        assert h.size() == 4
        self.assertTrue(is_max_heap(h))

        p = h.replace(3, 99)
        assert p == HeapNode(7)
        assert h.size() == 4
        self.assertTrue(is_max_heap(h))

        p = h.replace(0, HeapNode(0))
        assert p == HeapNode(99)
        assert h.size() == 4

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

        assert h.is_good_index(0)
        assert h.is_good_index(1)
        assert h.is_good_index(2)
        assert not h.is_good_index(-1)
        assert not h.is_good_index(3)

    def test_parent_index(self):
        h = MaxHeap([12, 14, 28])

        self.assertRaises(IndexError, h.parent_index, -1)
        self.assertRaises(IndexError, h.parent_index, 3)

        assert h.parent_index(0) == -1
        assert h.parent_index(1) == 0
        assert h.parent_index(2) == 0

    def test_grandparent_index(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.grandparent_index, -1)
        self.assertRaises(IndexError, h.grandparent_index, 5)

        assert h.grandparent_index(0) == -1
        assert h.grandparent_index(1) == -1
        assert h.grandparent_index(2) == -1
        assert h.grandparent_index(3) == 0
        assert h.grandparent_index(4) == 0

    def test_left_index(self):
        h = MaxHeap([12, 14, 28])

        self.assertRaises(IndexError, h.left_index, -1)
        self.assertRaises(IndexError, h.left_index, 3)

        assert h.left_index(0) == 1
        assert h.left_index(1) == -1
        assert h.left_index(2) == -1

    def test_right_index(self):
        h = MaxHeap([12, 14, 28, 6])

        self.assertRaises(IndexError, h.right_index, -1)
        self.assertRaises(IndexError, h.right_index, 4)

        assert h.right_index(0) == 2
        assert h.right_index(1) == -1
        assert h.right_index(2) == -1
        assert h.right_index(3) == -1
        assert h.left_index(1) == 3

    def test_has_children(self):
        h = MaxHeap([12, 14, 28, 6])

        self.assertRaises(IndexError, h.has_children, -1)

        assert h.has_children(0)
        assert h.has_children(1)
        assert not h.has_children(2)
        assert not h.has_children(3)

    def test_is_child(self):
        h = MaxHeap([12, 14, 28, 6])

        self.assertRaises(IndexError, h.is_child, -1, 3)
        self.assertRaises(IndexError, h.is_child, 0, 4)

        assert not h.is_child(0, 0)
        assert not h.is_child(1, 1)
        assert not h.is_child(2, 2)
        assert not h.is_child(3, 3)

        assert h.is_child(3, 1)
        assert h.is_child(2, 0)
        assert h.is_child(1, 0)
        assert not h.is_child(3, 0)
        assert not h.is_child(3, 2)

    def test_is_grandchild(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.is_grandchild, -1, 3)
        self.assertRaises(IndexError, h.is_grandchild, 0, 6)

        assert not h.is_grandchild(0, 0)
        assert not h.is_grandchild(1, 1)
        assert not h.is_grandchild(2, 2)
        assert not h.is_grandchild(3, 3)
        assert not h.is_grandchild(4, 4)

        assert h.is_grandchild(3, 0)
        assert not h.is_grandchild(3, 1)
        assert not h.is_grandchild(3, 2)
        assert not h.is_grandchild(3, 4)

        assert h.is_grandchild(4, 0)
        assert not h.is_grandchild(4, 1)
        assert not h.is_grandchild(4, 2)
        assert not h.is_grandchild(4, 3)

        assert not h.is_grandchild(1, 0)
        assert not h.is_grandchild(1, 2)
        assert not h.is_grandchild(1, 3)
        assert not h.is_grandchild(1, 4)

        assert not h.is_grandchild(2, 0)
        assert not h.is_grandchild(2, 1)
        assert not h.is_grandchild(2, 3)
        assert not h.is_grandchild(2, 4)

    def test_is_parent(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.is_parent, -1, 3)
        self.assertRaises(IndexError, h.is_parent, 0, 6)

        assert not h.is_parent(0, 0)
        assert not h.is_parent(1, 1)
        assert not h.is_parent(2, 2)
        assert not h.is_parent(3, 3)
        assert not h.is_parent(4, 4)

        assert h.is_parent(0, 1)
        assert h.is_parent(0, 2)
        assert not h.is_parent(0, 3)
        assert not h.is_parent(0, 4)

        assert h.is_parent(1, 3)
        assert h.is_parent(1, 4)
        assert not h.is_parent(1, 2)
        assert not h.is_parent(1, 0)

        assert not h.is_parent(2, 0)
        assert not h.is_parent(2, 1)
        assert not h.is_parent(2, 3)
        assert not h.is_parent(2, 4)

        assert not h.is_parent(3, 0)
        assert not h.is_parent(3, 1)
        assert not h.is_parent(3, 2)
        assert not h.is_parent(3, 4)

        assert not h.is_parent(4, 0)
        assert not h.is_parent(4, 1)
        assert not h.is_parent(4, 2)
        assert not h.is_parent(4, 3)

    def test_is_grandparent(self):
        h = MaxHeap([12, 14, 28, 6, 7])

        self.assertRaises(IndexError, h.is_grandparent, -1, 3)
        self.assertRaises(IndexError, h.is_grandparent, 0, 6)

        assert not h.is_grandparent(0, 0)
        assert not h.is_grandparent(1, 1)
        assert not h.is_grandparent(2, 2)
        assert not h.is_grandparent(3, 3)
        assert not h.is_grandparent(4, 4)

        assert not h.is_grandparent(0, 1)
        assert not h.is_grandparent(0, 2)
        assert h.is_grandparent(0, 3)
        assert h.is_grandparent(0, 4)

        assert not h.is_grandparent(1, 0)
        assert not h.is_grandparent(1, 2)
        assert not h.is_grandparent(1, 3)
        assert not h.is_grandparent(1, 4)

        assert not h.is_grandparent(2, 0)
        assert not h.is_grandparent(2, 1)
        assert not h.is_grandparent(2, 3)
        assert not h.is_grandparent(2, 4)

        assert not h.is_grandparent(3, 0)
        assert not h.is_grandparent(3, 1)
        assert not h.is_grandparent(3, 2)
        assert not h.is_grandparent(3, 4)

        assert not h.is_grandparent(4, 0)
        assert not h.is_grandparent(4, 1)
        assert not h.is_grandparent(4, 2)
        assert not h.is_grandparent(4, 3)

    def test_is_on_even_level(self):
        h = MaxHeap([12, 14, 28, 6, 7, 18, 10, 3, 1])

        self.assertRaises(IndexError, h.is_on_even_level, -1)

        assert h.is_on_even_level(0)
        assert not h.is_on_even_level(1)
        assert not h.is_on_even_level(2)
        assert h.is_on_even_level(3)
        assert h.is_on_even_level(4)
        assert h.is_on_even_level(5)
        assert h.is_on_even_level(6)
        assert not h.is_on_even_level(7)
        assert not h.is_on_even_level(8)

    def test_is_on_odd_level(self):
        h = MaxHeap([12, 14, 28, 6, 7, 18, 10, 3, 1])

        self.assertRaises(IndexError, h.is_on_odd_level, 10)

        assert not h.is_on_odd_level(0)
        assert h.is_on_odd_level(1)
        assert h.is_on_odd_level(2)
        assert not h.is_on_odd_level(3)
        assert not h.is_on_odd_level(4)
        assert not h.is_on_odd_level(5)
        assert not h.is_on_odd_level(6)
        assert h.is_on_odd_level(7)
        assert h.is_on_odd_level(8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
