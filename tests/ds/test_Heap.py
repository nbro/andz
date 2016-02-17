#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 14/02/16

Last update: 16/02/16

Tests for the abstract class Heap.
"""

from ands.ds.Heap import Heap
from ands.ds.HeapNode import HeapNode


def test_heap_creation():
    try:
        Heap([12, 14, 28])
        assert False
    except NotImplementedError:
        pass

if __name__ == "__main__":
    from tools import main
    main(globals().copy(), __name__, __file__)
