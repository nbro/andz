#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string


def gen_rand_message(size):
    return "".join(random.choice(string.printable) for _ in range(size))


def gen_key(size):
    """Generate a random key of printable characters."""
    return gen_rand_message(size)


def gen_rand_keys(size, _min, _max):
    return [random.randint(_min, _max) for _ in range(size)]


def find_max(m):
    """m is a message"""
    return max(ord(c) for c in m)
