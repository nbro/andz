#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Last update: 28/08/16

Tests for the BSTNode class.
"""

import unittest
from ands.ds.BST import BSTNode


class TestBSTNode(unittest.TestCase):

    def test_None(self):
        try:
            BSTNode(None)
            assert False
        except ValueError:
            pass

    def test_init(self):
        try:
            BSTNode()
            assert False
        except TypeError:
            pass

        n = BSTNode(12)
        assert n.key == 12
        assert not n.value
        assert not n.left and not n.right and not n.parent
        assert n.label == "[" + str(n.key) + "]"
        assert not n.sibling
        assert not n.grandparent
        assert not n.uncle

        try:
            n.is_left_child()
            assert False
        except AttributeError:
            pass

        try:
            n.is_right_child()
            assert False
        except AttributeError:
            pass

        assert not n.has_children()
        assert not n.has_one_child()
        assert not n.has_two_children()
        assert n.count() == 1

        n2 = BSTNode(14, "Fourteen")
        assert n2.value == "Fourteen"

        # BSTNode objects are not comparable
        try:
            n < n2
            assert False
        except TypeError:
            pass

        try:
            n >= n2
            assert False
        except TypeError:
            pass

        # You need explicitly to set the parent
        n.left = n2
        assert n.left == n2
        assert n2.parent is None

        n2.parent = n
        assert n2.parent == n
        assert n.has_children()
        assert n.has_one_child()
        assert not n.has_two_children()
        assert n.count() == 2
        assert not n.parent

        n3 = BSTNode(28)
        n.right = n3
        assert n.has_children()
        assert not n.has_one_child()
        assert n.has_two_children()
        assert n.count() == 3
        assert not n.right.parent
        assert n.left == n2 and n.right == n3
        assert not n.parent

        n3.parent = n
        assert n.right.parent

        n.reset()
        assert not n.has_children()
        assert not n.has_one_child()
        assert not n.has_two_children()
        assert n.count() == 1
        assert not n.parent

    def test_sibling(self):
        p = BSTNode(12)
        l = BSTNode(14)
        r = BSTNode(28)
        p.left = l
        p.right = r
        l.parent = p
        r.parent = p

        assert l.sibling and r.sibling
        assert l.sibling == r and r.sibling == l
        p.left = None
        assert not r.sibling
        assert not l.sibling

    def test_grandparent(self):
        n = BSTNode(12)
        assert not n.grandparent

        n2 = BSTNode(14)
        n2.left = n
        n.parent = n2
        assert not n.grandparent

        n3 = BSTNode(28)
        n3.right = n2
        n2.parent = n3
        assert not n2.grandparent and n2.parent and not n3.grandparent
        assert n.grandparent and n.grandparent == n3

    def test_uncle(self):
        n = BSTNode(12)
        p = BSTNode(14)
        g = BSTNode(28)

        n.parent = p
        p.left = n
        p.parent = g
        g.right = p
        assert n.parent and n.grandparent
        assert not n.sibling
        assert not n.uncle

        u = BSTNode(7)
        g.left = u
        u.parent = g
        assert n.uncle and n.uncle == u
        n.reset()
        assert not n.parent and not n.grandparent and not n.uncle and not n.sibling
        try:
            n.is_left_child()
            assert False
        except AttributeError:
            pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
