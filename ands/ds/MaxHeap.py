#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Last update: 19/02/16

Mirror-class to the MinHeap class.
For more info, see the introductory doc-strings of the file [`MinHeap.py`](MinHeap.py).

## References

- [https://en.wikipedia.org/wiki/Binary_heap](https://en.wikipedia.org/wiki/Binary_heap)

- Slides by prof. A. Carzaniga

- Chapter 13 of [Introduction to Algorithms (3rd ed.)](https://mitpress.mit.edu/books/introduction-algorithms) by CLRS
"""

from ands.ds.Heap import Heap
from ands.ds.HeapNode import HeapNode


__all__ = ["MaxHeap", "is_max_heap"]


class MaxHeap(Heap):

    def __init__(self, ls=[]):
        Heap.__init__(self, ls)

    def push_down(self, i: int) -> None:
        """'Max-heapify' this max-heap starting from index `i`.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        m = i
        l = self.left_index(i)
        r = self.right_index(i)

        if l != -1 and self.heap[l] > self.heap[m]:
            m = l
        if r != -1 and self.heap[r] > self.heap[m]:
            m = r

        if m != i:
            self.swap(m, i)
            self.push_down(m)

    def push_up(self, i: int) -> None:
        """Pushes up the node at index `i`.

        Note that this operation only happens
        if the node at index `i` is greater than its parent.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        c = i  # current index
        p = self.parent_index(i)
        
        if p != -1 and self.heap[c] > self.heap[p]:
            c = p
            
        if c != i:
            self.swap(c, i)
            self.push_up(c)

    def find_max(self) -> HeapNode:
        """Returns (without removing) the greatest element in this max-heap.

        **Time Complexity:** O(1)."""
        return self.heap[0] if not self.is_empty() else None

    def remove_max(self) -> HeapNode:
        """Removes and returns the greatest element in this max-heap.

        **Time Complexity:** O(log<sub>2</sub> n),
        if removing the last element of a list is a constant-time operation."""
        if not self.is_empty():
            self.swap(0, self.size() - 1)
            m = self.heap.pop()
            if not self.is_empty():
                self.push_down(0)
            return m

    def replace(self, i: int, x) -> HeapNode:
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

        Returns the previous `HeapNode` object at `i`.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, HeapNode):
            x = HeapNode(x)
            
        if not self.is_good_index(i):
            raise IndexError("i is not a valid index.")

        c = self.heap[i]
        self.heap[i] = x

        if x < c:
            self.push_down(i)
        elif x > c:
            self.push_up(i)
            
        return c


def is_max_heap(h) -> bool:
    """Returns `True` if `h` is a valid `MaxHeap`. `False` otherwise."""
    if not isinstance(h, MaxHeap):
        return False
    if h.heap:
        for item in h.heap:
            if not isinstance(item, HeapNode):
                return False
        for i, item in enumerate(h.heap):
            l = h.left_index(i)
            r = h.right_index(i)
            if r != -1 and l == -1:
                return False
            if l != -1 and item < h.heap[l]:
                return False
            if r != -1 and item < h.heap[r]:
                return False
    return True 
