#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 15/02/2016

Updated: 14/02/2017

# Description

Mirror-class to the MinHeap class.
For more info, see the introductory doc-strings of the file [`MinHeap.py`](MinHeap.py).

# References

- [https://en.wikipedia.org/wiki/Binary_heap](https://en.wikipedia.org/wiki/Binary_heap)
- Slides by prof. A. Carzaniga
- Chapter 13 of [Introduction to Algorithms (3rd ed.)](https://mitpress.mit.edu/books/introduction-algorithms) by CLRS

"""

from ands.ds.Heap import BinaryHeap, BHNode

__all__ = ["MaxHeap", "is_max_heap"]


class MaxHeap(BinaryHeap):
    def __init__(self, ls=None):
        BinaryHeap.__init__(self, ls)

    def find_max(self) -> BHNode:
        """Returns (without removing) the greatest element in this max-heap.

        **Time complexity:** O(1)."""
        return self.heap[0] if not self.is_empty() else None

    def remove_max(self) -> BHNode:
        """Removes and returns the greatest element in this max-heap.

        **Time complexity:** O(log(n)),
        if removing the last element of a list is a constant-time operation."""
        if not self.is_empty():
            self._swap(0, self.size() - 1)
            m = self.heap.pop()
            if not self.is_empty():
                self._push_down(0)
            return m

    def delete(self, i: int) -> BHNode:
        """Deletes and returns the `BHNode` object at index `i`.

        `IndexError` is raised if `i` is not a valid index.

        Implementation based on:
        [http://www.math.clemson.edu/~warner/M865/HeapDelete.html](http://www.math.clemson.edu/~warner/M865/HeapDelete.html)

        **Time complexity:** O(log(h)),
        where `h` is the number of nodes rooted at `i`."""
        if not self._is_good_index(i):
            raise IndexError("i is not a valid index.")
        if i == self.size() - 1:
            return self.heap.pop()
        self._swap(i, self.size() - 1)
        d = self.heap.pop()
        self._push_down(i)
        return d

    def replace(self, i: int, x: object) -> BHNode:
        """Replaces element at index `i` with `x`.

        `x` can either be a key or a `BHNode` object.
        If it's a key, then a `BHNode` object
        first created to represent `x`.

        1. If `x == self.heap[i]`,
        then just replace `self.heap[i]` with `x`.

        2. Else if `x > self.heap[i]`,
        then _push_up(index).

        3. Else `x < self.heap[i]`,
        then call `self._push_down(i)`.

        Returns the previous `BHNode` object at `i`.

        **Time complexity:** O(log(n))."""
        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, BHNode):
            x = BHNode(x)
        if not self._is_good_index(i):
            raise IndexError("i is not a valid index.")

        c = self.heap[i]
        self.heap[i] = x

        if x < c:
            self._push_down(i)
        elif x > c:
            self._push_up(i)

        return c

    def _push_down(self, i: int) -> None:
        """'Max-heapify' this max-heap starting from index `i`.

        **Time complexity:** O(log(n))."""
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
        """Pushes up the node at index `i`.

        Note that this operation only happens
        if the node at index `i` is greater than its parent.

        **Time complexity:** O(log(n))."""
        c = i  # current index
        p = self._parent_index(i)

        if p != -1 and self.heap[c] > self.heap[p]:
            c = p

        if c != i:
            self._swap(c, i)
            self._push_up(c)


def is_max_heap(h: MaxHeap) -> bool:
    """Returns `True` if `h` is a valid `MaxHeap`. `False` otherwise."""
    if not isinstance(h, MaxHeap):
        return False
    if h.heap:
        for item in h.heap:
            if not isinstance(item, BHNode):
                return False
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
