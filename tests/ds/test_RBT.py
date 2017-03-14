#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 15/02/2016

Updated: 12/03/2017

# Description

Unit tests for the RBT and RBTNode classes.
"""

import unittest
from random import randint, choice

from ands.ds.RBT import RED, BLACK, RBT, RBTNode


class TestRBTNode(unittest.TestCase):
    # Only testing new functionality with respect to BSTNode

    def test_default_color(self):
        n = RBTNode(3)
        self.assertEqual(n.color, BLACK)

    def test_set_color(self):
        n = RBTNode(3)
        n.color = RED
        self.assertEqual(n.color, RED)

    def test_reset(self):
        n = RBTNode(3)
        n.color = RED
        n.reset()
        self.assertEqual(n.color, BLACK)

    def test_default_label(self):
        n = RBTNode(3)
        self.assertEqual(n.label, "[3, BLACK]")


class TestRBT(unittest.TestCase):
    def test_insert_one_key_None(self):
        t = RBT()
        self.assertRaises(ValueError, t.insert, None)

    def test_insert_one_rbt_node_not_reset(self):
        t = RBT()
        n = RBTNode(2)
        n.parent = "not None"
        self.assertRaises(ValueError, t.insert, n)

    def test_insert_one_key_default_value(self):
        t = RBT()

        t.insert("one")
        self.assertEqual(t.size, 1)
        self.assertEqual(t.height(), 1)

        one = t.search("one")
        self.assertTrue(isinstance(one, RBTNode))
        self.assertIs(one, t.minimum())
        self.assertIs(one, t.maximum())

    def test_insert_one_key(self):
        t = RBT()

        t.insert("one", 25)

        self.assertEqual(t.size, 1)
        self.assertEqual(t.height(), 1)
        self.assertEqual(t.rank("one"), 0)

        one = t.search("one")

        self.assertEqual(one.value, 25)
        self.assertIs(one, t.minimum())
        self.assertIs(one, t.maximum())
        self.assertIsNone(t.successor("one"))
        self.assertIsNone(t.predecessor("one"))

    def test_insert_many(self):
        t = RBT()
        ls = [4, 6, 2, 0, 9, 1, RBTNode(5), 3, RBTNode(7), 8]

        t.insert_many(ls)

        self.assertEqual(t.size, 10)
        self.assertEqual(t.rank(5), 5)

        zero = t.search(0)
        nine = t.search(9)

        self.assertIs(zero, t.minimum())
        self.assertIs(nine, t.maximum())

    def test_insert_many_random(self):
        t = RBT()

        ls = [randint(-100, 100) for _ in range(500)]

        t.insert_many(ls)
        self.assertEqual(t.size, 500)

        for elem in ls:
            self.assertTrue(t.contains_key(elem))

    def test_remove_max_empty_tree(self):
        t = RBT()
        self.assertIsNone(t.remove_max())

    def test_remove_max_one_node(self):
        t = RBT()
        five = RBTNode(5)
        t.insert(five)
        self.assertEqual(five, t.remove_max())
        self.assertTrue(t.is_empty())

    def test_remove_max_when_many(self):
        t = RBT()
        five = RBTNode(5)
        t.insert_many([-10, 3, -5, 2, 3, 2, 4, -4, five])
        self.assertEqual(five, t.remove_max())
        self.assertEqual(t.size, 8)

    def test_remove_min_empty_tree(self):
        t = RBT()
        self.assertIsNone(t.remove_min())

    def test_remove_min_one_node(self):
        t = RBT()
        five = RBTNode(5)
        t.insert(five)
        self.assertEqual(five, t.remove_min())
        self.assertTrue(t.is_empty())

    def test_remove_min_when_many(self):
        t = RBT()
        minus_ten = RBTNode(-10)
        t.insert_many([minus_ten, 3, -5, 2, 3, 2, 4, -4, 10])
        self.assertEqual(minus_ten, t.remove_min())
        self.assertEqual(t.size, 8)

    def test_delete_key_None(self):
        t = RBT()
        self.assertRaises(ValueError, t.delete, None)

    def test_delete_key_not_found(self):
        t = RBT()
        self.assertRaises(LookupError, t.delete, 3)
        t = RBT()
        t.insert_many([1, 3, 4])
        self.assertRaises(LookupError, t.delete, 5)

    def test_delete_rbt_node_not_found(self):
        t = RBT()
        n = RBTNode(3)
        self.assertRaises(LookupError, t.delete, n)

    def test_delete_one_size(self):
        t = RBT()
        t.insert(12)
        t.delete(12)
        self.assertFalse(t.contains_key(12))
        self.assertTrue(t.is_empty())

    def test_delete_no_children(self):
        t = RBT()
        nine = RBTNode(9)
        t.insert_many([5, 2, 10, 8, nine])
        deleted = t.delete(9)
        self.assertIs(nine, deleted)
        self.assertIsNone(deleted.left)
        self.assertIsNone(deleted.right)
        self.assertIsNone(deleted.parent)
        self.assertEqual(t.size, 4)

    def test_delete_one_child(self):
        t = RBT()
        eight = RBTNode(8)
        t.insert_many([5, 2, 10, eight, 9])
        deleted = t.delete(8)
        self.assertIs(eight, deleted)
        self.assertIsNone(deleted.left)
        self.assertIsNone(deleted.right)
        self.assertIsNone(deleted.parent)
        self.assertEqual(t.size, 4)

    def test_delete_two_children(self):
        t = RBT()
        ten = RBTNode(10)
        t.insert_many([5, 2, ten, 8, 9, 8, 12, 11, 13])
        deleted = t.delete(10)
        self.assertIs(ten, deleted)
        self.assertIsNone(deleted.left)
        self.assertIsNone(deleted.right)
        self.assertIsNone(deleted.parent)
        self.assertEqual(t.size, 8)

    def test_delete_all_in_random_order(self):
        t = RBT()

        ls = [RBTNode(randint(-100, 100), randint(-100, 100)) for _ in range(500)]
        t.insert_many(ls)

        size = len(ls)
        for _ in range(size):
            elem = choice(ls)
            ls.remove(elem)
            self.assertEqual(t.delete(elem), elem)

        self.assertTrue(t.is_empty())
