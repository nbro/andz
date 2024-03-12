#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 25/07/2015

Updated: 19/09/2017

# Description

Raising an integer a to the k >= 0 using recursion, i.e., aᵏ = b.
"""

__all__ = ["power"]


def power(base: int, p: int) -> int:
    """Assumes inputs are integers and that the power p >= 0.

    Base case: a⁰ = 1.
    Recursive step: aⁿ⁺¹ = aⁿ * a."""
    assert p >= 0
    if p == 0:
        return 1
    return base * power(base, p - 1)
