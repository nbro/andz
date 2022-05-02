#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 01/09/2015

Updated: 19/09/2017

# Description

Given a string s of numbers (s₁ s₂ s₃ ... sᵢ), is it possible to insert some
plus signs (that is, a +) in the string so that the remaining expression is
equal to a certain number k?

## Example

Is it possible to insert some + signs in 214, so that the resulting expression
is 25? Yes, if we insert a + sign between 1 and 4, that is 21 + 4, we obtain 25.

# TODO

- Prove that this problem exhibits or NOT optimal substructure and overlapping
sub-problems.
- Add complexity analysis for current algorithms.
"""


def _generate_combinations_matrix(p: int, num_of_combinations: int) -> list:
    m = [["" for _ in range(p)] for _ in range(num_of_combinations)]

    c = num_of_combinations - 1
    interval = num_of_combinations // 2

    j = interval
    sign = "+"

    for i in range(p):

        while c >= 0:

            m[c][i] = sign
            c -= 1
            j -= 1

            if j == 0:
                j = interval
                sign = "" if sign == "+" else "+"

        sign = "+"
        c = num_of_combinations - 1
        interval //= 2
        j = interval

    return m


def _build_expressions(s: str, m: list) -> list:
    combinations = [["" for _ in range(len(m[0]))] for _ in range(len(m))]

    for i, c in enumerate(m):
        result = ""

        for j, sign in enumerate(c):
            if result == "":
                result = s[j] + sign + s[j + 1]
            else:
                result += sign + s[j + 1]

            combinations[i] = result

    return combinations


def _evaluate_combinations(combinations: list, k: int) -> str:
    """Returns the right combination (if it exists), among all the combinations
    in "combinations", of inserting plus signs in a certain string of numbers s,
    such that the resulting expression is equal to k.

    If no combination yields k, None is returned."""
    for c in combinations:
        if int(eval(c)) == k:
            return c


def plus_sign_game(s: int, k: int) -> str:
    """Returns a modified expression of s with inserted + signs, so that the
    evaluated expression is equal to k. If no such expression is possible, then
    None is returned."""

    s = str(s)

    # Number of places where to place a + sign.
    p = len(s) - 1

    # Number of possible combinations.
    num_of_combinations = 2 ** p

    # Generating a matrix with all possible combinations of alternating between
    # + and no +.
    m = _generate_combinations_matrix(p, num_of_combinations)

    # Building all possible expressions.
    combinations = _build_expressions(s, m)

    return _evaluate_combinations(combinations, k)


if __name__ == "__main__":
    print(plus_sign_game("21347823", 2000))
    print(plus_sign_game("214", 25))
    print(plus_sign_game("1214", 26))
    print(plus_sign_game("1214", 215))
    print(plus_sign_game("1214", 125))
    # Do not run this script with the following line uncommented.
    # print(plus_sign_game("646805736141599100791159198", 472004))
