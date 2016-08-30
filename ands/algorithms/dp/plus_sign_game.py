#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 01/09/15

Given a string s of numbers (s1 s2 s3...sn),
is it possible to insert some plus signs "+"
in the string so that the remaining expression
is equal to a certain number k?

Example: Is it possible to insert some + signs in 214,
so that the resulting expression is 25?
Yes, if we insert a + sign between 1 and 4,
that is 21 + 4, we obtain 25.

TODO: PROVE THAT THIS PROBLEM EXHIBITS OR NOT OPTIMAL SUBSTRUCTURE!
"""


def _generate_combinations_matrix(p, combinations):
    m = [["" for _ in range(p)] for _ in range(combinations)]

    c = combinations - 1
    interval = combinations // 2

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
        c = combinations - 1
        interval //= 2
        j = interval

    return m


def _build_expressions(string, m):
    combinations = [["" for _ in range(len(m[0]))] for _ in range(len(m))]

    for i, c in enumerate(m):

        result = ""

        for j, sign in enumerate(c):

            if result == "":
                result = string[j] + sign + string[j + 1]
            else:
                result += sign + string[j + 1]

            combinations[i] = result

    return combinations


def _evaluate_combinations(combinations, k):
    """Returns the right combination (if it exists),
    among all the combinations in "combinations",
    of inserting plus signs in a certain string of numbers s,
    such that the resulting expression is equal to k.

    If no combination yields k, None is returned.

    :type combinations : list of str
    :type k : int
    """
    for c in combinations:
        if int(eval(c)) == k:
            return c
    return None


def plus_sign_game(s, k):
    """Given a string s of numbers (s1 s2 s3...sn),
    is it possible to insert_key some plus signs "+"
    in the string so that the remaining expression
    is equal to a certain number k?

    Example: Is it possible to insert_key some + signs in 214,
    so that the resulting expression is 25?
    Yes, if we insert_key a + sign between 1 and 4,
    that is 21 + 4, we obtain 25.

    :type s : str | int
    :type k : int
    """

    s = str(s)

    # Number of places where to place a + sign
    p = len(s) - 1

    # Number of possible combinations
    combinations = 2 ** p

    # Generating a matrix with all possible combinations
    # of alternating between +  and no +
    m = _generate_combinations_matrix(p, combinations)

    # Building all possible expressions
    combinations = _build_expressions(s, m)

    return _evaluate_combinations(combinations, k)


if __name__ == "__main__":
    print(plus_sign_game("21347823", 2000))
    print(plus_sign_game("214", 25))
    print(plus_sign_game("1214", 26))
    print(plus_sign_game("1214", 215))
    print(plus_sign_game("1214", 125))

    # Do not run this script with the following statement uncommented
    # if you are in a hurry.
    # print(plus_sign_game("646805736141599100791159198", 472004))
