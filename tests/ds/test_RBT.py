#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Last update: 28/08/16

Tests for the RBT class.
"""

import unittest

from random import randint, shuffle
from ands.ds.RBT import RED, BLACK, RBT, RBTNode, upper_bound_height, is_rbt
from ands.ds.BST import BSTNode


def assert_rbt_props(t):
    assert is_rbt(t)
    assert upper_bound_height(t)
    if t.root:
        assert not t.root.parent


class TestRBTNode(unittest.TestCase):

    def test_None(self):
        try:
            RBTNode(None)
            assert False
        except ValueError:
            pass

    def test_init(self):
        n = RBTNode(12)
        assert n.key == 12 and not n.value
        assert n.color == BLACK
        n.color = RED
        assert n.color == RED
        assert not n.parent and not n.left and not n.right
        n.reset()
        assert n.color == BLACK


class TestRBT(unittest.TestCase):

    def test_insert_one(self):
        rbt = RBT()
        try:
            rbt.insert(None)
            assert False
        except ValueError:
            pass
        h = RBTNode(12)
        j = RBTNode(14)
        h.left = j
        j.parent = h

        try:
            rbt.insert(h)
            assert False
        except ValueError:
            pass

        rbt.insert(12)
        one = rbt.search(12)
        two = rbt.search(14)
        assert not two and one
        assert one.color == BLACK
        assert one == rbt.root
        assert rbt.height() == 1
        assert rbt.n == rbt.size() == one.count() == 1
        assert_rbt_props(rbt)

    def test_insert_two(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(14)
        one = rbt.search(12)
        two = rbt.search(14)
        three = rbt.search(28)
        assert not three and one and two
        assert one.color == BLACK
        assert one == rbt.root
        assert two.color == RED
        assert two != rbt.root
        assert one.right == two
        assert not one.left
        assert rbt.height() == 2
        assert rbt.n == rbt.size() == one.count() == 2
        assert_rbt_props(rbt)

    def test_insert_three(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(14)
        rbt.insert(28)
        one = rbt.search(12)
        two = rbt.search(14)
        three = rbt.search(28)
        four = rbt.search(7)
        assert two == rbt.root
        assert two.parent is None
        assert one.left == one.right == three.left == three.right
        assert one.left is None
        assert one and two and three and not four
        assert one.color == RED == three.color
        assert two.color == BLACK
        assert rbt.n == rbt.size() == two.count() == 3
        assert_rbt_props(rbt)

    def test_height_and_insert_many(self):
        # Lemma proved above put in practice!
        ls = [randint(-100, 100) for _ in range(20)]
        rbt = RBT()
        rbt.insert_many(ls)
        assert_rbt_props(rbt)

    def test_delete_root(self):
        rbt = RBT()
        rbt.insert(12)
        assert_rbt_props(rbt)
        assert rbt.n == rbt.size() == rbt.root.count() == 1
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert not rbt.root
        assert rbt.n == rbt.size() == 0
        assert_rbt_props(rbt)

    def test_delete_root2(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(14)
        assert rbt.n == rbt.size() == rbt.root.count() == 2
        assert_rbt_props(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.root and rbt.search(14)
        assert not rbt.root.left and not rbt.root.right
        assert rbt.n == rbt.size() == rbt.root.count() == 1
        assert_rbt_props(rbt)

    def test_delete_root3(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        assert rbt.n == rbt.size() == rbt.root.count() == 2
        assert_rbt_props(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.root and rbt.root == rbt.search(7)
        # already check rbt.root.parent is not None in assert_rbt_props
        assert not rbt.root.left and not rbt.root.right
        assert rbt.n == rbt.size() == rbt.root.count() == 1
        assert_rbt_props(rbt)

    def test_delete_root4(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        assert rbt.n == rbt.size() == rbt.root.count() == 3
        assert_rbt_props(rbt)
        # print(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.root and rbt.root == rbt.search(14)
        assert rbt.root.right is None
        assert rbt.n == rbt.size() == rbt.root.count() == 2
        assert_rbt_props(rbt)

    def test_delete_root5(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        assert rbt.n == rbt.size() == rbt.root.count() == 4
        assert_rbt_props(rbt)
        # print(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.root and rbt.root == rbt.search(14)
        assert rbt.root.right == rbt.search(
            28) and rbt.root.left == rbt.search(7)
        assert rbt.n == rbt.size() == rbt.root.count() == 3
        assert_rbt_props(rbt)

    def test_delete_root6(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)
        assert rbt.n == rbt.size() == rbt.root.count() == 5
        assert_rbt_props(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.root and rbt.root == rbt.search(13)
        assert rbt.root.right == rbt.search(
            14) and rbt.root.left == rbt.search(7)
        assert not rbt.search(14).left
        assert rbt.search(14).right == rbt.search(28)
        assert rbt.n == rbt.size() == rbt.root.count() == 4
        assert_rbt_props(rbt)

    def test_delete_root7(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)
        rbt.insert(35)
        assert rbt.n == rbt.size() == rbt.root.count() == 6
        assert_rbt_props(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.root and rbt.root == rbt.search(13)
        assert rbt.root.right == rbt.search(
            28) and rbt.root.left == rbt.search(7)
        assert not rbt.search(14).left and not rbt.search(14).right
        assert not rbt.search(35).left and not rbt.search(35).right
        assert rbt.search(28).left == rbt.search(
            14) and rbt.search(28).right == rbt.search(35)
        assert rbt.n == rbt.size() == rbt.root.count() == 5
        assert_rbt_props(rbt)

    def test_delete_root8(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)
        rbt.insert(35)
        rbt.insert(25)
        assert rbt.n == rbt.size() == rbt.root.count() == 7
        assert_rbt_props(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.root and rbt.root == rbt.search(13)
        assert rbt.n == rbt.size() == rbt.root.count() == 6
        assert not rbt.search(14).left
        assert_rbt_props(rbt)

    def test_delete_root9(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)
        rbt.insert(35)
        rbt.insert(25)
        rbt.insert(12)
        assert rbt.n == rbt.size() == rbt.root.count() == 8
        assert_rbt_props(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert not rbt.search(13).left and not rbt.search(13).right
        assert_rbt_props(rbt)

    def test_delete_root10(self):
        rbt = RBT()
        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)
        rbt.insert(35)
        rbt.insert(25)
        rbt.insert(12)
        rbt.insert(13)
        assert rbt.n == rbt.size() == rbt.root.count() == 9
        assert_rbt_props(rbt)
        r = rbt.delete(12)
        assert r
        assert r.left == r.right == r.parent
        assert r.left is None
        assert rbt.n == rbt.size() == rbt.root.count() == 8
        assert_rbt_props(rbt)

    def test_delete_all_rand_items(self):
        rbt = RBT()

        def get_rand_list():
            return [randint(-100, 100) for _ in range(randint(0, 100))]

        for _ in range(100):
            ls = get_rand_list()

            for j, x in enumerate(ls):
                rbt.insert(x)
                assert rbt.n == rbt.size() == (j + 1)
                assert_rbt_props(rbt)

            assert rbt.n == rbt.size() == len(ls)
            assert_rbt_props(rbt)
            shuffle(ls)

            for j, x in enumerate(ls):
                r = rbt.delete(x)
                assert r
                assert r.left == r.right == r.parent
                assert r.left is None
                assert rbt.n == rbt.size() == (len(ls) - (j + 1))
                assert_rbt_props(rbt)

            assert rbt.n == rbt.size() == 0
            assert_rbt_props(rbt)

    def test_remove_max(self):
        rbt = RBT()
        n = rbt.remove_max()
        assert not n
        rbt.insert(12)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(6)
        rbt.insert(18)
        rbt.insert(7)
        rbt.insert(10)

        m = rbt.search(28)
        assert m
        _m = rbt.remove_max()
        assert m == _m
        assert not rbt.search(28)

        m = rbt.search(18)
        assert m
        _m = rbt.remove_max()
        assert m == _m
        assert not rbt.search(18)

    def test_remove_min(self):
        rbt = RBT()
        n = rbt.remove_min()
        assert not n
        rbt.insert(12)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(6)
        rbt.insert(6)
        rbt.insert(18)
        rbt.insert(7)
        rbt.insert(10)

        _m = rbt.remove_min()
        assert rbt.search(6)
        assert rbt.search(6) != _m

        m = rbt.search(6)
        assert m
        _m = rbt.remove_min()
        assert m == _m
        assert not rbt.search(6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
