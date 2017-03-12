#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 01/08/2015

Updated: 20/01/2017

# Description

Checking recursively if a string is a palindrome.
A palindrome is a string that reads the same way forward and backward.
For example, "anna" is a palindrome, whereas "prime" is not.

# Resources

- [https://en.wikipedia.org/wiki/Palindrome](https://en.wikipedia.org/wiki/Palindrome)

"""

__all__ = ["is_palindrome"]


def _is_palindrome(s: str, l: int, r: int) -> bool:
    """`l` is the index that indexes `s` from the left
    and, similarly, `r` indexes it from the right."""
    if l >= r:
        return True
    if s[l] == s[r]:
        return _is_palindrome(s, l + 1, r - 1)
    else:
        return False


def is_palindrome(s: str) -> bool:
    """Returns true if the string `s` is a palindrome, false otherwise."""
    if len(s) <= 1:
        return True
    else:
        return _is_palindrome(s, 0, len(s) - 1)
