#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 04/09/2015

Updated: 07/03/2018

# Description

Given a sequence of numbers A = {a₁, a₂, ..., a_n}, computes, with worst-case
complexity O(n), the maximal weight (or sum) of any sub-sequence of non-adjacent
elements in A.

A sub-sequence of non-adjacent elements may include aᵢ or aᵢ₊₁ but not both, for
all i.

For example, with A = {2, 9, 6, 2, 6, 8, 5}, the algorithms returns 20, because
we can pick sub-sequence B = {9, 6, 5}, where the 6 is the second 6 in A.

The dynamic programming algorithm scans the input sequence once.

# Notes

See exercise 140 (of the Carzaniga's exercises).

# TODO

- Add tests for functions in this module.

# References

- http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
"""

__all__ = ["max_non_adj_seq_weight"]


def max_non_adj_seq_weight(seq: list) -> int:
    """Returns the sum (or weight) of the elements of a subsequence of seq, such
    that no two elements from this subsequence were initially adjacent in seq
    and this subsequence is the one whose elements summed together give the
    maximum value (weight or sum).

    Time complexity: O(n)."""

    include = seq[0]  # Maximum sum including the previous element.
    exclude = 0  # Maximum sum excluding the previous element.

    # The maximum sum excluding the current element will be:
    # max(include, exclude).
    # The maximum sum including the current element will be exclude + current
    # element, because we cannot sum two consecutive numbers.

    for i in range(1, len(seq)):

        if include > exclude:
            new_exclude = include
        else:
            new_exclude = exclude

        include = exclude + seq[i]
        exclude = new_exclude

    return max(include, exclude)


if __name__ == "__main__":
    a = [5, 5, 9, 100, 11, 5]  # 5 + 5 + 100 = 110
    b = [3, 2, 5, 10, 7]  # 3 + 5 + 7 = 15
    c = [3, 2, 7, 10]  # 3 + 10 = 13
    print(max_non_adj_seq_weight(a))
    print(max_non_adj_seq_weight(b))
    print(max_non_adj_seq_weight(c))
