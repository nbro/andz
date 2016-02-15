#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 14/02/16

Tests for the MinHeap class.
"""

from random import randint
from ands.ds.MinHeap import MinHeap
from ands.ds.HeapNode import HeapNode


def assert_min_heap_props(h):
    if h.heap:
        for item in h.heap:
            assert isinstance(item, HeapNode)
        for i, item in enumerate(h.heap):
            left_index = MinHeap.get_left_child_index(h.heap, i)
            right_index = MinHeap.get_right_child_index(h.heap, i)
            if right_index:
                assert left_index                
            if left_index:
                assert item <= h.heap[left_index]
            if right_index:
                assert item <= h.heap[right_index]

def test_empty_heap_creation():
    h = MinHeap()
    assert_min_heap_props(h)

def test_is_empty_and_size():
    h = MinHeap()
    assert_min_heap_props(h)
    assert h.is_empty()
    assert h.size() == 0
    assert_min_heap_props(h)

    ls = []
    for i in range(10):
        ls.append(randint(-100, 100))
        h.add(ls[-1])    
        assert not h.is_empty()
        assert h.size() == (i + 1)
        assert_min_heap_props(h)

    c = 0
    while not h.is_empty():
        n = h.remove_min()
        assert n and n.key in ls
        c += 1
        assert_min_heap_props(h)
    assert c == 10
    assert h.is_empty() and h.size() == 0

def test_build_min_heap():
    h = MinHeap([12])
    assert h.search_by_value(12) == 0
    assert h.contains(12)
    assert h.size() == 1
    assert not h.is_empty()
    assert h.find_min() == HeapNode(12, 12)
    assert_min_heap_props(h)

    h.remove_min() == HeapNode(12, 12)
    assert h.is_empty()
    assert_min_heap_props(h)
    
    h = MinHeap([28, 14, 12, 10, 7, 6, 18])
    assert h.search_by_value(6) == 0
    assert h.contains(28)
    assert h.contains(7)
    assert h.size() == 7
    assert not h.is_empty()
    assert h.find_min() == HeapNode(6, 6)
    assert_min_heap_props(h)

    m = h.remove_min()
    assert m == HeapNode(6, 6)
    assert h.find_min() == HeapNode(7, 7)
    assert h.search_by_value(6) == -1
    assert not h.contains(6)
    assert h.contains(7)
    assert h.size() == 6
    assert not h.is_empty()
    assert_min_heap_props(h)

def test_push_down():
    h = MinHeap([28, 14, 12, 10, 7, 6, 18])
    assert_min_heap_props(h)
    h.heap[0] = HeapNode(94)
    h.push_down(0)
    assert_min_heap_props(h)
    
def test_push_up():
    h = MinHeap([28, 14, 12, 10, 7, 6, 18])
    assert_min_heap_props(h)
    h.heap[h.size() - 1] = HeapNode(3)
    h.push_up(h.size() - 1)
    assert_min_heap_props(h)

def test_add():
    h = MinHeap()
    assert_min_heap_props(h)
    try:
        h.add(None)
        assert False
    except ValueError:
        pass
    
    h.add(12)
    assert h.size() == 1
    assert h.find_min() == HeapNode(12)
    assert h.heap[0] == h.find_min()
    assert_min_heap_props(h)

    ls = []
    for i in range(100):
        ls.append(randint(-100, 100))
        h.add(ls[-1])
        assert h.size() == (i + 2)
        assert h.contains(HeapNode(ls[-1]))        
        assert_min_heap_props(h)

    s = h.size()
    h.add(HeapNode(1024))
    assert h.size() == (s + 1)
    assert h.search(HeapNode(1024)) != -1
    assert_min_heap_props(h)

    s = h.size()
    h.add(HeapNode(2048, "2^11"))
    assert h.size() == (s + 1)
    assert h.contains(HeapNode(2048, "2^11"))
    assert_min_heap_props(h)
    
def test_find_min():
    h = MinHeap([28, 14, 12, 10])

    assert h.size() == 4    
    assert_min_heap_props(h)

    m = h.find_min()
    assert m == h.remove_min() == HeapNode(10)
    assert h.size() == 3
    assert_min_heap_props(h)
    
    m = h.find_min()
    assert m == h.remove_min() == HeapNode(12)
    assert h.size() == 2
    assert_min_heap_props(h)

    m = h.find_min()
    assert m == h.remove_min() == HeapNode(14)
    assert h.size() == 1
    assert_min_heap_props(h)

    m = h.find_min()
    assert m == h.remove_min() == HeapNode(28)
    assert h.size() == 0
    assert not h.find_min()
    assert_min_heap_props(h)
    
def test_remove_min():
    ls = [28, 14, 12, 10, 7, 6, 18]
    h = MinHeap(ls)
    assert_min_heap_props(h)
    c = len(ls)
    
    while not h.is_empty():
        m = h.remove_min()
        assert m
        assert m.key in ls
        assert h.size() == (c - 1)
        c -= 1
        assert_min_heap_props(h)
        
    assert c == 0
    assert not h.remove_min()
    assert_min_heap_props(h)
    
def test_search():
    ls = [28, 14, 12, 10, 7, 6, 18]
    h = MinHeap(ls)

    v = h.search(12)
    assert v in range(0, len(ls))
    assert h.size() == len(ls)
    assert_min_heap_props(h)
    
    v = h.search(HeapNode(14))
    assert v in range(0, len(ls))
    assert h.size() == len(ls)
    assert_min_heap_props(h)

    v = h.search(HeapNode(12, "Noi"))
    assert v == -1
    assert h.size() == len(ls)
    assert_min_heap_props(h)

    try:
        h.search(None)
        assert False
    except ValueError:
        assert_min_heap_props(h)
    
def test_search_by_value():
    ls = [28, 14, 12]
    h = MinHeap(ls)

    try:
        # values are not comparable
        h.search_by_value(HeapNode(14))
        assert False
    except Exception:
        assert_min_heap_props(h)

    v = h.search_by_value(14)
    assert v in range(0, len(ls))
    assert h.size() == len(ls)
    assert_min_heap_props(h)

    ls = [(12, "Noi"), (14, "Tu")]
    h = MinHeap(ls)
    v = h.search_by_value("Tu")
    assert v in range(0, len(ls))
    assert h.size() == len(ls)
    assert_min_heap_props(h)

    try:
        v = h.search_by_value(None)
        assert False
    except ValueError:
        assert_min_heap_props(h)    
    
def test_contains():
    ls = [28, 14, 12]
    h = MinHeap(ls)
    assert h.contains(28) and h.contains(14) and h.contains(12)
    assert_min_heap_props(h)
    assert not h.contains(200) and not h.contains(7)
    
    try:
        h.search(None)
        assert False
    except ValueError:
        assert_min_heap_props(h)  
    
def test_merge():
    h = MinHeap([12, 14, 28])
    assert_min_heap_props(h)
    assert h.size() == 3

    h2 = MinHeap([(30, "15x2"), (1, "1")])
    assert h2.size() == 2
    assert_min_heap_props(h)

    h.merge(h2)
    assert h.size() == 5
    assert h.find_min() == HeapNode(1, "1")
    assert h2.size() == 2
    assert_min_heap_props(h)
    
def test_replace():
    h = MinHeap([28, 12, 14, 7])

    p = h.replace(0, 3)
    assert p == HeapNode(7)
    assert h.size() == 4
    assert_min_heap_props(h)

    p = h.replace(3, 1)
    assert p == HeapNode(28)
    assert h.size() == 4
    assert_min_heap_props(h)

    p = h.replace(0, HeapNode(1))
    assert p == HeapNode(1)
    assert h.size() == 4
    assert_min_heap_props(h)

    try:
        h.replace(0, None)
        assert False
    except ValueError:
        pass

    try:
        h.replace(-1, 3)
        assert False
    except IndexError:
        pass
        
    
if __name__ == "__main__":
    from tools import main
    main(globals().copy(), __name__, __file__)
