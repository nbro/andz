#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

One Time Pad cipher algorithm, which provides 'perfect secrecy',
but has some drawbacks, for example the key used
must be at least of the same length of the original message.
"""

from random import choice
import string


def gen_message(size):
    """Generate a random message of printable characters."""
    return "".join(choice(string.printable) for _ in range(size))


def gen_key(size):
    """Generate a random key of printable characters."""
    return gen_message(size)


def encrypt(message, key):
    """Encrypt message using key according to the one-time-pad algorithm."""
    return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(message, key))


def decrypt(ciphertext, key):
    """Decript ciphertext using key according to the OTP algorithm."""
    return encrypt(ciphertext, key)


def test1(n, m):
    """m is the size of the string and key"""
    for i in range(n):
        message = gen_message(m)
        # print("Message:", message)

        key = gen_key(m)
        # print("Key:", key)

        ciphertext = encrypt(message, key)
        # print("Ciphertext:", ciphertext)

        original = decrypt(ciphertext, key)
        # print("Decoded message:", original)

        assert original == message


if __name__ == "__main__":
    test1(1000, 0)
    test1(1000, 1)
    test1(1000, 5)
    test1(1000, 10)
    test1(10, 100)
    test1(10, 1000)
    test1(5, 10000)
    test1(5, 100000)
    test1(1, 1000000)
    print("Tests finished.")
