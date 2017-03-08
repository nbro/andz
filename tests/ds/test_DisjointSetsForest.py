#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 22/02/2016

Updated: 08/03/2017

# Description

Tests for the DisjointSetsForest class and associated classes.
"""

import unittest
from random import randint, choice

from ands.ds.DisjointSetsForest import DisjointSetsForest, DSFNode


class TestDSFNode(unittest.TestCase):
    def test_creation(self):
        n = DSFNode(7)
        self.assertTrue(n.is_root())
        self.assertEqual(n.parent, n)
        self.assertEqual(n.next, n)
        self.assertEqual(n.rank, 0)
        self.assertEqual(n.value, 7)

    def test_creation_custom_rank(self):
        n = DSFNode(9, 101)
        self.assertEqual(n.rank, 101)

    def test_repr(self):
        n = DSFNode(31)
        self.assertEqual("(value: 31, rank: 0, parent: self)", repr(n))
        n.parent = "null"
        self.assertEqual("(value: 31, rank: 0, parent: null)", repr(n))

    def test_str(self):
        n = DSFNode(39)
        self.assertEqual("39", str(n))


class TestDSForests(unittest.TestCase):
    def setUp(self):
        self.d = DisjointSetsForest()

    def test_make_set_elem_already_exits(self):
        self.d.make_set(3)
        self.assertRaises(LookupError, self.d.make_set, 3)

    def test_make_set_one(self):
        self.assertIsNone(self.d.make_set(3))
        self.assertEqual(self.d.size, 1)
        self.assertEqual(self.d.sets, 1)
        self.assertEqual(self.d.find(3), 3)

    def test_make_set_many(self):
        n = randint(5, 11)

        for elem in range(n):
            self.d.make_set(elem)
            self.assertEqual(self.d.find(elem), elem)

        self.assertEqual(self.d.size, n)
        self.assertEqual(self.d.sets, n)

    def test_contains(self):
        self.assertFalse(self.d.contains(3))
        self.d.make_set(3)
        self.assertTrue(self.d.contains(3))

    def test_find_one_when_does_not_exist(self):
        self.assertRaises(LookupError, self.d.find, 7)

    def test_find_one(self):
        self.d.make_set(5)
        self.assertEqual(self.d.find(5), 5)

    def test_find_two(self):
        self.d.make_set(-11)
        self.d.make_set(13)
        self.assertEqual(self.d.find(-11), -11)
        self.assertEqual(self.d.find(13), 13)

    def test_union_elements_do_not_exist(self):
        self.d.make_set(7)
        self.assertRaises(LookupError, self.d.union, 5, 7)
        self.assertRaises(LookupError, self.d.union, 7, 5)
        self.assertRaises(LookupError, self.d.union, 11, 5)

    def test_union_same_element(self):
        self.d.make_set(51)
        self.assertIsNone(self.d.union(51, 51))
        self.assertEqual(self.d.size, 1)
        self.assertEqual(self.d.sets, 1)

    def test_union(self):
        self.d.make_set(51)
        self.d.make_set(53)
        self.assertEqual(self.d.sets, 2)
        self.assertIsNotNone(self.d.union(51, 53))
        self.assertEqual(self.d.size, 2)
        self.assertEqual(self.d.sets, 1)

    def test_union_when_already_in_same_set(self):
        self.d.make_set(17)
        self.d.make_set(19)
        self.d.union(17, 19)
        self.assertIsNone(self.d.union(17, 19))
        self.assertEqual(self.d.size, 2)
        self.assertEqual(self.d.sets, 1)

    def test_sequence_of_make_set_find_and_union(self):

        n = randint(43, 101)
        ls = []

        for _ in range(n):

            x = randint(-33, 77)
            while self.d.contains(x):
                x = randint(-33, 77)
            ls.append(x)

            self.d.make_set(x)

        # While there's more than one set do a few unions
        while self.d.sets > 1:
            x = choice(ls)
            y = choice(ls)
            self.d.union(x, y)

        # Assert that all elements are still in the ds
        for elem in ls:
            self.assertIsNotNone(self.d.find(elem))
            self.assertTrue(self.d.contains(elem))

        self.assertEqual(self.d.size, n)

    def test_print_set_when_elem_not_exist(self):
        self.assertRaises(LookupError, self.d.print_set, 3)

    def test_print_set(self):
        for i in range(1, 17):
            self.d.make_set(i)

        for i in range(1, 16, 2):
            self.d.union(i, i + 1)

        for i in range(2, 15, 4):
            self.d.union(i, i + 2)

        self.d.union(4, 7)
        self.d.union(10, 16)
        self.d.union(8, 13)

        self.d.print_set(3)
