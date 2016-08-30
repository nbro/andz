#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 02/09/15
"""


def _get_longest_common_substring_matrix(s1, s2):
    return [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]


def _build_longest_common_substring(s1, c, m):
    lcs = []

    while m[c[0]][c[1]] != 0:
        lcs.append(s1[c[0] - 1])
        c = (c[0] - 1, c[1] - 1)

    lcs.reverse()
    return lcs, c


def longest_common_substring(s1, s2):
    m = _get_longest_common_substring_matrix(s1, s2)
    c = (0, 0)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):

            if s2[j - 1] == s1[i - 1]:
                m[i][j] = m[i - 1][j - 1] + 1

                if m[i][j] > m[c[0]][c[1]]:
                    c = (i, j)
            else:
                m[i][j] = 0

    return _build_longest_common_substring(s1, c, m)


if __name__ == "__main__":
    print(longest_common_substring("abcdaf", "zbcdf"))
    print(longest_common_substring("zbcdf", "abcdaf"))
    print(longest_common_substring("Nelson Brochado", "John Lennon"))
    print(longest_common_substring("Hello World!", "Halo Welt!"))
