#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 13/02/16

Last update: 28/08/16

Tests for the BST class.
"""

import unittest
from ands.ds.BST import BST, BSTNode, is_bst


def assert_consistencies(bst):
    """Call only when bst.root is not None"""
    assert bst.root.count() == bst.n == bst.size()
    assert bst.root.parent is None


def assert_empty(b):
    assert not b.root
    assert b.size() == b.n == 0


class TestBST(unittest.TestCase):

    def test_empty_size(self):
        b = BST()
        assert_empty(b)
        self.assertTrue(is_bst(b))

    def test_empty_contains(self):
        b = BST()
        for i in range(-10, 11):
            self.assertFalse(b.contains(i))

    def test_one_size(self):
        b = BST()
        b.insert(12)
        self.assertTrue(b.size() == 1)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

    def test_one_contains(self):
        b = BST()
        b.insert(12)
        for i in range(-10, 11):
            self.assertFalse(b.contains(i))
        self.assertTrue(b.contains(12))

    def test_many_size(self):
        b = BST()
        size = 0

        for i in range(-10, 11):
            b.insert(i)
            size += 1
            self.assertTrue(size == b.size())
            self.assertTrue(is_bst(b))
            assert_consistencies(b)

    def test_many_contains(self):
        b = BST()
        for i in range(-10, 11):
            b.insert(i)
        for i in range(-10, 11):
            self.assertTrue(b.contains(i))

    def test_structure_many(self):
        b = BST()
        b.insert(10)
        b.insert(5)
        b.insert(15)
        b.insert(7)
        b.insert(20)
        b.insert(18)
        b.insert(14)
        b.insert(14)
        b.insert(12)
        b.insert(3)
        b.insert(4)

        self.assertTrue(11 == b.size())
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

    def test_delete_not_found(self):
        b = BST()
        self.assertRaises(LookupError, b.delete, 12)

    def test_delete_one_size(self):
        b = BST()
        b.insert(12)
        b.delete(12)

        self.assertFalse(b.contains(12))
        assert_empty(b)
        self.assertTrue(is_bst(b))

    def test_multiple_remove1(self):
        b = BST()

        for i in range(15):
            b.insert(i)

        for i in range(0, 15, 2):
            b.delete(i)
            self.assertFalse(b.contains(i))

        for i in range(1, 15, 2):
            self.assertTrue(b.contains(i))

        self.assertTrue(b.size() == 7)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

    def test_multiple_remove2(self):
        b = BST()

        for i in range(0, 15, 2):
            b.insert(i)

        for i in range(-1, 15, 2):
            self.assertRaises(LookupError, b.delete, i)
            self.assertFalse(b.contains(i))

        for i in range(0, 15, 2):
            self.assertTrue(b.contains(i))

        self.assertTrue(b.size() == 8)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

    def test_multiple_remove3(self):
        b = BST()
        assert_empty(b)

        b.insert(5)
        b.insert(3)
        b.insert(4)
        b.insert(10)
        b.insert(7)
        b.insert(6)
        b.insert(8)
        b.insert(9)
        b.insert(12)
        b.insert(11)

        self.assertTrue(b.size() == 10)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

        b.delete(3)
        b.delete(10)
        b.delete(12)

        self.assertTrue(b.size() == 7)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

    def test_search(self):
        b = BST()
        b.insert(10)
        b.insert(5)
        b.insert(15)
        self.assertRaises(ValueError, b.search, None)

        self.assertIsNone(b.search(12))
        self.assertIsNotNone(b.search(5))
        self.assertIsNotNone(b.search(10))
        self.assertIsNotNone(b.search(15))

        self.assertTrue(b.size() == 3)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

        b.delete(10)
        self.assertIsNone(b.search(10))

        self.assertTrue(b.size() == 2)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

    def test_remove_min_and_max(self):
        b = BST()
        self.assertIsNone(b.remove_min())
        self.assertIsNone(b.remove_max())

        b.insert(14)
        b.insert(12)
        b.insert(28)

        m = b.remove_min()
        self.assertIsNotNone(m)
        self.assertTrue(m.key == 12)

        self.assertTrue(b.size() == 2)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

        M = b.remove_max()
        self.assertIsNotNone(M)
        self.assertTrue(M.key == 28)

        self.assertTrue(b.size() == 1)
        self.assertTrue(is_bst(b))
        assert_consistencies(b)

    def test_predecessor_and_successor(self):
        b = BST()
        b.insert(12)
        b.insert(14)
        b.insert(28)

        self.assertIsNone(b.successor(28))
        self.assertIs(b.successor(12), b.search(14))
        self.assertIsNone(b.predecessor(12))
        self.assertIs(b.predecessor(14), b.search(12))

        self.assertRaises(LookupError, b.successor, 7)
        self.assertRaises(LookupError, b.predecessor, 6)

    def test_rank(self):
        b = BST()
        self.assertRaises(ValueError, b.rank, None)
        self.assertRaises(LookupError, b.rank, 12)

        b.insert(12)
        self.assertEqual(b.rank(12), 0)

        b.insert(14)
        b.insert(28)
        b.insert(10)
        b.insert(7)

        self.assertEqual(b.rank(12), 2)
        self.assertEqual(b.rank(7), 0)
        self.assertEqual(b.rank(28), 4)

    def test_switch(self):
        b = BST()

        b.insert(12)
        b.insert(20)
        b.insert(28)
        b.insert(8)
        b.insert(16)
        b.insert(10)
        b.insert(4)
        b.insert(2)
        b.insert(5)
        b.insert(9)
        b.insert(11)
        b.insert(14)
        b.insert(18)
        b.insert(22)
        b.insert(30)

        def asserts():
            self.assertTrue(is_bst(b))
            assert_consistencies(b)

        self.assertRaises(ValueError, b._switch, b.search(12), b.search(12))
        self.assertRaises(ValueError, b._switch, b.search(12), None)
        self.assertRaises(
            LookupError,
            b._switch,
            b.search(12),
            BSTNode(100),
            True)

        asserts()

        b._switch(b.search(8), b.search(12))
        self.assertIs(b.root, b.search(8))
        self.assertIsNone(b.root.parent)
        b._switch(b.search(8), b.search(8).left)
        asserts()

        b._switch(b.search(20), b.search(12))
        self.assertIs(b.root, b.search(20))
        self.assertIsNone(b.root.parent)
        b._switch(b.search(20), b.search(20).right)
        asserts()

        b._switch(b.search(4), b.search(10))
        self.assertIs(b.root, b.search(12))
        b._switch(b.search(8).left, b.search(8).right)
        asserts()

        b._switch(b.search(8), b.search(20))
        self.assertIs(b.root, b.search(12))
        b._switch(b.search(12).left, b.search(12).right)
        asserts()

        b._switch(b.search(8), b.search(28))
        self.assertIs(b.root, b.search(12))
        b._switch(b.search(12).left, b.search(20).right)
        asserts()

        b._switch(b.search(8), b.search(14))
        self.assertIs(b.root, b.search(12))
        b._switch(b.search(12).left, b.search(12).right.left.left)
        asserts()

        b._switch(b.search(2), b.search(28))
        self.assertIs(b.root, b.search(12))
        b._switch(b.search(12).left.left.left, b.search(12).right.right)
        asserts()

        self.assertIsNone(b.search(2).left)
        self.assertIsNone(b.search(2).right)
        self.assertIs(b.search(28).left, b.search(22))
        self.assertIs(b.search(28).right, b.search(30))

        b._switch(b.search(8), b.search(5))
        self.assertIs(b.root, b.search(12))
        b._switch(b.search(12).left, b.search(12).left.left.right)
        asserts()

        b._switch(b.search(8), b.search(2))
        self.assertIs(b.root, b.search(12))
        b._switch(b.search(12).left, b.search(12).left.left.left)

        self.assertIsNone(b.search(12).left.left.left.left)
        self.assertIsNone(b.search(12).left.left.left.right)
        self.assertIs(
            b.search(12).left.left.left.parent,
            b.search(12).left.left)

        b._switch(b.search(12), b.search(10))

        self.assertIs(b.root, b.search(10))
        self.assertIsNone(b.root.parent)

        b._switch(b.search(10), b.search(10).left.right)
        asserts()


if __name__ == "__main__":
    unittest.main(verbosity=2)
