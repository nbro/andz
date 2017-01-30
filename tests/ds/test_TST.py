#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado
Created: 29/01/2017
Updated: 30/01/2017

# Description

Unit tests for the TST class.

"""

import random
import string
import unittest

from ands.ds.TST import TST


class TestTST(unittest.TestCase):
    def gen_rand_str(self, n):
        """Generates a string of size n of printable characters."""
        return "".join(random.choice(string.printable) for _ in range(n))

    def test_creation(self):
        t = TST()
        # state guaranteed at creation time
        self.assertEqual(t.count(), 0)
        self.assertTrue(t.is_empty())
        self.assertIsNone(t._root)

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

        # using just count() since count calls size() as a post-condition assertion!!
        self.assertEqual(t.count(), 1)
        self.assertEqual(t.search("one"), 97)

        # Testing the structure of the TST remains as expected.
        r = t._root
        self.assertIsNone(r.left)
        self.assertIsNone(r.right)
        self.assertIsNone(r.parent)
        self.assertIsNotNone(r.mid)
        self.assertEqual(r.key, "o")
        self.assertEqual(r.value, None)

        p = r
        r = r.mid
        self.assertIsNotNone(r)
        self.assertIsNone(r.left)
        self.assertIsNone(r.right)
        self.assertIsNotNone(r.mid)
        self.assertIs(r.parent, p)
        self.assertEqual(r.key, "n")
        self.assertEqual(r.value, None)

        p = r
        r = r.mid
        self.assertIsNotNone(r)
        self.assertIsNone(r.left)
        self.assertIsNone(r.right)
        self.assertIsNone(r.mid)
        self.assertIs(r.parent, p)
        self.assertEqual(r.key, "e")
        self.assertEqual(r.value, 97)

    def test_insert_some_no_update(self):
        """This only tests a permutation of the keys,
        but exhaustive testing is also impossible in most of the cases!
        This example is based on: https://www.youtube.com/watch?v=CIGyewO7868, min. 7.30"""
        t = TST()

        t.insert("she", 2)
        self.assertEqual(t.count(), 1)
        self.assertEqual(t.search("she"), 2)

        t.insert("sells", 3)
        self.assertEqual(t.count(), 2)
        self.assertEqual(t.search("she"), 2)
        self.assertEqual(t.search("sells"), 3)

        t.insert("sea", 5)
        self.assertEqual(t.count(), 3)
        self.assertEqual(t.search("she"), 2)
        self.assertEqual(t.search("sells"), 3)
        self.assertEqual(t.search("sea"), 5)

        t.insert("shells", 7)
        self.assertEqual(t.count(), 4)
        self.assertEqual(t.search("she"), 2)
        self.assertEqual(t.search("sells"), 3)
        self.assertEqual(t.search("sea"), 5)
        self.assertEqual(t.search("shells"), 7)

        t.insert("by", 11)
        self.assertEqual(t.count(), 5)
        self.assertEqual(t.search("she"), 2)
        self.assertEqual(t.search("sells"), 3)
        self.assertEqual(t.search("sea"), 5)
        self.assertEqual(t.search("shells"), 7)
        self.assertEqual(t.search("by"), 11)

        t.insert("the", 13)
        self.assertEqual(t.count(), 6)
        self.assertEqual(t.search("she"), 2)
        self.assertEqual(t.search("sells"), 3)
        self.assertEqual(t.search("sea"), 5)
        self.assertEqual(t.search("shells"), 7)
        self.assertEqual(t.search("by"), 11)
        self.assertEqual(t.search("the"), 13)

    def test_insert_some_with_update(self):
        # Test based on example: This example is based on: https://www.youtube.com/watch?v=CIGyewO7868
        t = TST()
        t.insert("she", 2)
        t.insert("sells", 3)
        t.insert("sea", 5)
        t.insert("shells", 7)
        t.insert("by", 11)
        t.insert("the", 13)

        # Updating value associated with key "sea"
        t.insert("sea", 17)

        self.assertEqual(t.count(), 6)  # The size of the TST should not have changed!
        self.assertEqual(t.search("she"), 2)
        self.assertEqual(t.search("sells"), 3)
        self.assertEqual(t.search("sea"), 17)
        self.assertEqual(t.search("shells"), 7)
        self.assertEqual(t.search("by"), 11)
        self.assertEqual(t.search("the"), 13)

    def test_insert_some_after_update(self):
        # Test based on example: This example is based on: https://www.youtube.com/watch?v=CIGyewO7868
        t = TST()
        t.insert("she", 2)
        t.insert("sells", 3)
        t.insert("sea", 5)
        t.insert("shells", 7)
        t.insert("by", 11)
        t.insert("the", 13)
        t.insert("sea", 17)
        t.insert("shore", 19)

        self.assertEqual(t.count(), 7)  # The size of the TST should not have changed!
        self.assertEqual(t.search("she"), 2)
        self.assertEqual(t.search("sells"), 3)
        self.assertEqual(t.search("sea"), 17)
        self.assertEqual(t.search("shells"), 7)
        self.assertEqual(t.search("by"), 11)
        self.assertEqual(t.search("the"), 13)
        self.assertEqual(t.search("shore"), 19)

    def test_insert_random_keys(self):
        t = TST()

        n = random.randint(10, 100)

        random_pairs = {}

        for _ in range(n):
            str_size = random.randint(1, 11)
            key = self.gen_rand_str(str_size)
            value = random.randint(-100, 100)
            random_pairs[key] = value
            t.insert(key, value)

        self.assertEqual(t.count(), len(random_pairs))

        for k, v in random_pairs.items():
            self.assertEqual(t.search(k), v)
