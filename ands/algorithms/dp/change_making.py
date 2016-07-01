#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Problem (https://en.wikipedia.org/wiki/Change-making_problem):
Given a set of coins, which is the smallest subset of these coins,
such that summed together yields a certain number n.

This problem is similar to the integer knapsack problem,
the different is that here values=weights.


This problem can be solved using dynamic programming.

Proof that it exhibits optimal substructure.

Suppose S is the optimal solution for making n cents.
Then S' = S - c, where c is a coin in the optimal solution S,
is an optimal solution for making n - c cents.
Suppose S' is not the optimal solution for making n - c cents,
then there exists an optimal solution X != S'.
Now, if we add c to X, we obtain an optimal solution for making n cents,
but this contradicts that fact that S is the optimal solution.
"""

from pprint import pprint


def _get_change_making_matrix(set_of_coins, r):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]

    for i in range(r + 1):
        m[0][i] = i

    return m


def _get_sets_of_coins_matrix(set_of_coins, r):
    m = [[[] for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]

    for i in range(r + 1):
        for x in range(i):
            m[0][i].append(1)

    for j in range(len(set_of_coins) + 1):
        m[j][0] = []

    return m


def change_making(coins, n):
    """This function assumes that all coins are available infinitely.

    I will assume that all coins and n are integers.

    n is number that we need to obtain
    with the fewest number of coins in set of coins.

    Running time complexity: O(number of coins * quantity to obtain)

    :type coins : list of int | tuple of int
    :type n : int
    """
    m = _get_change_making_matrix(coins, n)

    for c in range(1, len(coins) + 1):

        for r in range(1, n + 1):

            if coins[c - 1] == r:
                m[c][r] = 1

            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]

            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])

    return m[-1][-1]


def extended_change_making(coins, rest):
    """Returns the smallest amount of coins
    you need to use to obtain the quantity "rest".

    This function is a super version of change_making.

    Running time complexity: O(number of coins * quantity to obtain)

    :type coins : list of int | tuple of int
    :type rest : int
    """
    m = _get_change_making_matrix(coins, rest)

    # Matrix used to keep track of which coins are used
    p = _get_sets_of_coins_matrix(coins, rest)

    for c in range(1, len(coins) + 1):

        for r in range(1, rest + 1):

             # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1
                p[c][r].append(coins[c - 1])

            # coins[c - 1] cannot be included.
            # We use the previous solution for for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
                p[c][r] = p[c - 1][r]

            # We can use coins[c - 1].
            # We need to decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using coins[c - 1] + the optimal solution for making r -
            # coins[c - 1].
            else:
                if m[c - 1][r] < 1 + m[c][r - coins[c - 1]]:
                    p[c][r] = p[c - 1][r]
                    m[c][r] = m[c - 1][r]
                else:
                    p[c][r] = [coins[c - 1]] + p[c][r - coins[c - 1]]
                    m[c][r] = 1 + m[c][r - coins[c - 1]]

    return p[-1][-1]


def recursive_change_making(coins, n, index):
    # http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
    if n < 0:
        return 0

    if n == 0:
        return 1

    if index == len(coins) and n > 0:
        return 0

    return recursive_change_making(
        coins, n - coins[index], index) + recursive_change_making(coins, n, index + 1)


if __name__ == "__main__":
    pprint(extended_change_making((12, 25, 1, 5), 16))
    pprint(extended_change_making((1, 5, 10, 21, 25), 63))
    print(recursive_change_making((4, 2, 1), 5, 0))
