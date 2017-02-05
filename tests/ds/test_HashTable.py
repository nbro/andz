#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado
Created: 21/02/2016
Updated: 08/10/2016

# Description

Test the HashTable class.
"""

import string
import unittest
from random import sample, randint, uniform, choice

from ands.ds.HashTable import HashTable, has_duplicates


def gen_rand_str(size):
    return "".join(choice(string.printable) for _ in range(size))


class TestHashTable(unittest.TestCase):
    def put_and_get_numbers(self, random_func=randint, n=100):
        t = HashTable()

        a = [random_func(-100, 100) for _ in range(100)]
        p = None

        def find_all_indices(e, ls):
            return [index for index, item in enumerate(ls) if item == e]

        for i in range(1, n + 1):

            for _, num in enumerate(a):

                if i == 1:
                    self.assertIsNone(p)
                else:
                    self.assertIsNotNone(p)

                    try:
                        find_all_indices(num, p).index(t.get(num))
                    except ValueError:
                        find_all_indices(num, a).index(t.get(num))

                t.put(num, a.index(num))

            p = a
            a = sample(a, len(a))
            self.assertFalse(has_duplicates(t.keys))

        for i, num in enumerate(a):
            try:
                find_all_indices(num, p).index(t.get(num))
            except ValueError:
                find_all_indices(num, a).index(t.get(num))

            self.assertFalse(has_duplicates(t.keys))

    def test_put_and_get_1(self):
        """Testing that errors are raised."""
        t = HashTable()
        self.assertRaises(TypeError, t.put, None, 12)
        self.assertRaises(TypeError, t.get, None)

    def test_put_and_get_2(self, n=100):
        """Testing that the same elements inserted
        multiple times in the same order,
        but always with different values associated with them."""
        t = HashTable()
        ls = list(string.ascii_lowercase)

        for i in range(1, n + 1):

            for j, letter in enumerate(ls):

                if i == 1:
                    self.assertIsNone(t.get(letter))
                else:
                    self.assertEqual(t.get(letter), (i - 1) + j)

                t.put(letter, i + j)

            self.assertEqual(t.size, len(ls))
            self.assertFalse(has_duplicates(t.keys))

        for i, letter in enumerate(ls):
            self.assertEqual(t.get(letter), ls.index(letter) + n)
            self.assertEqual(t.size, len(ls))
            self.assertFalse(has_duplicates(t.keys))

    def test_put_and_get_3(self, n=100):
        """Testing insertion of permutations of the same items
        and possibly different values associated with them."""
        t = HashTable()
        a = list(string.printable)

        p = None
        a = sample(a, len(a))

        for i in range(1, n + 1):

            for j, letter in enumerate(a):

                if i == 1:
                    self.assertIsNone(t.get(letter))
                    self.assertIsNone(p)
                else:
                    self.assertIsNotNone(p)
                    self.assertEqual(t.get(letter), (i - 1) + p.index(letter))

                t.put(letter, i + j)

            p = a
            a = sample(a, len(a))

            self.assertEqual(t.size, len(a))
            self.assertFalse(has_duplicates(t.keys))

        for i, letter in enumerate(a):
            self.assertEqual(t.get(letter), p.index(letter) + n)
            self.assertEqual(t.size, len(a))
            self.assertFalse(has_duplicates(t.keys))

    def test_put_and_get_ints(self):
        self.put_and_get_numbers()

    def test_put_and_get_floats(self):
        self.put_and_get_numbers(uniform)

    def test_put_and_get_strings(self, n=100):
        """Test adding different permutations of a list of the same strings."""
        t = HashTable()
        a = [gen_rand_str(10) for _ in range(100)]
        p = None

        for i in range(1, n + 1):

            for j, s in enumerate(a):

                if i == 1:
                    self.assertIsNone(t.get(s))
                    self.assertIsNone(p)
                else:
                    self.assertIsNotNone(p)
                    self.assertEqual(t.get(s), (i - 1) + p.index(s))

                t.put(s, i + j)

            p = a
            a = sample(a, len(a))

            self.assertEqual(t.size, len(a))
            self.assertFalse(has_duplicates(t.keys))

        for i, s in enumerate(a):
            self.assertEqual(t.get(s), p.index(s) + n)
            self.assertEqual(t.size, len(a))
            self.assertFalse(has_duplicates(t.keys))

    def test_put_and_get_non_hashable_type(self):
        t = HashTable()

        self.assertRaises(TypeError, t.put, [], 12)
        self.assertRaises(TypeError, t.put, {}, 12)

        t.put(1, "Number 1")

        self.assertRaises(TypeError, t.get, [])
        self.assertRaises(TypeError, t.get, {})

    def test_delete_letters(self, n=100):
        t = HashTable()
        ls = list(string.ascii_lowercase)

        for i in range(1, n + 1):

            for j, letter in enumerate(ls):
                if i == 1:
                    self.assertIsNone(t[letter])
                else:
                    self.assertEqual(t[letter], (i - 1) + j)
                t[letter] = i + j

            self.assertEqual(t.size, len(ls))
            self.assertFalse(has_duplicates(t.keys))

        for i, letter in enumerate(ls):
            self.assertEqual(t[letter], ls.index(letter) + n)
            self.assertEqual(t.size, len(ls))
            self.assertFalse(has_duplicates(t.keys))

        for i, letter in enumerate(ls):
            v = t.delete(letter)
            self.assertIsNotNone(v)
            self.assertFalse(has_duplicates(t.keys))
            self.assertEqual(t.size, len(ls) - (i + 1))

        self.assertEqual(t.size, 0)
        self.assertFalse(has_duplicates(t.keys))

    def test_empty_hash_table_capacity(self):
        h = HashTable()

        self.assertEqual(h.capacity, 11)
        self.assertEqual(h.size, 0)

        for i in range(99):
            h = HashTable(capacity=i)
            self.assertEqual(h.capacity, i)
            self.assertEqual(h.size, 0)
