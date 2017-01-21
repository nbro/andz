#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado

Created: 2015

Updated: 18/01/2017

## Description

Raising an integer `a` to the `k >= 0` using recursion, i.e., a<sup>k</sup> = b.
"""


def power(base: int, p: int) -> int:
    """Assumes inputs are integers and that the power `p >= 0`.

    Base case: a<sup>0</sup> = 1.
    Recursive step: a<sup>n + 1</sup> = a<sup>n</sup> * a."""
    assert p >= 0

    if p == 0:
        return 1
    else:
        return base * power(base, p - 1)
