#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

A binary min heap is a data structure similar to a binary tree,
where the parent nodes are smaller or equal to their children.

In addition to the previous constraint, a binary min heap is a complete binary tree,
that is, all levels of the tree, except possibly the deepest one are fully filled,
and, if the last level of the tree is not complete,
the nodes of that level are filled from left to right.

A min heap can be implemented with a classic array or list in Python.

If we have a node at index i, then

- its left child can be found at index i*2 + 1
- its right child is found at i*2 + 2,
- its parent can be found at index floor((i - 1) / 2),
where floor(x) truncates x to the smallest integer.

Note that these indexes are for 0-index based lists (or arrays).
"""

from Heap import *


class MinHeap(Heap):

    def __init__(self, ls=[]):
        Heap.__init__(self)
        self.heap = self.create_list_of_heap_nodes(ls)
        self.build_min_heap()

    def build_min_heap(self):
        """Creates a min heap using the list passed to the constructor.

        Note that in a heap A all nodes from A[n/2 + 1] to A[n] are leaf nodes.

        Time complexity: O(n)
        """
        for index in range(len(self.heap) // 2, -1, -1):
            self.heapify(index)
        return self.heap

    def heapify(self, i: int):
        """Min-heapify this mean heap starting from index i.

        Time complexity: O(log n)
        """
        _min = i
        left = Heap.get_left_child_index(self.heap, i)
        right = Heap.get_right_child_index(self.heap, i)

        if left and self.heap[left] < self.heap[_min]:
            _min = left

        if right and self.heap[right] < self.heap[_min]:
            _min = right

        # One of the children of ls[i] was smaller than ls[i],
        # and we need to swap ls[i] with its smallest child ls[m].
        if _min != i:
            self.swap(_min, i)
            self.heapify(_min)

        return _min

    def add(self, heap_node: HeapNode):
        """Adds a heap_node to this heap.

        Time complexity: O(log n)"""

        # Sets the current index of heap_node.
        # This index could change by a "push up" operation.
        heap_node.index = self.size()
        self.heap.append(heap_node)

        if self.size() > 1:
            self.push_up(self.size() - 1)

    def find_min(self):
        """Returns (without removing) the smallest element in the heap.

        Time complexity: O(1)
        """
        if not self.is_empty():
            return self.heap[0]

    def remove_min(self):
        """Removes and returns the smallest element in this heap.

        Time complexity: O(log n),
        unless the list's pop operation is linear
        also when popping the last element,
        which would make this algorithm to have a time complexity O(n).
        """
        if self.is_not_empty():

            self.swap(0, self.size() - 1)

            min_element = self.heap.pop()

            if self.is_not_empty():
                self.push_down(0)

            return min_element

    def push_down(self, i: int):
        """Calls self.heapify(i)."""
        self.heapify(i)

    def push_up(self, i):
        """Pushes up the heap the node at index i.

        Note that this operation only happens
        if the node at index i is smaller than its parent.

        This function is simpler than push_down or heapify,
        because in this case we just need to compare
        the current node's index with its parent's index.

        Time complexity: O(log n)"""
        current_index = i
        p = MinHeap.get_parent_index(self.heap, i)

        # We need specifically to check if p is not None,
        # because it could be 0,
        # and the following if statement would not be executed (wrongly).
        if p is not None and self.heap[current_index] < self.heap[p]:
            current_index = p

        if current_index != i:
            self.swap(current_index, i)
            self.push_up(current_index)

    def search(self, heap_node: HeapNode):
        """Searches for heap_node in this heap,
        and if present, returns its index, otherwise returns -1.

        Time complexity: O(n).

        This complexity could be improved to O(1),
        because I am keeping track of the index of each HeapNode,
        (in the index field of each HeapNode),
        but this technique would not work
        in case the heap_node is not in the heap."""
        for i, node in enumerate(self.heap):
            if node == heap_node:
                return i
        return -1

    def contains(self, heap_node: HeapNode):
        """Returns True, if heap_node is in the heaps.

        Time complexity: O(n)"""
        if self.search(heap_node) != -1:
            return True
        return False

    def search_by_value(self, value: object):
        """Returns the index of the HeapNode with value=value.
        -1 is returned if no such a HeapNode exists.

        Time complexity: O(n)"""
        for i, node in enumerate(self.heap):
            if node.value == value:
                return i
        return -1

    def _merge_aux(self):
        """Updates the indices of all HeapNode objects."""
        for i, heap_node in enumerate(self.heap):
            heap_node.index = i

    def merge(self, other_heap: Heap):
        """Merges this heap with other_heap."""
        self.heap += other_heap.get()
        self._merge_aux()
        return self.build_min_heap()

    def swap(self, i: int, j: int):
        """Swaps HeapNode objects at indexes i and j,
        and updates their new index field's value.

        Time complexity: O(1)"""
        self.is_good_index(self.heap, i)
        self.is_good_index(self.heap, j)

        # Updates the index field of each HeapNode.
        # This is useful for example when search for a Node's position
        # which can then be done therefore in constant time.
        self.heap[i].index = j
        self.heap[j].index = i

        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def replace(self, i: int, new_heap_node: HeapNode):
        """Replaces element at index i with new_heap_node.

        1. If new_heap_node == self.heap[i],
        then just replace self.heap[i] with new_heap_node.

        2. Else if new_heap_node less than self.heap[i],
        then push_up(index).

        3. Else new_heap_node > self.heaps[index],
        then self.heapify(index)

        Time complexity: O(log n)"""
        self.is_good_index(self.heap, i)

        current_node = self.heap[i]
        new_heap_node.index = current_node.index

        self.heap[i] = new_heap_node

        if new_heap_node > current_node:
            self.push_down(i)

        elif new_heap_node < current_node:
            self.push_up(i)

        return current_node


if __name__ == "__main__":
    from random import randrange

    a = [randrange(0, 100) for x in range(10)]
    # a = [70, 96, 29, 77, 77, 53, 19, 70, 92, 14]
    print(a)
    h = MinHeap(a)
    h.show()

    def show_indexes():
        print()
        for hn in h.get():
            print("HeapNode:", hn, ", Index:", hn.index)

    show_indexes()
    print("\nRemoving the minimum...\n")
    h.remove_min()
    h.show()
    show_indexes()
