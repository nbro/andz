#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Last update: 15/02/16

Mirror-class to the MinHeap class.
"""

from ands.ds.Heap import Heap
from ands.ds.HeapNode import HeapNode


__all__ = ["MaxHeap"]


class MaxHeap(Heap):

    def __init__(self, ls=[]):
        Heap.__init__(self, ls)
        self._build_heap()

    def _build_heap(self):
        """Creates a max-heap using the list passed to the constructor.

        Note that in a heap A all nodes from A[n/2 + 1] to A[n] are leaf nodes.

        **Time Complexity:** O(n)."""
        if self.heap:
            for index in range(len(self.heap) // 2, -1, -1):
                self.push_down(index)
        return self.heap

    def push_down(self, i: int):
        """'Max-heapify' this max-heap starting from index `i`.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        max_index = i
        left_index = MaxHeap.get_left_child_index(self.heap, i)
        right_index = MaxHeap.get_right_child_index(self.heap, i)

        if left_index and self.heap[left_index] > self.heap[max_index]:
            max_index = left_index

        if right_index and self.heap[right_index] > self.heap[max_index]:
            max_index = right_index

        if max_index != i:
            MaxHeap.swap(self.heap, max_index, i)
            self.push_down(max_index)

        return max_index

    def push_up(self, i: int):
        """Pushes up the node at index `i`.

        Note that this operation only happens
        if the node at index `i` is greater than its parent.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        c = i  # current index
        p = MaxHeap.get_parent_index(self.heap, i)

        if p is not None and self.heap[c] > self.heap[p]:
            c = p

        if c != i:
            MaxHeap.swap(self.heap, c, i)
            self.push_up(c)
            
    def add(self, x):
        """Adds a `x` to this max-heap.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`.
         
        **Time Complexity:** O(log<sub>2</sub> n)."""
        if x is None:
            raise ValueError("x cannot be None.")
        
        if not isinstance(x, HeapNode):
            x = HeapNode(x)
    
        self.heap.append(x)
        
        if self.size() > 1:
            self.push_up(self.size() - 1)

    def find_max(self):
        """Returns (without removing) the greatest element in this max-heap.

        **Time Complexity:** O(1)."""
        return self.heap[0] if not self.is_empty() else None

    def remove_max(self):
        """Removes and returns the greatest element in this max-heap.

        **Time Complexity:** O(log<sub>2</sub> n),
        if removing the last element of a list is a constant-time operation."""
        if not self.is_empty():

            MaxHeap.swap(self.heap, 0, self.size() - 1)
            max_element = self.heap.pop()
            
            if not self.is_empty():
                self.push_down(0)

            return max_element

    def search(self, x) -> int:
        """Searches for `x` in this max-heap,
        and if present, returns its index, otherwise returns -1.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`.
 
        **Time Complexity:** O(n)."""
        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, HeapNode):
            x = HeapNode(x)
        for i, node in enumerate(self.heap):
            if node == x:
                return i
        return -1

    def search_by_value(self, val) -> int:
        """Returns the index of the `HeapNode` object with `value=val`.
        -1 is returned if no such a `HeapNode` object exists.

        If `val` and the values in this max-heap are not comparable,
        the behaviour of this method is undefined.

        **Time Complexity:** O(n)."""
        if val is None:
            raise ValueError("val cannot be None.")    
        for i, node in enumerate(self.heap):
            if node.value == val:
                return i
        return -1
    
    def contains(self, x) -> bool:
        """Returns True, if `x` is in this max-heap. `False` otherwise.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`.
        
        **Time Complexity:** O(n)."""
        return self.search(x) != -1    

    def merge(self, other: Heap) -> list:
        """Merges this max-heap with the `other` max-heap.
        
        Returns the `list` object representing internally the new merged max-heap.

        **Time Complexity:** O(n + m).

        Time complexity analysis based on:
        [http://stackoverflow.com/a/29197855/3924118](http://stackoverflow.com/a/29197855/3924118)."""
        self.heap += other.get()
        return self._build_heap()

    def replace(self, i: int, x):
        """Replaces element at index `i` with `x`.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, then a `HeapNode` object
        first created to represent `x`.

        1. If `x == self.heap[i]`,
        then just replace `self.heap[i]` with `x`.

        2. Else if `x > self.heap[i]`,
        then push_up(index).

        3. Else `x < self.heap[i]`,
        then call `self.push_down(i)`.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        if x is None:
            raise ValueError("x cannot be None.")
        
        if not isinstance(x, HeapNode):
            x = HeapNode(x)
        
        MaxHeap.is_good_index(self.heap, i)

        c = self.heap[i]
        self.heap[i] = x

        if x < c:
            self.push_down(i)
        elif x > c:
            self.push_up(i)
            
        return c
