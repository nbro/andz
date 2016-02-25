#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 04/09/15

See exercise 140.

Based on: http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
"""


def max_non_adj_seq_weight(s):
    """
    Time complexity: O(n).
    """

    include = s[0]  # Maximum sum including the previous element.
    exclude = 0  # Maximum sum excluding the previous element.
    # The maximum sum excluding the current element will be max(include, exclude).
    # The maximum sum including the current element will be exclude + current_element
    # because we cannot sum two consecutive numbers.

    new_exclude = None

    for i in range(1, len(s)):

        if include > exclude:
            new_exclude = include
        else:
            new_exclude = exclude

        include = exclude + s[i]
        exclude = new_exclude

    return max(include, exclude)


if __name__ == "__main__":
    a = [5, 5, 9, 100, 11, 5]  # 5 + 5 + 100 = 110
    b = [3, 2, 5, 10, 7]  # 3 + 5 + 7 = 15
    c = [3, 2, 7, 10]  # 3 + 10 = 13
    print(max_non_adj_seq_weight(a))
    print(max_non_adj_seq_weight(b))
    print(max_non_adj_seq_weight(c))
