#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 30/08/2015

Updated: 10/03/2017

# Description

# TODO

- Add description
- Add tests for theses functions
- Add complexity analysis

# References

- [http://www.radford.edu/~nokie/classes/360/dp-rod-cutting.html]
(http://www.radford.edu/~nokie/classes/360/dp-rod-cutting.html)

- Introduction to Algorithms (3rd edition) by CLSR

- Slides by prof. E. Papadopoulou

"""

import sys


def recursive_rod_cut(prices: list, n: int) -> int:
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

    **Time complexity:** O(2^n)."""

    if n == 0:  # Base case
        return 0

    max_revenue = -sys.maxsize

    for i in range(1, n + 1):  # Last i is n.
        max_revenue = max(max_revenue, prices[i] + recursive_rod_cut(prices, n - i))

    return max_revenue


def _memoized_rod_cut_aux(prices: list, n: int, revenues: list, s: list) -> int:
    """Auxiliary function for the memoized_rod_cut function."""

    # If the following condition is true, that would mean that the revenue
    # for a rod of length n has already been "memoised",
    # and we don't need to recompute it again, but we simply return it.
    if revenues[n] >= 0:
        return revenues[n]

    max_revenue = -sys.maxsize

    if n == 0:  # If the size of the rod is 0, then max_revenue is 0.
        max_revenue = 0
    else:
        for i in range(1, n + 1):
            q = _memoized_rod_cut_aux(prices, n - i, revenues, s)

            if prices[i] + q > max_revenue:
                max_revenue = prices[i] + q
                s[n] = i

    # Memoising the maximum revenue for sub-problem with a rod of length n.
    revenues[n] = max_revenue

    return max_revenue


def memoized_rod_cut(prices: list, n: int) -> int:
    """Top-down dynamic programming version of `recursive_rod_cut`,
    using "memoisation" to store sub problems' solutions.

    Memoisation is basically the name to the technique
    of storing what it's been computed previously.

    In this algorithm, as oppose to the plain recursive one,
    instead of repeatedly solving the same sub-problems,
    we store the solution to a sub-problem in a table,
    the first time we solve the sub-problem,
    so that this solution can simply be looked up, if needed again.

    The disadvantage of this solution is that we need additional memory,
    i.e., a table, to store intermediary solutions.

    **Time complexity:** Θ(n^2)."""

    # Initialing the revenues list f
    # or the sub-problems length i = 0, 1, 2, ... , n
    # to a small and negative number,
    # which simply means that we have not yet computed
    # the revenue for those sub-problems.
    # Note that revenue values are always non-negative,
    # unless prices contain negative numbers.
    revenues = [-sys.maxsize] * (n + 1)

    # optimal first cut for rods of length 0..n
    s = [0] * (n + 1)

    return _memoized_rod_cut_aux(prices, n, revenues, s), s


def bottom_up_rod_cut(prices: list, n: int) -> int:
    """Bottom-up dynamic programming solution to the rod cut problem.

    **Time complexity:** Θ(n^2)."""
    revenues = [-sys.maxsize] * (n + 1)
    revenues[0] = 0  # Revenue for rod of length 0 is 0.

    for i in range(1, n + 1):
        max_revenue = -sys.maxsize

        for j in range(1, i + 1):  # Find the max cut position for length i
            max_revenue = max(max_revenue, prices[j] + revenues[i - j])

        revenues[i] = max_revenue

    return revenues[n]


def extended_bottom_up_rod_cut(prices: list, n: int) -> tuple:
    """Dynamic programming solution to the rod cut problem.

    This dynamic programming version uses a bottom-up approach.

    It returns a tuple, whose first item is a list of the revenues
    and second is a list containing the rod pieces that are used in the revenue.

    **Time complexity:** O(2^n)."""
    revenues = [-sys.maxsize] * (n + 1)
    s = [[]] * (n + 1)  # Used to store the optimal choices

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
            # we need to insert together a rod of length j < i and a rod of length i - j < j,
            # because j + (i - j) = i, as we stated at the beginning.
            if max_revenue < prices[j] + revenues[i - j]:

                max_revenue = prices[j] + revenues[i - j]

                if revenues[i - j] != 0:
                    s[i] = [j] + s[i - j]
                else:
                    # revenue[i] (current) uses a rod of length j
                    # left most cut is at j
                    s[i] = [j]

        revenues[i] = max_revenue

    return revenues, s


def rod_cut_solution_print(prices: list, n: int, s: list) -> None:
    """`prices` is the list of initial prices.

    `n` is the number of those prices - 1.

    `s` is the solution returned by `memoized_rod_cut`."""
    while n > 0:
        print(s[n], end=" ")
        n = n - s[n]
    print()


if __name__ == "__main__":
    p1 = [0, 1, 5, 8, 9, 10, 17, 17, 20]


    def test0():
        r = recursive_rod_cut(p1, len(p1) - 1)
        print("Revenue:", r)
        print("--------------------------------------------")


    def test1():
        r, s = memoized_rod_cut(p1, len(p1) - 1)
        print("Revenue:", r)
        print("s:", s)
        rod_cut_solution_print(p1, len(p1) - 1, s)
        print("--------------------------------------------")


    def test2():
        r = bottom_up_rod_cut(p1, len(p1) - 1)
        print("Revenue:", r)
        print("--------------------------------------------")


    def test3():
        r, s = extended_bottom_up_rod_cut(p1, len(p1) - 1)
        print("Revenues:", r)
        print("s:", s)
        print("--------------------------------------------")


    test0()
    test1()
    test2()
    test3()
