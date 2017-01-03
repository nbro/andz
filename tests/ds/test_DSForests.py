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
from random import randint

from ands.ds.DSForests import DSForests, DSNode


class TestDSNode(unittest.TestCase):
    def test_creation(self):
        n = DSNode(7)
        self.assertTrue(n.is_root())
        self.assertEqual(n.parent, n)
        self.assertEqual(n.next, n)
        self.assertEqual(n.rank, 0)
        self.assertEqual(n.value, 7)

    def test_creation_custom_rank(self):
        n = DSNode(9, 101)
        self.assertEqual(n.rank, 101)

    def test_repr(self):
        n = DSNode(31)
        self.assertEqual("(value: 31, rank: 0, parent: self)", repr(n))
        n.parent = "null"
        self.assertEqual("(value: 31, rank: 0, parent: null)", repr(n))

    def test_str(self):
        n = DSNode(39)
        self.assertEqual("39", str(n))


class TestDSForests(unittest.TestCase):
    def test_empty_creation(self):
        DSForests()

    def test_make_set_one(self):
        ds = DSForests()
        s = ds.make_set(3)
        self.assertEqual(len(ds.sets), 1)
        self.assertEqual(s.value, 3)
        self.assertEqual(s.rank, 0)
        self.assertEqual(s.parent, s)
        self.assertEqual(s.next, s)

    def test_make_set_many(self):
        ds = DSForests()

        n = randint(5, 11)
        for elem in range(n):
            a = ds.make_set(elem)
            self.assertEqual(a.value, elem)
            self.assertEqual(a.rank, 0)
            self.assertEqual(a.parent, a)
            self.assertEqual(a.next, a)

        self.assertEqual(len(ds.sets), n)

    def test_find_one(self):
        ds = DSForests()
        a = ds.make_set(12)
        self.assertEqual(ds.find_iteratively(a), a)

    def test_find_two(self):
        ds = DSForests()
        a = ds.make_set(-11)
        b = ds.make_set(13)
        self.assertEqual(ds.find_iteratively(a), a)
        self.assertEqual(ds.find_iteratively(b), b)

    def test_union_same_element(self):
        ds = DSForests()

        ds.make_set(51)
        u = ds.union(51, 51)

        self.assertIsNone(u)

    def test_union_same_set(self):
        ds = DSForests()

        ds.make_set(17)
        ds.make_set(19)
        ds.union(17, 19)
        u = ds.union(17, 19)

        self.assertIsNone(u)

    def test_union_else(self):
        # it also tests the if statement inside the else
        ds = DSForests()
        a = ds.make_set(19)
        b = ds.make_set(23)
        u = ds.union(19, 23)

        self.assertEqual(u, a)

        self.assertEqual(a.next, b)
        self.assertEqual(b.next, a)

        self.assertEqual(ds.find_iteratively(a), a)
        self.assertEqual(a.value, 19)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)

        self.assertEqual(ds.find_iteratively(b), a)
        self.assertEqual(b.value, 23)
        self.assertEqual(b.rank, 0)
        self.assertEqual(b.parent, a)

    def test_union_if(self):
        ds = DSForests()

        a = ds.make_set(12)
        b = ds.make_set(14)
        ds.union(12, 14)
        c = ds.make_set(28)
        u2 = ds.union(28, 12)

        self.assertEqual(a.next, c)
        self.assertEqual(b.next, a)
        self.assertEqual(c.next, b)

        self.assertEqual(u2, a)

        self.assertEqual(ds.find_iteratively(c), a)
        self.assertEqual(c.value, 28)
        self.assertEqual(c.rank, 0)
        self.assertEqual(c.parent, a)
        self.assertEqual(a.value, 12)
        self.assertEqual(a.rank, 1)
        self.assertEqual(a.parent, a)

    def test_print_set(self):
        # This is not really a test with assertions, but just a visual one.
        # This example was actually from an exercise of an assignment
        # that I had during the course "Algorithms and Data Structures 2" at USI.
        ds = DSForests()

        print()

        for i in range(1, 17):
            ds.make_set(i)
            # ds.print_set(i)

        # print("--------------------------------------")

        for i in range(1, 16, 2):
            ds.union(i, i + 1)
            # ds.print_set(i)

        # print("--------------------------------------")

        for i in range(2, 15, 4):
            ds.union(i, i + 2)
            # ds.print_set(i)

        # print("--------------------------------------")

        ds.union(4, 7)
        # ds.print_set(5)
        # ds.print_set(11)
        # ds.print_set(16)

        # print("--------------------------------------")

        ds.union(10, 16)
        # ds.print_set(8)
        # ds.print_set(13)

        # print("--------------------------------------")

        ds.union(8, 13)
        ds.print_set(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
