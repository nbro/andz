#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Basic data structure to represent heaps.
Note that you should not instantiate objects of this class,
but instead you should just create objects of derived classes,
namely of MinHeap and MaxHeap.
"""

from ands.ds.HeapNode import *


class Heap:
    """Base class to represent heaps.
    You can inherit from this,
    for example when implementing a max heaps."""

    NIE = " needs to be overridden."

    def __init__(self):
        self.heap = []

    def heapify(self, i: int):
        """Classical heapify operation for heaps."""
        raise NotImplementedError("'heapify'" + Heap.NIE)

    def add(self, heap_node: HeapNode):
        """Adds heap_node to this heap."""
        raise NotImplementedError("'add'" + Heap.NIE)

    def search(self, heap_node: HeapNode):
        """Returns the index of heap_node, if it exists,
        otherwise None is returned."""
        raise NotImplementedError("'search'" + Heap.NIE)

    def search_by_value(self, value: object):
        """Returns the index of the node with the field value=value."""
        raise NotImplementedError("'search_by_value'" + Heap.NIE)

    def contains(self, heap_node: HeapNode):
        """Returns True if heap_node is in this heap."""
        raise NotImplementedError("'remove'" + Heap.NIE)

    def replace(self, i: int, new_heap_node: HeapNode):
        """Replaces the HeapNode object at index i with new_heap_node."""
        raise NotImplementedError("'replace'" + Heap.NIE)

    def remove(self, i: int):
        """Removes the HeapNode object at index i. """
        raise NotImplementedError("'remove'" + Heap.NIE)

    def size(self):
        """Returns the size of this heaps."""
        return len(self.heap)

    def is_empty(self):
        """Returns True if this heap is empty."""
        return self.size() == 0

    def is_not_empty(self):
        return not self.is_empty()

    def clear(self):
        """Clears all nodes from this heap.
        This mean that if you call "is_empty",
        it will return True."""
        self.heap.clear()

    def get(self):
        """Returns the list representing internally the heaps."""
        return self.heap

    @staticmethod
    def create_list_of_heap_nodes(ls: list):
        """Creates and returns a list of HeapNode objects
        with the objects in "ls". """
        list_of_heap_nodes = []
        for i, x in enumerate(ls):
            # x should be an int and should also represent its priority!
            if isinstance(x, (int, float)):
                list_of_heap_nodes.append(HeapNode(key=x, value=x, index=i))
            else:
                # x should be a tuple or a list of 2 elements
                # x[0] := element to add
                # x[1] := element's priority

                # updating the index, even if not necessary for now
                list_of_heap_nodes.append(HeapNode(key=x[1], value=x[0], index=i))

        return list_of_heap_nodes

    @staticmethod
    def is_good_index(ls: list, i: int, raise_error=True):
        """Checks if i is valid index for ls.

        By default, if i is not a good index, a IndexError is raised.
        """
        if i < 0 or i >= len(ls):
            if raise_error:
                raise IndexError("i is not a good index.")
            else:
                return False
        return True

    @staticmethod
    def swap(ls: list, i: int, j: int):
        """Swaps elements at indexes i and j,
        if they are valid indexes,
        otherwise an IndexError is raised."""
        Heap.is_good_index(ls, i)
        Heap.is_good_index(ls, j)
        ls[i], ls[j] = ls[j], ls[i]

    @staticmethod
    def get_parent_index(ls: list, i: int):
        """Returns the parent's position of the node at index i.
        If i = 0, then None is returned, because the _initialise has no parent."""
        Heap.is_good_index(ls, i)

        if i == 0:
            return None
        else:
            return (i - 1) // 2

    @staticmethod
    def get_left_child_index(ls: list, i: int):
        """Returns the left child of the node at index i, if it exists.
        Otherwise this function returns None."""
        left = i * 2 + 1

        if Heap.is_good_index(ls, left, raise_error=False):
            return left
        else:
            return None

    @staticmethod
    def get_right_child_index(ls: list, i: int):
        """Returns the right child of the node at index i, if it exists.
        Otherwise this function returns None."""
        right = i * 2 + 2

        if Heap.is_good_index(ls, right, raise_error=False):
            return right
        else:
            return None

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

        Adapted for Python 3 from: http://pymotw.com/2/heapq/"""
        if self.heap:
            from io import StringIO
            import math

            output = StringIO()
            last_row = -1

            h_space = 1.5  # float
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
            print("Nothing to show_nodes: heap is empty.")


if __name__ == "__main__":
    h = Heap()
    h.show()
