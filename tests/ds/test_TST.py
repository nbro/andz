#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 29/01/2017

Updated: 12/03/2017

# Description

Unit tests for the TST and _TSTNode classes.

In these tests I only test the count method instead of testing also size and _n,
this is because `count` asserts its result is equal to the result returned by size, which is _n.
"""

import random
import string
import unittest

from ands.ds.TST import TST, _TSTNode


class TestTST(unittest.TestCase):
    @staticmethod
    def gen_rand_str(n):
        """Generates a string of size n of printable characters."""
        return "".join(random.choice(string.ascii_letters) for _ in range(n))

    def test_creation(self):
        t = TST()
        self.assertTrue(t.is_empty())
        self.assertEqual(t.count(), 0)

    def test_insert_key_not_string(self):
        t = TST()
        self.assertRaises(TypeError, t.insert, 10, 5)

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
            key = TestTST.gen_rand_str(random.randint(1, 11))
            random_pairs[key] = key
            t.insert(key, key)

            self.assertFalse(t.is_empty())
            self.assertEqual(t.count(), len(random_pairs))

        for k, v in random_pairs.items():
            self.assertEqual(t.search(k), v)
            self.assertTrue(t.contains(k))

    # Testing search and contains_key in the "bad" cases (of inputs)

    def test_search_empty_tst(self):
        t = TST()
        self.assertIsNone(t.search("search in an empty tst"))
        self.assertIsNone(t.search_iteratively("search in an empty tst"))

    def test_search_key_not_string(self):
        t = TST()
        self.assertRaises(TypeError, t.search, 5)
        self.assertRaises(TypeError, t.search_iteratively, 5)

    def test_search_key_empty_string(self):
        t = TST()
        self.assertRaises(ValueError, t.search, "")
        self.assertRaises(ValueError, t.search_iteratively, "")

    def test_contains_key_not_string(self):
        t = TST()
        self.assertRaises(TypeError, t.contains, 3.14)

    def test_contains_empty_tst(self):
        t = TST()
        self.assertFalse(t.contains("contains in an empty tst"))

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

        n = random.randint(3, 2000)
        random_pairs = {}

        for _ in range(n):
            key = TestTST.gen_rand_str(random.randint(1, 11))
            random_pairs[key] = key
            t.insert(key, key)

        for k, v in random_pairs.items():
            self.assertEqual(t.delete(k), v)
            self.assertIsNone(t.search(k))
            self.assertFalse(t.contains(k))

        self.assertTrue(t.is_empty())
        self.assertEqual(t.count(), 0)

    # TODO: test_insert_delete_some_insert_delete_all

    def test_keys_with_prefix_not_str_prefix(self):
        t = TST()
        self.assertRaises(TypeError, t.keys_with_prefix, 3)

    def test_keys_with_prefix_empty_prefix(self):
        t = TST()

        n = random.randint(1, 50)
        keys = set()

        for _ in range(n):
            key = TestTST.gen_rand_str(random.randint(1, 11))
            keys.add(key)
            t.insert(key, key)

        kwp = t.keys_with_prefix("")
        kwp_set = set(kwp)
        self.assertEqual(len(kwp), len(kwp_set))  # I should not need to check this here!!!
        self.assertEqual(kwp_set, keys)

    def test_keys_with_prefix_none_found(self):
        t = TST()
        t.insert("one", 1)
        t.insert("two", 2)
        t.insert("three", 3)
        self.assertEqual(t.keys_with_prefix("four"), [])

    def test_keys_with_prefix_prefix_size_equal_to_key_size(self):
        t = TST()
        t.insert("valete", "dama")
        self.assertEqual(t.keys_with_prefix("valete"), ["valete"])

    def test_keys_with_prefix_one_found(self):
        t = TST()
        t.insert("one", 1)
        t.insert("two", 2)
        t.insert("three", 3)
        self.assertEqual(t.keys_with_prefix("on"), ["one"])

    def test_keys_with_prefix_two_found(self):
        t = TST()
        t.insert("one", 1)
        t.insert("two", 2)
        t.delete("one")
        t.insert("three", 3)
        self.assertEqual(sorted(t.keys_with_prefix("t")), ["three", "two"])

    def test_keys_with_prefix_all_found(self):
        t = TST()
        t.insert("occasion", 2)
        t.insert("occasionally", 2)
        t.insert("occam", 2)
        self.assertEqual(sorted(t.keys_with_prefix("occa")), ["occam", "occasion", "occasionally"])

    def test_all_pairs_empty_tst(self):
        t = TST()
        self.assertEqual(t.all_pairs(), {})

    def test_all_pairs_tst_size_1(self):
        t = TST()
        t.insert("the most sadistic", "necro")
        self.assertEqual(t.all_pairs(), {"the most sadistic": "necro"})

    def test_all_pairs_random_size_and_strings(self):
        t = TST()

        n = random.randint(3, 1000)
        random_pairs = {}

        for _ in range(n):
            key = TestTST.gen_rand_str(random.randint(1, 17))
            random_pairs[key] = key
            t.insert(key, key)

        self.assertEqual(t.all_pairs(), random_pairs)

    def test_longest_prefix_of_query_not_str(self):
        t = TST()
        self.assertRaises(TypeError, t.longest_prefix_of, -0.12)

    def test_longest_prefix_of_query_empty(self):
        t = TST()
        self.assertRaises(ValueError, t.longest_prefix_of, "")

    def test_longest_prefix_of_empty_tst(self):
        t = TST()
        self.assertEqual(t.longest_prefix_of(TestTST.gen_rand_str(10)), "")

    def test_longest_prefix_of_longest_prefix_size_zero(self):
        t = TST()
        t.insert("obnoxious", 7)
        # obnoxious is NOT even a prefix of over
        self.assertEqual(t.longest_prefix_of("over"), "")

    def test_longest_prefix_of_longest_prefix_size_one(self):
        t = TST()
        t.insert("o", 7)
        t.insert("obnoxious", 23)
        self.assertEqual(t.longest_prefix_of("overall"), "o")

    def test_longest_prefix_of_longest_prefix_size_two(self):
        t = TST()
        t.insert("p", 7)
        t.insert("oa", 23)
        self.assertEqual(t.longest_prefix_of("oak"), "oa")

    def test_longest_prefix_of_longest_prefix_size_of_query(self):
        t = TST()
        t.insert("allen", "first")
        t.insert("allen halloween", "underrated!")
        self.assertEqual(t.longest_prefix_of("allen halloween"), "allen halloween")

    def test_keys_that_match_pattern_not_str(self):
        t = TST()
        self.assertRaises(TypeError, t.keys_that_match, 1 / 2)

    def test_keys_that_match_pattern_empty_str(self):
        t = TST()
        self.assertRaises(ValueError, t.keys_that_match, "")

    def test_keys_that_match_tst_empty_pattern_one_dot(self):
        t = TST()
        self.assertEqual(t.keys_that_match("."), [])

    def test_keys_that_match_tst_empty_pattern_many_dots(self):
        t = TST()
        self.assertEqual(t.keys_that_match("......."), [])

    def test_keys_that_match_pattern_no_dots(self):
        t = TST()
        t.insert("one", 1)
        t.insert("on", "fire")
        self.assertEqual(t.keys_that_match("on"), ["on"])

    def test_keys_that_match_example_docs(self):
        t = TST()
        t.insert("food", 3)
        t.insert("good", 3)
        t.insert("foodie", 3)
        self.assertEqual(sorted(t.keys_that_match(".ood")), ["food", "good"])

    def test_keys_that_match_pattern_using_dots(self):
        t = TST()
        t.insert("nop", 0)
        t.insert("one", 1)
        t.insert("on", "fire")
        t.insert("fno", "ok")
        self.assertEqual(sorted(t.keys_that_match(".n.")), ["fno", "one"])

    def test_keys_that_match_pattern_using_dots_to_retrieve_all_keys_of_certain_length(self):
        t = TST()
        t.insert("zero", 0)
        t.insert("one", 1)
        t.insert("two", 2)
        t.insert("three", 3)
        t.insert("four", 4)
        t.insert("five", 5)
        t.insert("six", 6)
        self.assertEqual(sorted(t.keys_that_match("...")), ["one", "six", "two"])
        self.assertEqual(sorted(t.keys_that_match("....")), ["five", "four", "zero"])
        self.assertEqual(sorted(t.keys_that_match(".....")), ["three"])


class TestTSTNode(unittest.TestCase):
    def test_create_key_not_string(self):
        self.assertRaises(TypeError, _TSTNode, 13)

    def test_create_key_empty_string(self):
        self.assertRaises(ValueError, _TSTNode, "")

    def test_create_acceptable_key(self):
        self.assertIsInstance(_TSTNode("unit testing"), _TSTNode)

    def test_create_default(self):
        u = _TSTNode("default values")
        self.assertEqual(u.key, "default values")
        self.assertIsNone(u.value)
        self.assertIsNone(u.parent)
        self.assertIsNone(u.mid)
        self.assertIsNone(u.left)
        self.assertIsNone(u.right)

    def test_create_custom(self):
        p = _TSTNode("parent")
        left = _TSTNode("left")
        mid = _TSTNode("mid")
        right = _TSTNode("right")
        u = _TSTNode("u", 11, p, left, mid, right)
        self.assertEqual(u.value, 11)
        self.assertIs(u.parent, p)
        self.assertIs(u.left, left)
        self.assertIs(u.mid, mid)
        self.assertIs(u.right, right)

    def test_is_left_child_no_parent(self):
        u = _TSTNode("u")
        self.assertRaises(AttributeError, u.is_left_child)

    def test_is_left_child_false(self):
        p = _TSTNode("p")
        u = _TSTNode("u", 3, p)
        self.assertFalse(u.is_left_child())

    def test_is_left_child_true(self):
        p = _TSTNode("p")
        u = _TSTNode("u", 3, p)
        p.left = u
        self.assertTrue(u.is_left_child())

    def test_is_right_child_no_parent(self):
        u = _TSTNode("u")
        self.assertRaises(AttributeError, u.is_right_child)

    def test_is_right_child_false(self):
        p = _TSTNode("p")
        u = _TSTNode("u", 3, p)
        self.assertFalse(u.is_right_child())

    def test_is_right_child_true(self):
        p = _TSTNode("p")
        u = _TSTNode("u", 3, p)
        p.right = u
        self.assertTrue(u.is_right_child())

    def test_is_mid_child_no_parent(self):
        u = _TSTNode("u")
        self.assertRaises(AttributeError, u.is_mid_child)

    def test_is_mid_child_false(self):
        p = _TSTNode("p")
        u = _TSTNode("u", 3, p)
        self.assertFalse(u.is_mid_child())

    def test_is_mid_child_true(self):
        p = _TSTNode("p")
        u = _TSTNode("u", 3, p)
        p.mid = u
        self.assertTrue(u.is_mid_child())

    def test_has_children_0(self):
        u = _TSTNode("u")
        self.assertFalse(u.has_children())

    def test_has_children_1(self):
        u = _TSTNode("u", right=_TSTNode("right"))
        self.assertTrue(u.has_children())

    def test_has_children_2(self):
        u = _TSTNode("u", mid=_TSTNode("mid"), left=_TSTNode("left"))
        self.assertTrue(u.has_children())

    def test_has_children_3(self):
        u = _TSTNode("u", mid=_TSTNode("mid"), left=_TSTNode("left"), right=_TSTNode("right"))
        self.assertTrue(u.has_children())