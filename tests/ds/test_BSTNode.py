#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 15/02/2016

Updated: 16/02/2017

# Description

Tests for the BSTNode class.
"""

import unittest

from ands.ds.BST import *


class TestBSTNode(unittest.TestCase):
    def test_create_key_None(self):
        self.assertRaises(ValueError, BSTNode, None)

    def test_create_no_key(self):
        self.assertRaises(TypeError, BSTNode)

    def test_create_default(self):
        n = BSTNode(12)
        self.assertEqual(n.key, 12)
        self.assertIsNone(n.value)
        self.assertIsNone(n.left)
        self.assertIsNone(n.right)
        self.assertIsNone(n.parent)
        self.assertEqual(n.label, "[" + str(n.key) + "]")
        self.assertEqual(n.count(), 1)

    def test_create_with_key_and_value(self):
        n = BSTNode(14, "fourteen")
        self.assertEqual(n.value, "fourteen")

    def test_comparison_when_values_are_of_different_types(self):
        a = BSTNode(12)
        b = BSTNode(14, "fourteen")
        with self.assertRaises(TypeError):
            a < b
        with self.assertRaises(TypeError):
            a >= b

    def test_no_parent(self):
        n = BSTNode(12)
        self.assertRaises(AttributeError, n.is_left_child)
        self.assertRaises(AttributeError, n.is_right_child)
        self.assertIsNone(n.sibling)
        self.assertIsNone(n.grandparent)
        self.assertIsNone(n.uncle)

    def test_set_parent(self):
        a = BSTNode(12)
        b = BSTNode(14, "fourteen")

        b.parent = a

        self.assertIs(b.parent, a)
        self.assertEqual(a.count(), 1)

        self.assertIsNone(a.parent)
        self.assertIsNone(a.left)
        self.assertIsNone(a.right)

        # If we just set the parent of a node
        # the parent does NOT automatically have children.
        self.assertFalse(a.has_children())
        self.assertFalse(a.has_one_child())
        self.assertFalse(a.has_two_children())

    def test_no_children(self):
        n = BSTNode(12)
        self.assertFalse(n.has_children())
        self.assertFalse(n.has_one_child())
        self.assertFalse(n.has_two_children())

    def test_set_left_child(self):
        a = BSTNode(12)
        b = BSTNode(14, "fourteen")
        a.left = b

        self.assertIs(a.left, b)
        self.assertIsNone(b.parent)
        self.assertEqual(a.count(), 2)

        self.assertTrue(a.has_children())
        self.assertTrue(a.has_one_child())
        self.assertFalse(a.has_two_children())

    def test_set_right_child(self):
        a = BSTNode(12)
        b = BSTNode(28)
        a.right = b

        self.assertIs(a.right, b)
        self.assertEqual(a.count(), 2)
        self.assertIsNone(b.parent)

        self.assertTrue(a.has_children())
        self.assertTrue(a.has_one_child())
        self.assertFalse(a.has_two_children())

    def test_set_both_children(self):
        a = BSTNode(12)
        a.left = BSTNode(11)
        a.right = BSTNode(13)
        self.assertEqual(a.count(), 3)
        self.assertTrue(a.has_children())
        self.assertFalse(a.has_one_child())
        self.assertTrue(a.has_two_children())

    def test_is_left_child(self):
        a = BSTNode(3)
        b = BSTNode(4)
        a.left = b
        b.parent = a
        self.assertTrue(b.is_left_child())
        self.assertFalse(b.is_right_child())

    def test_is_left_child(self):
        a = BSTNode(3)
        b = BSTNode(4)
        a.right = b
        b.parent = a
        self.assertFalse(b.is_left_child())
        self.assertTrue(b.is_right_child())

    def test_sibling(self):
        p = BSTNode(12)
        l = BSTNode(14)
        r = BSTNode(28)

        self.assertIsNone(r.sibling)
        self.assertIsNone(l.sibling)

        p.left = l
        p.right = r
        l.parent = p
        r.parent = p

        self.assertIs(l.sibling, r)
        self.assertIs(r.sibling, l)

        # Without the parent pointers to its children,
        # we can't determine if the children are siblings.
        p.left = None
        self.assertIsNone(r.sibling)
        self.assertIsNone(l.sibling)

    def test_grandparent(self):
        a = BSTNode(12)
        b = BSTNode(14)
        c = BSTNode(28)

        self.assertIsNone(a.grandparent)
        self.assertIsNone(b.grandparent)
        self.assertIsNone(c.grandparent)

        b.left = a
        a.parent = b

        self.assertIsNone(a.grandparent)

        c.right = b
        b.parent = c
        self.assertIsNone(b.grandparent)
        self.assertIsNotNone(b.parent)
        self.assertIsNone(c.grandparent)
        self.assertIsNotNone(a.grandparent)
        self.assertIs(a.grandparent, c)

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

    def test_reset(self):
        n = BSTNode(10, "ten")
        n.left = BSTNode(20)
        n.parent = BSTNode(30)

        n.reset()

        self.assertEqual(n.key, 10)
        self.assertEqual(n.value, "ten")
        self.assertEqual(n.count(), 1)

        self.assertIsNone(n.left)
        self.assertIsNone(n.right)
        self.assertIsNone(n.parent)

        self.assertIsNone(n.grandparent)
        self.assertIsNone(n.uncle)
        self.assertIsNone(n.sibling)
