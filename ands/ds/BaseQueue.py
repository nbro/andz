#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/16

Basic queue, which is FIFO (first-in-first-out) data structure.
"""


class BaseQueue:

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

    def is_not_empty(self):
        """Returns `True` if this queue has at least one element, `False` otherwise."""        
        return not self.is_empty()

    def size(self):
        """Returns the size of this stack."""        
        return len(self.q)
