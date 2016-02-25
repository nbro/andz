#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Checking recursively if a string is a palindrome.
"""

import string
from random import choice


def generate_palindromes(n, s):
    """Generates `n` palindromes of lower and upper case letters
    and numbers (in a list) of size `s`."""
    palindromes = []
    for i in range(n):
        p = []
        for i in range(s):
            char = choice(string.ascii_letters)
            p.insert(len(p) // 2, char) 
            p.insert(len(p) // 2, char)
        palindromes.append("".join(p))
    return palindromes

def generate_random_words(n, s):
    w = []
    for i in range(n):
        p = []
        for i in range(s):
            char = choice(string.ascii_letters)
            p.append(char)
        w.append("".join(p))
    return w

def _is_palindrome(s, i, j):
    if i >= j:
        return True
    if s[i] == s[j]:
        return _is_palindrome(s, i + 1, j - 1)
    else:
        return False

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return _is_palindrome(s, 0, len(s) - 1)


if __name__ == "__main__":
    p = generate_palindromes(10000, 10)
    
    for i in p:
        if not is_palindrome(i):
            raise Exception("Something wrong with the implementation...")

    p = generate_random_words(10000, 10)

    for i in p:
        if is_palindrome(i):
            print("Palindrome:", i)
