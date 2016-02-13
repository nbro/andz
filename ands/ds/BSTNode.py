#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/16

Class to represent a BST's node.
"""

import sys
from tabulate import tabulate
from ands.ds.BaseNode import BaseNode


__all__ = ["BSTNode"]


class BSTNode(BaseNode):
    """Base class for a BST's node."""

    def __init__(self, key, value=None, parent=None, left=None, right=None):
        BaseNode.__init__(self, key, value)
        self.parent = parent
        self.left = left
        self.right = right
        self.label = "[" + str(self.key) + "]"  # Used for printing purposes.

    @property
    def sibling(self):
        """Returns the sibling node of this node,
        which can of course be `None`."""
        if self.parent is not None:
            if self.is_left_child():
                return self.parent.right
            else:
                return self.parent.left

    @property
    def grandparent(self):
        """Returns the parent of the parent of this node."""
        if self.parent is not None:
            return self.parent.parent

    @property
    def uncle(self):
        """Returns the uncle node of this node.
        The uncle is the sibling of the parent of this node,
        if it exists. None is returned if it doesn't exist,
        or the parent or grandparent of this node is None."""
        if self.grandparent is not None:  # implies that also parent is not None
            if self.parent == self.grandparent.left:
                return self.grandparent.right
            else:  # self.parent == self.grandparent.right:
                return self.grandparent.left

    def reset(self):
        self.parent = None
        self.left = None
        self.right = None

    def is_left_child(self):
        if self.parent is not None:
            if self.parent.left is not None:
                return self.parent.left == self
        else:
            raise AttributeError("self does not have a parent.")

    def is_right_child(self):
        if self.parent is not None:
            if self.parent.right is not None:
                return self.parent.right == self
        else:
            raise AttributeError("self does not have a parent.")

    def has_children(self) -> bool:
        """Returns True if self has at least one child."""
        return self.left or self.right

    def has_one_child(self) -> bool:
        """Returns True only if self has exactly one child."""
        return (self.left and not self.right) or (not self.left and self.right)

    def has_two_children(self) -> bool:
        """Returns True if self has exactly two children."""
        return self.left and self.right

    def count(self):
        if not self.has_children():
            return 1
        else:
            c = 0
            return self._count(self, c)

    def _count(self, u, c: int):
        if u is None:
            return c
        else:
            c += 1
        c = self._count(u.left, c)
        c = self._count(u.right, c)
        return c

    def __str__(self):
        return "{" + str(self.key) + ": " + str(self.value) + "}"

    def __fields(self):
        return[["Node (Key)", self.key],
              ["Value", self.value],
              ["Parent", self.parent],
              ["Left child", self.left],
              ["Right child", self.right],
              ["Sibling", self.sibling],
              ["Grandparent", self.grandparent],
              ["Uncle", self.uncle]]

    def __repr__(self):
        return tabulate(self.__fields(), tablefmt="fancy_grid")

    def show(self):
        print(self.__repr__())
