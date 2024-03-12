#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 15/02/2016

Updated: 14/03/2017

# Description

Unit tests for the classes and functions in the andz.ds.RBT module.
"""

from andz.ds.RBT import BLACK, RBT, RED, _RBTNode
from tests.ds.test_BST import TestBST, TestBSTNode

# Only testing new functionality with respect to _BSTNode


class TestRBTNode(TestBSTNode):
    def test_default_color(self):
        n = _RBTNode(3)
        self.assertEqual(n.color, BLACK)

    def test_set_color(self):
        n = _RBTNode(3)
        n.color = RED
        self.assertEqual(n.color, RED)


class TestRBT(TestBST):
    def setUp(self):
        self.t = RBT()
