#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 04/09/2015

Updated: 10/03/2017

# Description

The maximum sub-array problem is the task of finding the contiguous sub-array
within a one-dimensional array of numbers which has the largest sum.

For example, for the sequence of values −2, 1, −3, 4, −1, 2, 1, −5, 4;
the contiguous sub-array with the largest sum is 4, −1, 2, 1, with sum 6.

# TODO

- Add tests for these functions

# References

- [https://en.wikipedia.org/wiki/Maximum_subarray_problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [https://tkramesh.wordpress.com/2011/03/09/dynamic-programming-maximum-sum-contiguous-subsequence/]
(https://tkramesh.wordpress.com/2011/03/09/dynamic-programming-maximum-sum-contiguous-subsequence/)
"""


def brute_force_max_sum_contiguous_subsequence(seq: list) -> tuple:
    """Brute force approach to compute the sum of all subsequences of seq.

    There are n + (n - 1) + (n - 2) + ... + 1 different subsequences.

    **Time complexity:** O(n^3)."""
    _sum = _max = seq[0]
    start = end = 0

    for i in range(0, len(seq)):

        for j in range(i, len(seq)):

            _sum = 0

            for k in range(i, j + 1):
                _sum += seq[k]

            if _sum > _max:
                _max = _sum
                start = i
                end = j

    return _max, start, end


def better_brute_force_max_sum_contiguous_subsequence(seq: list) -> tuple:
    """Brute force approach to compute the sum of all subsequences of seq.
    There are n + (n - 1) + (n - 2) + ... + 1 different subsequences.

    **Time complexity:** O(n^2)."""
    _sum = _max = seq[0]
    start = end = 0

    for i in range(0, len(seq)):

        _sum = 0

        for j in range(i, len(seq)):
            _sum += seq[j]

            # We need to update every iteration of the inner loop,
            # because we need to check if from i to j we have found a better sum.
            if _sum > _max:
                _max = _sum
                start = i
                end = j

    return _max, start, end


def bottom_up_max_sum_contiguous_subsequence(seq: list) -> tuple:
    """Dynamic programming bottom-up algorithm which finds the sub-sequence of `seq`,
     such that the sum of the elements of that sub-sequence is maximal.

    Let sum[k] denote the max contiguous sequence ending at k.
    So, sum[k + 1] = max(seq[k], sum[k] + seq[k]).
    sum[0] = seq[0]

    To keep track where the max contiguous subsequence starts, we use another list.

    **Time complexity:** O(n).

    **Space complexity:** O(n)."""
    indices = [0] * len(seq)

    _sum = [0] * len(seq)
    _sum[0] = seq[0]
    _max = _sum[0]

    start = end = 0

    for i in range(1, len(seq)):

        if _sum[i - 1] > 0:
            _sum[i] = _sum[i - 1] + seq[i]
            indices[i] = indices[i - 1]

        else:
            _sum[i] = seq[i]
            indices[i] = i

        if _sum[i] > _max:
            _max = _sum[i]
            end = i
            start = indices[i]

    return _max, start, end


def better_bottom_up_max_sum_contiguous_subsequence(seq: list) -> tuple:
    """Returns a tuple or three elements (sum, start index, ending index),
    where sum is the sum of the maximum contiguous subsequence,
    start index is the starting index of the subsequence,
    and ending index is the corresponding ending index.

    Let sum[k] denote the max contiguous sequence ending at k.
    So, sum[k + 1] = max(seq[k], sum[k] + seq[k]).
    sum[0] = seq[0]

    To keep track where the max contiguous subsequence starts, we use another list.

    **Time complexity:** O(n).

    **Space complexity:** O(1)."""
    _max = seq[0]
    _sum = seq[0]
    index = 0

    start = end = 0

    for i in range(1, len(seq)):

        if _sum > 0:
            _sum = _sum + seq[i]
        else:
            _sum = seq[i]
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
