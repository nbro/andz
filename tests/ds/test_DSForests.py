#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 22/02/16

Last update: 28/08/16

Tests for the DSForests class and associated classes.
"""

import unittest

from ands.ds.DSForests import DSForests


class TestDSForests(unittest.TestCase):

    def test_empty_creation(self):
        DSForests()

    def test_operations(self):
        ds = DSForests()
        a = ds.make_set(12)
        b = ds.make_set(14)

        assert ds.find(a) == a
        assert a.value == 12 and a.rank == 0 and a.parent == a
        assert ds.find(b) == b
        assert b.value == 14 and b.rank == 0 and b.parent == b

        u1 = ds.union(12, 14)
        assert u1 == a
        assert ds.find(a) == a
        assert a.value == 12 and a.rank == 1 and a.parent == a
        assert ds.find(b) == a
        assert b.value == 14 and b.rank == 0 and b.parent == a

        c = ds.make_set(28)
        assert ds.find(c) == c
        assert c.value == 28 and c.rank == 0 and c.parent == c

        u2 = ds.union(12, 28)
        assert u2 == a
        assert ds.find(c) == a
        assert c.value == 28 and c.rank == 0 and c.parent == a
        assert a.value == 12 and a.rank == 1 and a.parent == a

        u3 = ds.union(14, 28)
        assert u3 == a
        assert ds.find(c) == a
        assert c.value == 28 and c.rank == 0 and c.parent == a
        assert a.value == 12 and a.rank == 1 and a.parent == a

        d = ds.make_set(7)
        e = ds.make_set(10)

        u4 = ds.union(7, 10)
        assert u4 == d
        assert ds.find(d) == d
        assert d.value == 7 and d.rank == 1 and d.parent == d
        assert ds.find(e) == d
        assert e.value == 10 and e.rank == 0 and d.parent == d
        assert ds.find(e) == d
        assert ds.find(a) == a

        assert ds.find(e) != ds.find(a)
        assert ds.find(d) != ds.find(a)

        ds.union(7, 12)
        assert ds.find(e) == ds.find(a)
        assert ds.find(d) == ds.find(a)


if __name__ == "__main__":
    unittest.main(verbosity=2)
