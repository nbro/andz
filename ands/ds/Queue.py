#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 02/07/2015

Updated: 04/02/2017

# Description

Basic queue, which is FIFO (first-in-first-out) data structure.
It's implemented using a deque, because a deque supports better the _dequeue_ operation than lists.

# References

- [https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-queues](https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-queues)

"""

from collections import deque, Iterable

__all__ = ["Queue"]


class Queue:
    """This is a wrapper class around the Python deque data structure
    to represent logically a queue (FIFO) data structure.

    You can initialize the class using an iterable (list, tuple, etc) of values,
    which will be assumed to be already in the FIFO order.

    If `ls` is not an instance of `Iterable`, `TypeError` is raised.
    If one of the values in `ls` is None, `ValueError` is raised.
    A copy of `ls` is made, so that changes to the original self
    do not reflect in the original iterable.

    This class does not allow None to be inserted as value
    to the data structure through the methods of the same.

    It also returns None, instead of raising exceptions,
    when trying to dequeue, when the data structure is empty.

    Clients of this class should **never** access fields whose names start with _,
    which are considered private fields."""

    def __init__(self, ls=None):
        if ls is not None:
            if not isinstance(ls, Iterable):
                raise TypeError("ls must be an iterable object")
            if any(elem is None for elem in ls):
                raise ValueError("all elements of ls must be not None")
        else:
            ls = []
        self._q = deque(ls)

    def enqueue(self, elem) -> None:
        """Adds `elem` to the end of this queue.
        If `elem` is None, ValueError is raised."""
        if elem is None:
            raise ValueError("elem cannot be None")
        self._q.append(elem)

    def dequeue(self):
        """Returns the first element of this queue, or None if the queue is empty."""
        return None if self.is_empty() else self._q.popleft()

    def is_empty(self) -> bool:
        """Returns `True` if this queue is empty, `False` otherwise."""
        return self.size() == 0

    def size(self) -> int:
        """Returns the size of this queue."""
        return len(self._q)

    def __str__(self):
        return str(list(self._q))

    def __repr__(self):
        return self.__str__()
