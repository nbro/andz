#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado
Created: 15/02/2016
Updated: 30/08/2016

# Description

Tests for the BSTNode class.
"""

import unittest

from ands.ds.BST import BSTNode


class TestBSTNode(unittest.TestCase):
    def test_None(self):
        self.assertRaises(ValueError, BSTNode, None)

    def test_init(self):
        self.assertRaises(TypeError, BSTNode)

        n = BSTNode(12)
        self.assertEqual(n.key, 12)
        self.assertIsNone(n.value)
        self.assertIsNone(n.left)
        self.assertIsNone(n.right)
        self.assertIsNone(n.parent)
        self.assertEqual(n.label, "[" + str(n.key) + "]")
        self.assertIsNone(n.sibling)
        self.assertIsNone(n.grandparent)
        self.assertIsNone(n.uncle)

        self.assertRaises(AttributeError, n.is_left_child)
        self.assertRaises(AttributeError, n.is_right_child)

        self.assertFalse(n.has_children())
        self.assertFalse(n.has_one_child())
        self.assertFalse(n.has_two_children())
        self.assertEqual(n.count(), 1)

        n2 = BSTNode(14, "Fourteen")
        self.assertEqual(n2.value, "Fourteen")

        # BSTNode objects are not comparable
        with self.assertRaises(TypeError):
            n < n2
        with self.assertRaises(TypeError):
            n >= n2

        # You need explicitly to set the parent
        n.left = n2
        self.assertIs(n.left, n2)
        self.assertIsNone(n2.parent)

        n2.parent = n
        self.assertIs(n2.parent, n)
        self.assertTrue(n.has_children())
        self.assertTrue(n.has_one_child())
        self.assertFalse(n.has_two_children())
        self.assertEqual(n.count(), 2)
        self.assertIsNone(n.parent)

        n3 = BSTNode(28)
        n.right = n3
        self.assertTrue(n.has_children())
        self.assertFalse(n.has_one_child())
        self.assertTrue(n.has_two_children())
        self.assertEqual(n.count(), 3)
        self.assertIsNone(n.right.parent)

        self.assertIs(n.left, n2)
        self.assertIs(n.right, n3)
        self.assertIsNone(n.parent)

        n3.parent = n
        self.assertIsNotNone(n.right.parent)

        n.reset()
        self.assertFalse(n.has_children())
        self.assertFalse(n.has_one_child())
        self.assertFalse(n.has_two_children())
        self.assertEqual(n.count(), 1)
        self.assertIsNone(n.parent)

    def test_sibling(self):
        p = BSTNode(12)
        l = BSTNode(14)
        r = BSTNode(28)
        p.left = l
        p.right = r
        l.parent = p
        r.parent = p
        self.assertIsNotNone(l.sibling)
        self.assertIsNotNone(r.sibling)
        self.assertIs(l.sibling, r)
        self.assertIs(r.sibling, l)

        p.left = None
        self.assertIsNone(r.sibling)
        self.assertIsNone(l.sibling)

    def test_grandparent(self):
        n = BSTNode(12)
        self.assertIsNone(n.grandparent)

        n2 = BSTNode(14)
        n2.left = n
        n.parent = n2
        self.assertIsNone(n.grandparent)

        n3 = BSTNode(28)
        n3.right = n2
        n2.parent = n3
        self.assertIsNone(n2.grandparent)
        self.assertIsNotNone(n2.parent)
        self.assertIsNone(n3.grandparent)
        self.assertIsNotNone(n.grandparent)
        self.assertIs(n.grandparent, n3)

    def test_uncle(self):
        n = BSTNode(12)
        p = BSTNode(14)
        g = BSTNode(28)

        n.parent = p
        p.left = n
        p.parent = g
        g.right = p
        self.assertIsNotNone(n.parent)
        self.assertIsNotNone(n.grandparent)
        self.assertIsNone(n.sibling)
        self.assertIsNone(n.uncle)

        u = BSTNode(7)
        g.left = u
        u.parent = g
        self.assertIsNotNone(n.uncle)
        self.assertIs(n.uncle, u)

        n.reset()
        self.assertIsNone(n.parent)
        self.assertIsNone(n.grandparent)
        self.assertIsNone(n.uncle)
        self.assertIsNone(n.sibling)
        self.assertRaises(AttributeError, n.is_left_child)
