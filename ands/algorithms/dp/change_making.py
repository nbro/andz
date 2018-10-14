#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 23/08/2015

Updated: 05/08/2018

# Description

The change-making problem may arise in the following way. A cashier has a
number of coins of different denominations at his (or her) disposal and wishes
to make a selection, using the LEAST number of coins, to meet a given total.

It is assumed that the number of coins available in each denomination is not
limited, that each denomination can be represented by a non-negative integer
number, that the total is also a non-negative integer and that we always have
the denomination (or coin) 1.

This problem is a special case of the integer knapsack problem, where each
denomination also corresponds to its weight (or value).

## Linear Programming Formulation

The change-making problem is a constrained minimization problem, so we can
formulate it as a linear programming problem.

Suppose that an unlimited number of coins of denominations c₁, c₂, ..., cᵢ are
made available. So, we have i different denominations (or types of coins) and
we have an unlimited number of denomination c₁, denomination c₂, etc. For
convenience, without loss of generality, these may be ordered so that
c₁ < c₂ < ... < cᵢ. So, for example, c₁ could be 1 cent, c₂ could be 5 cents,
and cᵢ could be 2 euros.

Assuming that xⱼ coins of denomination cⱼ are selected to meet a total C, the
linear programming problem to be solved is then

    minimize    Z = ∑ⱼ₌₁ᶦ xⱼ

    subject to  ∑ xⱼ * cⱼ = C,
                xⱼ >= 0,
                xⱼ is a non-negative integer, and
                C is a non-negative integer

## Dynamic Programming Solution

This problem can be solved using dynamic programming. The recursive formulation
of the change-making problem is

    fᵤ(z) = min(xᵤ + fᵤ₋₁(z - xᵤ * cᵤ)),

where xᵤ is allowed to range over the values 0, 1, 2, ..., ⌈z / cᵤ⌉, where
⌈z / cᵤ⌉ is the greatest integer smaller than or equal to z / cᵤ. For u = 1,
f₁(z) = ⌈z / c₁⌉. So, u is the number of stages, in the multi-stage decision
process, such that, in turn, u = 1, 2, ..., i, where i is the number of
different denominations (or types of coin).

At each stage u, z is ranged from 0 to C in incremental steps (of 1), where C
is the total sum to which the change must be totaled.

# Notes

In the functions below, we use a slightly different notation, because the code
style and the mathematical formulations are usually not 100% compatible and
because it is cumbersome to write mathematical formulations in the doc-strings.

In the formulation above, C (or the parameter n in the implementations) can be
changed exactly because we assume the existence of the denomination 1, even
though it may not be contained in the original list of coins.

The total C (or n in the implementations) is assumed to be a non-negative
integer and the available coins (or denominations) are all assumed to also be
non-negative integers.

Furthermore, there are other ways of solving this problem. For example, we can
also use a greedy strategy. However, the greedy strategy is not guaranteed to
compute the optimal solution (for all inputs).

# TODO

- Show that this problem exhibits optimal sub-structure and contains
overlapping sub-problems.

- Add recursive change_making (for comparison with the dynamic programming
solution).

- Use a 1-dimensional list (instead of a 2d one) to implement the solution, if
possible.

# References

