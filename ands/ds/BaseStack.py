#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last Update: 05/02/16

Basic class to represent simple stacks,
which are LIFO (last-in-first-out) data structures.
"""


class BaseStack:

    def __init__(self, s=[]):
        self.stack = s

    def get(self):
        """Returns the list containing the elements of `self`."""
        return self.stack

    def push(self, e):
        """Pushes `e` on top of this stack."""
        self.stack.append(e)

    def pop(self):
        """Returns the top of this stack, or `None` if the stack is empty."""
        return None if self.empty() else self.stack.pop()

    def size(self):
        """Returns the size of this stack."""
        return len(self.stack)

    def empty(self):
        """Returns `True` if this stack is empty, `False` otherwise."""
        return self.size() == 0

    def top(self):
        """Returns but does **not** pop the top of the stack.
        If the stack is empty, `None` is returned."""
        return None if self.empty() else self.stack[-1]
