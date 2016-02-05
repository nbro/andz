#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/16


All elements of Heap objects are represented
with objects of the class HeapNode.
"""

from ands.ds.BSTNode import BSTNode


__all__ = ["HeapNode"]


class HeapNode(BSTNode):
    """HeapNode objects are added to Heap objects as wrappers to their elements."""

    def __init__(self, key, value, p=None, left=None, right=None, index=-1):
        """key is used to heapify the heap.

        value can be used for example for the name of the HeapNode object.

        index should contain the position of this HeapNode object in the heap,
        but the used of this variable is for now deprecated."""
        BSTNode.__init__(self, key, value, p, left, right)
        self.index = index

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.value) + " -> " + str(self.key) + "$"

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        return self.key <= other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __lt__(self, other):
        return not self.__ge__(other)

    def __gt__(self, other):
        return not self.__le__(other)
