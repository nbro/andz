#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Converts a number in a certain base to a decimal number (number in base 10).
"""


import string


def build_alphabet_table():
    alphabet = {}

    for i, char in enumerate(string.ascii_lowercase):
        alphabet[char] = i + 10

    for i, char in enumerate(string.digits):
        alphabet[char] = i

    # from pprint import pprint
    # pprint(alphabet)

    return alphabet


alphabet = build_alphabet_table()


def _make_decimal(n, base, pos):
    if len(n) == 0:
        return 0
    else:
        last = base**pos * alphabet[n[-1]]
        return _make_decimal(n[:-1], base, pos + 1) + last
    
def make_decimal(n, base):
    if base > 36 or base < 2:
        raise ValueError("not base >= 2 and base <= 36")        
        
    if len(n) == 0:
        return 0
    else:
        return _make_decimal(n, base, 0)


print(make_decimal("af10bb1", 16))
