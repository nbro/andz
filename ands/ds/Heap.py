#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 15/02/16

Base abstract class to represent heaps.
See `MinHeap` and `MaxHeap` (not yet created) if you want to instantiate heap objects.

## [NotImplementedError](https://docs.python.org/3/library/exceptions.html#NotImplementedError)

This exception is derived from `RuntimeError`.
In user defined base classes,
abstract methods should raise this exception
when they require derived classes to override the method.
"""

from ands.ds.HeapNode import HeapNode


__all__ = ["Heap"]


class Heap:

    NIE = " needs to be overridden."

    def __init__(self, ls=[]):
        self.heap = Heap._create_list_of_heap_nodes(ls)

    # ABSTRACT NOT-IMPLEMENTED METHODS

    def push_down(self, i: int):
        """Classical so-called heapify operation for heaps.
        If this is a min-heap, then this is a min-heapify operation,
        if this is a max-heap, then this is a max-heapify operation."""
        raise NotImplementedError("'push_down'" + Heap.NIE)

    def push_up(self, i: int):
        """Classical reverse-heapify operation for heaps."""
        raise NotImplementedError("'push_up'" + Heap.NIE)

    def _build_heap(self):
        """Builds the heap data structure from `self.heap`.
        If this is a min-heap, then this is a "build-min-heap" operation,
        if this is a max-heap, then this is a "build-max-heap" operation."""
        raise NotImplementedError("'_build_heap'" + Heap.NIE)

    def add(self, x):
        """Adds `x to this heap.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError("'add'" + Heap.NIE)

    def search(self, x) -> int:
        """Searches for `x` in this heap,
        and if present, returns its index, otherwise returns -1.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError("'search'" + Heap.NIE)

    def search_by_value(self, val) -> int:
        """Returns the index of the node with the field value=`val`."""
        raise NotImplementedError("'search_by_value'" + Heap.NIE)

    def contains(self, x) -> bool:
        """Returns True, if `x` is in the heap. `False` otherwise.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError("'contains'" + Heap.NIE)

    def replace(self, i: int, x):
        """Replaces the `HeapNode` object at index `i` with `x`.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError("'replace'" + Heap.NIE)

    def remove(self, i: int) -> HeapNode:
        """Removes the `HeapNode` object at index `i`. """
        raise NotImplementedError("'remove'" + Heap.NIE)

    def merge(self, other):
        """Merges this heap with the `other` heap."""
        raise NotImplementedError("'merge'" + Heap.NIE)
    
    def size(self):
        """Returns the size of this heaps.

        **Time Complexity:** O(1)."""
        return len(self.heap)

    # BASE-IMPLEMENTED METHODS

    def is_empty(self):
        """Returns `True` if this heap is empty.

        **Time Complexity:** O(1)."""
        return self.size() == 0

    def clear(self):
        """Clears all nodes from this heap.
        This mean that if you call `is_empty`,
        it will return `True`.

        **Time Complexity:** O(1)."""
        self.heap.clear()

    def get(self):
        """Returns the list representing internally the heap.

        **Time Complexity:** O(1)."""
        return self.heap

    # STATIC FUNCTIONS

    @staticmethod
    def _create_list_of_heap_nodes(ls: list):
        """Creates and returns a list of `HeapNode`
        objects with the objects in `ls`.

        **Time Complexity:** O(n)."""
        nodes = []
        for i, x in enumerate(ls):
            # x represents also its priority.
            if isinstance(x, (int, float)):
                nodes.append(HeapNode(x))
            else:
                if len(x) != 2:
                    raise ValueError("x should be a tuple or list of 2 elements.")
                # x[0] := priority
                # x[1] := value associated with x[0]
                if x[0] is None or x[1] is None:
                    raise ValueError("keys or values cannot be None.")
                nodes.append(HeapNode(key=x[0], value=x[1]))
        return nodes

    @staticmethod
    def is_good_index(ls: list, i: int, raise_error=True):
        """Checks if `i` is valid index for `ls`.

        By default, if `i` is not a good index, a `IndexError` is raised.
        If `raise_error` is set to `False`, then a `bool` value is returned.

        **Time Complexity:** O(1)."""
        if i < 0 or i >= len(ls):
            if raise_error:
                raise IndexError("i is not a good index.")
            else:
                return False
        return True

    @staticmethod
    def swap(ls: list, i: int, j: int):
        """Swaps elements at indexes `i` and `j`,
        if they are valid indexes,
        otherwise an `IndexError` is raised.
        
        **Time Complexity:** O(1)."""
        Heap.is_good_index(ls, i)
        Heap.is_good_index(ls, j)
        ls[i], ls[j] = ls[j], ls[i]

    @staticmethod
    def get_parent_index(ls: list, i: int):
        """Returns the parent's position of the node at index `i`.
        If `i = 0`, then `None` is returned, because the root has no parent.
        If `i` is not a valid index for `ls`, an `IndexError` is raised.

        **Time Complexity:** O(1)."""
        Heap.is_good_index(ls, i)
        if i == 0:
            return None
        else:
            return (i - 1) // 2

    @staticmethod
    def get_left_child_index(ls: list, i: int):
        """Returns the left child of the node at index `i`, if it exists.
        Otherwise this function returns `None`.
        If `i` is not a valid index for `ls`, an `IndexError` is raised.

        **Time Complexity:** O(1)."""
        Heap.is_good_index(ls, i)
        left = i * 2 + 1
        if Heap.is_good_index(ls, left, raise_error=False):
            return left
        else:
            return None

    @staticmethod
    def get_right_child_index(ls: list, i: int):
        """Returns the right child of the node at index `i`, if it exists.
        Otherwise this function returns `None`.
        If `i` is not a valid index for `ls`, an `IndexError` is raised.

        **Time Complexity:** O(1)."""
        Heap.is_good_index(ls, i)        
        right = i * 2 + 2
        if Heap.is_good_index(ls, right, raise_error=False):
            return right
        else:
            return None

    # PRINT FUNCTIONS

    def __str__(self):
        return str(self.heap)

    def show(self, total_width=36, fill=" "):
        """Pretty-prints this heap.

        To increase/decrease the horizontal space between nodes,
        just increase/decrease the float number h_space.

        To increase/decrease the vertical space between nodes,
        just increase/decrease the integer number v_space.
        Note that v_space must be an integer.

        To change the length of the line under the heap,
        you can simply change the line_length variable.

        Adapted for Python 3 from:
        [http://pymotw.com/2/heapq/](http://pymotw.com/2/heapq/)."""
        if self.heap:
            from io import StringIO
            import math

            output = StringIO()
            last_row = -1

            h_space = 1.4  # float
            v_space = 2    # int

            for i, heap_node in enumerate(self.heap):
                if i:
                    row = int(math.floor(math.log(i + 1, 2)))
                else:
                    row = 0
                if row != last_row:
                    output.write("\n"*v_space)

                columns = 2 ** row

                column_width = int(math.floor((total_width * h_space) / columns))
                output.write(str(heap_node).center(column_width, fill))
                last_row = row

            print(output.getvalue())

            line_length = total_width + 15  # int
            print('-' * line_length)
        else:
            print("Nothing to show: heap is empty.")
