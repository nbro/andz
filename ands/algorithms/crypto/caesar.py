#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 04/08/2015

Updated: 03/03/2017

# Description

Caesar cipher (also known as "shift" or "substitution" cipher) is one of the simplest forms of encryption,
where each letter in the original message (called the "plaintext")
is replaced with a letter corresponding to a certain number of letters up or down in the alphabet.

In this way, a message that initially was quite readable,
ends up in a form that can not be understood at first glance.

For example, suppose we want to caesar_encrypt the plaintext m = "abc".
Suppose further that our alphabet is the English alphabet (of lower case letters from 'a' to 'z').
So we have an alphabet of 26 symbols or, more commonly known, letters.

The general formula of the caesar cipher goes like this:

    e(x) := (x + k) mod 26

where x is a numerical representation of a character, k is non-negative number
and _mod_ is the modulo function, i.e. a function that returns the remainder of the division between (x + k) and 26.
In practice, this allows us to have numbers always smaller than 26.

This function e(x) is applied to all integer representations of the characters of a certain message.
The integer representations may depend on the programming language, environment, etc.
Lets suppose that we have a map like this: 'a' maps to 0, 'b' to 1, and so on until 'z', which maps to 25.
Let's call this function that maps the characters to integers g
and h the one that maps integers to characters.

Now, suppose, as an example, that k = 3, and let's try to apply the function e(x)
to all characters of the message m = "abc" previously mentioned.

Lets start by converting the characters to their integer representation, just to have a clear visualization.

    x1 = g('a') = 0
    x2 = g('b') = 1
    x3 = g('c') = 2

so, let's apply

    e(x1) = (x1 + k) mod 26
    e(0) = (0 + 3) mod 26
    e(0) = 3 mod 26 = 3

we do the same for the other characters and we obtain;

    e(1) = (1 + 3) mod 26
    e(1) = 4 mod 26 = 4

and

    e(2) = (2 + 3) mod 26
    e(2) = 5 mod 26 = 5

Now we convert the resulting numbers to their corresponding characters, that is

    h(e(0) = 3) = 'd'
    h(e(1) = 4) = 'e'
    h(e(2) = 5) = 'f'

Thus the plaintext m = "abc" has been converted to "def".

The decryption phase works in the reverse direction, i.e. instead of using k, we use -k,
that is the general decryption formula can be described as follows

    d(x) := (x - k) mod 26

where x is in this case a integer representation of a character, not from the plaintext,
but from an caesar_encrypt text using the previously described Caesar encryption algorithm.

## Implementation

The following implementation accepts messages of characters
whose value returned by the `ord` function is between 0 and 2^16 - 1.

# Comments

Caesar cipher is far from being a good cryptographic algorithm,
so, in general, you should never use it to caesar_encrypt your messages!

# References

- [https://learncryptography.com/classical-encryption/caesar-cipher](https://learncryptography.com/classical-encryption/caesar-cipher)

"""

__all__ = ["caesar_encrypt",
           "caesar_decrypt",
           "caesar_encrypt_with_multiple_keys",
           "caesar_decrypt_with_multiple_keys"]

from random import choice

# A number which conventionally represents the maximum number that the function `ord` can return,
# since it returns the Unicode code point for a one-character strings (assuming that 16-bit Unicode system).
MAX_MAPPED_INT = 2 ** 16 - 1


def _move_char(c: str, k: int) -> str:
    return chr(ord(c) + k)


def caesar_encrypt(m: str, k: int) -> str:
    """Given a string `m` (i.e. the plaintext) and a non-negative key `k`,
    it returns the encrypted version of `m` with the key `k` using the Caesar cipher algorithm,
    over an alphabet of possible maximum value `MAX_MAPPED_INT`."""
    return "".join(_move_char(c, k) for c in m)


def caesar_decrypt(cipher: str, k: int) -> str:
    """Reverts the operation performed by `caesar_encrypt`."""
    return "".join(_move_char(c, -k) for c in cipher)


# Example of poly-alphabetic encryption

def caesar_encrypt_with_multiple_keys(m: str, keys: list) -> tuple:
    """Given a message m and a set of keys, it encrypts each symbol of m with a random key from `keys`.
    The random pattern of keys chosen is the second item of the tuple returned."""
    pattern = []
    cipher = []

    for c in m:
        k = choice(keys)
        pattern.append(k)
        cipher.append(_move_char(c, k))

    return "".join(cipher), pattern


def caesar_decrypt_with_multiple_keys(cipher: str, pattern: list) -> tuple:
    """`len(pattern) == len(keys)`, where `keys` are the keys passed to `caesar_encrypt_with_multiple_keys`."""
    return "".join(_move_char(cipher[i], -k) for i, k in enumerate(pattern))
