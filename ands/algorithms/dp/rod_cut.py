#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 30/08/15

Based on pseudo-codes that you can find in
"Introduction to Algorithms" (3rd edition) by CLSR.
"""

import sys


def recursive_rod_cut(prices, n):
    """Returns the maximum revenue of cutting a rod of length n.

    It does not return which rod pieces
    you need to pick to obtain the maximum revenue.

    The rod cutting problem is the following:
    given a rod of length n,
    and a table of prices p_i, for i = 0, 1, 2, 3, ...,
    determine the maximum revenue r_n obtainable
    by cutting up the rod and selling the pieces.

    Note that if the price p_n
    for a rod of length n is large enough,
    an optimal solution may require no cutting at all.

    We can cut up a rod of length n in 2^{n - 1} different ways,
    since we have an independent option of cutting, or not cutting,
    at distance i inches from the left end,
    for i = 1, 2, ... , n - 1.

    prices contains the prices for each rod of different length.
    prices[0] would be the price of the rod of length 0 (not useful).
    prices[1] would be the price of the rod of length 1,
    prices[2] would be the price for a rod of length 2, and so on.

    Running time complexity: O(2^n)

    :type prices : list | tuple
    :type n : int
    """

    if n == 0:  # Base case
        return 0

    max_revenue = -sys.maxsize

    for i in range(1, n + 1):  # Last i is n.
        max_revenue = max(max_revenue, prices[i] + recursive_rod_cut(prices, n - i))

    return max_revenue


def _memoized_rod_cut_aux(prices, n, revenues):
    """Auxiliary function for the memoized_rod_cut function.

    :type prices : list | tuple
    :type n : int
    :type revenues : list | tuple
    """
    # If the following condition is true,
    # that would mean that the revenue
    # for a rod of length n has already been "memoised",
    # and we don't need to recompute it again,
    # but we simply return it.
    if revenues[n] >= 0:
        return revenues[n]

    max_revenue = -sys.maxsize

    if n == 0:  # If the size of the rod is 0, then max_revenue is 0.
        max_revenue = 0
    else:
        for i in range(1, n + 1):
            max_revenue = max(max_revenue, prices[i] + _memoized_rod_cut_aux(prices, n - i, revenues))

    # Memoising the maximum revenue for sub-problem with a rod of length n.
    revenues[n] = max_revenue

    return max_revenue


def memoized_rod_cut(prices, n):
    """_Top-down_ dynamic programming version of `recursive_rod_cut`,
    using _memoisation_ to store sub problems' solutions.
    _Memoisation_ is basically the name to the technique 
    of storing what it's been computed previously.

    In this algorithm, as opppose to the plain recursive one,
    instead of repeatedly solving the same subproblems,
    we store the solution to a subproblem in a table,
    the first time we solve the subproblem,
    so that this solution can simply be looked up, if needed again.

    The disadvantge of this solution is that we need additional memory,
    i.e., a table, to store intermediary solutions.

    Running time complexity: theta(n^2)

    :type prices : list | tuple
    :type n : int
    :rtype : int
    """

    # Initialing the revenues list f
    # or the sub-problems length i = 0, 1, 2, ... , n
    # to a small and negative number,
    # which simply means that we have not yet computed
    # the revenue for those sub-problems.
    # Note that revenue values are always nonnegative,
    # unless prices contain negative numbers.
    revenues = [-sys.maxsize] * (n + 1)
    
    return _memoized_rod_cut_aux(prices, n, revenues)


def bottom_up_rod_cut(prices, n):
    """_Bottom-up_ dynamic programming solution to the rod cut problem.

    Running time complexity: theta(n^2)

    :type prices : list | tuple
    :type n : int
    """
    revenues = [-sys.maxsize] * (n + 1)
    revenues[0] = 0  # Revenue for rod of length 0 is 0.

    for i in range(1, n + 1):        
        max_revenue = -sys.maxsize

        for j in range(1, i + 1):
            max_revenue = max(max_revenue, prices[j] + revenues[i - j])

        revenues[i] = max_revenue

    return revenues[n]


def extended_bottom_up_rod_cut(prices, n):
    """Dynamic programming solution to the rod cut problem.

    This dynamic programming version uses a bottom-up approach.

    It returns a tuple, whose first item is a list of the revenues
    and second is a list containing the rod pieces that are used in the revenue.

    Running time complexity: O(n^2)

    :type prices : list
    :type n : int
    :rtype : tuple
    """
    revenues = [-sys.maxsize] * (n + 1)
    s = [[]] * (n + 1)

    revenues[0] = 0
    s[0] = [0]

    for i in range(1, n + 1):

        max_revenue = -sys.maxsize

        for j in range(1, i + 1):
            # Note that j + (i - j) = i.
            # What does this mean, or why should this fact be useful?
            # Note that at each iteration of the outer loop,
            # we are trying to find the max_revenue for a rod of length i
            # (and we want also to find which items we are including to obtain that max_revenue).
            # To obtain a rod of size i, we need at least 2 other smaller rods,
            # unless we do not cut the rod.
            # Now, to obtain a rod of length i,
            # we need to insert_key together a rod of length j < i and a rod of length i - j < j,
            # because j + (i - j) = i, as we stated at the beginning.
            if max_revenue < prices[j] + revenues[i - j]:

                max_revenue = prices[j] + revenues[i - j]

                if revenues[i - j] != 0:
                    s[i] = [j] + s[i - j]
                else:
                    s[i] = [j]

        revenues[i] = max_revenue

    return revenues, s


if __name__ == "__main__":
    
    p1 = [0, 1, 5, 2, 9, 10, 17, 17, 20, 27, 30]

    r, pieces = extended_bottom_up_rod_cut(p1, 10)

    print("Revenues:", r)
    print("Pieces:", pieces)
