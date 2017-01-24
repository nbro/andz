#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado
Created: July, 2015
Updated: 24/01/2017

## Description

Basic queue, which is FIFO (first-in-first-out) data structure.
It's implemented using a deque, because a deque supports better the _dequeue_ operation than lists.

## References

- [https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-queues](https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-queues)

"""

from collections import deque

__all__ = ["Queue"]


class Queue:
    """This is a wrapper class around the Python deque data structure
    to represent logically a queue (FIFO) data structure.

    You can initialize the class using a list of values,
    which will be assumed to be already in the FIFO order.
    These values are assumed not to be None.

    This class does not allow None to be inserted as value
    to the data structure through the methods of the same.

    It also returns None, instead of raising exceptions,
    when trying to dequeue, but the data structure is empty."""

    def __init__(self, ls=None):
        if ls is not None:
            if not isinstance(ls, list):
                raise TypeError("ls must be an instance of list")
            assert all(elem is not None for elem in ls)
        else:
            ls = []
        self.q = deque(ls)

    def enqueue(self, elem) -> None:
        """Adds `elem` to the end of this queue.

        Assumes `elem` is not None."""
        assert elem is not None
        self.q.append(elem)

    def dequeue(self):
        """Returns the first element of this queue, or None if the queue is empty."""
        return None if self.is_empty() else self.q.popleft()

    def is_empty(self) -> bool:
        """Returns `True` if this queue is empty, `False` otherwise."""
        return self.size() == 0

    def size(self) -> int:
        """Returns the size of this queue."""
        return len(self.q)

    def __str__(self):
        return str(list(self.q))

    def __repr__(self):
        return self.__str__()
