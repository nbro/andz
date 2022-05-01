#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 23/08/2015

Updated: 18/09/2017

# Description

Given a set of coins, which is the smallest subset of these coins, such that
summed together yields a certain number n?

This problem is similar to the integer knapsack problem, the difference is that
here values=weights.

This problem can be solved using dynamic programming.

## Proof

### Proof that it exhibits optimal substructure.

Suppose S is the optimal solution for making n cents. Then S' = S - c, where c
is a coin in the optimal solution S, is an optimal solution for making n - c
cents. Suppose S' is not the optimal solution for making n - c cents, then there
exists an optimal solution X != S'. Now, if we add c to X, we obtain an optimal
solution for making n cents, but this contradicts that fact that S is the
optimal solution.

# TODO

- Add complexity analysis
- Add proof of overlapping sub-problems
- Add recursive change_making, for comparison with the dynamic programming
solution.

# References

- https://en.wikipedia.org/wiki/Change-making_problem
- http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
"""

__all__ = ["change_making", "extended_change_making"]


def _get_change_making_matrix(coins: list, rest: int) -> list:
    m = [[0 for _ in range(rest + 1)] for _ in range(len(coins) + 1)]

    for i in range(rest + 1):
        m[0][i] = i

    return m


def _get_sets_of_coins_matrix(coins: list, rest: int) -> list:
    m = [[[] for _ in range(rest + 1)] for _ in range(len(coins) + 1)]

    for i in range(rest + 1):
        for _ in range(i):
            m[0][i].append(1)

    for j in range(len(coins) + 1):
        m[j][0] = []

    return m


def change_making(coins: list, rest: int) -> int:
    """Returns the minimum number of coins needed to obtain at most rest.

    This function assumes that all coins are available infinitely, that is, if
    coins = [c1, c2, ..., cn], then it assumes that we have at our disposal an
    arbitrary number of c1, c2, ..., or cn coins.

    Assumes that all coins and rest are integers.

    rest is number that we need to obtain with the fewest number of coins in set
    of coins.

    Time complexity: O(n * rest), where "number of coins" == n == len(ls) and
    "quantity to obtain" == rest."""
    m = _get_change_making_matrix(coins, rest)

    for c in range(1, len(coins) + 1):

        for r in range(1, rest + 1):

            if coins[c - 1] == r:
                m[c][r] = 1

            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]

            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])

    return m[-1][-1]


def extended_change_making(coins: list, rest: int) -> list:
    """Returns a list of integers representing the coins to use to obtain at
    most rest, such that the size of the returned list is minimized.

    This function is a "super" version of change_making, in that this function
    also returns the list of coins to obtain rest, and not simply the number of
    coins required (as change_making does).

    This function assumes that all coins are available infinitely, that is, if
    coins = [c1, c2, ..., cn], then it assumes that we have at our disposal an
    arbitrary number of c1, c2, ..., or cn coins.

    Assumes that all coins and rest are integers.

    Time complexity: O(n * rest), where "number of coins" == n == len(ls) and
    "quantity to obtain" == rest."""
    m = _get_change_making_matrix(coins, rest)

    # Matrix used to keep track of which coins are used
    p = _get_sets_of_coins_matrix(coins, rest)

    for c in range(1, len(coins) + 1):

        for r in range(1, rest + 1):

            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1
                p[c][r].append(coins[c - 1])

            # coins[c - 1] cannot be included. We use the previous solution for
            # for making r, excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
                p[c][r] = p[c - 1][r]

            # We can use coins[c - 1]. We need to decide which one of the
            # following solutions is the best:
            # 1. Using the previous solution for making r (without using
            # coins[c - 1]).
            # 2. Using coins[c - 1] + the optimal solution for making
            # r - coins[c - 1].
            else:
                if m[c - 1][r] < 1 + m[c][r - coins[c - 1]]:
                    p[c][r] = p[c - 1][r]
                    m[c][r] = m[c - 1][r]
                else:
                    p[c][r] = [coins[c - 1]] + p[c][r - coins[c - 1]]
                    m[c][r] = 1 + m[c][r - coins[c - 1]]

    return p[-1][-1]
