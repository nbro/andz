#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string


def generate_random_string(size):
    return "".join(random.choice(string.printable) for _ in range(size))


def gen_rand_keys(size, _min, _max):
    return [random.randint(_min, _max) for _ in range(size)]


def find_max_char_ord_value(message: str):
    return max(ord(c) for c in message)
