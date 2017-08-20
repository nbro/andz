#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 29/08/2015

Updated: 20/08/2017

# Description

The longest increasing subsequence problem is to find a subsequence of a given sequence
in which the subsequence's elements are in sorted order, lowest to highest,
and in which the subsequence is as long as possible.

This subsequence is not necessarily contiguous, or unique.

Longest increasing subsequences are studied in the context of various disciplines related to mathematics,
including algorithmics, random matrix theory, representation theory, and physics.

# TODO

- Add tests for these functions
- Add complexity analysis
- Improve documentation under functions
- Add ASCII art to explain the problem
- Implement recursive longest common substring
(http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming)

# References

- http://stackoverflow.com/a/19639755/3924118
- https://www.youtube.com/watch?v=CE2b_-XfVDk
- https://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""


def build_longest_increasing_subsequence(seq, prev, index_of_max_size) -> list:
    """Build the longest increasing subsequence from original sequence (list) `seq`,
    the list `prev` produced by the function `longest_increasing_subsequence` and `index_of_max_size`."""
    a = []

    while index_of_max_size != -1:
        a.append(seq[index_of_max_size])
        index_of_max_size = prev[index_of_max_size]

    a.reverse()
    return a


def longest_increasing_subsequence(seq: list) -> list:
    """Returns a list with one of the possible longest increasing subsequences of `seq`.

    `seq` is an initial list of comparable objects.

    This algorithm uses a dynamic programming strategy.

    Time complexity: O(n^2), where `n` is the size of `seq`."""

    # At the end of the algorithm, each item of this list (indexed, say, by i)
    # will be the size of the LIS seen so far starting from the beginning of seq (seq[0]) up to seq[i].

    # For example, suppose seq = [3, 2, 5], then, at the end of the algorithm, a = [1, 1, 2]. Why?
    # The maximum possible LIS from the beginning of `seq` up to the beginning of `seq` is 1,
    # because the beginning of `seq` contains only one element, that is 3.
    # The LIS from seq[0] to seq[1] is still one.
    # The LIS from seq[0] to seq[2] is 2, because we can either pick 3, or 2 and 5.
    a = [1] * len(seq)

    # This list is useful to retrieve information
    # about the indexes of the chosen numbers to belong to the LIS.
    # See the function `build_longest_increasing_subsequence`,
    # if you understand how to retrieve the numbers in the LIS.
    prev = [-1] * len(seq)

    # Current maximum size of the longest increasing subsequence.
    # Note that initially all numbers in `seq` are increasing subsequences of size 1.
    current_max_size = 1

    # Index of `a`, which contains the size of the current LIS.
    index_of_max_size = 0

    for i in range(1, len(seq)):

        for j in range(0, i):

            if seq[j] < seq[i] and a[i] < a[j] + 1:
                a[i] = a[j] + 1

                prev[i] = j

        # Updates the current index of where the size of the current LIS is in `a`,
        # and also the current maximum size of the so far LIS.
        if a[i] > current_max_size:
            index_of_max_size = i
            current_max_size = a[i]

    return build_longest_increasing_subsequence(seq, prev, index_of_max_size)


if __name__ == "__main__":
    print(longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
