#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 20/02/2016

Updated: 14/02/2017

# Description

Tests for the MinMaxHeap class.
"""

import unittest
from random import randint, randrange

from ands.ds.MinMaxHeap import MinMaxHeap, is_min_max_heap, HeapNode


class TestMinMaxHeap(unittest.TestCase):
    def test_empty_heap_creation(self):
        h = MinMaxHeap()
        self.assertTrue(is_min_max_heap(h))
        self.assertEqual(h.size(), 0)
        self.assertTrue(h.is_empty())

    def test_build_heap(self):
        t = randint(100, 500)
        ls = [randint(0, 100) for _ in range(t)]
        h = MinMaxHeap(ls)
        self.assertTrue(is_min_max_heap(h))
        self.assertEqual(h.size(), t)

    def test_add(self):
        h = MinMaxHeap([100, 12, 14, 28, 7])
        t = randint(100, 500)
        ls = [randint(0, 100) for _ in range(t)]

        for i, item in enumerate(ls):
            h.add(item)
            self.assertEqual(h.size(), 6 + i)
            self.assertEqual(h.find_min(), h.heap[0])

            m = h.heap[1] if h.heap[1] > h.heap[2] else h.heap[2]

            self.assertEqual(h.find_max(), m)
            self.assertTrue(is_min_max_heap(h))

        self.assertEqual(h.size(), 5 + t)

    def test_add_heap_nodes(self):
        h = MinMaxHeap()
        t = randint(100, 500)
        ls = [HeapNode(randint(0, 100)) for _ in range(t)]

        for i, item in enumerate(ls):
            h.add(item)
            self.assertEqual(h.size(), i + 1)
            self.assertEqual(h.find_min(), h.heap[0])

            if h.size() == 1:
                self.assertEqual(h.find_max(), h.heap[0])
            elif h.size() == 2:
                self.assertEqual(h.find_max(), h.heap[1])
            else:
                m = h.heap[1] if h.heap[1] > h.heap[2] else h.heap[2]
                self.assertEqual(h.find_max(), m)

            self.assertTrue(is_min_max_heap(h))

        self.assertEqual(h.size(), t)

    def test_find_min_and_max(self):
        h = MinMaxHeap()

        # should return none if heap is empty
        self.assertIsNone(h.find_max())
        self.assertIsNone(h.find_min())

        t = randint(100, 500)
        ls = [randint(0, 100) for _ in range(t)]

        for i, item in enumerate(ls):
            h.add(item)

            # asserts that the min is always at index 0
            self.assertEqual(1 + i, h.size())
            self.assertEqual(h.find_min(), h.heap[0])
            self.assertEqual(h.heap[0], min(h.heap))

            # checking that max is in correct position
            # depending if size is 1, 2 or >2
            if h.size() == 1:
                self.assertEqual(h.find_max(), h.find_min())
                self.assertEqual(h.find_min(), h.heap[0])
                self.assertEqual(h.heap[0], min(h.heap))
                self.assertEqual(min(h.heap), max(h.heap))
            elif h.size() == 2:
                self.assertEqual(h.find_max(), h.heap[1])
                self.assertEqual(h.heap[1], max(h.heap))
            else:
                m = h.heap[1] if h.heap[1] > h.heap[2] else h.heap[2]
                self.assertEqual(max(h.heap), h.find_max())
                self.assertEqual(h.find_max(), m)

            self.assertTrue(is_min_max_heap(h))

    def test_remove_min_and_max(self):
        t = randint(500, 1000)
        ls = [randint(0, 100) for _ in range(t)]
        h = MinMaxHeap(ls)

        while not h.is_empty():
            m = h.remove_min()
            self.assertIsInstance(m, HeapNode)
            self.assertEqual(min(ls), m.key)
            ls.remove(m.key)
            self.assertEqual(len(ls), h.size())
            self.assertTrue(is_min_max_heap(h))

            if not h.is_empty():
                M = h.remove_max()
                self.assertIsInstance(M, HeapNode)
                self.assertEqual(max(ls), M.key)
                ls.remove(M.key)
                self.assertEqual(len(ls), h.size())
                self.assertTrue(is_min_max_heap(h))

        self.assertTrue(h.is_empty())
        self.assertIsNone(h.remove_max())
        self.assertIsNone(h.remove_min())

    def test_delete(self):
        t = randint(500, 1000)
        ls = [randint(0, 100) for _ in range(t)]
        h = MinMaxHeap(ls)

        self.assertRaises(IndexError, h.delete, -1)
        self.assertRaises(IndexError, h.delete, h.size())

        while not h.is_empty():
            n = h.delete(randrange(0, h.size()))
            t -= 1
            self.assertIsInstance(n, HeapNode)
            self.assertEqual(h.size(), t)
            self.assertTrue(is_min_max_heap(h))

    def replace_helper(self, h, t, ls):
        for x in ls:
            i = randrange(0, h.size())
            elem = h.heap[i]
            d = h.replace(i, x)
            self.assertIs(d, elem)
            self.assertEqual(h.size(), t)
            self.assertTrue(is_min_max_heap(h))

    def test_replace(self):
        m1, m2 = 500, 1000
        t = randint(m1, m2)
        ls = [randint(0, 100) for _ in range(t)]

        h = MinMaxHeap(ls)

        self.assertRaises(IndexError, h.delete, -1)
        self.assertRaises(IndexError, h.delete, h.size())
        self.assertRaises(ValueError, h.replace, 0, None)

        t2 = randint(m1, m2)
        ls = [randint(0, 100) for _ in range(t2)]

        self.replace_helper(h, t, ls)

    def test_replace_with_heap_nodes(self):
        # testing when replacing with a HeapNode object
        m1, m2 = 500, 1000
        t = randint(m1, m2)
        ls = [randint(0, 100) for _ in range(t)]

        h = MinMaxHeap(ls)

        t2 = randint(m1, m2)
        ls = [HeapNode(randint(0, 100)) for _ in range(t2)]

        self.replace_helper(h, t, ls)

    def test_find_max_index(self):
        h = MinMaxHeap()
        self.assertEqual(h.find_max_index(), -1)

        h.add(randint(-10, 10))
        self.assertEqual(h.find_max_index(), 0)

        h.add(randint(-10, 10))
        self.assertEqual(h.find_max_index(), 1)

        t = randint(50, 100)
        ls = [randint(0, 100) for _ in range(t)]

        for elem in ls:
            h.add(elem)
            i = h.find_max_index()
            self.assertTrue(i == 1 or i == 2)

            m = h.heap[i]
            real_m = max(h.heap)
            self.assertEqual(real_m, m)
            self.assertTrue(is_min_max_heap(h))

        while not h.is_empty():
            i = h.find_max_index()

            if h.size() > 1:
                self.assertTrue(i == 1 or i == 2)
            else:
                self.assertEqual(i, 0)

            m = h.heap[i]
            real_m = max(h.heap)
            self.assertEqual(real_m, m)
            self.assertIsNotNone(h.delete(randrange(0, h.size())))
            self.assertTrue(is_min_max_heap(h))

    def test_index_of_min_and_max(self):
        h = MinMaxHeap([28, 12, 14, 7, 10, 6, 18, 3, 11])

        self.assertRaises(IndexError, h.index_of_min, -1)
        self.assertRaises(IndexError, h.index_of_min, 30)
        self.assertRaises(TypeError, h.index_of_min, "0")
        self.assertRaises(TypeError, h.index_of_min, None)

        self.assertEqual(h.index_of_min(0), 5)
        self.assertEqual(h.index_of_max(0), 1)
        self.assertEqual(h.index_of_min(1), 3)
        self.assertEqual(h.index_of_max(1), 7)
        self.assertEqual(h.index_of_min(2), 5)
        self.assertEqual(h.index_of_max(2), 6)
        self.assertEqual(h.index_of_min(3), 8)
        self.assertEqual(h.index_of_max(3), 7)

        self.assertEqual(h.index_of_min(5), -1)
        self.assertEqual(h.index_of_max(5), -1)
        self.assertEqual(h.index_of_min(6), -1)
        self.assertEqual(h.index_of_max(6), -1)
        self.assertEqual(h.index_of_min(7), -1)
        self.assertEqual(h.index_of_max(7), -1)
        self.assertEqual(h.index_of_min(8), -1)
        self.assertEqual(h.index_of_max(8), -1)

    def test_str(self):
        h = MinMaxHeap([7, 2, 92, 67])
        print(h)

    def test_repr(self):
        h = MinMaxHeap([7, 2, 92, 67])
        print(repr(h))
