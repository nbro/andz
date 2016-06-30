#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 20/02/16

Last update: 30/06/16

Tests for the MinMaxHeap class.
"""

import unittest

from random import randint, choice
from ands.ds.MinMaxHeap import MinMaxHeap, is_min_max_heap, HeapNode


class TestMinMaxHeap(unittest.TestCase):

    def test_empty_heap_creation(self):
        h = MinMaxHeap()
        assert is_min_max_heap(h)
        assert h.size() == 0 and h.is_empty()

    def test_build_heap(self):
        h = MinMaxHeap([12, 14, 28, 7, 10, 6, 18])
        assert is_min_max_heap(h)
        assert h.size() == 7

        t = 20
        ls = [randint(0, 100) for _ in range(t)]
        h = MinMaxHeap(ls)
        assert h.size() == t
        assert is_min_max_heap(h)

    def test_add(self):
        h = MinMaxHeap([100, 12, 14, 28, 7])
        assert is_min_max_heap(h)
        assert h.size() == 5
        
        t = 20
        ls = [randint(0, 100) for _ in range(t)]
        
        for i, item in enumerate(ls):
            h.add(item)
            assert h.size() == 6 + i
            assert h.find_min() == h.heap[0]
            assert (h.find_max() == h.heap[1] or h.find_max() == h.heap[2])
            assert is_min_max_heap(h)
        assert h.size() == 25

    def test_remove_and_find_min_and_remove_max(self):
        h = MinMaxHeap()
        assert is_min_max_heap(h)

        t = 20
        ls = [randint(0, 100) for _ in range(t)]
        for i, item in enumerate(ls):
            h.add(item)
            assert 1 + i == h.size()
            assert is_min_max_heap(h)
            assert h.find_min() == h.heap[0] == min(h.heap)        
            if h.size() == 1:
                assert h.find_max() == h.find_min() == h.heap[0] == min(h.heap) == max(h.heap)
            elif h.size() == 2:
                assert h.find_max() == h.heap[1] == max(h.heap)
            else:
                assert (max(h.heap) == h.find_max() == h.heap[1] or max(h.heap) == h.find_max() == h.heap[2])
            assert is_min_max_heap(h)        

        while not h.is_empty():
            m = h.remove_min()
            assert isinstance(m, HeapNode)
            assert min(ls) == m.key
            ls.remove(m.key)
            assert len(ls) == h.size()
            assert is_min_max_heap(h)

            M = h.remove_max()
            assert isinstance(M, HeapNode)
            assert max(ls) == M.key
            ls.remove(M.key)
            assert len(ls) == h.size()
            assert is_min_max_heap(h)

        assert h.is_empty()

    def test_delete(self):
        h = MinMaxHeap([28, 12, 14, 7, 10])
        assert is_min_max_heap(h)
        assert h.size() == 5

        while not h.is_empty():
            n = h.delete(choice(range(h.size())))
            assert isinstance(n, HeapNode)
            assert is_min_max_heap(h)

    def test_index_of_min_and_max(self):
        h = MinMaxHeap([28, 12, 14, 7, 10, 6, 18, 3, 11])
        assert is_min_max_heap(h)
        
        def assert_errors(a):
            try:
                h.index_of_min(a)
                assert False
            except IndexError:
                pass
            except TypeError:
                pass
            
        assert_errors(-1)
        assert_errors(None)
        assert_errors("0")
        assert_errors(30)

        h.show()

        assert h.index_of_min(0) == 5
        assert h.index_of_max(0) == 1

        assert h.index_of_min(1) == 3
        assert h.index_of_max(1) == 7

        assert h.index_of_min(2) == 5
        assert h.index_of_max(2) == 6

        assert h.index_of_min(3) == 8
        assert h.index_of_max(3) == 7

        assert h.index_of_min(5) == -1 == h.index_of_max(5)
        assert h.index_of_min(6) == -1 == h.index_of_max(6)
        assert h.index_of_min(7) == -1 == h.index_of_max(7)
        assert h.index_of_min(8) == -1 == h.index_of_max(8)
    
         
if __name__ == "__main__":
    unittest.main(verbose=2)
