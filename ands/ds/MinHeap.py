#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 17/02/16

A binary min-heap is a data structure similar to a binary tree,
where the parent nodes are smaller or equal to their children.

In addition to the previous constraint, a binary min-heap is a complete binary tree,
that is, all levels of the tree, except possibly the deepest one are fully filled,
and, if the last level of the tree is not complete,
the nodes of that level are filled from left to right.

A min-heap can be implemented with a classic array or list in Python.

If we have a node at index i, then

- its left child can be found at index i*2 + 1

- its right child is found at i*2 + 2,

- its parent can be found at index floor((i - 1) / 2),
where floor(x) truncates x to the smallest integer.

Note that these indexes are for 0-index based lists (or arrays).

## References

- [https://en.wikipedia.org/wiki/Binary_heap](https://en.wikipedia.org/wiki/Binary_heap)

- Slides by prof. A. Carzaniga

- Chapter 13 of _Introduction to Algorithms_ (3rd ed.) by CLRS
"""

from ands.ds.Heap import Heap
from ands.ds.HeapNode import HeapNode


__all__ = ["MinHeap", "is_min_heap"]


class MinHeap(Heap):

    def __init__(self, ls=[]):
        Heap.__init__(self, ls)

    def _build_heap(self):
        """Creates a min-heap using the list passed to the constructor.

        Note that in a heap A all nodes from A[n/2 + 1] to A[n] are leaf nodes.

        **Time Complexity:** O(n)."""
        if self.heap:
            for index in range(len(self.heap) // 2, -1, -1):
                self.push_down(index)
        return self.heap

    def push_down(self, i: int):
        """'Min-heapify' this min-heap starting from index `i`.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        m = i  # index of node with smallest value among i and its children
        l = self.left_index(i)
        r = self.right_index(i)

        if l and self.heap[l] < self.heap[m]:
            m = l
        if r and self.heap[r] < self.heap[m]:
            m = r
            
        if m != i:
            self.swap(m, i)
            self.push_down(m)

    def push_up(self, i: int):
        """Pushes up the node at index `i`.

        Note that this operation only happens
        if the node at index `i` is smaller than its parent.

        This function is simpler than `push_down` (or also called min-heapify),
        because in this case we just need to compare
        the current node's index with its parent's index.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        c = i  # current index
        p = self.parent_index(i)
        
        # p could be 0, so we evaluate against not None.
        if p is not None and self.heap[c] < self.heap[p]:
            c = p

        if c != i:
            self.swap(c, i)
            self.push_up(c)
            
    def add(self, x):
        """Adds a `x` to this min-heap.

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

    def find_min(self):
        """Returns (without removing) the smallest element in this min-heap.

        **Time Complexity:** O(1)."""
        return self.heap[0] if not self.is_empty() else None

    def remove_min(self):
        """Removes and returns the smallest element in this heap.

        **Time Complexity:** O(log<sub>2</sub> n),
        if removing the last element of a list is a constant-time operation."""
        if not self.is_empty():
            self.swap(0, self.size() - 1)
            m = self.heap.pop()            
            if not self.is_empty():
                self.push_down(0)
            return m

    def search(self, x) -> int:
        """Searches for `x` in this min-heap,
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

        If `val` and the values in this min-heap are not comparable,
        the behaviour of this method is undefined.

        **Time Complexity:** O(n)."""
        if val is None:
            raise ValueError("val cannot be None.")
        
        for i, node in enumerate(self.heap):
            if node.value == val:
                return i
        return -1
    
    def contains(self, x) -> bool:
        """Returns True, if `x` is in this min-heap. `False` otherwise.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`.
        
        **Time Complexity:** O(n)."""
        return self.search(x) != -1    

    def merge(self, other: Heap) -> list:
        """Merges this min-heap with the `other` heap.
        
        Returns the `list` object representing internally the new merged min-heap.

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

        2. Else if `x < self.heap[i]`,
        then push_up(index).

        3. Else `x > self.heap[i]`,
        then call `self.push_down(i)`.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, HeapNode):
            x = HeapNode(x)
        if not self.is_good_index(i):
            raise IndexError("i is not a valid index.")

        c = self.heap[i]
        self.heap[i] = x

        if x > c:
            self.push_down(i)
        elif x < c:
            self.push_up(i)
        return c


def is_min_heap(h):
    if not isinstance(h, MinHeap):
        return False
    if h.heap:
        for item in h.heap:
            if not isinstance(item, HeapNode):
                return False
        for i, item in enumerate(h.heap):
            l = h.left_index(i)
            r = h.right_index(i)
            if r and not l:
                return False
            if l and item > h.heap[l]:
                return False
            if r and item > h.heap[r]:
                return False
    return True  # h is empty
