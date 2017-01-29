#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado
Created: 29/01/2017
Updated: 29/01/2017

# Description

Testing the TSTNode class inside TST.py.

"""

import unittest

from ands.ds.TST import TSTNode


class TestTSTNode(unittest.TestCase):
    def test_create_key_not_string(self):
        self.assertRaises(TypeError, TSTNode, 13)

    def test_create_key_empty_string(self):
        self.assertRaises(ValueError, TSTNode, "")

    def test_create_acceptable_key(self):
        self.assertIsInstance(TSTNode("unit testing"), TSTNode)

    def test_create_default(self):
        u = TSTNode("default values")
        self.assertEqual(u.key, "default values")
        self.assertIsNone(u.value)
        self.assertIsNone(u.parent)
        self.assertIsNone(u.mid)
        self.assertIsNone(u.left)
        self.assertIsNone(u.right)

    def test_create_custom(self):
        p = TSTNode("parent")
        left = TSTNode("left")
        mid = TSTNode("mid")
        right = TSTNode("right")
        u = TSTNode("u", 11, p, left, mid, right)
        self.assertEqual(u.value, 11)
        self.assertIs(u.parent, p)
        self.assertIs(u.left, left)
        self.assertIs(u.mid, mid)
        self.assertIs(u.right, right)

    def test_is_left_child_no_parent(self):
        u = TSTNode("u")
        self.assertRaises(AttributeError, u.is_left_child)

    def test_is_left_child_false(self):
        p = TSTNode("p")
        u = TSTNode("u", 3, p)
        self.assertFalse(u.is_left_child())

    def test_is_left_child_true(self):
        p = TSTNode("p")
        u = TSTNode("u", 3, p)
        p.left = u
        self.assertTrue(u.is_left_child())

    def test_is_right_child_no_parent(self):
        u = TSTNode("u")
        self.assertRaises(AttributeError, u.is_right_child)

    def test_is_right_child_false(self):
        p = TSTNode("p")
        u = TSTNode("u", 3, p)
        self.assertFalse(u.is_right_child())

    def test_is_right_child_true(self):
        p = TSTNode("p")
        u = TSTNode("u", 3, p)
        p.right = u
        self.assertTrue(u.is_right_child())

    def test_is_mid_child_no_parent(self):
        u = TSTNode("u")
        self.assertRaises(AttributeError, u.is_mid_child)

    def test_is_mid_child_false(self):
        p = TSTNode("p")
        u = TSTNode("u", 3, p)
        self.assertFalse(u.is_mid_child())

    def test_is_mid_child_true(self):
        p = TSTNode("p")
        u = TSTNode("u", 3, p)
        p.mid = u
        self.assertTrue(u.is_mid_child())

    def test_has_children_0(self):
        u = TSTNode("u")
        self.assertFalse(u.has_children())

    def test_has_children_1(self):
        u = TSTNode("u", right=TSTNode("right"))
        self.assertTrue(u.has_children())

    def test_has_children_2(self):
        u = TSTNode("u", mid=TSTNode("mid"), left=TSTNode("left"))
        self.assertTrue(u.has_children())

    def test_has_children_3(self):
        u = TSTNode("u", mid=TSTNode("mid"), left=TSTNode("left"), right=TSTNode("right"))
        self.assertTrue(u.has_children())
