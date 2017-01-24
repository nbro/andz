#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Author: Nelson Brochado
Created: 24/01/2017
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

    def test_creation_not_list(self):
        self.assertRaises(TypeError, Queue, (13,))

    def test_creation_good_list_empty(self):
        q = Queue([])
        self.assertTrue(q.is_empty())

    def test_creation_good_list_size_1(self):
        q = Queue([3])
        self.assertEqual(q.size(), 1)

    def test_creation_good_list_random_size(self):
        r = randint(2, 50)
        q = Queue([randint(-10, 10) for _ in range(r)])
        self.assertEqual(q.size(), r)

    def test_enqueue_one(self):
        q = Queue()
        q.enqueue("first")
        self.assertEqual(q.size(), 1)

    def test_enqueue_many(self):
        q = Queue()

        r = randint(2, 100)
        ls = [randint(-100, 100) for _ in range(r)]

        for i, elem in enumerate(ls):
            q.enqueue(elem)
            self.assertEqual(q.size(), i + 1)

    def test_dequeue_empty(self):
        q = Queue()
        self.assertIsNone(q.dequeue())

    def test_dequeue_one(self):
        q = Queue(["one"])
        self.assertEqual(q.dequeue(), "one")
        self.assertTrue(q.is_empty())

    def test_dequeue_many(self):

        r = randint(2, 100)
        ls = [randint(-100, 100) for _ in range(r)]

        q = Queue(ls)

        for _ in range(r):
            elem = q.dequeue()
            self.assertIsNotNone(elem)

        self.assertTrue(q.is_empty())

    def test_str(self):
        self.assertEqual(repr(Queue(["first", "second", "last"])), str(["first", "second", "last"]))
