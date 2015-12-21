#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Basic queue data structure,
which is a FIFO (first-in-first-out) data structure.
"""


class BaseQueue:
    """Base queue data structure"""

    def __init__(self, ls):
        self.q = ls

    def enqueue(self, n):
        self.q.append(n)

    def dequeue(self):
        return self.q.pop(0)

    def is_empty(self):
        return self.size() == 0

    def is_not_empty(self):
        return not self.is_empty()

    def size(self):
        return len(self.q)
