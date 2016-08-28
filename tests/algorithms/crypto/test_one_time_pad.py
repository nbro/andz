#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Testing the one_time_pad algorithm.
"""

import unittest
from ands.algorithms.crypto.one_time_pad import *
from tests.algorithms.crypto.util import *


class TestOneTimePad(unittest.TestCase):

    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)

    def template_test(self, n, m):
        """m is the size of the string and key"""
        for _ in range(n):
            message = gen_rand_message(m)
            key = gen_key(m)
            ciphertext = encrypt(message, key)
            original = decrypt(ciphertext, key)
            assert original == message

    def test_empty_message(self):
        self.template_test(1000, 0)

    def test_size_1(self):
        self.template_test(1000, 1)

    def test_encrypt_and_decrypt(self):
        self.template_test(1000, 1)
        self.template_test(1000, 5)
        self.template_test(1000, 10)
        self.template_test(10, 100)
        self.template_test(10, 1000)
        self.template_test(5, 10000)
        self.template_test(5, 100000)
        self.template_test(1, 1000000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
