#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 13/02/2016

Updated: 14/03/2017

# Description

Unit tests for the BST and _BSTNode classes.
"""

import string
import unittest
from random import randint, choice

from ands.ds.BST import BST, _BSTNode


class TestBST(unittest.TestCase):
    def setUp(self):
        self.t = BST()

    def test_create_default(self):
        self.assertEqual(self.t.size, 0)
        self.assertTrue(self.t.is_empty())

    def test_clear(self):
        for e in [2, 3, 5]:
            self.t.insert(e)
        self.t.clear()
        self.assertTrue(self.t.is_empty())

    def test_insert_one_when_key_is_None(self):
        self.assertRaises(ValueError, self.t.insert, None)

    def test_insert_one(self):
        self.t.insert("one")
        self.assertEqual(self.t.size, 1)
        self.assertEqual(self.t.height(), 1)
        self.assertEqual(self.t.rank("one"), 0)
        self.assertTrue(self.t.contains("one"))

    def test_insert_many(self):
        for letter in string.printable:
            self.t.insert(letter)

        self.assertEqual(self.t.size, len(string.printable))

        for letter in string.printable:
            self.assertTrue(self.t.contains(letter))

    def test_contains_when_key_is_None(self):
        self.assertRaises(ValueError, self.t.contains, None)

    def test_contains_when_empty_tree(self):
        self.assertFalse(self.t.contains("two"))

    def test_contains_true(self):
        self.t.insert(12)
        self.t.insert(5)
        self.assertTrue(self.t.contains(12))

    def test_contains_false(self):
        self.t.insert(12)
        self.assertFalse(self.t.contains(14))

    def test_rank_when_key_is_None(self):
        self.assertRaises(ValueError, self.t.rank, None)

    def test_rank_when_key_not_found(self):
        self.assertRaises(LookupError, self.t.rank, 19)

    def test_rank_when_key_is_the_smallest_element(self):
        for i in range(3):
            self.t.insert(i)
        self.assertEqual(self.t.rank(0), 0)

    def test_rank_when_key_is_the_greatest_element(self):
        for i in range(5):
            self.t.insert(i)
        self.assertEqual(self.t.rank(4), 4)

    def test_rank_when_key_is_some_element_in_the_middle(self):
        for e in [10, 5, 6, 19]:
            self.t.insert(e)
        self.assertEqual(self.t.rank(6), 1)

    def test_height_when_tree_empty(self):
        self.assertEqual(self.t.height(), 0)

    def test_minimum_when_empty_tree(self):
        self.assertIsNone(self.t.minimum())

    def test_minimum(self):
        for e in [10, 8, 5, 5, 1, 2, 3]:
            self.t.insert(e)
        self.assertEqual(self.t.minimum(), 1)

    def test_maximum_when_empty_tree(self):
        self.assertIsNone(self.t.maximum())

    def test_maximum(self):
        for i in range(3):
            self.t.insert(i)
        self.assertEqual(self.t.maximum(), 2)

    def test_successor_when_key_is_None(self):
        self.assertRaises(ValueError, self.t.successor, None)

    def test_successor_when_key_does_not_exist(self):
        self.assertRaises(LookupError, self.t.successor, 4)

    def test_successor_when_no_successor(self):
        for e in [4, 2, 50, 8]:
            self.t.insert(e)
        self.assertIsNone(self.t.successor(50))

    def test_successor_when_is_min_of_right_sub_tree(self):
        for e in [5, 2, 10, 8, 9]:
            self.t.insert(e)
        self.assertEqual(8, self.t.successor(5))

    def test_successor_when_is_first_node_up_to_root_such_that_child_is_not_right(
            self):
        for e in [5, 2, 10, 8, 9]:
            self.t.insert(e)
        self.assertEqual(self.t.successor(9), 10)

    def test_predecessor_when_key_is_None(self):
        self.assertRaises(ValueError, self.t.predecessor, None)

    def test_predecessor_when_key_does_not_exist(self):
        self.assertRaises(LookupError, self.t.predecessor, 4)

    def test_predecessor_when_is_None(self):
        for e in [4, 5, 6, 10, 5]:
            self.t.insert(e)
        self.assertIsNone(self.t.predecessor(4))

    def test_predecessor_when_is_max_of_left_sub_tree(self):
        for e in [5, 2, 10, 8, 9]:
            self.t.insert(e)
        self.assertEqual(self.t.predecessor(10), 9)

    def test_predecessor_when_is_first_node_up_to_root_such_that_child_is_not_left(
            self):
        for e in [5, 2, 10, 8, 9]:
            self.t.insert(e)
        self.assertEqual(self.t.predecessor(8), 5)

    def test_remove_max_when_empty_tree(self):
        self.assertIsNone(self.t.remove_max())

    def test_remove_max_when_greatest_node_has_left_child_and_is_root(self):
        for e in [10, 8, 9]:
            self.t.insert(e)
        self.t.remove_max()
        self.assertEqual(self.t.size, 2)

    def test_remove_max_when_greatest_node_has_left_child_and_is_not_root(self):
        for e in [5, 2, 10, 8, 9]:
            self.t.insert(e)
        self.t.remove_max()
        self.assertEqual(self.t.size, 4)

    def test_remove_max_when_greatest_node_does_not_have_left_child_and_is_root(
            self):
        self.t.insert(5)
        self.t.remove_max()
        self.assertEqual(self.t.size, 0)

    def test_remove_max_when_greatest_node_does_not_have_left_child_and_is_not_root(
            self):
        for e in [5, 2, 10]:
            self.t.insert(e)
        self.t.remove_max()
        self.assertEqual(self.t.size, 2)

    def test_remove_min_when_empty_tree(self):
        self.assertIsNone(self.t.remove_min())

    def test_remove_min_when_smallest_node_has_right_child_and_is_root(self):
        for e in [2, 3, 5]:
            self.t.insert(e)
        self.t.remove_min()
        self.assertEqual(self.t.size, 2)

    def test_remove_min_when_smallest_node_has_right_child_and_is_not_root(
            self):
        for e in [5, 2, 3]:
            self.t.insert(e)
        self.t.remove_min()
        self.assertEqual(self.t.size, 2)

    def test_remove_min_when_smallest_node_does_not_have_right_child_and_is_root(
            self):
        self.t.insert(2)
        self.t.remove_min()
        self.assertTrue(self.t.is_empty())

    def test_remove_min_when_smallest_node_does_not_have_right_child_and_is_not_root(
            self):
        for e in [5, 10, 2]:
            self.t.insert(e)
        self.t.remove_min()
        self.assertTrue(self.t.size, 2)

    def test_delete_when_key_is_None(self):
        self.assertRaises(ValueError, self.t.delete, None)

    def test_delete_when_key_not_found(self):
        self.assertRaises(LookupError, self.t.delete, 3)
        for e in [1, 3, 4]:
            self.t.insert(e)
        self.assertRaises(LookupError, self.t.delete, 5)

    def test_delete_when_size_1(self):
        self.t.insert(12)
        self.assertIsNone(self.t.delete(12))
        self.assertFalse(self.t.contains(12))
        self.assertTrue(self.t.is_empty())

    def test_delete_when_no_children(self):
        for e in [5, 2, 10, 8, 9]:
            self.t.insert(e)
        self.assertIsNone(self.t.delete(9))
        self.assertEqual(self.t.size, 4)

    def test_delete_when_one_child(self):
        for e in [5, 2, 10, 8, 9]:
            self.t.insert(e)
        self.assertIsNone(self.t.delete(8))
        self.assertEqual(self.t.size, 4)

    def test_delete_when_two_children(self):
        for e in [5, 2, 10, 8, 9, 8, 12, 11, 13]:
            self.t.insert(e)
        self.assertIsNone(self.t.delete(10))
        self.assertEqual(self.t.size, 8)

    def test_delete_all_in_random_order(self):
        ls = [randint(-100, 100) for _ in range(1000)]

        for e in ls:
            self.t.insert(e)

        for _ in range(len(ls)):
            elem = choice(ls)
            ls.remove(elem)
            self.assertIsNone(self.t.delete(elem))

        self.assertTrue(self.t.is_empty())

    def test_in_order_traversal(self):
        for e in [10, 4, 85, 43, 6, 1, 69]:
            self.t.insert(e)
        self.t.in_order_traversal()

    def test_pre_order_traversal(self):
        for e in [10, 4, 85, 43, 6, 1, 69]:
            self.t.insert(e)
        self.t.pre_order_traversal()

    def test_post_order_traversal(self):
        for e in [10, 4, 85, 43, 6, 1, 69]:
            self.t.insert(e)
        self.t.post_order_traversal()

    def test_reverse_in_order_traversal(self):
        for e in [10, 4, 85, 43, 6, 1, 69]:
            self.t.insert(e)
        self.t.reverse_in_order_traversal()


class TestBSTNode(unittest.TestCase):
    def test_create_when_key_None(self):
        self.assertRaises(ValueError, _BSTNode, None)

    def test_create_when_no_key(self):
        self.assertRaises(TypeError, _BSTNode)

    def test_create_default(self):
        n = _BSTNode(12)
        self.assertEqual(n.key, 12)
        self.assertIsNone(n.left)
        self.assertIsNone(n.right)
        self.assertIsNone(n.parent)
        self.assertEqual(n.count(), 1)

    def test_comparison_when_values_are_of_different_types(self):
        a = _BSTNode(12)
        b = _BSTNode(14)
        with self.assertRaises(TypeError):
            a < b
        with self.assertRaises(TypeError):
            a >= b

    def test_when_no_parent(self):
        n = _BSTNode(12)
        self.assertRaises(AttributeError, n.is_left_child)
        self.assertRaises(AttributeError, n.is_right_child)
        self.assertIsNone(n.sibling)
        self.assertIsNone(n.grandparent)
        self.assertIsNone(n.uncle)

    def test_set_parent(self):
        a = _BSTNode(12)
        b = _BSTNode(14)
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

    def test_when_no_children(self):
        n = _BSTNode(12)
        self.assertFalse(n.has_children())
        self.assertFalse(n.has_one_child())
        self.assertFalse(n.has_two_children())

    def test_set_left_child(self):
        a = _BSTNode(12)
        b = _BSTNode(14)
        a.left = b

        self.assertIs(a.left, b)
        self.assertIsNone(b.parent)
        self.assertEqual(a.count(), 2)

        self.assertTrue(a.has_children())
        self.assertTrue(a.has_one_child())
        self.assertFalse(a.has_two_children())

    def test_set_right_child(self):
        a = _BSTNode(12)
        b = _BSTNode(28)
        a.right = b

        self.assertIs(a.right, b)
        self.assertEqual(a.count(), 2)
        self.assertIsNone(b.parent)

        self.assertTrue(a.has_children())
        self.assertTrue(a.has_one_child())
        self.assertFalse(a.has_two_children())

    def test_set_both_children(self):
        a = _BSTNode(12)
        a.left = _BSTNode(11)
        a.right = _BSTNode(13)
        self.assertEqual(a.count(), 3)
        self.assertTrue(a.has_children())
        self.assertFalse(a.has_one_child())
        self.assertTrue(a.has_two_children())

    def test_is_left_child(self):
        a = _BSTNode(3)
        b = _BSTNode(4)
        a.left = b
        b.parent = a
        self.assertTrue(b.is_left_child())
        self.assertFalse(b.is_right_child())

    def test_is_right_child(self):
        a = _BSTNode(3)
        b = _BSTNode(4)
        a.right = b
        b.parent = a
        self.assertFalse(b.is_left_child())
        self.assertTrue(b.is_right_child())

    def test_sibling(self):
        p = _BSTNode(12)
        l = _BSTNode(14)
        r = _BSTNode(28)

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
        a = _BSTNode(12)
        b = _BSTNode(14)
        c = _BSTNode(28)

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
        n = _BSTNode(12)
        p = _BSTNode(14)
        g = _BSTNode(28)

        n.parent = p
        p.left = n
        p.parent = g
        g.right = p

        self.assertIsNotNone(n.parent)
        self.assertIsNotNone(n.grandparent)
        self.assertIsNone(n.sibling)
        self.assertIsNone(n.uncle)

        u = _BSTNode(7)
        g.left = u
        u.parent = g

        self.assertIsNotNone(n.uncle)
        self.assertIs(n.uncle, u)
