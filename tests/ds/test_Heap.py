#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 13/02/16

Tests for the abstract class Heap.
"""

from ands.ds.Heap import Heap
from ands.ds.HeapNode import HeapNode


def test_add():
    h = Heap()
    try:
        h.add(12)
        assert False
    except NotImplementedError:
        pass
    print("test_add finished.")

def test_heapify():
    h = Heap()    
    try:
        h.heapify(0)
        assert False
    except NotImplementedError:
        pass
    print("test_heapify finished.")

def test_search():
    h = Heap()
    n = HeapNode(12, "Twelve")
    try:
        h.search(n)
        assert False
    except NotImplementedError:
        pass
    print("test_search finished.")

def test_search_by_value():
    h = Heap()
    try:
        h.search_by_value("Twelve")
        assert False
    except NotImplementedError:
        pass
    print("test_search_by_value finished.")

def test_contains():
    h = Heap()
    n = HeapNode(12, "Twelve")
    try:
        h.contains(n)
        assert False
    except NotImplementedError:
        pass
    print("test_contains finished.")

def test_replace():
    h = Heap()
    n = HeapNode(12, "Twelve")
    try:
        h.replace(0, n)
        assert False
    except NotImplementedError:
        pass
    print("test_replace finished.")

def test_remove():
    h = Heap()
    try:
        h.remove(0)
        assert False
    except NotImplementedError:
        pass
    print("test_remove finished.")

def test_size_and_is_empty():
    h = Heap()
    assert h.size() == 0
    assert h.is_empty()
    print("test_size_and_is_empty finished.")

def test_clear_and_get():
    h = Heap()
    h.clear()
    assert h.is_empty()
    assert [] == h.get()
    print("test_clear_and_get finished.")

def test_create_list_of_heap_nodes():
    ls = []
    heap_nodes = Heap._create_list_of_heap_nodes(ls)
    assert not heap_nodes
    
    ls = [12, 14, 28, 6, 18, 7, 10]
    heap_nodes = Heap._create_list_of_heap_nodes(ls)
    assert heap_nodes
    
    for item in heap_nodes:
        assert isinstance(item, HeapNode)
        assert item.index != -1
        assert item.key == item.value

    ls = [("Tu", 1), ("Io", 99), ("Noi", 2)]
    heap_nodes = Heap._create_list_of_heap_nodes(ls)
    assert heap_nodes
    
    for i, item in enumerate(heap_nodes):
        assert isinstance(item, HeapNode)
        assert item.index != -1
        assert item.index == i
        assert type(item.key) != type(item.value)
        assert item.key in (1, 99, 2)
        assert item.value in ("Tu", "Io", "Noi")
        
    print("test_create_list_of_heap_nodes finished.")

def test_is_good_index():
    ls = [12, 14, 28, 6, 18, 7, 10]
    try:
        Heap.is_good_index(ls, -1)
        assert False
    except IndexError:
        pass
    assert not Heap.is_good_index(ls, -10, raise_error=False)
    assert Heap.is_good_index(ls, 0, raise_error=False)
    print("test_is_good_index finished.")

def test_swap():
    ls = [12, 14, 28, 6, 18, 7, 10]
    first = ls[0]
    last = ls[-1]
    Heap.swap(ls, 0, len(ls) - 1)
    assert ls[0] == last and ls[-1] == first
    print("test_swap finished.")

def test_get_parent_index():
    ls = [12, 14, 28, 6, 18, 7, 10]        
    assert not Heap.get_parent_index(ls, 0)
    assert Heap.get_parent_index(ls, 1) == 0
    assert Heap.get_parent_index(ls, 2) == 0
    assert Heap.get_parent_index(ls, 3) == 1
    assert Heap.get_parent_index(ls, 4) == 1
    assert Heap.get_parent_index(ls, 5) == 2
    assert Heap.get_parent_index(ls, 6) == 2
    try:
        Heap.get_parent_index(ls, -1)
        assert False
    except IndexError:
        pass
    try:
        Heap.get_parent_index(ls, len(ls))
        assert False
    except IndexError:
        pass
    print("test_get_parent_index finished.")

def test_get_left_child_index():
    ls = [12, 14, 28, 6, 18, 7, 10]
    assert Heap.get_left_child_index(ls, 0) == 1
    assert Heap.get_left_child_index(ls, 1) == 3
    assert Heap.get_left_child_index(ls, 2) == 5
    assert not Heap.get_left_child_index(ls, 3)
    try:
        Heap.get_left_child_index(ls, -1)
        assert False
    except IndexError:
        pass    
    try:
        Heap.get_left_child_index(ls, len(ls))
        assert False
    except IndexError:
        pass    
    print("test_get_left_child_index finished.")

def test_get_right_child_index():
    ls = [12, 14, 28, 6, 18, 7, 10]
    assert Heap.get_right_child_index(ls, 0) == 2
    assert Heap.get_right_child_index(ls, 1) == 4
    assert Heap.get_right_child_index(ls, 2) == 6
    assert not Heap.get_right_child_index(ls, 3)
    try:
        Heap.get_right_child_index(ls, -1)
        assert False
    except IndexError:
        pass    
    try:
        Heap.get_right_child_index(ls, len(ls))
        assert False
    except IndexError:
        pass
    print("test_get_right_child_index finished.")

    
if __name__ == "__main__":
    test_add()
    test_heapify()
    test_search()
    test_search_by_value()
    test_contains()
    test_replace()
    test_remove()
    test_size_and_is_empty()
    test_clear_and_get()
    test_create_list_of_heap_nodes()
    test_is_good_index()
    test_swap()
    test_get_parent_index()
    test_get_left_child_index()
    test_get_right_child_index()
