#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 22/02/16

Ackermann function grows faster than an exponential function,
or even a multiple exponential function.
So, do not even try to run this function!

## References

- http://mathworld.wolfram.com/AckermannFunction.html

"""


def ackermann(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ackermann(x - 1, 1)
    else:
        return ackermann(x - 1, ackermann(x, y - 1))


if __name__ == "__main__":
    print(ackermann(2, 3))
    try:
        print(ackermann(3, 10))
    except RuntimeError:
        pass
