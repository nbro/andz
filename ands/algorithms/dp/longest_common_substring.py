#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 02/09/2015

Updated: 19/09/2017

# Description

The longest common substring problem is to find the longest string that is a
substring of two or more strings.

# TODO

- Add complexity analysis.
- Improve documentation under functions.
- Add ASCII art to explain the problem.

# References

- https://en.wikipedia.org/wiki/Longest_common_substring_problem
"""


def _get_longest_common_substring_matrix(x: str, y: str) -> list:
    return [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]


def _build_longest_common_substring(x: str, c: tuple, m: list) -> tuple:
    lcs = []

    while m[c[0]][c[1]] != 0:
        lcs.append(x[c[0] - 1])
        c = (c[0] - 1, c[1] - 1)

    lcs.reverse()
    return lcs, c


def longest_common_substring(x: str, y: str) -> tuple:
    """Returns a tuple whose first element is a list of characters representing
    the longest common substring, and the second element of the tuple is another
    tuple (of size 2, i.e. a pair), whose first element represents the index
    from string x from where the lcs starts, and similarly the second element of
    that tuple represents the index from y from where the lcs starts."""
    m = _get_longest_common_substring_matrix(x, y)
    c = (0, 0)

    for i in range(1, len(x) + 1):

        for j in range(1, len(y) + 1):

            if y[j - 1] == x[i - 1]:
                m[i][j] = m[i - 1][j - 1] + 1

                if m[i][j] > m[c[0]][c[1]]:
                    c = (i, j)
            else:
                m[i][j] = 0

    return _build_longest_common_substring(x, c, m)


if __name__ == "__main__":
    print(longest_common_substring("abcdaf", "zbcdf"))
    print(longest_common_substring("zbcdf", "abcdaf"))
    print(longest_common_substring("Nelson Brochado", "John Lennon"))
    print(longest_common_substring("Hello World!", "Halo Welt!"))
