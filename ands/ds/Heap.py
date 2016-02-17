#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 17/02/16

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

    def __init__(self, ls=[]):
        self.heap = Heap._create_list_of_heap_nodes(ls)
        self._build_heap()

    # ABSTRACT NOT-IMPLEMENTED METHODS

    def push_down(self, i: int):
        """Classical so-called heapify operation for heaps.
        If this is a min-heap, then this is a min-heapify operation,
        if this is a max-heap, then this is a max-heapify operation."""
        raise NotImplementedError()

    def push_up(self, i: int):
        """Classical reverse-heapify operation for heaps."""
        raise NotImplementedError()

    def _build_heap(self):
        """Builds the heap data structure from `self.heap`.
        If this is a min-heap, then this is a "build-min-heap" operation,
        if this is a max-heap, then this is a "build-max-heap" operation."""
        raise NotImplementedError()

    def add(self, x):
        """Adds `x to this heap.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError()

    def search(self, x) -> int:
        """Searches for `x` in this heap,
        and if present, returns its index, otherwise returns -1.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError()

    def search_by_value(self, val) -> int:
        """Returns the index of the node with the field value=`val`."""
        raise NotImplementedError()

    def contains(self, x) -> bool:
        """Returns True, if `x` is in the heap. `False` otherwise.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError()

    def merge(self, other):
        """Merges this heap with the `other` heap."""
        raise NotImplementedError()

    def replace(self, i: int, x):
        """Replaces the `HeapNode` object at index `i` with `x`.

        `x` can either be a key or a `HeapNode` object.
        If it's a key, an `HeapNode` is first created,
        whose key and value are equal to `x`."""
        raise NotImplementedError()

    # BASE-IMPLEMENTED METHODS    

    def size(self):
        """Returns the size of this heaps.

        **Time Complexity:** O(1)."""
        return len(self.heap)

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

    def swap(self, i: int, j: int):
        """Swaps elements at indexes `i` and `j`,
        if they are valid indexes,
        otherwise an `IndexError` is raised.
        
        **Time Complexity:** O(1)."""
        if self.is_good_index(i) and self.is_good_index(j):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        else:
            raise IndexError("i or j are not valid indexes.")

    def is_good_index(self, i: int):
        """Returns `True` if `i` is valid index for `self.heap`,
        `False` otherwise.

        **Time Complexity:** O(1)."""
        if not isinstance(i, int):
            raise TypeError("indexes can only be int.")
        return False if (i < 0 or i >= self.size()) else True        

    def parent_index(self, i: int):
        """Returns the parent's index of the node at index `i`.
        If `i = 0`, then `None` is returned, because the root has no parent.
        If `i` is not a valid index for `self.heap`, an `IndexError` is raised.

        **Time Complexity:** O(1)."""
        if not self.is_good_index(i):
            raise IndexError("i is not a valid index.")
        return None if i == 0 else (i - 1) // 2

    def grandparent_index(self, i: int):
        p = self.parent_index(i)
        return None if not p else self.parent_index(p)

    def left_index(self, i: int):
        """Returns the left child's index of the node at index `i`, if it exists.
        Otherwise this function returns `None`.
        If `i` is not a valid index for `ls`, an `IndexError` is raised.

        **Time Complexity:** O(1)."""
        if not self.is_good_index(i):
            raise IndexError("i is not a valid index.")        
        left = i * 2 + 1
        return left if self.is_good_index(left) else None

    def right_index(self, i: int):
        """Returns the right child of the node at index `i`, if it exists.
        Otherwise this function returns `None`.
        If `i` is not a valid index for `self.heap`, an `IndexError` is raised.

        **Time Complexity:** O(1)."""
        if not self.is_good_index(i):
            raise IndexError("i is not a valid index.")        
        right = i * 2 + 2
        return right if self.is_good_index(right) else None

    def has_children(self, i: int):
        """Returns `True` if the node at index `i`
        has at least one child, `False` otherwise.

        **Time Complexity:** O(1)."""
        if not self.is_good_index(i):
            raise IndexError("i is not a valid index.") 
        return self.left_index(i) or self.right_index(i)

    def is_child(self, c: int, i: int):
        """Returns `True` if `c` is a child of `i`. `False` otherwise.

        **Time Complexity:** O(1)."""
        if not self.is_good_index(c) or not self.is_good_index(i):
            raise IndexError("i or c are not valid indexes.")
        return c == self.left_index(i) or c == self.right_index(i)

    def is_grandchild(self, g: int, i: int):
        """Returns `True` if `g` is a grandchild of `i`. `False` otherwise.

        **Time Complexity:** O(1)."""
        l = self.left_index(i)
        if not l:
            assert not self.right_index(i)
            if not self.is_good_index(g):
                raise IndexError("g is not a valid index.")
            return False
        r = self.right_index(i)
        if not r:
            return self.is_child(g, l)
        else:
            return self.is_child(g, l) or self.is_child(g, r)

    def is_parent(self, p: int, i: int):
        """Returns `True` if `p` is the index of the parent
        of the node at `i`, `False` otherwise.

        **Time Complexity:** O(1)."""
        if not self.is_good_index(p):
            raise IndexError("p is not a valid index.")        
        return self.parent_index(i) == p

    def is_grandparent(self, g: int, i: int):
        """Returns `True` if `g` is the index of the grandparent
        of the node at `i`, `False` otherwise.

        **Time Complexity:** O(1)."""
        if not self.is_good_index(g):
            raise IndexError("g is not a valid index.")         
        p = self.parent_index(i)
        return False if not p else self.is_parent(g, p)
            
    def is_on_even_level(self, i: int):
        """Returns `True` if node at index `i` is on a even-level,
        i.e., if `i` is on a level multiple of 2 (0, 2, 4, 6,...).
        If `i` is not a valid index, an `IndexError` is raised.

        **Time Complexity:** O(log<sub>2</sub> n)."""
        if not self.is_good_index(i):
            raise IndexError("i is not a valid index.")
        if i == 0:
            return True
        c = 0
        while i != 0:
            c += 1
            i = self.parent_index(i)
        return c % 2 == 0

    def is_on_odd_level(self, i: int):
        """Returns `True` (`False`) if `self.is_on_even_level(i)` returns `False` (`True`).

        **Time Complexity:** O(log<sub>2</sub> n)."""
        return not self.is_on_even_level(i)

    # PRINT FUNCTIONS

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return HeapPrinter(self.heap).show()    

    def show(self):
        """Pretty-prints this heap."""
        print(repr(self))

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


class HeapPrinter:

    def __init__(self, heap):
        self.heap = heap

    def show(self, total_width=36, fill=" "):
        """Adapted for Python 3 from:
        [http://pymotw.com/2/heapq/](http://pymotw.com/2/heapq/).

        To increase/decrease the horizontal space between nodes,
        just increase/decrease the float number h_space.

        To increase/decrease the vertical space between nodes,
        just increase/decrease the integer number v_space.
        Note that v_space must be an integer.

        To change the length of the line under the heap,
        you can simply change the line_length variable."""
        if not self.heap:
            return print("Nothing to print: heap is empty.")
                
        import io
        import math
        
        output = io.StringIO()
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

        s = output.getvalue() + "\n"

        line_length = total_width + 15  # int
        s += ('-' * line_length + "\n")
        return s
