#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/16

Class to represent a `RBT`'s node.
"""

from ands.ds.BSTNode import BSTNode


__all__ = ["RBTNode", "RED", "BLACK"]


RED = "RED"
BLACK = "BLACK"


class RBTNode(BSTNode):

    def __init__(self, key, value=None, color=BLACK, parent=None, left=None, right=None):
        BSTNode.__init__(self, key, value, parent, left, right)
        self._color = color
        self.label = "[" + str(self.key) + ", " + str(self._color) + "]"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.label = "[" + str(self.key) + ", " + str(self._color) + "]"
        
    def reset(self):
        super().reset()
        self.color = BLACK

    def __fields(self):
        """Used by __repr__."""
        return[["Node (Key)", self.key],
              ["Value", self.value],
              ["Color", self.color],
              ["Parent", self.parent],
              ["Left child", self.left],
              ["Right child", self.right],
              ["Sibling", self.sibling],
              ["Grandparent", self.grandparent],
              ["Uncle", self.uncle]]
