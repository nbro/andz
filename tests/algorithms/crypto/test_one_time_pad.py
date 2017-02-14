#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 01/01/2017

# Description

Testing the one_time_pad algorithm.
"""

import unittest
from random import randint

from ands.algorithms.crypto.one_time_pad import *
from tests.algorithms.crypto.util import *


class TestOneTimePad(unittest.TestCase):
    def template_test(self, n, m):
        """m is the size of the string and key.
        n is the number of iterations."""
        for _ in range(n):
            message = gen_rand_message(m)
            key = gen_key(m)
            cipher_text = encrypt(message, key)
            original = decrypt(cipher_text, key)
            self.assertEqual(original, message)

    def test_empty_message(self):
        self.template_test(1000, 0)

    def test_size_1(self):
        self.template_test(1000, 1)

    def test_size_greater_than_1(self):
        self.template_test(1000, 100)

    def test_random_size(self):
        it = randint(3, 11)
        size = randint(10, 1000)
        self.template_test(it, size)
