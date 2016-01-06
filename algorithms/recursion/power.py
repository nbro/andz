#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Raising a number to the k using recursion: a^k = b
"""

def power_r(base, power, show_steps=False):
    """Base case: a^0 = 1

    Recursive step: a^{n + 1} = a^n * a"""
    if power == 0: # Base case
        if show_steps:
            print(base, "^{0} = 1", sep="")        
        return 1
    else: # recursive step
        if show_steps:
            print(base, "^{", power, "} = ", base, " * ", base, "^{", power - 1, "}", sep="")
        return base * power_r(base, power - 1, show_steps)


if __name__ == "__main__":
    for i in range(5):
        for j in range(5):
            print(power_r(i, j))
        print("-" * 18)
