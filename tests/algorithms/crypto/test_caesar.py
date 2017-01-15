#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Tests for the caesar cipher algorithms.
"""

import unittest
from random import randint

from ands.algorithms.crypto.caesar import *
from tests.algorithms.crypto.util import *


class TestCaesarCipher(unittest.TestCase):
    def template_test_one_key(self, n, size):
        """n is the number of iterations.
        size is the size of the message."""
        for _ in range(n):
            m = gen_rand_message(size)
            key = random.randint(1, MAX - find_max(m))
            cipher = encrypt(m, key)
            o = decrypt(cipher, key)
            self.assertEqual(m, o)

    def template_test_multi_keys(self, n, size, total_keys):
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

    def test_encrypt_and_decrypt_size_1(self):
        self.template_test_one_key(1000, 1)

    def test_encrypt_and_decrypt_random_size(self):
        it = randint(3, 13)
        size = randint(10, 1000)
        self.template_test_one_key(it, size)

    def test_multi_encrypt_decrypt_size_one_key(self):
        # Equivalent to Caesar because we just 1 key
        self.template_test_multi_keys(1000, 1, 1)

    def test_multi_encrypt_decrypt_size_random_keys(self):
        keys = randint(3, 7)
        self.template_test_multi_keys(100, 1, keys)

    def test_multi_encrypt_decrypt_random(self):
        """Random number of iterations, random length of message
        and random number of keys."""
        it = randint(3, 13)
        size = randint(10, 1000)
        keys = randint(3, 11)
        self.template_test_multi_keys(100, 1, keys)


if __name__ == "__main__":
    unittest.main(verbosity=2)
