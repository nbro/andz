#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 13/02/2016

Updated: 16/02/2017

# Description

Tests for the BST class.
"""

import unittest
from random import randint, choice

from ands.ds.BST import BST, BSTNode


class TestBST(unittest.TestCase):
    def test_create_default(self):
        t = BST()
        self.assertIsNone(t.root)
        self.assertEqual(t.size(), 0)

    def test_create_only_root_given_ok(self):
        n = BSTNode(3)
        t = BST(n)
        self.assertIs(t.root, n)
        self.assertEqual(t.size(), 1)

    def test_create_tree_given_ok(self):
        def gen_sub_tree():
            t = BST()
            t.insert(3)
            t.insert(1)
            t.insert(5)
            return t.root

        root = gen_sub_tree()
        t = BST(root)
        self.assertIs(t.root, root)
        self.assertEqual(t.size(), 3)

    def test_create_root_given_not_bst_node(self):
        self.assertRaises(TypeError, BST, 3)

    def test_create_root_given_has_parent(self):
        n = BSTNode(3)
        n.parent = BSTNode(5)
        self.assertRaises(ValueError, BST, n)

    def test_create_tree_given_not_all_bst_nodes(self):
        a = BSTNode(5)
        b = BSTNode(3)
        b.parent = a
        a.left = b
        a.right = "not a bst node"
        self.assertRaises(TypeError, BST, a)

    def test_create_tree_given_not_has_bst_property(self):
        a = BSTNode(3)
        b = BSTNode(5)
        b.parent = a
        a.left = b
        self.assertRaises(TypeError, BST, a)

    def test_clear(self):
        t = BST()
        t.insert(2)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        t.clear()
        self.assertTrue(t.is_empty())
        self.assertEqual(t.height(), 0)
        self.assertIsNone(t.minimum())
        self.assertIsNone(t.maximum())

    def test_is_root_empty_tree(self):
        t = BST()
        self.assertTrue(t.is_root(None))

    def test_is_root_one(self):
        n = BSTNode(3)
        t = BST(n)
        self.assertTrue(t.is_root(n))

    def test_insert_one_key_None(self):
        t = BST()
        self.assertRaises(ValueError, t.insert, None)

    def test_insert_one_bst_node_not_reset(self):
        t = BST()
        n = BSTNode(2)
        n.parent = "not None"
        self.assertRaises(ValueError, t.insert, n)

    def test_insert_one_key_default_value(self):
        t = BST()

        t.insert("one")

        self.assertEqual(t.size(), 1)
        self.assertEqual(t.height(), 1)

        one = t.search("one")

        self.assertTrue(isinstance(one, BSTNode))
        self.assertIs(one, t.minimum())
        self.assertIs(one, t.maximum())

    def test_insert_one_key(self):
        t = BST()

        t.insert("one", 25)

        self.assertEqual(t.size(), 1)
        self.assertEqual(t.height(), 1)
        self.assertEqual(t.rank("one"), 0)

        one = t.search("one")

        self.assertEqual(one.value, 25)
        self.assertIs(one, t.minimum())
        self.assertIs(one, t.maximum())
        self.assertIsNone(t.successor("one"))
        self.assertIsNone(t.predecessor("one"))

    def test_insert_many_not_list(self):
        t = BST()
        self.assertRaises(TypeError, t.insert_many, 5)
        self.assertRaises(TypeError, t.insert_many, 3.14)
        self.assertRaises(TypeError, t.insert_many, "")
        self.assertRaises(TypeError, t.insert_many, {})
        self.assertRaises(TypeError, t.insert_many, ())

    def test_insert_many_empty_list(self):
        t = BST()
        t.insert_many([])
        self.assertTrue(t.is_empty())

    def test_insert_many(self):
        t = BST()
        ls = [0, 1, 2, 3, 4, BSTNode(5), 6, BSTNode(7), 8, 9]

        t.insert_many(ls)

        self.assertEqual(t.size(), 10)
        self.assertEqual(t.rank(5), 5)

        zero = t.search(0)
        nine = t.search(9)

        self.assertIs(zero, t.minimum())
        self.assertIs(nine, t.maximum())

    def test_search_key_None(self):
        t = BST()
        self.assertRaises(ValueError, t.search, None)

    def test_search_starting_node_not_bst_node(self):
        t = BST()
        self.assertRaises(TypeError, t.search, 3, "not a BSTNode")

    def test_search_starting_node_has_bad_pointers(self):
        t = BST()
        n = BSTNode(5)
        n.parent = 10
        self.assertRaises(TypeError, t.search, 3, n)

    def test_search_starting_tree_has_not_bst_property(self):
        t = BST()
        a = BSTNode(5)
        b = BSTNode(3)
        a.right = b
        b.parent = a
        self.assertRaises(TypeError, t.search, 3, a)

    def test_search_empty_tree_starting_node_given(self):
        t = BST()
        self.assertIsNone(t.search("two", BSTNode("one")))

    def test_search_empty_tree(self):
        t = BST()
        self.assertIsNone(t.search("one"))

    def test_search_without_starting_node_exists(self):
        t = BST()
        t.insert_many([5, BSTNode(2, "two"), 6])
        two = t.search(2)
        self.assertIsInstance(two, BSTNode)
        self.assertEqual(two.key, 2)
        self.assertEqual(two.value, "two")

    def test_search_without_starting_node_not_exists(self):
        t = BST()
        t.insert_many([5, BSTNode(2, "two"), 6])
        seven = t.search(7)
        self.assertIsNone(seven)

    def test_search_with_starting_node_exists(self):
        t = BST()

        two = BSTNode(2, "two")
        t.insert_many([5, two, 6])
        found = t.search(2, two)

        self.assertIsInstance(found, BSTNode)
        self.assertEqual(two.key, 2)
        self.assertEqual(two.value, "two")

    def test_search_with_starting_node_not_exists(self):
        t = BST()

        two = BSTNode(2, "two")
        t.insert_many([5, two, 6])
        found = t.search(7, two)

        self.assertIsNone(found)

    def test_contains_empty_tree(self):
        t = BST()
        self.assertFalse(t.contains_key(3))

    def test_contains_true(self):
        t = BST()
        t.insert_many(12, 5)
        self.assertTrue(t.contains_key(12))

    def test_contains_false(self):
        t = BST()
        t.insert(12)
        self.assertFalse(t.contains_key(14))

    def test_rank_key_None(self):
        t = BST()
        self.assertRaises(ValueError, t.rank, None)

    def test_rank_key_not_found(self):
        t = BST()
        self.assertRaises(LookupError, t.rank, 19)

    def test_rank_key_is_the_smallest_elem(self):
        t = BST()
        t.insert_many([1, 2, 3])
        self.assertEqual(t.rank(1), 0)

    def test_rank_key_is_the_greatest_elem(self):
        t = BST()
        t.insert_many([1, 2, 3, 4, 5])
        self.assertEqual(t.rank(5), 4)

    def test_rank_key_some_elem_in_the_mid(self):
        t = BST()
        t.insert_many([10, 5, 6, 19])
        self.assertEqual(t.rank(6), 1)

    def test_height_tree_empty(self):
        t = BST()
        self.assertEqual(t.height(), 0)

    def test_height_insert_in_order(self):
        t = BST()
        for i in range(100):
            t.insert(i)
        self.assertEqual(t.height(), 100)

    def test_in_order_traversal(self):
        t = BST()
        t.insert_many([10, 4, 85, 43, 6, 1, 69])
        t.in_order_traversal()

    def test_pre_order_traversal(self):
        t = BST()
        t.insert_many([10, 4, 85, 43, 6, 1, 69])
        t.pre_order_traversal()

    def test_post_order_traversal(self):
        t = BST()
        t.insert_many([10, 4, 85, 43, 6, 1, 69])
        t.post_order_traversal()

    def test_reverse_in_order_traversal(self):
        t = BST()
        t.insert_many([10, 4, 85, 43, 6, 1, 69])
        t.reverse_in_order_traversal()

    def test_minimum_empty_tree(self):
        t = BST()
        self.assertIsNone(t.minimum())

    def test_minimum(self):
        t = BST()
        m = BSTNode(1)
        t.insert_many([10, 8, 5, 5, m, 2, 3])
        self.assertIs(t.minimum(), m)

    def test_maximum_empty_tree(self):
        t = BST()
        self.assertIsNone(t.maximum())

    def test_maximum(self):
        t = BST()
        m = BSTNode(3)
        t.insert_many([1, 2, m])
        self.assertIs(t.maximum(), m)

    def test_left_rotate_key_not_found(self):
        t = BST()
        self.assertRaises(LookupError, t._left_rotate, 5)

    def test_left_rotate_not_found(self):
        t = BST()
        a = BSTNode(2)
        b = BSTNode(1)
        t.insert(a)
        t.insert(b)
        self.assertRaises(ValueError, t._left_rotate, a)
        self.assertRaises(ValueError, t._left_rotate, 2)

    def test_right_rotate_key_not_found(self):
        t = BST()
        self.assertRaises(LookupError, t._right_rotate, 5)

    def test_right_rotate_not_found(self):
        t = BST()
        a = BSTNode(2)
        b = BSTNode(1)
        t.insert(b)
        t.insert(a)
        self.assertRaises(ValueError, t._right_rotate, b)
        self.assertRaises(ValueError, t._right_rotate, 1)

    def test_successor_key_not_found(self):
        t = BST()
        self.assertRaises(LookupError, t.successor, 4)

    def test_successor_node_not_found(self):
        t = BST()
        n = BSTNode(4)
        self.assertRaises(LookupError, t.successor, n)

    def test_successor_is_None(self):
        t = BST()
        t.insert_many([4, 5, 6, 10, 5])
        self.assertIsNone(t.successor(10))

    def test_successor_is_min_of_right_sub_tree(self):
        t = BST()
        eight = BSTNode(8)
        t.insert_many([5, 2, 10, eight, 9])
        self.assertIs(t.successor(5), eight)

    def test_successor_is_first_node_up_to_root_such_that_child_is_not_right(self):
        t = BST()
        ten = BSTNode(10)
        t.insert_many([5, 2, ten, 8, BSTNode(9)])
        self.assertIs(t.successor(9), ten)

    def test_predecessor_key_not_found(self):
        t = BST()
        self.assertRaises(LookupError, t.predecessor, 4)

    def test_predecessor_node_not_found(self):
        t = BST()
        n = BSTNode(4)
        self.assertRaises(LookupError, t.predecessor, n)

    def test_predecessor_is_None(self):
        t = BST()
        t.insert_many([4, 5, 6, 10, 5])
        self.assertIsNone(t.predecessor(4))

    def test_predecessor_is_max_of_left_sub_tree(self):
        t = BST()
        nine = BSTNode(9)
        t.insert_many([5, 2, 10, 8, nine])
        self.assertIs(t.predecessor(10), nine)

    def test_predecessor_is_first_node_up_to_root_such_that_child_is_not_left(self):
        t = BST()
        five = BSTNode(5)
        t.insert_many([five, 2, 10, 8, BSTNode(9)])
        self.assertIs(t.predecessor(8), five)

    def test_remove_max_empty_tree(self):
        t = BST()
        self.assertIsNone(t.remove_max())

    def test_remove_max_greatest_node_has_left_child_and_is_root(self):
        t = BST()
        ten = BSTNode(10)
        t.insert_many([ten, 8, 9])
        self.assertIs(ten, t.remove_max())
        self.assertEqual(t.size(), 2)

    def test_remove_max_greatest_node_has_left_child_and_is_not_root(self):
        t = BST()
        ten = BSTNode(10)
        t.insert_many([5, 2, ten, 8, 9])
        self.assertIs(ten, t.remove_max())
        self.assertEqual(t.size(), 4)

    def test_remove_max_greatest_node_does_not_have_left_child_and_is_root(self):
        t = BST()
        five = BSTNode(5)
        t.insert_many([five])
        self.assertIs(five, t.remove_max())
        self.assertEqual(t.size(), 0)

    def test_remove_max_greatest_node_does_not_have_left_child_and_is_not_root(self):
        t = BST()
        ten = BSTNode(10)
        t.insert_many([5, 2, ten])
        self.assertIs(ten, t.remove_max())
        self.assertEqual(t.size(), 2)

    def test_remove_min_empty_tree(self):
        t = BST()
        self.assertIsNone(t.remove_min())

    def test_remove_min_smallest_node_has_right_child_and_is_root(self):
        t = BST()
        two = BSTNode(2)
        t.insert_many([two, 3, 5])
        self.assertIs(two, t.remove_min())
        self.assertEqual(t.size(), 2)

    def test_remove_min_smallest_node_has_right_child_and_is_not_root(self):
        t = BST()
        two = BSTNode(2)
        t.insert_many([5, two, 3])
        self.assertIs(two, t.remove_min())
        self.assertEqual(t.size(), 2)

    def test_remove_min_smallest_node_does_not_have_right_child_and_is_root(self):
        t = BST()
        two = BSTNode(2)
        t.insert(two)
        self.assertIs(two, t.remove_min())
        self.assertTrue(t.is_empty())

    def test_remove_min_smallest_node_does_not_have_right_child_and_is_not_root(self):
        t = BST()
        two = BSTNode(2)
        t.insert_many([5, 10, two])
        self.assertIs(two, t.remove_min())
        self.assertTrue(t.size(), 2)

    # TODO: METHODS AFTER REMOVE_MAX

    def test_delete_not_found(self):
        b = BST()
        self.assertRaises(LookupError, b.delete, 12)

    def test_delete_one_size(self):
        b = BST()
        b.insert(12)
        b.delete(12)
        self.assertFalse(b.contains_key(12))

    def test_multiple_remove1(self):
        b = BST()

        for i in range(15):
            b.insert(i)

        for i in range(0, 15, 2):
            b.delete(i)
            self.assertFalse(b.contains_key(i))

        for i in range(1, 15, 2):
            self.assertTrue(b.contains_key(i))

        self.assertEqual(b.size(), 7)

    def test_multiple_remove2(self):
        b = BST()

        for i in range(0, 15, 2):
            b.insert(i)

        for i in range(-1, 15, 2):
            self.assertRaises(LookupError, b.delete, i)
            self.assertFalse(b.contains_key(i))

        for i in range(0, 15, 2):
            self.assertTrue(b.contains_key(i))

        self.assertEqual(b.size(), 8)

    def test_delete_tree_empty(self):
        pass

    def test_delete_key_None(self):
        t = BST()
        self.assertRaises(ValueError, t.delete, None)

    def test_delete_key_not_found(self):
        t = BST()
        self.assertRaises(LookupError, t.delete, 3)

    def test_delete_bst_node_not_found(self):
        t = BST()
        n = BSTNode(3)
        self.assertRaises(LookupError, t.delete, n)

    def test_delete_no_children(self):
        t = BST()

        nine = BSTNode(9)
        t.insert_many([5, 2, 10, 8, nine])

        deleted = t.delete(9)

        self.assertIs(nine, deleted)
        self.assertIsNone(deleted.left)
        self.assertIsNone(deleted.right)
        self.assertIsNone(deleted.parent)
        self.assertEqual(t.size(), 4)

    def test_delete_one_child(self):
        t = BST()

        eight = BSTNode(8)
        t.insert_many([5, 2, 10, eight, 9])

        deleted = t.delete(8)

        self.assertIs(eight, deleted)
        self.assertIsNone(deleted.left)
        self.assertIsNone(deleted.right)
        self.assertIsNone(deleted.parent)
        self.assertEqual(t.size(), 4)

    def test_delete_two_children(self):
        t = BST()

        ten = BSTNode(10)
        t.insert_many([5, 2, ten, 8, 9, 8, 12, 11, 13])

        deleted = t.delete(10)

        self.assertIs(ten, deleted)
        self.assertIsNone(deleted.left)
        self.assertIsNone(deleted.right)
        self.assertIsNone(deleted.parent)
        self.assertEqual(t.size(), 8)

    def test_delete_all_in_random_order(self):
        t = BST()

        ls = [BSTNode(randint(-100, 100), randint(-100, 100)) for _ in range(1000)]
        t.insert_many(ls)

        size = len(ls)
        for _ in range(size):
            elem = choice(ls)
            ls.remove(elem)
            t.delete(elem)

        self.assertTrue(t.is_empty())

    def test__switch_first_node_is_None(self):
        t = BST()
        self.assertRaises(ValueError, t._switch, None, BSTNode(3))

    def test__switch_second_node_is_None(self):
        t = BST()
        self.assertRaises(ValueError, t._switch, BSTNode(3), None)

    def test__switch_nodes_are_equal(self):
        t = BST()
        n = BSTNode(3)
        self.assertRaises(ValueError, t._switch, n, n)

    def test__switch_search_first_true_nodes_not_in_tree(self):
        t = BST()
        a = BSTNode(3)
        b = BSTNode(5)
        self.assertRaises(LookupError, t._switch, a, b, True)