- http://www.dis.uniroma1.it/~bonifaci/algo/doc/COIN.pdf
- https://en.wikipedia.org/wiki/Change-making_problem
- http://www.cs.toronto.edu/~yilan/TA/364/week3_solution.pdf
"""

__all__ = ["change_making", "extended_change_making"]


def _get_change_making_matrix(c: int, n: int) -> list:
    """Returns a list of c + 1 lists of size n + 1. Each of the c + 1 inner
    lists contains zeros, except for the first one, where each element is
    initialized to its index, because we assume that the first coin is 1 and
    it is always available, so that there's always a way to total n. Note that
    the list of coins given may already contain 1 as one of its denominations,
    but we do not know this, in general."""
    m = [[0 for _ in range(n + 1)] for _ in range(c + 1)]

    for i in range(n + 1):
        # m[0], the first list of m, is associated with the usage of the
        # denomination 1, which we assume is always available. So, using
        # denomination 1, we can total i using i 1s.
        m[0][i] = i

    return m


def _get_sets_of_coins_matrix(c: int, n: int) -> list:
    m = [[[] for _ in range(n + 1)] for _ in range(c + 1)]

    for i in range(n + 1):
        for _ in range(i):
            m[0][i].append(1)

    for j in range(c + 1):
        m[j][0] = []

    return m


def _pre_conditions(coins: list, n: int) -> None:
    assert isinstance(coins, list) or isinstance(coins, tuple)
    assert isinstance(n, int)
    assert all(isinstance(c, int) for c in coins)

    if n < 0:
        raise ValueError("n must be non-negative.")
    for c in coins:
        if c < 0:
            raise ValueError("All denominations must be non-negative.")
    if len(coins) == 0:
        raise ValueError("No coins available.")


def change_making(coins: list, n: int) -> int:
    """Returns the minimum number of coins needed to obtain n, which the total
    sum to which the change must be totaled (and it is C in the module's
    doc-strings above).

    Note that, even though the list (or tuple) coins may not contain the
    denomination 1, this function assumes that 1 is always available, so that
    we can always total n.

    Time complexity: O((len(coins) + 1) * (n + 1))."""
    _pre_conditions(coins, n)

    m = _get_change_making_matrix(len(coins), n)

    for c in range(1, len(coins) + 1):

        for z in range(1, n + 1):

            if coins[c - 1] == z:
                m[c][z] = 1

            elif coins[c - 1] > z:
                m[c][z] = m[c - 1][z]

            else:
                m[c][z] = min(m[c - 1][z], 1 + m[c][z - coins[c - 1]])

    # At this point, m[c][z] represents the minimum number of coins needed to
    # obtain (at most) z using the first c coins.
    return m[-1][-1]


def extended_change_making(coins: list, n: int) -> list:
    """Returns a list of integers representing the coins which total n, such
    that the size of the returned list is minimized.

    Note that, even though the list (or tuple) coins may not contain the
    denomination 1, this function assumes that 1 is always available, so that
    we can always total n.

    Time complexity: O((len(coins) + 1) * (n + 1))."""
    _pre_conditions(coins, n)

    m = _get_change_making_matrix(len(coins), n)

    # Matrix used to keep track of which coins are used.
    p = _get_sets_of_coins_matrix(len(coins), n)

    for c in range(1, len(coins) + 1):

        # In this module's doc-strings, z ranges from 0 to C. However, because
        # of implementation details (see _get_change_making_matrix), here we
        # range from 1 to n (or C).
        for z in range(1, n + 1):

            # Just use the coin coins[c - 1].
            if coins[c - 1] == z:
                m[c][z] = 1
                p[c][z].append(coins[c - 1])

            # coins[c - 1] cannot be included. We use the previous solution for
            # for totaling z, excluding coins[c - 1].
            elif coins[c - 1] > z:
                m[c][z] = m[c - 1][z]
                p[c][z] = p[c - 1][z]

            # We can use coins[c - 1]. We need to decide which one of the
            # following solutions is the best:
            #
            #   1. Using the previous solution for totaling z (without using
            #   coins[c - 1]).
            #
            #   2. Using coins[c - 1] + the optimal solution for totaling
            #   z - coins[c - 1].
            else:
                if m[c - 1][z] < 1 + m[c][z - coins[c - 1]]:
                    p[c][z] = p[c - 1][z]
                    m[c][z] = m[c - 1][z]
                else:
                    p[c][z] = [coins[c - 1]] + p[c][z - coins[c - 1]]
                    m[c][z] = 1 + m[c][z - coins[c - 1]]

    assert sum(p[-1][-1]) == n

    return p[-1][-1]
