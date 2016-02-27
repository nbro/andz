#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 27/02/16

Towers of Hanoi is a mathematical game.
It consists of 3 rods, and a number of disks of different sizes,
which can slide onto any rod.
The game starts with the disks in a neat stack
in ascending order of size on one rod,
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


# References

- [https://en.wikipedia.org/wiki/Tower_of_Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

- [http://www.cut-the-knot.org/recurrence/hanoi.shtml](http://www.cut-the-knot.org/recurrence/hanoi.shtml)

- [http://stackoverflow.com/questions/105838/real-world-examples-of-recursion](http://stackoverflow.com/questions/105838/real-world-examples-of-recursion)
"""


def hanoi_r(n, src='A', aux='B', dst='C'):
    """Recursively solve the Towers of Hannoi game for `n` disks.

    The smallest disk, which is the topmost one at the beginning,
    is called 1, and the largest one is called `n`.

    `src` is the start rod where all disks are set in a neat stack in ascending order.
    `aux` is the third rod.
    `dst` is similarly the destination rod."""
    if n > 0:
        hanoi_r(n - 1, src, dst, aux)
        print("Move disk", n, "from", src, "to", dst)
        hanoi_r(n - 1, aux, src, dst)    
        

if __name__ == "__main__":
    hanoi_r(3)
    hanoi_r(4)
