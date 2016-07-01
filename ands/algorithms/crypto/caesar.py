#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Caesar cipher that accepts messages of characters
whose value returned by the `ord` function is between 0 and 2**16 - 1.
Caeser cipher is far from being a good cryptographic algorithm,
so, in general, you should prefer other algorithms.
"""

import string
import random


def move_char(c, k):
    return chr(ord(c) + k)


def encrypt(m, k):
    return "".join(move_char(c, k) for c in m)


def decrypt(cipher, k):
    return "".join(move_char(c, -k) for c in cipher)


# Example of polyalphabetic encryption

def multi_encrypt(m, keys):
    """Given a message m and a set of keys,
    it encrypts each symbol of m with a random key from keys.
    The random pattern is the second item of the tuple returned."""
    pattern = []
    cipher = []

    for c in m:
        k = random.choice(keys)
        pattern.append(k)
        cipher.append(move_char(c, k))

    return "".join(cipher), pattern


def multi_decrypt(cipher, pattern):
    """`len(pattern) == len(keys)`,
    where `keys` are the keys passed to `multi_encrypt`."""
    return "".join(move_char(cipher[i], -k) for i, k in enumerate(pattern))


def gen_rand_message(size):
    return "".join(random.choice(string.printable) for _ in range(size))


def find_max(m):
    return max(ord(c) for c in m)


# Using `sys.maxunicode` causes some problems with encondings
# i.e. an error is thrown because Tcl/Tk do not support certain characters
MAX = 2**16 - 1


def test1(n, size):
    for _ in range(n):
        m = gen_rand_message(size)
        # print("Message:", m)

        key = random.randint(1, MAX - find_max(m))
        # print("Key:", key)

        cipher = encrypt(m, key)
        # print("Cipher:", repr(cipher))

        o = decrypt(cipher, key)
        # print("Original:", o)

        assert m == o

    print("Test of size", n, "with message size =", size, "finished.")


def gen_rand_keys(size, _min, _max):
    return [random.randint(_min, _max) for _ in range(size)]


def test2(n, size, total_keys):
    for _ in range(n):
        m = gen_rand_message(size)
        # print("Message:", m)

        keys = gen_rand_keys(total_keys, 1, MAX - find_max(m))
        # print("Keys:", keys)

        cipher, pattern = multi_encrypt(m, keys)
        # print("Cipher:", repr(cipher))
        # print("Pattern:", pattern)

        o = multi_decrypt(cipher, pattern)
        # print("Original:", o)

        assert m == o

    print(
        "Test of size",
        n,
        "with message size =",
        size,
        "and with",
        total_keys,
        "keys finished.")


if __name__ == "__main__":
    # Testing the Caesar cipher
    test1(5, 1)
    test1(5, 1000000)
    test1(10, 100000)
    test1(15, 10000)
    test1(20, 1000)
    test1(25, 100)
    test1(30, 10)

    # Testing the polyalphabetic cryptographic algorithm
    test2(10, 10, 1)  # Equivalent to Caesar because we just 1 key
    test2(10, 100000, 5)
    test2(5, 100000, 10)
    test2(10, 100000, 15)
    test2(15, 100000, 10)
    test2(15, 100000, 20)
    test2(20, 100000, 15)
