#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado

Creation: 22/02/16

Updated: 18/01/2017

## Description

The Ackermann function is the simplest example of a well defined total function.
Total function means that it's defined for all possible inputs.
The function is computable, but **not** primitive recursive.
A primitive recursive function is a function that can be implemented using only "for" loops,
i.e. loops that have a fixed number of iterations.
A computable function is a function that can be implemented using "while" loops.
Note that "do" loops are a particular case of while loops.

It grows faster than an exponential function, or even a multiple exponential function.

## References

- [http://mathworld.wolfram.com/AckermannFunction.html](http://mathworld.wolfram.com/AckermannFunction.html)
- [http://math.stackexchange.com/questions/75296/what-is-the-difference-between-total-recursive-and-primitive-recursive-functions](http://math.stackexchange.com/questions/75296/what-is-the-difference-between-total-recursive-and-primitive-recursive-functions)
- [https://en.wikipedia.org/wiki/Ackermann_function](https://en.wikipedia.org/wiki/Ackermann_function)
"""


def ackermann(m: int, n: int) -> int:
    assert m >= 0 and n >= 0
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
