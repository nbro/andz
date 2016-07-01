#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 22/02/16

Basic queue, which is FIFO (first-in-first-out) data structure.
"""

import sys
from ands.ds.MinHeap import MinHeap
from ands.ds.Heap import HeapNode


__all__ = ["Queue", "BFSQueue", "MinPriorityQueue"]


class Queue:

    def __init__(self, ls):
        self.q = ls

    def enqueue(self, n):
        """Adds `n` to the end of this queue."""
        self.q.append(n)

    def dequeue(self):
        """Returns the first element of this queue."""
        return self.q.pop(0)

    def is_empty(self):
        """Returns `True` if this queue is empty, `False` otherwise."""
        return self.size() == 0

    def size(self):
        """Returns the size of this stack."""
        return len(self.q)

    def __str__(self):
        return str(self.q)

    def __repr__(self):
        return self.__str__()


class BFSQueue(Queue):
    """Queue for the bfs algorihm."""

    def __init__(self):
        Queue.__init__(self, ls=[])

    def __str__(self):
        return "[" + ", ".join([u.key for u in self.q]) + "]"

    def __repr__(self):
        return self.__str__()


class MinPriorityQueue(MinHeap):

    def __init__(self, ls=[]):
        """If `ls` is provided, it should be a list of tuples,
        each of which contains 2 items:
        The first item of the tuple is the priority of the element,
        the second item of the tuple is the element.
        A smaller number means a higher priority."""
        MinHeap.__init__(self, ls)

    def insert(self, element: object, priority=sys.maxsize):
        """Adds `element` to this min priority queue.

        You can specify the priority of the element
        by assigning a value to "priority".

        Note that the value assigned to priority
        should be an object that overrides functions
        such as `__lt__`, `__gt__`, `__le__`, `__ge__`,
        `__eq__`, `__ne__`, in other words,
        it should be a comparable object,
        and it should be comparable to the other priorities
        of the other elements.

        If element is an `HeapNode`, the `priority` argument's value is ignored,
        and the priority of the key field of `HeapNode` is used as priority."""
        if not isinstance(element, HeapNode):
            self.add(HeapNode(key=priority, value=element))
        else:
            self.add(element)

    def extract_min(self, priority=False):
        """Removes and returns the element with highest priority to exit from the queue.

        In this `MinPriorityQueue` implementation,
        if A has an higher priority than B,
        then `A.priority <= B.priority`.

        If `priority` is set to `True`, a tuple is returned,
        whose first item is the initial added element
        and the second item is the priority of the element.

        If self is empty, `None` is returned.

        **Time Complexity**: O(log<sub>2</sub>(n))."""
        m = self.remove_min()
        if m is not None:
            if priority:
                return (m.value, m.key)
            else:
                return m.value

    def peek(self, priority=False):
        """Returns (without removing) the element with highest priority.

        In this `MinPriorityQueue` implementation,
        if A has an higher priority than B,
        then `A.priority <= B.priority`.

        If priority is set to True,
        a tuple of the form (element, priority) is returned,
        otherwise only element is returned,
        where element is the element in self with highest priority.

        **Time Complexity**: O(1)."""
        m = self.find_min()
        if m is not None:
            if priority:
                return (m.value, m.key)
            else:
                return m.value

    def contains(self, element):
        """Returns `True` if element is in this min-priority queue, `False` otherwise.

        **Time Complexity**: O(n)."""
        return self.search_by_value(element) != -1

    def change_priority(self, element, new_priority):
        """Assigns `new_priority` to be the new priority of `element`.

        If `element` is not in this min-priority queue,
        a `LookupError` is raised.

        **Time Complexity**: O(n)."""
        i = self.search_by_value(element)
        if i == -1:
            raise LookupError("No element found.")
        self.replace(i, HeapNode(key=new_priority, value=element))
