#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 01/07/2015

Updated: 29/09/2017

# Description

A binary min-heap is a data structure similar to a binary tree, where the parent
nodes are smaller or equal to their children. In addition to the previous
constraint, a binary min-heap is a complete binary tree, that is, all levels of
the tree, except possibly the deepest one are fully filled, and, if the last
level of the tree is not complete, the nodes of that level are filled from left
to right.

A min-heap can be implemented with a classic array (or list, in Python).

If we have a node at index i, then

- its left child can be found at index i*2 + 1

- its right child is found at i*2 + 2,

- its parent can be found at index floor((i - 1) / 2), where floor(x) truncates
x to the smallest integer.

Note: these indexes are for 0-index based lists (or arrays).

# References

- https://en.wikipedia.org/wiki/Binary_heap
- Slides by prof. A. Carzaniga
- Chapter 13 of Introduction to Algorithms (3rd ed.) by CLRS
- http://www.math.clemson.edu/~warner/M865/HeapDelete.html
"""

from andz.ds.BinaryHeap import BinaryHeap

__all__ = ["MinHeap", "is_min_heap"]


class MinHeap(BinaryHeap):
    """Sub-class of BinaryHeap, and thus provides the same public interface,
    but in addition provides two more operations:

    - find_min
    - remove_min"""

    def __init__(self, ls=None):
        BinaryHeap.__init__(self, ls)

    def find_min(self):
        """Returns the smallest element in this MinHeap.

        Time complexity: O(1)."""
        return self.heap[0] if not self.is_empty() else None

    def remove_min(self):
        """Removes and returns the smallest element in this MinHeap.

        Time complexity: O(log(n))."""
        assert is_min_heap(self)
        if not self.is_empty():
            self._swap(0, self.size - 1)
            m = self.heap.pop()
            if not self.is_empty():
                self._push_down(0)
            assert is_min_heap(self)
            return m

    def _push_down(self, i: int) -> None:
        """Min-heapifies this MinHeap starting from index i.

        This operation is also called "bubble-down" or "shift-down".

        Time complexity: O(log(n))."""
        m = i  # Index of node with the smallest value among i and its children.
        l = self._left_index(i)
        r = self._right_index(i)

        if l != -1 and self.heap[l] < self.heap[m]:
            m = l
        if r != -1 and self.heap[r] < self.heap[m]:
            m = r

        if m != i:
            self._swap(m, i)
            self._push_down(m)

    def _push_up(self, i: int) -> None:
        """Pushes up the node at index i from this MinHeap.

        Note: this operation only happens if the node at index i is smaller than
        its parent.

        This operation is also called "bubble-up" or "shift-up".

        Time complexity: O(log(n))."""
        c = i  # Current index.
        p = self._parent_index(i)

        if p != -1 and self.heap[c] < self.heap[p]:
            c = p

        if c != i:
            self._swap(c, i)
            self._push_up(c)


# pylint: disable=protected-access
def is_min_heap(h: MinHeap) -> bool:
    """Returns true if h is a valid MinHeap, false otherwise."""
    if not isinstance(h, MinHeap):
        return False
    if h.heap:
        for i, item in enumerate(h.heap):
            l = h._left_index(i)
            r = h._right_index(i)
            if r != -1 and l == -1:
                return False
            if l != -1 and item > h.heap[l]:
                return False
            if r != -1 and item > h.heap[r]:
                return False
    return True
