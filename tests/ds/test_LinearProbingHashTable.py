#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 21/02/2016

Updated: 19/02/2017

# Description

Unit tests for the LinearProbingHashTable class.

# Reference

- https://stackoverflow.com/q/9755538/3924118

"""

import string
import unittest
from random import sample, randint, choice, shuffle

from ands.ds.LinearProbingHashTable import LinearProbingHashTable, \
    has_duplicates_ignore_nones


def gen_rand_list_of_distinct_ascii_and_numbers() -> list:
    n = randint(1, 1000)
    ls = list(string.ascii_lowercase) + sample(range(n), n)
    shuffle(ls)
    return ls


class TestHasDuplicatesIgnoreNones(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(has_duplicates_ignore_nones([]))

    def test_list_size_1_no_None(self):
        self.assertFalse(has_duplicates_ignore_nones([3]))

    def test_list_size_1_None(self):
        self.assertFalse(has_duplicates_ignore_nones([None]))

    def test_list_size_2_no_None_no_duplicate(self):
        self.assertFalse(has_duplicates_ignore_nones([3, 5]))

    def test_list_size_2_no_None_with_duplicates(self):
        self.assertTrue(has_duplicates_ignore_nones([5, 5]))

    def test_list_size_2_with_None_no_duplicate(self):
        self.assertFalse(has_duplicates_ignore_nones([None, 5]))

    def test_list_size_2_both_None(self):
        self.assertFalse(has_duplicates_ignore_nones([None, None]))

    def test_list_size_n_all_None(self):
        self.assertFalse(has_duplicates_ignore_nones([None] * randint(3, 100)))

    def test_list_size_n_no_None_no_duplicate(self):
        self.assertFalse(has_duplicates_ignore_nones(sample(range(100), 100)))

    def test_list_has_duplicates_on_bounds(self):
        self.assertTrue(has_duplicates_ignore_nones([3, 12, 4, 6, 3]))

    def test_list_has_duplicates_not_on_bounds(self):
        self.assertTrue(has_duplicates_ignore_nones([3, 12, 3, 6, 17]))


class TestLinearProbingHashTable(unittest.TestCase):
    def test_create_capacity_not_int(self):
        self.assertRaises(TypeError, LinearProbingHashTable, 3.14)
        self.assertRaises(TypeError, LinearProbingHashTable, "not at int")

    def test_create_capacity_less_than_1(self):
        self.assertRaises(ValueError, LinearProbingHashTable, 0)
        self.assertRaises(ValueError, LinearProbingHashTable, -1)

    def test_create_set_initial_capacity(self):
        t = LinearProbingHashTable(9)
        self.assertEqual(t.capacity, 9)
        self.assertEqual(t.size, 0)

    def test_create_capacity_int(self):
        t = LinearProbingHashTable()
        self.assertEqual(t.size, 0)

    def test_get_key_None(self):
        t = LinearProbingHashTable()
        self.assertRaises(TypeError, t.get, None)

    def test_get_non_hashable_type(self):
        t = LinearProbingHashTable()
        t.put(23, 31)
        t.put(11, 13)
        self.assertRaises(TypeError, t.get, [])
        self.assertRaises(TypeError, t.get, {})

    def test_get_empty_table(self):
        t = LinearProbingHashTable()
        self.assertIsNone(t.get(3))

    def test_get_with_syntactic_sugar(self):
        t = LinearProbingHashTable()
        t.put(5, 12)
        self.assertEqual(t[5], 12)

    def test_get_no_key_found(self):
        t = LinearProbingHashTable()
        t.put("three", 3)
        t["four"] = 4
        self.assertIsNone(t.get("five"))

    def test_get_all(self):
        t = LinearProbingHashTable()

        ls = gen_rand_list_of_distinct_ascii_and_numbers()

        for elem in ls:
            t.put(elem, 13)

        for elem in reversed(ls):
            self.assertEqual(t.get(elem), 13)

    def test_put_key_None(self):
        t = LinearProbingHashTable()
        self.assertRaises(TypeError, t.put, None, 5)

    def test_put_non_hashable_type(self):
        t = LinearProbingHashTable()
        self.assertRaises(TypeError, t.put, [], 12)
        self.assertRaises(TypeError, t.put, {}, None)

    def test_put_key_not_None_value_None(self):
        t = LinearProbingHashTable()
        t.put(3, None)
        self.assertTrue(t.size, 1)
        self.assertIsNone(t.get(3))

    def test_put_key_not_None_value_not_None(self):
        t = LinearProbingHashTable()
        t.put(5, 19)
        self.assertTrue(t.size, 1)
        self.assertEqual(t.get(5), 19)

    def test_put_same_key_multiple_times(self):
        t = LinearProbingHashTable()
        t.put(3, "three")
        t.put(5, 6)
        t.put(3, 3)
        t.put(3, "three")
        self.assertEqual(t.size, 2)
        self.assertEqual(t.get(3), "three")

    def test_put_n_distinct_keys_equal_values(self):
        t = LinearProbingHashTable()

        n = randint(2, 1000)
        population = sample(range(n), n)

        for elem in population:
            t.put(elem, elem)

        self.assertEqual(t.size, n)

        for elem in population:
            self.assertIsNotNone(t.get(elem))

    def test_put_n_distinct_keys_all_values_different(self):
        """Testing that the same elements inserted
        multiple times in the same order,
        but always with different values associated with them."""
        t = LinearProbingHashTable()

        ls = gen_rand_list_of_distinct_ascii_and_numbers()
        n = len(ls)

        for val, key in enumerate(ls):
            t.put(key, val)

        self.assertEqual(t.size, n)
        for elem in ls:
            self.assertIsNotNone(t.get(elem))

    def test_delete_key_None(self):
        t = LinearProbingHashTable()
        self.assertRaises(TypeError, t.delete, None)

    def test_delete_non_hashable_type(self):
        t = LinearProbingHashTable()
        self.assertRaises(TypeError, t.delete, [])
        self.assertRaises(TypeError, t.delete, {})

    def test_delete_empty_table(self):
        t = LinearProbingHashTable()
        self.assertIsNone(t.delete(3))

    def test_delete_key_not_present(self):
        t = LinearProbingHashTable()
        t.put(-10, "testing deletion when key not in the table")
        self.assertIsNone(t.delete(7))

    def test_delete_some(self):
        t = LinearProbingHashTable()
        ls = [(1, 3), (5, "two"), (2.72, 10), ("one", 3.14), (1, "seven")]

        for k, v in ls:
            t.put(k, v)

        self.assertEqual(t.size, 4)
        self.assertEqual(t.delete(1), "seven")
        self.assertEqual(t.delete(2.72), 10)
        self.assertEqual(t.size, 2)

    def test_delete_all(self):
        t = LinearProbingHashTable()
        ls = gen_rand_list_of_distinct_ascii_and_numbers()
        for elem in ls:
            t.put(elem, elem)

        self.assertEqual(t.size, len(ls))

        for key in ls:
            self.assertEqual(t.delete(key), key)

        self.assertEqual(t.size, 0)

    def test_show(self):
        t = LinearProbingHashTable()
        ls = sample(range(3), 3)
        for elem in ls:
            t.put(elem, choice(string.ascii_letters))
        print()
        t.show()
