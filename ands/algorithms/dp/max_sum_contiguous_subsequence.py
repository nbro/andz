#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 04/09/15

Based on: https://tkramesh.wordpress.com/2011/03/09/dynamic-programming-maximum-sum-contiguous-subsequence/
"""


def brute_force_max_sum_contiguous_subsequence(s):
    """Brute force approach to compute the sum of all subsequences of s.
    There are n + (n - 1) + (n - 2) + ... + 1 different subsequences.

    Running time complexity: O(n^3).

    :type s : list or tuple
    """
    _sum = _max = s[0]
    start = end = 0

    for i in range(0, len(s)):

        for j in range(i, len(s)):

            _sum = 0

            for k in range(i, j + 1):
                _sum += s[k]

            if _sum > _max:
                _max = _sum
                start = i
                end = j

    return _max, start, end


def better_brute_force_max_sum_contiguous_subsequence(s):
    """Brute force approach to compute the sum of all subsequences of s.
    There are n + (n - 1) + (n - 2) + ... + 1 different subsequences.

    Running time complexity: O(n^2).

    :type s : list or tuple
    """
    _sum = _max = s[0]
    start = end = 0

    for i in range(0, len(s)):

        _sum = 0

        for j in range(i, len(s)):
            _sum += s[j]

            # We need to update every iteration of the inner loop,
            # because we need to check if from i to j
            # we have found a better sum...
            if _sum > _max:
                _max = _sum
                start = i
                end = j

    return _max, start, end


def bottom_up_max_sum_contiguous_subsequence(s):
    """
    Let sum[k] denote the max contiguous sequence ending at k.
    So, sum[k + 1] = max(s[k], sum[k] + s[k]).
    sum[0] = s[0]

    To keep track where the max contiguous subsequence starts,
    we use another array.

    Time complexity: O(n).
    Space complexity: O(n).

    :type s : list
    """
    indices = [0]*len(s)

    _sum = [0]*len(s)
    _sum[0] = s[0]
    _max = _sum[0]

    start = end = 0

    for i in range(1, len(s)):

        if _sum[i - 1] > 0:
            _sum[i] = _sum[i - 1] + s[i]
            indices[i] = indices[i - 1]

        else:
            _sum[i] = s[i]
            indices[i] = i

        if _sum[i] > _max:
            _max = _sum[i]
            end = i
            start = indices[i]

    return _max, start, end


def better_bottom_up_max_sum_contiguous_subsequence(s):
    """Returns a tuple or three elements (sum, start index, ending index),
    where sum is the sum of the maximum contiguous subsequence,
    start index is the starting index of the subsequence,
    and ending index is the corresponding ending index.

    Let sum[k] denote the max contiguous sequence ending at k.
    So, sum[k + 1] = max(s[k], sum[k] + s[k]).
    sum[0] = s[0]

    To keep track where the max contiguous subsequence starts,
    we use another array.

    Time complexity: O(n).
    Space complexity: O(1).

    :type s : list
    """
    _max = s[0]
    _sum = s[0]
    index = 0

    start = end = 0

    for i in range(1, len(s)):

        if _sum > 0:
            _sum = _sum + s[i]
        else:
            _sum = s[i]
            index = i

        if _sum > _max:
            _max = _sum
            end = i
            start = index

    return _max, start, end


if __name__ == "__main__":
    seq = [4, 2, -4]

    print(brute_force_max_sum_contiguous_subsequence(seq))
    print(better_brute_force_max_sum_contiguous_subsequence(seq))
    print(bottom_up_max_sum_contiguous_subsequence(seq))
    print(better_bottom_up_max_sum_contiguous_subsequence(seq))
