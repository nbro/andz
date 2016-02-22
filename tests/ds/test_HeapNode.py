#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Tests for the HeapNode class.
"""

from ands.ds.Heap import HeapNode


def test_None():
    try:
        HeapNode(None)
        assert False
    except ValueError:
        pass

def test_comparisons():        
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
    from tools import main
    main(globals().copy(), __name__, __file__)
