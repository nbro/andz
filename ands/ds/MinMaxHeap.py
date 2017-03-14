#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 18/02/2016

Updated: 12/03/2017

# Description

Min-Max Heap is a heap that supports find-min and find-max operations in constant time.
Moreover, both remove-min and remove-max are supported in logarithmic time.
It's therefore an useful data structure to implement (or represent) double-ended priority queues.

The min-max heap ordering is the following:
> values stored at nodes on even (or min) levels
are smaller than or equal to values stored at their descendants,
whereas values stored at nodes on odd (or max) levels
are greater than or equal to values stored at their descendants.

Even levels are 0, 2, 4, 6, etc,
whereas odd levels are 1, 3, 5, 7, etc.

# TODO

- find-kth, i.e. find the kth smallest element in the structure, in O(1) time
- delete-kth, i.e. delete the kth smallest element, in O(log n) time

# References

- [Min-Max Heaps and Generalized Priority Queues]
(http://www.akira.ruc.dk/~keld/teaching/algoritmedesign_f03/Artikler/02/Atkinson86.pdf),
original paper describing and introducing the min-max heap data structure,
by M. D. Atkinson, J.R. Sack, N. Santoro and T. Strothotte.

- [http://www.diku.dk/forskning/performance-engineering/Jesper/heaplab/heapsurvey_html/node11.html]
(http://www.diku.dk/forskning/performance-engineering/Jesper/heaplab/heapsurvey_html/node11.html)

- [http://www.math.clemson.edu/~warner/M865/HeapDelete.html](http://www.math.clemson.edu/~warner/M865/HeapDelete.html
(http://www.math.clemson.edu/~warner/M865/HeapDelete.html](http://www.math.clemson.edu/~warner/M865/HeapDelete.html)
"""

import math

from ands.ds.BinaryHeap import BinaryHeap

__all__ = ["MinMaxHeap", "is_min_max_heap"]


class MinMaxHeap(BinaryHeap):
    """Sub-class of BinaryHeap, and thus provides the same public interface,
    but in addition provides four more operations:

    - find_max
    - find_min
    - remove_max
    - remove_min"""

    def __init__(self, ls=None):
        BinaryHeap.__init__(self, ls)

    def find_max(self) -> object:
        """Returns the greatest element in this MinMaxHeap.

        Time complexity: O(1)."""
        if not self.is_empty():
            return self.heap[self._find_max_index()]

    def find_min(self) -> object:
        """Returns the smallest element in this MinMaxHeap.

        Time complexity: O(1)."""
        if not self.is_empty():
            return self.heap[0]

    def remove_max(self) -> object:
        """Removes and returns the greatest element in this MinMaxHeap.

        Time complexity: O(log(n))."""
        assert is_min_max_heap(self)

        if not self.is_empty():
            i = self._find_max_index()

            if i == self.size - 1:
                m = self.heap.pop()
                assert is_min_max_heap(self)
                return m

            self._swap(i, self.size - 1)
            m = self.heap.pop()
            self._push_up(i)
            self._push_down(i)
            assert is_min_max_heap(self)
            return m

    def remove_min(self) -> object:
        """Removes and returns the smallest element in this MinMaxHeap.

        Time complexity: O(log(n))."""
        if not self.is_empty():
            if self.size == 1:
                m = self.heap.pop()
                assert is_min_max_heap(self)
                return m

            self._swap(0, self.size - 1)
            m = self.heap.pop()
            self._push_up(0)
            self._push_down(0)
            assert is_min_max_heap(self)
            return m

    def delete(self, x: object) -> None:
        """Removes the first found `x` from this MinMaxHeap.

        If `x` is not in this MinMaxHeap, LookupError is raised.

        This function overrides the inherited one only for the purpose of asserting
        that before and after this operation self is still a MinHeap.

        Time complexity: O(n)."""
        assert is_min_max_heap(self)
        super(MinMaxHeap, self).delete(x)
        assert is_min_max_heap(self)

    def _push_down(self, i: int) -> None:
        """This operation is also called "bubble-down" or "shift-down"."""
        if self._is_on_even_level(i):
            self._push_down_min(i)
        else:
            self._push_down_max(i)

    def _push_down_min(self, i: int) -> None:
        """Helper method for self._push_down."""
        if self._has_children(i):
            m = self._index_of_min(i)

            if self._is_grandchild(m, i):
                if self.heap[m] < self.heap[i]:
                    self._swap(i, m)

                    mp = self._parent_index(m)
                    if mp != -1 and self.heap[m] > self.heap[mp]:
                        self._swap(m, mp)
                    self._push_down_min(m)

            else:  # self.heap[m] is a child of self.heap[i]
                if self.heap[m] < self.heap[i]:
                    self._swap(i, m)

    def _push_down_max(self, i: int) -> None:
        """Helper method for self._push_down."""
        if self._has_children(i):
            m = self._index_of_max(i)

            if self._is_grandchild(m, i):
                if self.heap[m] > self.heap[i]:
                    self._swap(i, m)

                    mp = self._parent_index(m)
                    if mp != -1 and self.heap[m] < self.heap[mp]:
                        self._swap(m, mp)
                    self._push_down_max(m)

            else:  # self.heap[m] is a child of self.heap[i]
                if self.heap[m] > self.heap[i]:
                    self._swap(i, m)

    def _push_up(self, i: int) -> None:
        """This operation is also called "bubble-up" or "shift-up"."""
        p = self._parent_index(i)

        # Let x be the element at index i.
        # If x has a parent at position p, we call it y.
        if self._is_on_even_level(i):
            if p != -1 and self.heap[i] > self.heap[p]:
                # If x is greater than y, swap x with y.
                # Now, x is at index p, and y at index i.
                # _push_up_max from the new index of x, i.e. p.
                self._swap(i, p)
                self._push_up_max(p)
            else:
                # x does not have a parent OR x <= y.
                self._push_up_min(i)
        else:
            # Odd or max level.
            if p != -1 and self.heap[i] < self.heap[p]:
                self._swap(i, p)
                self._push_up_min(p)
            else:
                self._push_up_max(i)

    def _push_up_min(self, i: int) -> None:
        """Helper method for `self._push_up`."""
        g = self._grandparent_index(i)
        # Let x be the element at index i.
        # If x has a grandparent at position g,
        # we call it z.

        # If the z exists and x is smaller than z,
        # swap x and z. Now, x is at index g and z at index i.
        if g != -1 and self.heap[i] < self.heap[g]:
            self._swap(i, g)
            self._push_up_min(g)

    def _push_up_max(self, i: int) -> None:
        """Helper method for `self._push_up`."""
        g = self._grandparent_index(i)
        if g != -1 and self.heap[i] > self.heap[g]:
            self._swap(i, g)
            self._push_up_max(g)

    def _find_max_index(self) -> int:
        """Returns the index of the maximum element in this MinMaxHeap.

        Time complexity: O(1)."""
        if self.is_empty():
            return -1
        elif self.size == 1:
            return 0
        elif self.size == 2:
            return 1
        else:
            return 1 if self.heap[1] > self.heap[2] else 2

    def _index_of_min(self, i: int) -> int:
        """Returns the index of the smallest element
        among the children and grandchildren of the node at index `i`.

        Time complexity: O(1)."""
        m = l = self._left_index(i)
        r = self._right_index(i)

        if r != -1 and self.heap[r] < self.heap[m]:
            m = r

        if l != -1:
            gll = self._left_index(l)
            if gll != -1 and self.heap[gll] < self.heap[m]:
                m = gll
            glr = self._right_index(l)
            if glr != -1 and self.heap[glr] < self.heap[m]:
                m = glr

        if r != -1:
            grl = self._left_index(r)
            if grl != -1 and self.heap[grl] < self.heap[m]:
                m = grl
            grr = self._right_index(r)
            if grr != -1 and self.heap[grr] < self.heap[m]:
                m = grr

        return m

    def _index_of_max(self, i: int) -> int:
        """Returns the index of the largest element
        among the children and grandchildren of the node at index `i`.

        Time complexity: O(1)."""
        m = l = self._left_index(i)
        r = self._right_index(i)

        if r != -1 and self.heap[r] > self.heap[m]:
            m = r

        if l != -1:
            gll = self._left_index(l)
            if gll != -1 and self.heap[gll] > self.heap[m]:
                m = gll
            glr = self._right_index(l)
            if glr != -1 and self.heap[glr] > self.heap[m]:
                m = glr

        if r != -1:
            grl = self._left_index(r)
            if grl != -1 and self.heap[grl] > self.heap[m]:
                m = grl
            grr = self._right_index(r)
            if grr != -1 and self.heap[grr] > self.heap[m]:
                m = grr

        return m

    def _has_children(self, i: int) -> bool:
        """Returns true if the node at index `i` has at least one child, false otherwise.

        Time complexity: O(1)."""
        assert self._is_good_index(i)
        return self._left_index(i) != -1 or self._right_index(i) != -1

    def _is_child(self, c: int, i: int) -> bool:
        """Returns true if `c` is a child of `i`, false otherwise.

        Time complexity: O(1)."""
        assert self._is_good_index(c) and self._is_good_index(i)
        return c == self._left_index(i) or c == self._right_index(i)

    def _is_grandchild(self, g: int, i: int) -> bool:
        """Returns true if `g` is a grandchild of `i`, false otherwise.

        Time complexity: O(1)."""
        l = self._left_index(i)
        if l == -1:
            assert self._right_index(i) == -1
            assert self._is_good_index(g)
            return False
        r = self._right_index(i)
        if r == -1:
            return self._is_child(g, l)
        else:
            return self._is_child(g, l) or self._is_child(g, r)

    def _grandparent_index(self, i: int) -> int:
        """Returns the grandparent's index of the node at index `i`.

        -1 is returned either if `i` has not a parent or
        the parent of `i` does not have a parent.

        Time complexity: O(1)."""
        p = self._parent_index(i)
        return -1 if p == -1 else self._parent_index(p)

    def _is_on_even_level(self, i: int) -> bool:
        """Returns true if node at index `i` is on a even-level,
        i.e., if `i` is on a level multiple of 2 (0, 2, 4, 6,...).

        Time complexity: O(int(log(i + 1) % 2) == 0)."""
        assert self._is_good_index(i)
        return int(math.log2(i + 1) % 2) == 0

    def _is_on_odd_level(self, i: int) -> bool:
        """Returns true when self._is_on_even_level(i) returns false, and vice-versa."""
        return not self._is_on_even_level(i)


def is_min_max_heap(h: MinMaxHeap) -> bool:
    """Returns true if `h` is a valid `MinMaxHeap` object, false otherwise.

    Min-max heap property:
    each node at an EVEN level in the tree is LESS THAN all of its descendants
    while each node at an ODD level in the tree is GREATER THAN all of its descendants."""
    if not isinstance(h, MinMaxHeap):
        return False

    if h.heap:

        if h.size == 1:
            return True
        if h.size == 2:
            return max(h.heap) == h.heap[1] and min(h.heap) == h.heap[0]
        if h.size >= 3:
            if h.heap[0] != min(h.heap) or (h.heap[1] != max(h.heap) and h.heap[2] != max(h.heap)):
                return False

        # i is the index of the current node
        for i, item in reversed(list(enumerate(h.heap))):
            p = h._parent_index(i)
            if p != -1:
                if h._is_on_even_level(i):
                    if h.heap[p] < item:
                        return False
                else:
                    if h.heap[p] > item:
                        return False

            g = h._grandparent_index(i)
            if g != -1:
                if h._is_on_even_level(i):
                    if h.heap[g] > item:
                        return False

                else:
                    if h.heap[g] < item:
                        return False

    return True
