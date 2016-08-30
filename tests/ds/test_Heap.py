#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 14/02/16

Last update: 28/08/16

Tests for the abstract class Heap.
"""

import unittest

from ands.ds.Heap import Heap, HeapNode


class TestHeap(unittest.TestCase):

    def test_heap_creation(self):
        try:
            Heap([12, 14, 28])
            assert False
        except NotImplementedError:
            pass
        assert Heap()


class TestHeapNode(unittest.TestCase):

    def test_None(self):
        try:
            HeapNode(None)
            assert False
        except ValueError:
            pass

    def test_comparisons(self):
        h = HeapNode(12)
        assert h.value is not None
        assert h.key == h.value

        h2 = HeapNode(14)
        assert h.value is not None

        h3 = HeapNode(12, "Twelve")
        assert h3.key != h3.value

        assert h < h2
        assert h != h3
        assert h3 < h2
        assert h3 == HeapNode(12, "Twelve")
        assert h3 != HeapNode("Twelve", 12)

        assert h <= h3
        assert h3 <= h
        assert h >= h3
        assert h3 >= h

        assert h == h
        assert h2 == h2
        assert h3 == h3

        assert h3 <= h3
        assert h2 <= h2
        assert h <= h

        assert not h < h
        assert not h > h
        assert not h2 < h2
        assert not h2 > h2
        assert not h3 < h3
        assert not h3 > h3


if __name__ == "__main__":
    unittest.main(verbosity=2)
