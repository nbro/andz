#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado
Created: 02/09/2015
Updated: 26/01/2017

## Description

The longest common subsequence or, in short, _lcs_, of _two_ strings `x` and `y`
is a common **measure of similarity** between the two strings.

More specifically the problem is as follows:

    given two strings x = x_1 x_2 .. x_m and y = y_1 y_2 .. y_n,
    what is (the length of) the longest common subsequence between strings `x` and `y`,
    where characters in the subsequences are not necessarily contiguous?
    
The solution is not necessarily unique.
You can find a recursive and a two dynamic programming implementations for the lcs problem.
You can find just one implementation using dynamic programming that actually returns the lcs,
instead of just computing its length, like all other implementations do.

## References

- Introduction to Algorithms (3rd ed.) by CLRS
- Slides by prof. Evanthia Papadopoulou

## Resources

- [https://en.wikipedia.org/wiki/Longest_common_subsequence_problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)

## TODO

- Create a version with case insensitive matching.
"""


def _get_lcs_length_matrix(s1: str, s2: str) -> list:
    """Let m = len(s1) and n = len(s2),
    then this function returns a (m + 1)x(n + 1) matrix,
    specifically it returns a list of length m + 1,
    whose elements are lists of length (n + 1).
    The "+ 1" in (m + 1) and (n + 1) is because the first row and column
    are reserved for the cases where we compare with _empty_ sequences.
    """
    return [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]


def _get_lcs_matrix(s1: str, s2: str) -> list:
    m = []
    for _ in range(len(s1) + 1):
        m.append([])
        for _ in range(len(s2) + 1):
            m[-1].append([])
    return m


def _recursive_lcs_length_aux(s1: str, n: int, s2: str, m: int, result: int) -> int:
    """Helper function of `recursive_lcs_length`."""
    if n == 0 or m == 0:
        return 0
    elif s1[n - 1] == s2[m - 1]:
        result = 1 + _recursive_lcs_length_aux(s1, n - 1, s2, m - 1, result)
    else:
        result = max(_recursive_lcs_length_aux(s1, n - 1, s2, m, result),
                     _recursive_lcs_length_aux(s1, n, s2, m - 1, result))
    return result


def recursive_lcs_length(s1: str, s2: str) -> int:
    """Returns the length of the longest common subsequence between s1 and s2.
    This algorithm uses a recursive solution, as the name suggests,
    but this results in an exponential algorithm.
    
    ### Idea
    Given two strings x and y, how do we find the length of the lcs between x and y?
    
    For every subsequence of x check weather it's a subsequence of y.
    There are 2^n subsequences of x to check, and each subsequence takes O(m) time to check:
    scan y for the first letter, from there scan for the second, and so on.
    
    ### Definition
    
    lcs(i, j) = length of the longest comment subsequence between
    x(i) = x(i)_1, x(i)_2, ..., x(i)_i and y(j) = y(j)_1, y(j)_2, ..., y(j)_j.
    
    where by x(i) it's meant a subsequence of x up to i,
    and by x(i)_i it's meant the ith element of that same subsequence x(i).
    A similar thing can be said for y(j) and y(j)_j.
        
    ### Goal 
    lcs(n, m), where n = length(x) and m = length(y).
    
    ### Algorithm  
  
    If x(i) or y(j) is empty, lcs(i, j) = 0.
    
    If x(i)_i == y(j)_j, then x(i)_i and y(j)_j must be included in the lcs(i, j),
    and we express it as lcs(i, j) = lcs(i - 1, j - 1) + 1,
    where the +1 stands for the inclusion of x(i)_i and y(j)_j.
    
    If x(i)_i != y(j)_j, then we can either skip x(i)_i or y(j)_j (or both):
    we need to choose the best!! So lets see these options more closely.
    
    Option 1: x(i)_i is not in the lcs, then lcs(i, j) = lcs(i - 1, j).
    Option 2: y(j)_j is not in the lcs, then lcs(i, j) = lcs(i, j - 1).
    
    So, basically, what we do is: lcs(i, j) = max(lcs(i - 1, j), lcs(i, j - 1)).
    
    Note that we don't really need to include lcs(i - 1, j - 1),
    for the case where neither x(i)_i nor y(j)_j are included in the lcs(i, j),
    because max(lcs(i - 1, j), lcs(i, j - 1), lcs(i - 1, j - 1)) = max(lcs(i - 1, j), lcs(i, j - 1)),
    i.e. the maximum "profit" can simply be retrieved from lcs(i - 1, j) and lcs(i, j - 1),
    since for sure lcs(i - 1, j - 1) brings less (or equal) profit than lcs(i - 1, j) or lcs(i, j - 1).
    
    #### Summary
    
                +--
                | 0                                   if i == 0 or j == 0.
    lcs(i, j) = | lcs(i - 1, j - 1) + 1               if i, j > 0 and x(i)_i == y(j)_j.
                | max(lcs(i - 1, j), lcs(i, j - 1))   if i, j > 0 and x(i)_i != y(j)_j.
                +--
                
    ### Complexity
    This plain recursive approach is very inefficient, 
    because we keep on recomputing sub-problems.
    
    **Time complexity**: &theta;(m*2^n).
    """
    n = len(s1)
    m = len(s2)
    result = 0
    return _recursive_lcs_length_aux(s1, n, s2, m, result)


def _memoized_recursive_lcs_length_aux(s1: str, n: int, s2: str, m: int, result: list, matrix: list) -> int:
    """Helper function of `recursive_lcs_length`."""
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


def memoized_recursive_lcs_length(s1: str, s2: str) -> int:
    """Returns the length of the longest common subsequence between strings s1 and s2.
    This algorithm uses _memoization_ to improve performance with respect to `recursive_lcs_length`.
    
    If n = length(s1) and m = length(s2), then time complexity of this algorithm O(n*m),
    which is very similar to the bottom-up version (below).
    """
    n = len(s1)
    m = len(s2)
    result = 0
    matrix = [[None for _ in range(len(s2))] for _ in range(len(s1))]
    
    return _memoized_recursive_lcs_length_aux(s1, n, s2, m, result, matrix)


def bottom_up_lcs_length(s1: str, s2: str, matrix: bool=False):
    """Returns the length of the longest common subsequence between strings s1 and s2,
    if `matrix` is set to `False`, 
    else it returns the matrix used to calculate the length of the lcs of sub-problems.
    
    If n = length(s1) and m = length(s2), 
    then the following are the asymptotic complexities of this algorithm.
    
    **Time complexity:** O(n*m)
    **Space complexity:** O(n*m)
    """
    # m is initialized with zeros everywhere
    m = _get_lcs_length_matrix(s1, s2)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):

            # note that i and j start from 1,
            # thus we index s1 and s2 using i - 1 and respectively j - 1,
            # instead of simply i and j.
            if s1[i - 1] == s2[j - 1]: 
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])

    return m[-1][-1] if not matrix else m


def bottom_up_lcs_length_partial(s1: str, s2: str, c1: str, c2: str, partial_weight: int = 0.5, matrix: bool=False):
    """Returns the length of the lcs between strings s1 and s2,
    but considers c1 and c2 partially equal characters,
    and thus instead of adding +1 to the length being computed `partial_weight` is added.
    
    **Time complexity:** O(n*m)
    **Space complexity:** O(n*m)   
    """
    
    m = _get_lcs_length_matrix(s1, s2)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            
            # partial match
            elif (s1[i - 1] == c1 and s2[j - 1] == c2) or (s1[i - 1] == c2 and s2[j - 1] == c1):
                m[i][j] = max(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1] + partial_weight)
                
            else: 
                m[i][j] = max(m[i - 1][j], m[i][j - 1])

    return m[-1][-1] if not matrix else m


def backtrack(m: list, s1: str, s2: str, i: int, j: int):
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


def get_lcs(s1: str, s2: str) -> None:
    m = bottom_up_lcs_length(s1, s2, matrix=True)
    backtrack(m, s1, s2, len(s1) - 1, len(s2) - 1)


def bottom_up_lcs(s1: str, s2: str):
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
    examples = [("acbcf", "abcdaf"),
                ("BANANA", "ATANA"),
                ("abdeccbbaede", "bbdccedacde"),
                ("abe", "eb")]

    for a, b in examples:
        print("a =", a, ", b =", b)
        print(recursive_lcs_length(a, b))
        print(bottom_up_lcs_length(a, b))        
        print(memoized_recursive_lcs_length(a, b))
        print(bottom_up_lcs_length_partial(a, b, 'a', 'e'))
        print()
        
    #backtrack(m, a, b, len(a) - 1, len(b) - 1)
