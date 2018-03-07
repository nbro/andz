#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 15/02/2016

Updated: 29/09/2017

# Description

Implementation of a max-heap.
See doc-strings of the module MinHeap.py.

# References

- https://en.wikipedia.org/wiki/Binary_heap
- Slides by prof. A. Carzaniga
- Chapter 13 of Introduction to Algorithms (3rd ed.) by CLRS
- http://www.math.clemson.edu/~warner/M865/HeapDelete.html
"""

from ands.ds.BinaryHeap import BinaryHeap

__all__ = ["MaxHeap", "is_max_heap"]


class MaxHeap(BinaryHeap):
    """Sub-class of BinaryHeap, and thus provides the same public interface,
    but in addition provides two more operations:

    - find_max
    - remove_max"""

    def __init__(self, ls=None):
        BinaryHeap.__init__(self, ls)

    def find_max(self) -> object:
        """Returns the greatest element in this MaxHeap.

        Time complexity: O(1)."""
        return self.heap[0] if not self.is_empty() else None

    def remove_max(self) -> object:
        """Removes and returns the greatest element in this MaxHeap.

        Time complexity: O(log(n))."""
        assert is_max_heap(self)
        if not self.is_empty():
            self._swap(0, self.size - 1)
            m = self.heap.pop()
            if not self.is_empty():
                self._push_down(0)
            assert is_max_heap(self)
            return m

    def _push_down(self, i: int) -> None:
        """Max-heapifies this MaxHeap starting from index i.

        This operation is also called "bubble-down" or "shift-down".

        Time complexity: O(log(n))."""
        m = i
        l = self._left_index(i)
        r = self._right_index(i)

        if l != -1 and self.heap[l] > self.heap[m]:
            m = l
        if r != -1 and self.heap[r] > self.heap[m]:
            m = r

        if m != i:
            self._swap(m, i)
            self._push_down(m)

    def _push_up(self, i: int) -> None:
        """Pushes up the node at index i from this MaxHeap.

        Note: this operation only happens if the node at index i is greater than
        its parent.

        This operation is also called "bubble-up" or "shift-up".

        Time complexity: O(log(n))."""
        c = i  # Current index.
        p = self._parent_index(i)

        if p != -1 and self.heap[c] > self.heap[p]:
            c = p

        if c != i:
            self._swap(c, i)
            self._push_up(c)


def is_max_heap(h: MaxHeap) -> bool:
    """Returns true if h is a valid MaxHeap, false otherwise."""
    if not isinstance(h, MaxHeap):
        return False
    if h.heap:
        for i, item in enumerate(h.heap):
            l = h._left_index(i)
            r = h._right_index(i)
            if r != -1 and l == -1:
                return False
            if l != -1 and item < h.heap[l]:
                return False
            if r != -1 and item < h.heap[r]:
                return False
    return True
