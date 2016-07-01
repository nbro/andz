#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 03/09/15
"""

from pprint import pprint


def m_print(m):
    pprint(m)
    input()


def _check_negativeness(subset):
    """Returns the largest negative number in the subset.
    If no negative number exists, it returns 0."""
    s = 0
    for n in subset:
        if n < s:  # Initially s is 0
            s = n
    return s


def _shift_numbers(subset, smallest):
    m = -smallest
    for i in range(len(subset)):
        subset[i] += m


def _recursive_subset_sum_aux(subset, current_sum, index, n, solution):
    if current_sum == n:  # Solution was found...
        print("Subset found.")

        for i, s in enumerate(solution):
            if s == 1:
                print(subset[i])

    elif index == len(subset):
        return
    else:
        # Include the current ith element
        solution[index] = 1
        current_sum += subset[index]
        _recursive_subset_sum_aux(subset, current_sum, index + 1, n, solution)

        # do not to include the ith element
        solution[index] = 0
        current_sum -= subset[index]
        _recursive_subset_sum_aux(subset, current_sum, index + 1, n, solution)


def recursive_subset_sum(subset, s):
    # Allows negative numbers too...
    c_sum = 0
    i = 0
    solution = [0] * len(subset)

    return _recursive_subset_sum_aux(subset, c_sum, i, s, solution)


def _get_subset_sum_matrix(subset, s):
    m = [[0 for _ in range(s + 1)] for _ in range(len(subset) + 1)]

    for i in range(1, s + 1):
        m[0][i] = 0

    for j in range(0, len(subset) + 1):
        m[j][0] = 1

    return m


def bottom_up_subset_sum(subset, s, return_matrix=False):
    """Returns 1 if there's a subset
    whose sum of the numbers is equal to s,
    if return_matrix == True,
    else it returns the matrix used during the computation.

    NOTE: the subset can only contain positive integers!

    :type subset : list or tuple
    :type s : int
    """

    m = _get_subset_sum_matrix(subset, s)

    for i in range(1, len(subset) + 1):

        for j in range(1, s + 1):

            if subset[i - 1] == j:
                m[i][j] = 1
            else:
                # We can include the current element,
                # because it is less than the current number j.
                if subset[i - 1] <= j:
                    m[i][j] = max(m[i - 1][j], m[i - 1][j - subset[i - 1]])
                else:
                    m[i][j] = m[i - 1][j]

    return m[-1][-1] if not return_matrix else m


if __name__ == "__main__":
    # print(bottom_up_subset_sum((1, 3, 5, 5, 2, 1, 1, 6), 12))

    pprint(bottom_up_subset_sum([2, 2, 2, 6], 6, return_matrix=True))

    print(bottom_up_subset_sum((1, 1, 6), 2, return_matrix=True))

    recursive_subset_sum([-2, 8, 6], 6)
    # recursive_subset_sum((4, 2, 6), 6)
    #recursive_subset_sum((0, 0, 6), 6)
    #recursive_subset_sum((1, 3, 5, 5, 2, 1, 1, 6), 12)
