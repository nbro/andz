#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Simulating the append operation of numbers to another

For example, suppose we have the following number: 3145

Now, we want to append the number 9393:

    31459393
"""


def create_base(n):
    zeros = len(str(n))
    mul = '1'
    for i in range(zeros):
        mul += '0'
    return int(mul)


previous = 9294
num = 322

new_num = previous * create_base(num) + num

print(new_num)
