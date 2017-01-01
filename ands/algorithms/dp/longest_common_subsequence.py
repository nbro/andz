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

## References
- Introduction to Algorithms (3rd ed) by CLRS
- Slides by prof. Evanthia Papadopoulou
"""


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
        result = max(_recursive_lcs_length_aux(s1, n - 1, s2, m, result),
                     _recursive_lcs_length_aux(s1, n, s2, m - 1, result))
    return result


def recursive_lcs_length(s1, s2):
    """Returns the length of the LCS between s1 and s2.

    This algorithm uses a recursive solution,
    as the name suggests, but this results in an exponential algorithm.
    
    ### Idea
    For every subsequence of s1 check weather it's a subsequence of s2.
    There are 2^n subsequences of s1 to check.
    Each subsequence takes O(m) time to check:
    scan s2 for the first letter, from there scan for the second, and so on.
    
    ### Definition
    LCS(i, j) = length of the longest comment subsequence between
    s1(i) = s1(i)_1, s1(i)_2, ..., s1(i)_i and s2(j) = s2(j)_1, s2(j)_2, ..., s2(j)_j.
    
    ### Goal 
    LCS(n, m), where n = length(s1) and m = length(s2).
    
    ### Algorithm  
    In the following descriptions s1(i) means a subsequence of s1 up to i.
    Instead, s1(i)_i means the ith element of that same subsequence s1(i).
    
    If s1(i) or s2(j) is empty, LCS(i, j) = 0.
    
    If s1(i)_i == s2(j)_j, then s1(i)_i and s2(j)_j must be included in the LCS(i, j),
    and we express it as LCS(i, j) = LCS(i - 1, j - 1) + 1,
    where the +1 stands for the inclusion of s1(i)_i and s2(j)_j.
    
    If s1(i)_i != s2(j)_j, then we can either skip s1(1)_i or s2(1)_j (or both):
    we need to choose the best. So lets see these options more closely.
    Option 1: s1(i)_i is not in the LCS, then LCS(i, j) = LCS(i - 1, j).
    Option 2: s2(j)_j is not in the LCS, then LCS(i, j) = LCS(i, j - 1).
    So, basically, what we do is: LCS(i, j) = max(LCS(i - 1, j), LCS(i, j - 1)).
    Note that we don't really need to include LCS(i - 1, j - 1), 
    for the case where neither s1(i)_i nor s2(j)_j are included in the LCS(i, j),
    because max(LCS(i - 1, j), LCS(i, j - 1), LCS(i - 1, j - 1)) = max(LCS(i - 1, j), LCS(i, j - 1)),
    i.e. the maximum "profit" can simply be retrieved from LCS(i - 1, j) and LCS(i, j - 1),
    since for sure LCS(i - 1, j - 1) brings less (or equal) profit than LCS(i - 1, j) or LCS(i, j - 1).
    
    ### Summary
                +--
                | 0                                   if i == 0 or j == 0.
    LCS(i, j) = | LCS(i - 1, j - 1) + 1               if i, j > 0 and s1(i)_i == s2(j)_j.
                | max(LCS(i - 1, j), LCS(i, j - 1))   if i, j > 0 and s1(i)_i != s2(j)_j.
                +--
                
    ### Complexity
    This plain recursive approach is very inefficient, 
    because we keep on recomputing sub-problems.
    
    Time complexity: theta(m*2^n).    

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
        result = 1 + _memoized_recursive_lcs_length_aux(s1, n - 1, s2, m - 1, result, matrix)
    else:
        result = max(_memoized_recursive_lcs_length_aux(s1, n - 1, s2, m, result, matrix),
                     _memoized_recursive_lcs_length_aux(s1, n, s2, m - 1, result, matrix))

    matrix[n - 1][m - 1] = result

    return result


def memoized_recursive_lcs_length(s1, s2):
    """Returns the length of the LCS between s1 and s2.

    This algorithm uses memoization to improve performance with respect to recursive_lcs_length.

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
    """Returns the length of the LCS between s1 and s2, if matrix is not set to True,
    else it returns the matrix used to calculate the length of the LCS of sub-problems.

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


def bottom_up_lcs_length_partial(s1, s2, matrix=False):
    m = _get_lcs_length_matrix(s1, s2)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            elif (s1[i - 1] == 'c' and s2[j - 1] == 'e') or (s1[i - 1] == 'e' and s2[j - 1] == 'c'):
                m[i][j] = max(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1] + 0.5)
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])

    return m[-1][-1] if not matrix else m


def backtrack(m, s1, s2, i, j):
    if i == 1 or j == 1:
        return ""
    elif s1[i] == s2[j]:
        print(s1[i])
        return backtrack(m, s1, s2, i - 1, j - 1) + s1[i]
    else:
        if m[i][j - 1] > m[i - 1][j]:
            return backtrack(m, s1, s2, i, j - 1)
        else:
            return backtrack(m, s1, s2, i - 1, j)


def get_lcs(s1, s2):
    m = bottom_up_lcs_length(s1, s2, matrix=True)
    backtrack(m, s1, s2, len(s1) - 1, len(s2) - 1)


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

    a = "abdeccbbaede"
    b = "bbdccedacde"

    ##    print(bottom_up_lcs_length(a, b, True))
    ##    print(recursive_lcs_length(a, b))
    ##    print(memoized_recursive_lcs_length(a, b))
    m = bottom_up_lcs_length_partial(a, b, True)
    backtrack(m, a, b, len(a) - 1, len(b) - 1)
    # pprint(bottom_up_lcs(a, b))


##    print(bottom_up_lcs_length(str9, str10))
##    print(recursive_lcs_length(str9, str10))
##    print(memoized_recursive_lcs_length(str9, str10))
##    pprint(bottom_up_lcs(str9, str10))
##
##    print(bottom_up_lcs_length(str3, str4))
##    print(recursive_lcs_length(str3, str4))
##    print(memoized_recursive_lcs_length(str3, str4))
##    pprint(bottom_up_lcs(str3, str4))
##
##    print(bottom_up_lcs_length(str5, str6))
##    print(recursive_lcs_length(str5, str6))
##    print(memoized_recursive_lcs_length(str5, str6))
##    pprint(bottom_up_lcs(str5, str6))
##
##    print(bottom_up_lcs_length(str7, str8))
##    print(recursive_lcs_length(str7, str8))
##    print(memoized_recursive_lcs_length(str7, str8))
##    pprint(bottom_up_lcs(str7, str8))
