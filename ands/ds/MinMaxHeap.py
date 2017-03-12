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

from ands.ds.Heap import BinaryHeap, BHNode


class MinMaxHeap(BinaryHeap):
    def __init__(self, ls=None):
        BinaryHeap.__init__(self, ls)

    def find_max(self) -> BHNode:
        """Returns the `BHNode` object representing the maximum element.

        **Time complexity:** O(1)."""
        if not self.is_empty():
            return self.heap[self._find_max_index()]

    def find_min(self) -> BHNode:
        """Returns the `BHNode` object representing the minimum element.

        **Time complexity:** O(1)."""
        if not self.is_empty():
            return self.heap[0]

    def remove_max(self) -> BHNode:
        """Deletes and returns the `BHNode` object representing the maximum element.

        **Time complexity:** O(log(n))."""
        if not self.is_empty():
            return self.delete(self._find_max_index())

    def remove_min(self) -> BHNode:
        """Deletes and returns the `BHNode` object representing the minimum element.

        **Time complexity:** O(log(n))."""
        if not self.is_empty():
            return self.delete(0)

    def delete(self, i: int) -> BHNode:
        """Deletes and returns the `BHNode` object at index `i`.

        `IndexError` is raised if `i` is not a valid index.

        **Time complexity:** O(log(n))."""
        if not self._is_good_index(i):
            raise IndexError("i is not a valid index.")
        if i == self.size() - 1:
            return self.heap.pop()
        self._swap(i, self.size() - 1)
        d = self.heap.pop()
        self._push_up(i)
        self._push_down(i)
        return d

    def replace(self, i: int, x: object) -> BHNode:
        """Replace node at index `i` with `x`.

        `x` can either be a key for a BHNode` object,
        which is created automatically by this function,
        and `x` becomes the key and value of that same `BHNode` object,
        or it can be (directly) a `BHNode` object.

        If `x` is NOT a `BHNode`, it should be comparable
        with the other keys in the other `BHNode` objects.
        If this is not true, the behaviour of this function is undefined.

        If `x` is a `BHNode`,
        it's the responsibility of the client of this function
        to make sure it's a "valid" `BHNode` object,
        i.e. it's comparable to the other `BHNode` objects in this heap.

        **Time complexity:** O(log(n))."""
        if not self._is_good_index(i):
            raise IndexError("i is not a valid index.")
        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, BHNode):
            x = BHNode(x)
        d = self.heap[i]
        self.heap[i] = x
        self._push_up(i)
        self._push_down(i)
        return d

    def _push_down(self, i: int) -> None:
        """Also called `bubble-down` or `shift-down`."""
        if self._is_on_even_level(i):
            self._push_down_min(i)
        else:
            self._push_down_max(i)

    def _push_down_min(self, i: int) -> None:
        """Helper method for `self._push_down`."""
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
        """Helper method for `self._push_down`."""
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
        """Also called `bubble-up` or `shift-up`."""
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
        """Returns the index of the maximum element in this min-max heap.

        **Time complexity:** O(1)."""
        if self.is_empty():
            return -1
        elif self.size() == 1:
            return 0
        elif self.size() == 2:
            return 1
        else:
            return 1 if self.heap[1] > self.heap[2] else 2

    def _index_of_min(self, i: int) -> int:
        """Returns the index of the smallest element
        among the children and grandchildren of the node at index `i`.

        **Time complexity:** O(1)."""
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

        **Time complexity:** O(1)."""
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


def is_min_max_heap(h: MinMaxHeap) -> bool:
    """Returns `True` if `h` is a valid `MinMaxHeap` object. `False` otherwise.

    Min-max heap property:
    each node at an EVEN level in the tree is LESS THAN all of its descendants
    while each node at an ODD level in the tree is GREATER THAN all of its descendants."""
    if not isinstance(h, MinMaxHeap):
        return False

    if h.heap:
        for item in h.heap:
            if not isinstance(item, BHNode):
                return False

        if h.size() == 1:
            return True

        if h.size() == 2:
            return max(h.heap) == h.heap[1] and min(h.heap) == h.heap[0]

        if h.size() >= 3:
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
