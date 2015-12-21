#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 24/01/2017

Updated: 12/03/2017

# Description

Unit tests for the classes and functions in the ands.ds.Queue module.
"""

import unittest
from random import randint

from ands.ds.Queue import Queue


class TestQueue(unittest.TestCase):
    """Size and is_empty are somehow tested implicitly."""

    def test_creation(self):
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_creation_explicit_None(self):
        q = Queue(None)
        self.assertTrue(q.is_empty())

    def test_creation_not_iterable(self):
        self.assertRaises(TypeError, Queue, 13)

    def test_creation_good_list_empty(self):
        q = Queue([])
        self.assertTrue(q.is_empty())

    def test_creation_good_list_size_1(self):
        q = Queue([3])
        self.assertEqual(q.size, 1)

    def test_creation_list_with_None(self):
        self.assertRaises(ValueError, Queue, [31, None, 2, 3])

    def test_creation_good_list_random_size(self):
        r = randint(2, 50)
        q = Queue([randint(-10, 10) for _ in range(r)])
        self.assertEqual(q.size, r)

    def test_enqueue_one(self):
        q = Queue()
        q.enqueue("first")
        self.assertEqual(q.size, 1)

    def test_enqueue_None(self):
        q = Queue([93, 97])
        self.assertRaises(ValueError, q.enqueue, None)

    def test_enqueue_many(self):
        q = Queue()

        r = randint(2, 100)
        ls = [randint(-100, 100) for _ in range(r)]

        for i, elem in enumerate(ls):
            q.enqueue(elem)
            self.assertEqual(q.size, i + 1)

    def test_dequeue_empty(self):
        q = Queue()
        self.assertIsNone(q.dequeue())

    def test_dequeue_one(self):
        q = Queue(["one"])
        self.assertEqual(q.dequeue(), "one")
        self.assertTrue(q.is_empty())

    def test_dequeue_many(self):
        ls = [2, 3, 5, 7, 11, 13]
        q = Queue(ls)

        for i, _ in enumerate(ls):
            elem = q.dequeue()
            self.assertEqual(elem, ls[i])

        self.assertTrue(q.is_empty())
