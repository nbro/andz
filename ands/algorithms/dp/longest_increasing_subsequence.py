#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 29/08/2015

Based on the following answer:
http://stackoverflow.com/a/19639755/3924118

https://www.youtube.com/watch?v=CE2b_-XfVDk
"""


def build_longest_increasing_subsequence(s, prev, index_of_max_size):
    a = []

    while index_of_max_size != -1:
        a.append(s[index_of_max_size])
        index_of_max_size = prev[index_of_max_size]

    a.reverse()
    return a


def lis(s):
    """Returns a list with one of the possible
    longest increasing subsequences of s.

    This algorithm uses a dynamic programming strategy,
    which runs in O(n^2) time, where n is the size of s.

    :type s : list of int
    :rtype : list of int
    """

    # At the end of the algorithm,
    # each item of this list (indexed, say, by i)
    # will be the size of the LIS seen so far
    # starting from the beginning of s (s[0]) up to s[i].
    # For example, suppose s = [3, 2, 5],
    # then, at the end of the algorithm,
    # a = [1, 1, 2]
    # Why is this true?
    # The maximum possible longest increasing subsequence
    # from the beginning of s up to the beginning of s is 1,
    # because the beginning of s contains_key only one element (3).
    # The LIS from s[0] to s[1] is still one.
    # The LIS from s[0] to s[2] is 2,
    # because we can either pick 3 or 2 and 5.
    a = [1] * len(s)

    # This array is useful to retrieve information
    # about the indexes of the chosen numbers to belong to the LIS.
    # See the function build_longest_increasing_subsequence,
    # if you understand how to retrieve the numbers in the LIS.
    prev = [-1] * len(s)

    # Current maximum size of the increasing subsequence
    # Note that initially all numbers in s are increasing subsequences of size
    # 1
    current_max_size = 1

    # Index of a, which contains_key the size of the current L.I.S.
    index_of_max_size = 0

    for i in range(1, len(s)):

        for j in range(0, i):

            if s[j] < s[i] and a[i] < a[j] + 1:
                a[i] = a[j] + 1

                prev[i] = j

        # Updates the current index of where the size of the current L.I.S is in a,
        # and also the current maximum size of the so far L.I.S.
        if a[i] > current_max_size:
            index_of_max_size = i
            current_max_size = a[i]

    return build_longest_increasing_subsequence(s, prev, index_of_max_size)


def recursive_lis(s):
    pass
    # http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming


# print(lis([3, 2, 6, 4, 5, 1]))
print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
