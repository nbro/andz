#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado

Creation: 22/02/16

Last update: 03/01/17

## Description

Tests for the DSForests class and associated classes.

## Note

Since find_iteratively internally asserts that its result is equal to find,
in these tests I'm using find_iteratively
to not need to write tests for both find and find_iteratively.
"""

import unittest

from ands.ds.DSForests import DSForests, DSNode


class TestDSNode(unittest.TestCase):

    def test_creation(self):
        n = DSNode(7)
        self.assertTrue(n.is_root())
        self.assertEqual(n.parent, n)
        self.assertEqual(n.rank, 0)
        self.assertEqual(n.value, 7)

    def test_creation_custom_rank(self):
        n = DSNode(9, 101)
        self.assertEqual(n.rank, 101)

    def test_repr(self):
        n = DSNode(31)
        self.assertEqual("(value: 31, rank: 0, parent: self)", str(n))
        n.parent = "null"
        self.assertEqual("(value: 31, rank: 0, parent: null)", str(n))


class TestDSForests(unittest.TestCase):
    def test_empty_creation(self):
        DSForests()

    def test_make_set_one(self):
        ds = DSForests()
        s = ds.make_set(12)
        self.assertEqual(len(ds.sets), 1)
        self.assertEqual(s.value, 12)
        self.assertEqual(s.rank, 0)
        self.assertEqual(s.parent, s)

    def test_find_one(self):
        ds = DSForests()
        a = ds.make_set(12)
        self.assertEqual(ds.find_iteratively(a), a)

    def test_make_set_two(self):
        ds = DSForests()
        a = ds.make_set(5)
        b = ds.make_set(3)

        self.assertEqual(a.value, 5)
        self.assertEqual(a.rank, 0)
        self.assertEqual(a.parent, a)

        self.assertEqual(b.value, 3)
        self.assertEqual(b.rank, 0)
        self.assertEqual(b.parent, b)

        self.assertEqual(len(ds.sets), 2)

    def test_find_two(self):
        ds = DSForests()
        a = ds.make_set(-11)
        b = ds.make_set(13)

        self.assertEqual(ds.find_iteratively(a), a)
        self.assertEqual(ds.find_iteratively(b), b)

    def test_union_one(self):
        ds = DSForests()
        a = ds.make_set(51)
        u = ds.union(51, 51)
        self.assertEqual(u, a)

    def test_union_two(self):
        ds = DSForests()
        a = ds.make_set(19)
        b = ds.make_set(23)
        u = ds.union(19, 23)

        self.assertEqual(len(ds.sets), 2)
        self.assertEqual(u, a)

        self.assertEqual(ds.find_iteratively(a), a)
        self.assertEqual(a.value, 19)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)

        self.assertEqual(ds.find_iteratively(b), a)
        self.assertEqual(b.value, 23)
        self.assertEqual(b.rank, 0)
        self.assertEqual(b.parent, a)

    def test_union_five(self):
        ds = DSForests()
        a = ds.make_set(12)
        b = ds.make_set(14)

        u1 = ds.union(12, 14)
        self.assertEqual(u1, a)
        self.assertEqual(ds.find_iteratively(a), a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)
        self.assertEqual(ds.find_iteratively(b), a)
        self.assertEqual(b.value, 14)
        self.assertEqual(b.rank, 0)
        self.assertEqual(b.parent, a)

        c = ds.make_set(28)
        self.assertEqual(ds.find_iteratively(c), c)
        self.assertEqual(c.value, 28)
        self.assertEqual(c.rank, 0)
        self.assertEqual(c.parent, c)

        u2 = ds.union(28, 12)
        self.assertEqual(u2, a)
        self.assertEqual(ds.find_iteratively(c), a)
        self.assertEqual(c.value, 28)
        self.assertEqual(c.rank, 0)
        self.assertEqual(c.parent, a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)

        u3 = ds.union(14, 28)
        self.assertEqual(u3, a)
        self.assertEqual(ds.find_iteratively(c), a)
        self.assertEqual(c.value, 28)
        self.assertEqual(c.rank, 0)
        self.assertEqual(c.parent, a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)

        d = ds.make_set(7)
        e = ds.make_set(10)

        u4 = ds.union(7, 10)
        self.assertEqual(u4, d)
        self.assertEqual(ds.find_iteratively(d), d)
        self.assertEqual(d.value, 7)
        self.assertEqual(d.rank, 1)
        self.assertEqual(d.parent, d)
        self.assertEqual(ds.find_iteratively(e), d)
        self.assertEqual(e.value, 10)
        self.assertEqual(e.rank, 0)
        self.assertEqual(e.parent, d)

        self.assertEqual(ds.find_iteratively(e), d)
        self.assertEqual(ds.find_iteratively(a), a)

        self.assertNotEqual(ds.find_iteratively(e), ds.find_iteratively(a))
        self.assertNotEqual(ds.find_iteratively(d), ds.find_iteratively(a))

        ds.union(7, 12)
        self.assertEqual(ds.find_iteratively(e), ds.find_iteratively(a))
        self.assertEqual(ds.find_iteratively(d), ds.find_iteratively(a))

        self.assertEqual(len(ds.sets), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)