#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 02/09/15

Problem (https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)
What is (length of) the longest common subsequence between strings s1 and s2,
where characters are not necessarily contiguous?

You can find a recursive and a two dynamic programming implementations for the LCS problem.
You can find just one implementation using dynamic programming that actually returns the LCS,
instead of just computing its length, like all other implementations do.
"""

from pprint import pprint


def _get_lcs_length_matrix(s1, s2):
    """Returns a (len(s1) + 1)x(len(s2) + 1) matrix,
    specifically it returns a list of length len(s1) + 1,
    whose elements are lists of length (len(s2) + 1).

    Why +1 in (len(s2) + 1) and (len(s1) + 1)?
    Because the first row and column are reserved
    for the cases where we compare with empty sequences.
    """
    return [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]


def _get_lcs_matrix(s1, s2):
    m = []
    for _ in range(len(s1) + 1):
        m.append([])
        for _ in range(len(s2) + 1):
            m[-1].append([])
    return m


def _recursive_lcs_length_aux(s1, n, s2, m, result):
    """See recursive_lcs_length.

    :type s1 : str
    :type n : int
    :type s2 : str
    :type m : int
    :type result : int
    :rtype : int
    """
    if n == 0 or m == 0:
        return 0
    elif s1[n - 1] == s2[m - 1]:
        result = 1 + _recursive_lcs_length_aux(s1, n - 1, s2, m - 1, result)
    else:
        result = max(
            _recursive_lcs_length_aux(
                s1,
                n - 1,
                s2,
                m,
                result),
            _recursive_lcs_length_aux(
                s1,
                n,
                s2,
                m - 1,
                result))
    return result


def recursive_lcs_length(s1, s2):
    """Returns the length of the LCS between s1 and s2.

    This algorithm uses a recursive solution,
    as the name suggests, but this results in an exponential algorithm.

    :type s1 : str
    :type s2 : str"""

    n = len(s1)
    m = len(s2)
    result = 0
    return _recursive_lcs_length_aux(s1, n, s2, m, result)


def _memoized_recursive_lcs_length_aux(s1, n, s2, m, result, matrix):
    """See recursive_lcs_length.

    :type s1 : str
    :type n : int
    :type s2 : str
    :type m : int
    :type result : list of list
    :rtype : int
    """
    if n == 0 or m == 0:
        return 0
    elif matrix[n - 1][m - 1] is not None:
        return matrix[n - 1][m - 1]
    elif s1[n - 1] == s2[m - 1]:
        result = 1 + \
            _memoized_recursive_lcs_length_aux(
                s1, n - 1, s2, m - 1, result, matrix)
    else:
        result = max(_memoized_recursive_lcs_length_aux(s1, n - 1, s2, m, result, matrix),
                     _memoized_recursive_lcs_length_aux(s1, n, s2, m - 1, result, matrix))

    matrix[n - 1][m - 1] = result

    return result


def memoized_recursive_lcs_length(s1, s2):
    """Returns the length of the LCS between s1 and s2.

    This algorithm uses memoization
    to improve performance with respect to recursive_lcs_length.

    The running time complexity of this algorithm
    should be O(len(s1) * len(s2)),
    which is very similar to the bottom-up version.

    :type s1 : str
    :type s2 : str
    """
    n = len(s1)
    m = len(s2)
    result = 0

    matrix = [[None for _ in range(len(s2))] for _ in range(len(s1))]

    return _memoized_recursive_lcs_length_aux(s1, n, s2, m, result, matrix)


def bottom_up_lcs_length(s1, s2, matrix=False):
    """Returns the length of the LCS between s1 and s2,
    if matrix is not set to True,
    else it returns the matrix used
    to calculate the length of the LCS of sub-problems.

    :type s1 : str
    :type s2 : str
    :rtype : int | list of list
    """
    m = _get_lcs_length_matrix(s1, s2)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])

    return m[-1][-1] if not matrix else m


# def backtrack(m, s1, s2, i, j):
#     if i == 1 or j == 1:
#         return ""
#     elif s1[i] == s2[j]:
#         print(s1[i])
#         return backtrack(m, s1, s2, i - 1, j - 1) + s1[i]
#     else:
#         if m[i][j - 1] > m[i - 1][j]:
#             return backtrack(m, s1, s2, i, j - 1)
#         else:
#             return backtrack(m, s1, s2, i - 1, j)
#
#
# def get_lcs(s1, s2):
#     m = bottom_up_lcs_length(s1, s2, matrix=True)
#     backtrack(m, s1, s2, len(s1) - 1, len(s2) - 1)


def bottom_up_lcs(s1, s2):
    """Builds all lists with all LCSs to sub-strings of sub-problems,
    and then returns a list of characters representing
    the longest common subsequence for the original problem.

    :type s1 : str
    :type s2 : str
    :rtype : list of str"""

    m = _get_lcs_matrix(s1, s2)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                m[i][j] += m[i - 1][j - 1]
                m[i][j].append(s2[j - 1])
            else:
                if len(m[i - 1][j]) > len(m[i][j - 1]):
                    m[i][j] += m[i - 1][j]
                else:
                    m[i][j] += m[i][j - 1]

    return m[-1][-1]


if __name__ == "__main__":
    str2 = "acbcf"
    str1 = "abcdaf"

    str3 = "BANANA"
    str4 = "ATANA"

    str5 = "GAC"
    str6 = "AGCAT"

    str7 = "XMJYAUZ"
    str8 = "MZJAWXU"

    str9 = "ABAZDC"
    str10 = "BACBAD"

    print(bottom_up_lcs_length(str9, str10))
    print(recursive_lcs_length(str9, str10))
    print(memoized_recursive_lcs_length(str9, str10))
    pprint(bottom_up_lcs(str9, str10))

    print(bottom_up_lcs_length(str3, str4))
    print(recursive_lcs_length(str3, str4))
    print(memoized_recursive_lcs_length(str3, str4))
    pprint(bottom_up_lcs(str3, str4))

    print(bottom_up_lcs_length(str5, str6))
    print(recursive_lcs_length(str5, str6))
    print(memoized_recursive_lcs_length(str5, str6))
    pprint(bottom_up_lcs(str5, str6))

    print(bottom_up_lcs_length(str7, str8))
    print(recursive_lcs_length(str7, str8))
    print(memoized_recursive_lcs_length(str7, str8))
    pprint(bottom_up_lcs(str7, str8))
