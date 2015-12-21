#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Basic class to represent simple stacks,
which are LIFO (last-in-first-out) data structures.
"""


class BaseStack:

    def __init__(self, s=[]):
        self.stack = s

    def get(self):
        return self.stack

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        return None if self.empty() else self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0

    def top(self):
        """Returns but does NOT pop the top of the stack.
        If the stack is empty, None is returned."""
        return None if self.empty() else self.stack[-1]
