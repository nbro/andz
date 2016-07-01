#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last Update: 01/07/16

Basic class to represent simple stacks,
which are LIFO (last-in-first-out) data structures.
"""

from tabulate import tabulate


__all__ = ["Stack"]


class Stack:

    def __init__(self, s=[]):
        self.stack = s

    def push(self, e):
        """Pushes `e` on top of this stack."""
        self.stack.append(e)

    def pop(self):
        """Returns the top of this stack, or `None` if the stack is empty."""
        return None if self.is_empty() else self.stack.pop()

    def size(self):
        """Returns the size of this stack."""
        return len(self.stack)

    def is_empty(self):
        """Returns `True` if this stack is empty, `False` otherwise."""
        return self.size() == 0

    def top(self):
        """Returns but does **not** pop the top of the stack.
        If the stack is empty, `None` is returned."""
        return None if self.is_empty() else self.stack[-1]

    def __str__(self):
        return tabulate([[e] for e in reversed(self.stack)], tablefmt="grid")

    def __repr__(self):
        return self.__str__()
