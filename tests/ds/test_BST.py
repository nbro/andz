#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 13/02/16

Tests for the BST class.
"""

from ands.ds.BST import BST, bst_invariant
from ands.ds.BSTNode import BSTNode


def assert_consistencies(bst):
    """Call only when bst.root is not None"""
    assert bst.root.count() == bst.n == bst.size()
    assert bst.root.parent is None

def test_empty(b):
    assert not b.root
    assert b.size() == b.n == 0
    print("test_empty finished.")

def test_empty_size():
    b = BST()
    test_empty(b)
    assert bst_invariant(b)
    print("test_empty_size finished.")

def test_empty_contains():
    b = BST()
    for i in range(-10, 11):
        assert not b.contains(i)
    print("test_empty_contains finished.")

def test_one_size():
    b = BST()
    b.insert(12)
    assert b.size() == b.n == b.root.count() == 1
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_one_size finished.")

def test_one_contains():
    b = BST()
    b.insert(12)
    for i in range(-10, 11):
        assert not b.contains(i)
    assert b.contains(12)
    print("test_one_contains finished.")

def test_many_size():
    b = BST()
    size = 0
    for i in range(-10, 11):
        b.insert(i)
        size += 1
        assert size == b.size() == b.n == b.root.count()
        assert bst_invariant(b)
        assert_consistencies(b)
    print("test_many_size finished.")

def test_many_contains():
    b = BST()
    for i in range(-10, 11):
        b.insert(i)
    for i in range(-10, 11):
        assert b.contains(i)
    print("test_many_contains finished.")

def test_structure_many():
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
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_structure_many finished.")
    
def test_delete_not_found():
    b = BST()
    try:
        b.delete(12)
        assert False
    except LookupError as e:
        pass
    print("test_delete_not_found finished.")

def test_delete_one_size():
    b = BST()
    b.insert(12)    
    b.delete(12)
    assert not b.contains(12)
    test_empty(b)
    assert bst_invariant(b)
    print("test_delete_one_size finished.")

def test_multiple_remove1():
    b = BST()
    for i in range(15):
        b.insert(i)
    for i in range(0, 15, 2):
        b.delete(i)
        assert not b.contains(i)
    for i in range(1, 15, 2):
        assert b.contains(i)
    assert b.size() == b.n == b.root.count() == 7
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_multiple_remove1 finished.")

def test_multiple_remove2():
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
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_multiple_remove2 finished.")

def test_multiple_remove3():
    b = BST()
    test_empty()
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
    assert bst_invariant(b)
    assert_consistencies(b)
    b.delete(3)
    b.delete(10)
    b.delete(12)
    assert b.size() == b.n == b.root.count() == 7
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_multiple_remove3 finished.")

def test_search():
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
    assert bst_invariant(b)
    assert_consistencies(b)
    b.delete(10)
    assert not b.search(10)
    assert b.size() == b.n == b.root.count() == 2
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_search finished.")
    
def test_remove_min_and_max():
    b = BST()
    assert not b.remove_min()
    assert not b.remove_max()    
    b.insert(14)
    b.insert(12)
    b.insert(28)
    
    m = b.remove_min()
    assert m and m.key == 12
    assert b.size() == b.n == b.root.count() == 2
    assert bst_invariant(b)
    assert_consistencies(b)

    M = b.remove_max()
    assert M and M.key == 28
    assert b.size() == b.n == b.root.count() == 1
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_remove_min_and_max finished.")

def test_predecessor_and_successor():
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
    print("test_predecessor_and_successor finished.")

def test_rank():
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
    print("test_rank finished.")

def test_switch():
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
        bst_invariant(b)
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
    print("test_switch finished.")


def run_tests():
    test_empty_size()
    test_empty_contains()
    test_one_size()
    test_one_contains()
    test_many_size()
    test_many_contains()
    test_structure_many()
    test_delete_not_found()
    test_delete_one_size()
    test_multiple_remove1()
    test_multiple_remove2()
    test_search()
    test_remove_min_and_max()
    test_predecessor_and_successor()
    test_rank()
    test_switch()


if __name__ == "__main__":
    run_tests()
