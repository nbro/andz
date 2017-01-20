#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Created: 2015

Updated: 20/01/2017

Checking recursively if a string is a palindrome.
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
    """Returns `True` if the string `s` is a palindrome, `False` otherwise."""
    if len(s) <= 1:
        return True
    else:
        return _is_palindrome(s, 0, len(s) - 1)
