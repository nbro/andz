#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Caesar cipher that accepts messages of characters
whose value returned by the `ord` function is between 0 and 2**16 - 1.
Caeser cipher is far from being a good cryptographic algorithm,
so, in general, you should prefer other algorithms.
"""

import unittest
import string
import random
from ands.algorithms.crypto.caesar import *


def gen_rand_message(size):
    return "".join(random.choice(string.printable) for _ in range(size))


def gen_rand_keys(size, _min, _max):
    return [random.randint(_min, _max) for _ in range(size)]


def find_max(m):
    return max(ord(c) for c in m)


def test1(n, size):
    for _ in range(n):
        m = gen_rand_message(size)
        key = random.randint(1, MAX - find_max(m))
        cipher = encrypt(m, key)
        o = decrypt(cipher, key)
        assert m == o


def test2(n, size, total_keys):
    for _ in range(n):
        m = gen_rand_message(size)
        keys = gen_rand_keys(total_keys, 1, MAX - find_max(m))
        cipher, pattern = multi_encrypt(m, keys)
        o = multi_decrypt(cipher, pattern)
        assert m == o


class TestCaesarCipher(unittest.TestCase):

    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)

    def test_empty_message(self):
        for i in range(100):
            m = ""
            cipher = encrypt(m, i)
            o = decrypt(cipher, i)
            assert m == o

    def test_encrypt_and_decrypt(self):
        test1(5, 1)
        test1(5, 1000000)
        test1(10, 100000)
        test1(15, 10000)
        test1(20, 1000)
        test1(25, 100)
        test1(30, 10)

    def test_multi_encrypt_decrypt(self):
        test2(10, 10, 1)  # Equivalent to Caesar because we just 1 key
        test2(10, 100000, 5)
        test2(5, 100000, 10)
        test2(10, 100000, 15)
        test2(15, 100000, 10)
        test2(15, 100000, 20)
        test2(20, 100000, 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
