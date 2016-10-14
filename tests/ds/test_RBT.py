#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Last update: 08/10/16

Tests for the RBT class.
"""

import unittest
from random import randint, shuffle

from ands.ds.RBT import RED, BLACK, RBT, RBTNode, upper_bound_height, is_rbt


class TestRBTNode(unittest.TestCase):
    def test_None(self):
        self.assertRaises(ValueError, RBTNode, None)

    def test_init(self):
        n = RBTNode(12)
        self.assertEqual(n.key, 12)
        self.assertIsNone(n.value)
        self.assertEqual(n.color, BLACK)

        n.color = RED
        self.assertEqual(n.color, RED)
        self.assertIsNone(n.parent)
        self.assertIsNone(n.left)
        self.assertIsNone(n.right)

        n.reset()
        self.assertEqual(n.color, BLACK)


class TestRBT(unittest.TestCase):
    def assert_invariants(self, t):
        self.assertTrue(is_rbt(t))
        self.assertTrue(upper_bound_height(t))
        if t.root:
            self.assertIsNone(t.root.parent)

    def assert_size_invariant(self, t, size, elem=None):
        self.assertEqual(t.n, size)
        self.assertEqual(t.size(), size)
        if elem is None:
            if size != 0:
                self.assertEqual(t.root.count(), size)
        else:
            self.assertEqual(elem.count(), size)

    def assert_removed_node_invariant(self, r):
        self.assertIsNotNone(r)
        self.assertEqual(r.left, r.right)
        self.assertEqual(r.right, r.parent)
        self.assertIsNone(r.left)

    def test_insert_one(self):
        rbt = RBT()
        self.assertRaises(ValueError, rbt.insert, None)

        h = RBTNode(12)
        j = RBTNode(14)
        h.left = j
        j.parent = h

        self.assertRaises(ValueError, rbt.insert, h)

        rbt.insert(12)
        one = rbt.search(12)
        two = rbt.search(14)

        self.assertIsNone(two)
        self.assertIsNotNone(one)

        self.assertEqual(one.color, BLACK)
        self.assertEqual(one, rbt.root)

        self.assertEqual(rbt.height(), 1)
        self.assert_size_invariant(rbt, 1, one)
        self.assert_invariants(rbt)

    def test_insert_two(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(14)

        one = rbt.search(12)
        two = rbt.search(14)
        three = rbt.search(28)

        self.assertIsNone(three)
        self.assertIsNotNone(one)
        self.assertIsNotNone(two)

        self.assertEqual(one.color, BLACK)
        self.assertEqual(one, rbt.root)
        self.assertEqual(two.color, RED)
        self.assertNotEqual(two, rbt.root)
        self.assertEqual(one.right, two)
        self.assertIsNone(one.left)

        self.assertEqual(rbt.height(), 2)
        self.assert_size_invariant(rbt, 2, one)
        self.assert_invariants(rbt)

    def test_insert_three(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(14)
        rbt.insert(28)

        self.assert_size_invariant(rbt, 3)
        self.assert_invariants(rbt)

        one = rbt.search(12)
        two = rbt.search(14)
        three = rbt.search(28)
        four = rbt.search(7)

        self.assertIsNotNone(one)
        self.assertIsNotNone(two)
        self.assertIsNotNone(three)
        self.assertIsNone(four)

        self.assertEqual(two, rbt.root)
        self.assertIsNone(two.parent)
        self.assertEqual(one.left, one.right)
        self.assertEqual(one.right, three.left)
        self.assertEqual(three.left, three.right)
        self.assertIsNone(one.left)

        self.assertEqual(one.color, RED)
        self.assertEqual(three.color, RED)
        self.assertEqual(two.color, BLACK)

        self.assert_size_invariant(rbt, 3, two)
        self.assert_invariants(rbt)

    def test_height_and_insert_many(self):
        # Lemma proved above put in practice!
        ls = [randint(-100, 100) for _ in range(20)]
        rbt = RBT()
        rbt.insert_many(ls)
        self.assert_invariants(rbt)

    def test_delete_root(self):
        rbt = RBT()

        rbt.insert(12)

        self.assert_size_invariant(rbt, 1)
        self.assert_invariants(rbt)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNone(rbt.root)

        self.assert_size_invariant(rbt, 0)
        self.assert_invariants(rbt)

    def test_delete_root2(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(14)

        self.assert_size_invariant(rbt, 2)
        self.assert_invariants(rbt)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNotNone(rbt.root)

        self.assertIsNotNone(rbt.search(14))
        self.assertIsNone(rbt.root.left)
        self.assertIsNone(rbt.root.right)

        self.assert_size_invariant(rbt, 1)
        self.assert_invariants(rbt)

    def test_delete_root3(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(7)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNotNone(rbt.root)

        self.assertEqual(rbt.root, rbt.search(7))
        self.assertIsNone(rbt.root.left)
        self.assertIsNone(rbt.root.right)

        self.assert_size_invariant(rbt, 1)
        self.assert_invariants(rbt)

    def test_delete_root4(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNotNone(rbt.root)

        self.assertEqual(rbt.root, rbt.search(14))
        self.assertIsNone(rbt.root.right)

        self.assert_size_invariant(rbt, 2)
        self.assert_invariants(rbt)

    def test_delete_root5(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)

        self.assert_size_invariant(rbt, 4)
        self.assert_invariants(rbt)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNotNone(rbt.root)

        self.assertEqual(rbt.root, rbt.search(14))
        self.assertEqual(rbt.root.right, rbt.search(28))
        self.assertEqual(rbt.root.left, rbt.search(7))

        self.assert_size_invariant(rbt, 3)
        self.assert_invariants(rbt)

    def test_delete_root6(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)

        self.assert_size_invariant(rbt, 5)
        self.assert_invariants(rbt)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNotNone(rbt.root)

        self.assertEqual(rbt.root, rbt.search(13))
        self.assertEqual(rbt.root.right, rbt.search(14))
        self.assertEqual(rbt.root.left, rbt.search(7))

        self.assertIsNone(rbt.search(14).left)
        self.assertEqual(rbt.search(14).right, rbt.search(28))

        self.assert_size_invariant(rbt, 4)
        self.assert_invariants(rbt)

    def test_delete_root7(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)
        rbt.insert(35)

        self.assert_size_invariant(rbt, 6)
        self.assert_invariants(rbt)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNotNone(rbt.root)

        self.assertEqual(rbt.root, rbt.search(13))
        self.assertEqual(rbt.root.right, rbt.search(28))
        self.assertEqual(rbt.root.left, rbt.search(7))

        self.assertIsNone(rbt.search(14).left)
        self.assertIsNone(rbt.search(14).right)
        self.assertIsNone(rbt.search(35).left)
        self.assertIsNone(rbt.search(35).right)
        self.assertEqual(rbt.search(28).left, rbt.search(14))
        self.assertEqual(rbt.search(28).right, rbt.search(35))

        self.assert_size_invariant(rbt, 5)
        self.assert_invariants(rbt)

    def test_delete_root8(self):
        rbt = RBT()

        rbt.insert(12)
        rbt.insert(7)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(13)
        rbt.insert(35)
        rbt.insert(25)

        self.assert_size_invariant(rbt, 7)
        self.assert_invariants(rbt)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNotNone(rbt.root)

        self.assertEqual(rbt.root, rbt.search(13))
        self.assertIsNone(rbt.search(14).left)

        self.assert_size_invariant(rbt, 6)
        self.assert_invariants(rbt)

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

        self.assert_size_invariant(rbt, 8)
        self.assert_invariants(rbt)

        r = rbt.delete(12)

        self.assert_removed_node_invariant(r)
        self.assertIsNone(rbt.search(13).left)
        self.assertIsNone(rbt.search(13).right)

        self.assert_size_invariant(rbt, 7)
        self.assert_invariants(rbt)

    def test_delete_all_rand_items(self):
        rbt = RBT()

        def get_rand_list():
            return [randint(-100, 100) for _ in range(randint(0, 100))]

        for _ in range(100):
            ls = get_rand_list()

            for j, x in enumerate(ls):
                rbt.insert(x)
                self.assert_size_invariant(rbt, j + 1)
                self.assert_invariants(rbt)

            self.assert_size_invariant(rbt, len(ls))
            self.assert_invariants(rbt)

            shuffle(ls)

            for j, x in enumerate(ls):
                r = rbt.delete(x)
                self.assert_removed_node_invariant(r)
                self.assert_size_invariant(rbt, len(ls) - (j + 1))
                self.assert_invariants(rbt)

            self.assert_size_invariant(rbt, 0)
            self.assert_invariants(rbt)

    def test_remove_max(self):
        rbt = RBT()

        n = rbt.remove_max()
        self.assertIsNone(n)

        rbt.insert(12)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(6)
        rbt.insert(18)
        rbt.insert(7)
        rbt.insert(10)

        m = rbt.search(28)
        self.assertIsNotNone(m)

        _m = rbt.remove_max()
        self.assertEqual(m, _m)
        self.assertIsNone(rbt.search(28))

        m = rbt.search(18)
        self.assertIsNotNone(m)

        _m = rbt.remove_max()
        self.assertEqual(m, _m)
        self.assertIsNone(rbt.search(18))

    def test_remove_min(self):
        rbt = RBT()

        n = rbt.remove_min()
        self.assertIsNone(n)

        rbt.insert(12)
        rbt.insert(14)
        rbt.insert(28)
        rbt.insert(6)
        rbt.insert(6)
        rbt.insert(18)
        rbt.insert(7)
        rbt.insert(10)

        _m = rbt.remove_min()
        self.assertIsNotNone(rbt.search(6))
        self.assertNotEqual(rbt.search(6), _m)

        m = rbt.search(6)
        self.assertIsNotNone(m)

        _m = rbt.remove_min()
        self.assertEqual(m, _m)
        self.assertIsNone(rbt.search(6))


if __name__ == "__main__":
    unittest.main(verbosity=2)
