#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

One Time Pad cipher algorithm, which provides 'perfect secrecy',
but has some drawbacks, for example the key used
must be at least of the same length of the original message.

The functions below use the module random to generate random keys,
but apparently the functions from the random module do not produce
really random numbers or choices.
"""

from random import choice
import string


def convert_to_bits(s):
    """Converts string s to a string containing only 0s or 1s,
    representing the original string."""
    return "".join(format(ord(x), 'b') for x in s)


def gen_random_key(n):
    """Generates a random key of bits (with 0s or 1s) of length n"""
    k = []
    for i in range(n):
        k.append(choice(["0", "1"]))
    return "".join(k)

def str_xor(m, k):
    """Given strings m and k of characters 0 or 1,
    it returns the string representing the XOR
    between each character in the same position.
    
    m and k should be of the same length.

    Use this function both for encrypting and decrypting."""
    r = []
    for i, j in zip(m, k):
        r.append(str(int(i) ^ int(j)))  # xor between bits i and j
    return "".join(r)


def test1(n, m):
    ls = []
    
    for i in range(n):
        for i in range(m):
            ls.append(choice(string.ascii_letters))

        s = "".join(ls)
        bits = convert_to_bits(s)
        key = gen_random_key(len(bits))
        cipher = str_xor(bits, key)
        original = str_xor(key, cipher)

        assert original == bits


def test_empty():
    m = ""
    key = gen_random_key(len(m))
    cipher = str_xor(m, key)
    original = str_xor(key, cipher)
    assert original == m

if __name__ == "__main__":
    test_empty()
    test1(1000, 1)
    test1(1000, 5)
    test1(1000, 10)
    test1(10, 100)
    test1(10, 1000)
    test1(5, 10000)
    test1(5, 100000)
    test1(1, 1000000)
    print("Tests finished")
