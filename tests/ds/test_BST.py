#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 13/02/16

Last update: 30/06/16

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
        assert b.size() == b.n == b.root.count() == 1
        assert is_bst(b)
        assert_consistencies(b)

    def test_one_contains(self):
        b = BST()
        b.insert(12)
        for i in range(-10, 11):
            assert not b.contains(i)
        assert b.contains(12)

    def test_many_size(self):
        b = BST()
        size = 0
        for i in range(-10, 11):
            b.insert(i)
            size += 1
            assert size == b.size() == b.n == b.root.count()
            assert is_bst(b)
            assert_consistencies(b)

    def test_many_contains(self):
        b = BST()
        for i in range(-10, 11):
            b.insert(i)
        for i in range(-10, 11):
            assert b.contains(i)

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
        assert 11 == b.size() == b.n == b.root.count()
        assert is_bst(b)
        assert_consistencies(b)
        
    def test_delete_not_found(self):
        b = BST()
        try:
            b.delete(12)
            assert False
        except LookupError as e:
            pass

    def test_delete_one_size(self):
        b = BST()
        b.insert(12)    
        b.delete(12)
        assert not b.contains(12)
        assert_empty(b)
        assert is_bst(b)

    def test_multiple_remove1(self):
        b = BST()
        for i in range(15):
            b.insert(i)
        for i in range(0, 15, 2):
            b.delete(i)
            assert not b.contains(i)
        for i in range(1, 15, 2):
            assert b.contains(i)
        assert b.size() == b.n == b.root.count() == 7
        assert is_bst(b)
        assert_consistencies(b)

    def test_multiple_remove2(self):
        b = BST()
        for i in range(0, 15, 2):
            b.insert(i)
        for i in range(-1, 15, 2):
            try:
                b.delete(i)
                assert False
            except LookupError:
                pass
            assert not b.contains(i)
        for i in range(0, 15, 2):
            assert b.contains(i)
        assert b.size() == b.n == b.root.count() == 8
        assert is_bst(b)
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
        assert b.size() == b.n == b.root.count() == 10
        assert is_bst(b)
        assert_consistencies(b)
        b.delete(3)
        b.delete(10)
        b.delete(12)
        assert b.size() == b.n == b.root.count() == 7
        assert is_bst(b)
        assert_consistencies(b)

    def test_search(self):
        b = BST()
        b.insert(10)
        b.insert(5)
        b.insert(15)
        try:
            b.search(None)
            assert False
        except ValueError:
            pass
        assert not b.search(12)
        assert b.search(5)
        assert b.search(10)
        assert b.search(15)
        assert b.size() == b.n == b.root.count() == 3
        assert is_bst(b)
        assert_consistencies(b)
        b.delete(10)
        assert not b.search(10)
        assert b.size() == b.n == b.root.count() == 2
        assert is_bst(b)
        assert_consistencies(b)
        
    def test_remove_min_and_max(self):
        b = BST()
        assert not b.remove_min()
        assert not b.remove_max()    
        b.insert(14)
        b.insert(12)
        b.insert(28)
        
        m = b.remove_min()
        assert m and m.key == 12
        assert b.size() == b.n == b.root.count() == 2
        assert is_bst(b)
        assert_consistencies(b)

        M = b.remove_max()
        assert M and M.key == 28
        assert b.size() == b.n == b.root.count() == 1
        assert is_bst(b)
        assert_consistencies(b)

    def test_predecessor_and_successor(self):
        b = BST()
        b.insert(12)
        b.insert(14)
        b.insert(28)
        assert not b.successor(28)
        assert b.successor(12) == b.search(14)
        assert not b.predecessor(12)
        assert b.predecessor(14) == b.search(12)
        try:
            b.successor(7)
            b.predecessor(6)
            assert False
        except LookupError as e:
            pass

    def test_rank(self):
        b = BST()
        try:
            b.rank(None)
            assert False
        except ValueError:
            pass
        try:
             b.rank(12)
             assert False
        except LookupError:
            pass
        b.insert(12)
        assert b.rank(12) == 0
        b.insert(14)
        b.insert(28)
        b.insert(10)
        b.insert(7)
        assert b.rank(12) == 2
        assert b.rank(7) == 0
        assert b.rank(28) == 4

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
            assert is_bst(b)
            assert_consistencies(b)

        try:
            b._switch(b.search(12), b.search(12))
            assert False
        except ValueError as e:
            pass
        try:
            b._switch(b.search(12), None)
            assert False
        except ValueError as e:
            pass

        try:
            b._switch(b.search(12), BSTNode(100), search_first=True)
            assert False
        except LookupError as e:
            pass

        asserts()

        b._switch(b.search(8), b.search(12))
        assert b.root == b.search(8)
        assert not b.root.parent    
        b._switch(b.search(8), b.search(8).left)
        asserts()

        b._switch(b.search(20), b.search(12))
        assert b.root == b.search(20)
        assert not b.root.parent    
        b._switch(b.search(20), b.search(20).right)
        asserts()
        
        b._switch(b.search(4), b.search(10))
        assert b.root == b.search(12)
        b._switch(b.search(8).left, b.search(8).right)
        asserts()

        b._switch(b.search(8), b.search(20))
        assert b.root == b.search(12)
        b._switch(b.search(12).left, b.search(12).right)
        asserts()
        
        b._switch(b.search(8), b.search(28))
        assert b.root == b.search(12)
        b._switch(b.search(12).left, b.search(20).right)
        asserts()

        b._switch(b.search(8), b.search(14))
        assert b.root == b.search(12)
        b._switch(b.search(12).left, b.search(12).right.left.left)
        asserts()
        
        b._switch(b.search(2), b.search(28))
        assert b.root == b.search(12)
        b._switch(b.search(12).left.left.left, b.search(12).right.right)
        asserts()
        assert b.search(2).left is None
        assert b.search(2).right is None
        assert b.search(28).left == b.search(22)
        assert b.search(28).right == b.search(30)

        b._switch(b.search(8), b.search(5))
        assert b.root == b.search(12)
        b._switch(b.search(12).left, b.search(12).left.left.right)
        asserts()

        b._switch(b.search(8), b.search(2))
        assert b.root == b.search(12)
        b._switch(b.search(12).left, b.search(12).left.left.left)
        assert not b.search(12).left.left.left.left
        assert not b.search(12).left.left.left.right
        assert b.search(12).left.left.left.parent == b.search(12).left.left

        b._switch(b.search(12), b.search(10))
        assert b.root == b.search(10)
        assert not b.root.parent
        b._switch(b.search(10), b.search(10).left.right)
        asserts()


if __name__ == "__main__":
    unittest.main(verbosity=2)
