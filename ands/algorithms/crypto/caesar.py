#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Caesar cipher that accepts messages of characters
whose value returned by the `ord` function is between 0 and 2**16 - 1.
Caeser cipher is far from being a good cryptographic algorithm,
so, in general, you should prefer other algorithms.
"""

import random

# Using `sys.maxunicode` causes some problems with encondings
# i.e. an error is thrown because Tcl/Tk do not support certain characters
MAX = 2 ** 16 - 1


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
