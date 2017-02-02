#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado
Created: 29/01/2017
Updated: 02/02/2017

# Description

Unit tests for the TST class.

In these tests I only test the count method instead of testing also size and _n,
this is because `count` asserts its result is equal to the result returned by size, which is _n.
"""

import random
import string
import unittest

from ands.ds.TST import TST


class TestTST(unittest.TestCase):
    def gen_rand_str(self, n):
        """Generates a string of size n of printable characters."""
        return "".join(random.choice(string.ascii_letters) for _ in range(n))

    def test_creation(self):
        t = TST()
        self.assertTrue(t.is_empty())
        self.assertEqual(t.count(), 0)

    def test_insert_key_not_string(self):
        t = TST()
        self.assertRaises(TypeError, t.insert, 5)

    def test_insert_key_empty_string(self):
        t = TST()
        self.assertRaises(ValueError, t.insert, "", 2)

    def test_insert_none_value(self):
        t = TST()
        self.assertRaises(ValueError, t.insert, "key", None)

    def test_insert_one(self):
        t = TST()
        t.insert("one", 97)
        self.assertFalse(t.is_empty())
        self.assertEqual(t.count(), 1)
        self.assertEqual(t.search("one"), 97)
        self.assertTrue(t.contains("one"))

    def test_insert_two(self):
        t = TST()
        t.insert("he", 0)
        t.insert("she", 1)
        self.assertFalse(t.is_empty())
        self.assertEqual(t.count(), 2)
        self.assertEqual(t.search("he"), 0)
        self.assertEqual(t.search("she"), 1)
        self.assertTrue(t.contains("he"))
        self.assertTrue(t.contains("she"))

    def test_insert_same_twice_to_update(self):
        t = TST()
        t.insert("seven", 7)
        t.insert("fly away", 11)
        t.insert("fly away", 101)
        t.insert("bandit queen", "Looptroop")
        self.assertFalse(t.is_empty())
        self.assertEqual(t.count(), 3)
        self.assertEqual(t.search("seven"), 7)
        self.assertEqual(t.search("fly away"), 101)
        self.assertEqual(t.search("bandit queen"), "Looptroop")
        self.assertTrue(t.contains("seven"))
        self.assertTrue(t.contains("fly away"))
        self.assertTrue(t.contains("bandit queen"))

    def test_insert_random_keys(self):
        t = TST()

        n = random.randint(4, 100)
        random_pairs = {}

        for _ in range(n):
            key = self.gen_rand_str(random.randint(1, 11))
            random_pairs[key] = key
            t.insert(key, key)

            self.assertFalse(t.is_empty())
            self.assertEqual(t.count(), len(random_pairs))

        for k, v in random_pairs.items():
            self.assertEqual(t.search(k), v)
            self.assertTrue(t.contains(k))

    # Testing search and contains in the "bad" cases (of inputs)

    def test_search_empty_tst(self):
        t = TST()
        self.assertIsNone(t.search("search in an empty tst"))

    def test_search_key_not_string(self):
        t = TST()
        self.assertRaises(TypeError, t.search, 5)

    def test_search_key_empty_string(self):
        t = TST()
        self.assertRaises(ValueError, t.search, "")

    def test_contains_empty_tst(self):
        t = TST()
        self.assertFalse(t.contains("contains in an empty tst"))

    def test_contains_key_not_string(self):
        t = TST()
        self.assertRaises(TypeError, t.contains, 3.14)

    def test_contains_key_empty_string(self):
        t = TST()
        self.assertRaises(ValueError, t.contains, "")

    def test_traverse_tst(self):
        t = TST()
        t.insert("one", 1)
        t.insert("two", 2)
        t.insert("three", 3)
        self.assertIsNone(t.traverse())

    def test_delete_empty_tst(self):
        t = TST()
        self.assertIsNone(t.delete("war"))

    def test_delete_key_not_string(self):
        t = TST()
        self.assertRaises(TypeError, t.delete, 0.1)

    def test_delete_key_empty_string(self):
        t = TST()
        self.assertRaises(ValueError, t.delete, "")

    def test_delete_inexistent_key(self):
        t = TST()
        t.insert("first", "1st")

        self.assertIsNone(t.delete("second"))
        self.assertFalse(t.is_empty())
        self.assertEqual(t.count(), 1)
        self.assertTrue(t.contains("first"))
        self.assertEqual(t.search("first"), "1st")

    def test_delete_same_key_twice(self):
        t = TST()
        t.insert("one", 1)
        t.insert("two", 2)
        t.insert("three", 3)

        self.assertEqual(t.delete("three"), 3)
        self.assertIsNone(t.delete("three"))
        self.assertFalse(t.is_empty())
        self.assertEqual(t.count(), 2)
        self.assertTrue(t.contains("one"))
        self.assertTrue(t.contains("two"))
        self.assertEqual(t.search("one"), 1)
        self.assertEqual(t.search("two"), 2)

    def test_delete_the_only_key(self):
        t = TST()
        t.insert("seven", 7)

        self.assertEqual(t.delete("seven"), 7)
        self.assertTrue(t.is_empty())
        self.assertEqual(t.count(), 0)
        self.assertFalse(t.contains("seven"))
        self.assertIsNone(t.search("seven"))

    def test_delete_the_two_keys(self):
        t = TST()
        t.insert("one", 1)
        t.insert("two", 2)

        self.assertEqual(t.delete("one"), 1)
        self.assertFalse(t.is_empty())
        self.assertEqual(t.count(), 1)
        self.assertFalse(t.contains("one"))
        self.assertTrue(t.contains("two"))
        self.assertIsNone(t.search("one"))
        self.assertEqual(t.search("two"), 2)

        self.assertEqual(t.delete("two"), 2)
        self.assertTrue(t.is_empty())
        self.assertEqual(t.count(), 0)
        self.assertFalse(t.contains("one"))
        self.assertFalse(t.contains("two"))
        self.assertIsNone(t.search("one"))
        self.assertIsNone(t.search("two"))

    def test_delete_after_inserting_again(self):
        t = TST()

        t.insert("boo", 0.5)
        t.insert("neg", 1)
        self.assertEqual(t.delete("neg"), 1)

        t.insert("neg", 1)
        self.assertEqual(t.delete("neg"), 1)

        self.assertFalse(t.is_empty())
        self.assertEqual(t.count(), 1)

    def test_delete_all_random_keys(self):
        t = TST()

        n = random.randint(3, 10000)
        random_pairs = {}

        for _ in range(n):
            key = self.gen_rand_str(random.randint(1, 11))
            random_pairs[key] = key
            t.insert(key, key)

        for k, v in random_pairs.items():
            self.assertEqual(t.delete(k), v)
            self.assertIsNone(t.search(k))
            self.assertFalse(t.contains(k))

        self.assertTrue(t.is_empty())
        self.assertEqual(t.count(), 0)
