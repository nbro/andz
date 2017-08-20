#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 01/07/2015

Updated: 20/08/2017

# Description

Contains the abstract class BinaryHeap.

# References

- Slides by prof. A. Carzaniga
- Chapter 13 of Introduction to Algorithms (3rd ed.)
- http://www.math.clemson.edu/~warner/M865/HeapDelete.html
- https://docs.python.org/3/library/exceptions.html#NotImplementedError
- http://effbot.org/pyfaq/how-do-i-check-if-an-object-is-an-instance-of-a-given-class-or-of-a-subclass-of-it.htm
- https://en.wikipedia.org/wiki/Heap_(data_structure)
- https://arxiv.org/pdf/1012.0956.pdf
- http://pymotw.com/2/heapq/
- http://stackoverflow.com/a/29197855/3924118
"""

import io
import math
from abc import ABCMeta, abstractmethod

__all__ = ["BinaryHeap", "build_pretty_binary_heap"]


class BinaryHeap(metaclass=ABCMeta):
    """Abstract class to represent binary heaps.

    This binary heap allows duplicates.

    It's the responsibility of the client to ensure that inserted elements are comparable among them.

    Their order also defines their priority.

    Public interface:

    - size
    - is_empty
    - clear
    - add
    - contains
    - delete
    - merge

    MinHeap, MaxHeap and MinMaxHeap all derive from this class."""

    def __init__(self, ls=None):
        self.heap = [] if not isinstance(ls, list) else ls
        self._build_heap()

    @property
    def size(self) -> int:
        """Returns the number of elements in this heap.

        Time complexity: O(1)."""
        return len(self.heap)

    def is_empty(self) -> bool:
        """Returns true if this heap is empty, false otherwise.

        Time complexity: O(1)."""
        return self.size == 0

    def clear(self) -> None:
        """Removes all elements from this heap.

        Time complexity: O(1)."""
        self.heap.clear()

    def add(self, x: object) -> None:
        """Adds object `x` to this heap.

        This algorithm proceeds by placing `x` at an available leaf of this heap,
        then bubbles up from there, in order to maintain the heap property.

        Time complexity: O(log n)."""
        if x is None:
            raise ValueError("x cannot be None")
        self.heap.append(x)
        if self.size > 1:
            self._push_up(self.size - 1)

    def contains(self, x: object) -> bool:
        """Returns true if `x` is in this heap, false otherwise.

        Time complexity: O(n)."""
        if x is None:
            raise ValueError("x cannot be None")
        return self._index(x) != -1

    def delete(self, x: object) -> None:
        """Removes the first found `x` from this heap.

        If `x` is not in this heap, LookupError is raised.

        Time complexity: O(n)."""
        if x is None:
            raise ValueError("x cannot be None")

        i = self._index(x)
        if i == -1:
            raise LookupError("x not found")

        # self has at least one element.
        if i == self.size - 1:
            self.heap.pop()
        else:
            self._swap(i, self.size - 1)
            self.heap.pop()
            self._push_down(i)
            self._push_up(i)

    def merge(self, o: "Heap") -> None:
        """Merges this heap with the `o` heap.

        Time complexity: O(n + m)."""
        self.heap += o.heap
        self._build_heap()

    @abstractmethod
    def _push_down(self, i: int) -> None:
        """Classical _heapify_ operation for heaps."""
        pass

    @abstractmethod
    def _push_up(self, i: int) -> None:
        """Classical reverse-heapify operation for heaps."""
        pass

    def _build_heap(self) -> list:
        """Builds the heap data structure using Robert Floyd's heap construction algorithm.

        Floyd's algorithm is optimal as long as complexity is expressed in terms of sets of functions
        described via the asymptotic symbols O, Θ and Ω.
        Indeed, its linear complexity Θ(n), both in the worst and best case,
        cannot be improved as each object must be examined at least once.

        Floyd's algorithm was invented in 1964 as an improvement of the construction phase
        of the classical heap-sort algorithm introduced earlier that year by Williams J.W.J.

        Time complexity: Θ(n)."""
        if self.heap:
            for index in range(len(self.heap) // 2, -1, -1):
                self._push_down(index)

    def _index(self, x: object) -> int:
        """Returns the index of `x` in this heap if `x` is in this heap, otherwise it returns -1.

        Time complexity: O(n)."""
        for i, node in enumerate(self.heap):
            if node == x:
                return i
        return -1

    def _swap(self, i: int, j: int) -> None:
        """Swaps elements at indexes `i` and `j`.

        Time complexity: O(1)."""
        assert self._is_good_index(i) and self._is_good_index(j)
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _left_index(self, i: int) -> int:
        """Returns the left child's index of the node at index `i`,
        if it exists, otherwise this function returns -1.

        Time complexity: O(1)."""
        assert self._is_good_index(i)
        left = i * 2 + 1
        return left if self._is_good_index(left) else -1

    def _right_index(self, i: int) -> int:
        """Returns the right child's index of the node at index `i`,
        if it exists, otherwise this function returns -1.

        Time complexity: O(1)."""
        assert self._is_good_index(i)
        right = i * 2 + 2
        return right if self._is_good_index(right) else -1

    def _parent_index(self, i: int) -> int:
        """Returns the parent's index of the node at index `i`.
        If `i = 0`, then -1 is returned, because the root has no parent.

        Time complexity: O(1)."""
        assert self._is_good_index(i)
        return -1 if i == 0 else (i - 1) // 2

    def _is_good_index(self, i: int) -> bool:
        """Returns true if `i` is in the bounds of elf.heap, false otherwise.

        Time complexity: O(1)."""
        return False if (i < 0 or i >= self.size) else True

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return build_pretty_binary_heap(self.heap)


def build_pretty_binary_heap(heap: list, total_width=36, fill=" ") -> str:
    """Returns a string (which can be printed) representing `heap` as a tree.

    To increase/decrease the horizontal space between nodes,
    just increase/decrease the float number h_space.

    To increase/decrease the vertical space between nodes,
    just increase/decrease the integer number v_space.
    Note that v_space must be an integer.

    To change the length of the line under the heap,
    you can simply change the line_length variable."""
    if not isinstance(heap, list):
        raise TypeError("heap must be an list object")
    if len(heap) == 0:
        return "Nothing to print: heap is empty."

    output = io.StringIO()
    last_row = -1
    h_space = 3.0  # float
    v_space = 2  # int

    for i, heap_node in enumerate(heap):
        if i != 0:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0

        if row != last_row:
            output.write("\n" * v_space)

        columns = 2 ** row
        column_width = int(math.floor((total_width * h_space) / columns))
        output.write(str(heap_node).center(column_width, fill))
        last_row = row

    s = output.getvalue() + "\n"
    line_length = total_width + 15  # int
    s += ('-' * line_length + "\n")
    return s
