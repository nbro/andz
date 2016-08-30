#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Tests for the caesar cipher algorithms.
"""

import unittest

from ands.algorithms.crypto.caesar import *
from tests.algorithms.crypto.util import *


class TestCaesarCipher(unittest.TestCase):

    def __init__(self, method_name="runTest"):
        unittest.TestCase.__init__(self, method_name)

    def template_test1(self, n, size):
        for _ in range(n):
            m = gen_rand_message(size)
            key = random.randint(1, MAX - find_max(m))
            cipher = encrypt(m, key)
            o = decrypt(cipher, key)
            self.assertEqual(m, o)

    def template_test2(self, n, size, total_keys):
        for _ in range(n):
            m = gen_rand_message(size)
            keys = gen_rand_keys(total_keys, 1, MAX - find_max(m))
            cipher, pattern = multi_encrypt(m, keys)
            o = multi_decrypt(cipher, pattern)
            self.assertEqual(m, o)

    def test_empty_message(self):
        for i in range(100):
            m = ""
            cipher = encrypt(m, i)
            o = decrypt(cipher, i)
            self.assertEqual(m, o)

    def test_encrypt_and_decrypt(self):
        self.template_test1(5, 1)
        self.template_test1(5, 1000000)
        self.template_test1(10, 100000)
        self.template_test1(15, 10000)
        self.template_test1(20, 1000)
        self.template_test1(25, 100)
        self.template_test1(30, 10)

    def test_multi_encrypt_decrypt(self):
        self.template_test2(10, 10, 1)  # Equivalent to Caesar because we just 1 key
        self.template_test2(10, 100000, 5)
        self.template_test2(5, 100000, 10)
        self.template_test2(10, 100000, 15)
        self.template_test2(15, 100000, 10)
        self.template_test2(15, 100000, 20)
        self.template_test2(20, 100000, 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
