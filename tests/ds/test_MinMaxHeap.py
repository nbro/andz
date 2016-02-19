#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 18/02/16

Tests for the MinMaxHeap class.
"""

from random import randint
from ands.ds.MinMaxHeap import MinMaxHeap, is_min_max_heap


def test_empty_heap_creation():
    h = MinMaxHeap()
    assert is_min_max_heap(h)
    h.show()
    assert h.size() == 0 and h.is_empty()

def test_build_heap():
    h = MinMaxHeap([12, 14, 28, 7, 10, 6, 18])
    assert is_min_max_heap(h)
    assert h.size() == 7

    t = 20
    ls = [randint(0, 100) for _ in range(t)]
    h = MinMaxHeap(ls)
    assert h.size() == t
    assert is_min_max_heap(h)

        
if __name__ == "__main__":
    from tools import main
    main(globals().copy(), __name__, __file__)
