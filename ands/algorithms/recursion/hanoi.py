#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado

Creation: 27/02/16

Updated: 18/01/2017

## Description

Towers of Hanoi is a mathematical game.
It consists of 3 rods, and a number of disks of different sizes, which can slide onto any rod.
The game starts with the disks in a neat stack in ascending order of size on one rod,
the smallest at the top, thus making a conical shape.

The objective of the game is to move the entire stack to another rod,
obeying the following rules:

1. Only 1 disk can be moved at a time.

2. Each move consists of taking the upper disk
from one of the stacks and placing it on top of another stack,
i.e. a disk can only be moved if it is the uppermost disk on its stack.

3. No disk may be placed on top of a smaller disk.

With 3 disks, the game can be solved with at least 7 moves (best case).
The minimum number of moves required to solve a tower of hanoi game
is 2^n - 1, where n is the number of disks.

For simplicity, in the following algorithm
the source (='A'), auxiliary (='B') and destination (='C') rodes are fixed,
and therefore the algorithm always shows the steps to go from 'A' to 'C'.

## References

- [https://en.wikipedia.org/wiki/Tower_of_Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)
- [http://www.cut-the-knot.org/recurrence/hanoi.shtml](http://www.cut-the-knot.org/recurrence/hanoi.shtml)
- [http://stackoverflow.com/questions/105838/real-world-examples-of-recursion](http://stackoverflow.com/questions/105838/real-world-examples-of-recursion)
"""

__all__ = ["hanoi"]


def _hanoi(n: int, ls: list, src='A', aux='B', dst='C') -> list:
    """Recursively solve the Towers of Hanoi game for `n` disks.

    The smallest disk, which is the topmost one at the beginning,
    is called 1, and the largest one is called `n`.

    `src` is the start rod where all disks are set in a neat stack in ascending order.
    `aux` is the third rod.
    `dst` is similarly the destination rod."""
    if n > 0:
        _hanoi(n - 1, ls, src, dst, aux)
        ls.append((n, src, dst))
        _hanoi(n - 1, ls, aux, src, dst)
    return ls


def hanoi(n: int) -> list:
    """Returns a list L of tuples each of them representing a move to be done.

    `n` is the number of disks.
    The number of rods is clearly always 3.

    L[i] must be done before L[i + 1], for all i.
    L[i][0] := the disk number (or id).
    Numbers start from 1 and go up to n.
    L[i][1] := the source rod from which to move L[i][0].
    L[i][2] := the destination rod to which to move L[i][0].

    The disk with the smallest radius (at the top) is the disk number 1,
    its successor in terms or radius' size is disk number 2, and so on.
    So the largest disk is disk number n."""
    assert n >= 0
    return _hanoi(n, [])
