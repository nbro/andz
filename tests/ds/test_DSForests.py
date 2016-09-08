#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 22/02/16

Last update: 06/09/16

Tests for the DSForests class and associated classes.
"""

import unittest

from ands.ds.DSForests import DSForests


class TestDSForests(unittest.TestCase):

    def test_empty_creation(self):
        DSForests()

    def test_make_set_1_and_find(self):
        ds = DSForests()
        a = ds.make_set(12)
        self.assertEqual(ds.find(a), a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 0)
        self.assertEqual(a.parent, a)

    def test_make_set_2_and_find(self):
        ds = DSForests()
        a = ds.make_set(12)
        b = ds.make_set(14)
        self.assertEqual(ds.find(a), a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 0)
        self.assertEqual(a.parent, a)
        self.assertEqual(ds.find(b), b)
        self.assertEqual(b.value, 14)
        self.assertEqual(b.rank, 0)
        self.assertEqual(b.parent, b)

    def test_union_and_find(self):
        ds = DSForests()
        a = ds.make_set(12)
        b = ds.make_set(14)

        u1 = ds.union(12, 14)
        self.assertEqual(u1, a)
        self.assertEqual(ds.find(a), a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)
        self.assertEqual(ds.find(b), a)
        self.assertEqual(b.value, 14)
        self.assertEqual(b.rank, 0)
        self.assertEqual(b.parent, a)

        c = ds.make_set(28)
        self.assertEqual(ds.find(c), c)
        self.assertEqual(c.value, 28)
        self.assertEqual(c.rank, 0)
        self.assertEqual(c.parent, c)

        u2 = ds.union(12, 28)
        self.assertEqual(u2, a)
        self.assertEqual(ds.find(c), a)
        self.assertEqual(c.value, 28)
        self.assertEqual(c.rank, 0)
        self.assertEqual(c.parent, a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)

        u3 = ds.union(14, 28)
        self.assertEqual(u3, a)
        self.assertEqual(ds.find(c), a)
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
        self.assertEqual(ds.find(d), d)
        self.assertEqual(d.value, 7)
        self.assertEqual(d.rank, 1)
        self.assertEqual(d.parent, d)
        self.assertEqual(ds.find(e), d)
        self.assertEqual(e.value, 10)
        self.assertEqual(e.rank, 0)
        self.assertEqual(e.parent, d)

        self.assertEqual(ds.find(e), d)
        self.assertEqual(ds.find(a), a)

        self.assertNotEqual(ds.find(e), ds.find(a))
        self.assertNotEqual(ds.find(d), ds.find(a))

        ds.union(7, 12)
        self.assertEqual(ds.find(e), ds.find(a))
        self.assertEqual(ds.find(d), ds.find(a))


if __name__ == "__main__":
    unittest.main(verbosity=2)
