#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

One Time Pad cipher algorithm, which provides 'perfect secrecy',
but has some drawbacks, for example the key used
must be at least of the same length of the original message.
"""


def encrypt(message, key):
    """Encrypt message using key according to the one-time-pad algorithm."""
    return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(message, key))


def decrypt(ciphertext, key):
    """Decript ciphertext using key according to the OTP algorithm."""
    return encrypt(ciphertext, key)
