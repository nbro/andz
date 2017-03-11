#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 15/08/2015

Updated: 10/03/2017

# Description

Given n objects and a "knapsack".
Item i weighs w_i > 0 and has a value v_i > 0.
Knapsack has capacity W.

## Goal

Fill knapsack so as to maximize total value.

# References

- Slides by prof. Evanthia Papadopoulou

"""

from pprint import pprint


def _get_zero_one_knapsack_matrix(total_weight: int, n: int) -> list:
    """Returns a matrix for a dynamic programming solution to the 0/1 knapsack problem.

    The first row of this matrix contains the numbers
    corresponding to the weights of the (sub)problems.
    The first column contains an enumeration of the items,
    starting from the fact that we could not include any item,
    and this is represented with a 0.

    m[0][0] is 0 just because of the alignment,
    it does make any logical sense for this purpose,
    it could be None, or any other value."""
    m = [[0 for _ in range(total_weight + 2)] for _ in range(n + 2)]

    for x in range(1, total_weight + 2):
        m[0][x] = x - 1

    for j in range(1, n + 2):
        m[j][0] = j - 1
        m[j][1] = 0

    return m


def zero_one_knapsack_verbose(total_weight: int, weights, values) -> int:
    """Verbose version of zero_one_knapsack."""
    assert len(weights) == len(values)
    assert total_weight >= 0

    n = len(weights)

    profits = _get_zero_one_knapsack_matrix(total_weight, n)

    print("Initial empty profits matrix:\n")
    pprint(profits)
    print()

    for i in range(2, n + 2):

        for w in range(2, total_weight + 2):

            print("-" * 30)
            print("Weight of item", i - 1, ":", weights[i - 2])
            print("Value of item", i - 1, ":", values[i - 2])
            print("Current total weight:", w - 1)
            print()

            if weights[i - 2] > w - 1:
                profits[i][w] = profits[i - 1][w]
            else:
                profits[i][w] = max(profits[i - 1][w], values[i - 2] + profits[i - 1][w - weights[i - 2]])

            print("Profits matrix after calculation:\n")
            pprint(profits)
            input()

    return profits[-1][-1]


def zero_one_knapsack(total_weight: int, weights: list, values: list) -> int:
    """Returns the maximum profit that can be obtained by
    using items with weights and values and a total_weight.

    This version does not tell which items to pick.

    **Time complexity**: O(n * total_weight), where n is the number of items.
    This is consider a pseudo-polynomial time algorithm, **not** polynomial!

    The decision version of this problem is actually NP-Complete,
    and the running time complexity above does not contradict it:
    total_weight is not polynomial in the length of the input!"""
    assert len(weights) == len(values)
    assert total_weight >= 0

    n = len(weights)

    profits = _get_zero_one_knapsack_matrix(total_weight, n)

    # Iterating through the items
    for i in range(2, n + 2):

        # Iterating through the weights
        for w in range(2, total_weight + 2):

            # If the weight of the (i - 2)th item is greater than w - 1,
            # which is the current weight being analysed.
            # Note that the weights in the matrix `profits` are shifted to the right by 1.
            if weights[i - 2] > w - 1:
                profits[i][w] = profits[i - 1][w]
            else:
                # Note: indices in the `profits` matrix are also shifted 2 positions to the bottom.

                # The weight of the current item is less (or equal) than the total weight,
                # but we need to decide if it is convenient to include this item or not.
                # To do this, we compare if we gain more by including it or not.

                # `profits[i - 1][w]` refers to the profit of not including current item.
                # `values[i - 2]` refers to the value of the current item.
                # `w - weights[i - 2]` is the remaining weight, if we include the current item.
                # Note: `weights[i - 2]` is the weight of the current item.
                profits[i][w] = max(profits[i - 1][w], values[i - 2] + profits[i - 1][w - weights[i - 2]])

    return profits[-1][-1]


def _recursive_01_knapsack_aux(capacity: int, w: list, v: list, value: int) -> int:
    """Either takes the last element or it doesn't.

    This algorithm takes exponential time."""
    if capacity == 0:
        return 0
    if len(w) > 0 and len(v) > 0:
        if w[-1] > capacity:  # We cannot include the nth item
            value = _recursive_01_knapsack_aux(capacity, w[:-1], v[:-1], value)
        else:
            value = max(v[-1] + _recursive_01_knapsack_aux(capacity - w[-1], w[:-1], v[:-1], value),
                        _recursive_01_knapsack_aux(capacity, w[:-1], v[:-1], value))
    return value


def recursive_01_knapsack(total_weight: int, weights: list, values: list):
    assert len(weights) == len(values)
    assert total_weight >= 0

    value = 0
    return _recursive_01_knapsack_aux(total_weight, weights, values, value)


def _memoized_01_knapsack_aux(capacity: int, w: list, v: list, value: int, m: list) -> int:
    """Either takes the last element or it doesn't.

    Memoization version of _recursive_01_knapsack_aux"""
    if capacity == 0:
        return 0

    if m[len(w) - 1][capacity - 1] is not None:
        return m[len(w) - 1][capacity - 1]

    if len(w) > 0 and len(v) > 0:

        if w[-1] > capacity:  # We cannot include the nth item
            value = _memoized_01_knapsack_aux(capacity, w[:-1], v[:-1], value, m)
        else:
            value = max(v[-1] + _memoized_01_knapsack_aux(capacity - w[-1], w[:-1], v[:-1], value, m),
                        _memoized_01_knapsack_aux(capacity, w[:-1], v[:-1], value, m))

    m[len(w) - 1][capacity - 1] = value

    return value


def memoized_01_knapsack(capacity: int, weights: list, values: list) -> int:
    result = 0
    m = [[None for _ in range(capacity)] for _ in range(len(weights))]
    return _memoized_01_knapsack_aux(capacity, weights, values, result, m)


if __name__ == "__main__":
    tw = 7  # total weight that you can carry

    ws = [1, 3, 4, 5]  # weights
    vs = [1, 4, 5, 7]  # values

    print(recursive_01_knapsack(tw, ws, vs))
    print(memoized_01_knapsack(tw, ws, vs))
    # print(zero_one_knapsack_verbose(tw, ws, vs))
