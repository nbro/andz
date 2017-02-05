#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado
Created: 14/02/2016
Updated: 05/02/2017

# Description

Tests for the abstract class BinaryHeap.
"""

import unittest

from ands.ds.heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):
    def test_heap_creation(self):
        self.assertRaises(NotImplementedError, BinaryHeap, [12, 14, 28])
        self.assertIsNotNone(BinaryHeap())
        self.assertEqual(BinaryHeap().heap, [])
        self.assertEqual(BinaryHeap([]).heap, [])
