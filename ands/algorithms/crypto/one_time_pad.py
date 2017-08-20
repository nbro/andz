#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 10/08/2015

Updated: 20/08/2017

# Description

One time pad (or, in short, OTP) is an encryption technique that cannot be cracked,
but requires the use of a one-time pre-shared key the same size as the message being sent.

In this technique, a plaintext is paired with a random secret key (also referred to as a one-time pad).
Specifically, each bit or character of the plaintext is encrypted by combining it
with the corresponding bit or character from the secret key either using the XOR operation,
or modular addition as the encryption function and modular subtraction as the decryption function.

If the key is truly random, is at least as long as the plaintext,
is never reused in whole or in part, and is kept completely secret,
then the resulting ciphertext will be impossible to decrypt or break.

It has also been proven that any cipher with the _perfect secrecy_ property
must use keys with effectively the same requirements as OTP keys.
However, practical problems (i.e. it's too expensive to exchange keys of the same length of the plaintext)
have prevented one-time pads from being widely used.

## Example

Suppose Alice wishes to send the message m = "hi" to Bob.
Assume the key was somehow previously produced and securely issued to both.
Lets assume key k = "ab".
Lets assume, for simplicity, that messages only contain lower case letters
from the English alphabet, so we have letters from 'a'..'z'.
Lets assume further that the mapping between these letters goes like follows

    'a' -> 1,
    'b' -> 2,
    'c' -> 3,
    ...
    'z' -> 26

Lets call this mapping function h. Lets call the reversing function f.

The general one-time pad algorithm proceeds as follows.

    let c be an empty string (which will represent the ciphertext at the end of the algorithm)

    iterate through message m:

        let n be the current iteration
        let i me the nth character of m
        let j me the nth character of k
        let h(i) be the integer representation of i
        let h(j) be the integer representation of j

        x = XOR(h(i), h(j))
        y = f(x)

        c = c + y

Thus the one-time pad algorithm to encrypt the message m = "hi"
with the randomly generated key k = "ab" proceeds as follows.


    c = ""

    Let n = 1.

        i = 'h'
        j = 'a'
        h(i) = 8
        h(j) = 1

        In binary, h(i) = 8  is 1000 and h(j) = 1 is 0001.

        x = XOR(1000, 0001) = 1001, which is 9 in decimal.
        y = f(1001) = 'i'

        c = '' + 'i' = "i"

    Let n = 2.

        i = 'i'
        j = 'b'
        h(i) = 9
        h(j) = 2

        In binary, h(i) = 9 is 1001 and h(j) = 2 is 0010.

        x = XOR(1001, 0010) = 1011, which is 11 in decimal.
        y = f(1011) = 'k'

        c = 'i' + 'k' = "ik"

So the encrypted text c = "ik".

To decrypt we simply apply the one-time pad with the same key but to c = "ik".

### How does the XOR operation work in general?

Given two binary strings A and B (over a binary alphabet consisting of the symbols 0 and 1)
then the XOR operation works as follows

    +---+---+---------+
    | A | B | A XOR B |
    +---+---+---------+
    | 0 | 0 |       0 |
    | 1 | 1 |       0 |
    | 1 | 0 |       1 |
    | 0 | 1 |       1 |
    +---+---+---------+

In other words, the output is 1 only when the two inputs are different.

### Why to decrypt we use the XOR on the ciphertext (with the same secret key) and the result is the plain text?

In short, it's because XOR is its own inverse!

#### Example

Suppose we have two binary strings X=101 and K=001, where K is the key.
Lets apply the XOR operation on this two strings.

    C = X XOR K =   101
                    001 XOR
                    -------
                    100

    X = C XOR K = 100
                  001 XOR
                  -------
                  101

This works in general because, at position i of the strings:

- If you have two 0s, the result will be 0, which XORed with 0, gives again 0.

- If you have two 1s, the result will be 0, which XORed with 1, gives 1.

- If you have message 0 and key 1, the the result will be 1, which XORed with 1, gives 0.

- Similarly, if you have message 1 and key 0, the the result will be 1, which XORed with 0, gives 1.

## Notes

- one-time pad provides "perfect" secrecy
- one-time pad requires a key of the same length of the plaintext
- one-time pad may be impractical for messages greater than a certain length

# TODO

- Implement OTP using module arithmetic
(i.e. modular addition for encryption and modular subtraction for decryption)
- Add complexity analysis

# References

- https://learncryptography.com/classical-encryption/one-time-pad
- https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/one-time-pad
- http://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html
- https://en.wikipedia.org/wiki/One-time_pad
- http://crypto.stackexchange.com/questions/59/taking-advantage-of-one-time-pad-key-reuse
- http://crypto.stackexchange.com/questions/41798/one-time-pad-xor-question
- http://crypto.stackexchange.com/questions/33065/is-all-of-encryption-based-on-xor/
"""

__all__ = ["encrypt", "decrypt"]


def encrypt(plaintext: str, key: str) -> str:
    """Encrypts `plaintext` using `key` according to the one-time-pad algorithm."""
    return "".join(chr(ord(p) ^ ord(k)) for (p, k) in zip(plaintext, key))


def decrypt(ciphertext: str, key: str) -> str:
    """Decrypts`ciphertext` using `key` according to the one-time-pad algorithm."""
    return encrypt(ciphertext, key)
