#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 31/08/2015

Updated: 07/03/2018

# Description

Calculate the edit distance between two strings.

# TODO

- Add a better description of the problem and of possible solutions.
- Add complexity analysis

# References

- https://github.com/dossan/interview/blob/master/src/com/interview/dynamic/EditDistance.java
- https://www.youtube.com/watch?v=We3YDTzNXEk
"""

__all__ = ["min_edit_distance", "extended_min_edit_distance",
           "build_min_edit_instructions"]


def _get_edit_distance_matrix(x: str, y: str) -> list:
    """Returns a len(y) + 1 by len(x) + 1 matrix, where the first row and column
    are filled with 0s and the rest is filled with -1s."""
    matrix = [[-1 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    for j in range(len(matrix[0])):
        matrix[0][j] = j

    for i, _ in enumerate(matrix):
        matrix[i][0] = i

    return matrix


def _get_coordinates_matrix(x: str, y: str) -> list:
    return [[(0, 0) for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]


def min_edit_distance(x: str, y: str, return_matrix: bool = False) -> object:
    """Returns the edit distance of x to y, where x and y are two strings.

    The edit distance is the minimum number of operations, among insertion,
    deletion and substitution, that we need to turn x into y.

    If return_matrix = True, the matrix used to calculate the edit distance is
    returned, instead of the edit distance.

    This algorithm uses a dynamic programming solution.

    Time complexity: O(m * n), where m = len(x) and n = len(y)."""
    m = _get_edit_distance_matrix(x, y)

    for i in range(1, len(x) + 1):

        for j in range(1, len(y) + 1):
            # How do we obtain the m[i][j] value?
            # We need to look at three positions while iterating:
            # 1. m[i - 1][j -1]
            # 2. m[i][j - 1]
            # 3. m[i - 1][j]

            # x[i - 1] and y[j - 1] are the characters.

            # Note: i and j start from 1.

            # If the characters are equal, we don't need to perform any of the
            # operations: insertion, deletion or substitution, and the minimum
            # edit distance to convert x[i - 1] to y[j - 1] is the same as the
            # one to convert x[i] to s[j], because, as stated above, x[i - 1]
            # and y[j - 1] are equal, so we don't have to perform any other
            # operation.
            if x[i - 1] == y[j - 1]:
                m[i][j] = m[i - 1][j - 1]
            else:
                m[i][j] = min(m[i - 1][j - 1] + 1, m[i - 1]
                [j] + 1, m[i][j - 1] + 1)

    return m[len(x)][len(y)] if not return_matrix else m


def extended_min_edit_distance(x: str, y: str) -> tuple:
    """Returns a tuple whose first item is the minimum edit distance, and the
    second item is a list of lists containing the instructions (in the "language
    of coordinates") to convert a string to another.

    Time complexity: O(m * n), where m = len(x) and n = len(y)."""
    m = _get_edit_distance_matrix(x, y)

    o = _get_coordinates_matrix(x, y)

    for i in range(1, len(x) + 1):

        for j in range(1, len(y) + 1):

            coordinates = (i - 1, j - 1)

            if x[i - 1] == y[j - 1]:
                m[i][j] = m[i - 1][j - 1]
            else:
                _min = -1
                if m[i][j - 1] + 1 < m[i - 1][j] + 1:
                    _min = m[i][j - 1] + 1
                    coordinates = (i, j - 1)
                else:
                    _min = m[i - 1][j] + 1
                    coordinates = (i - 1, j)

                if m[i - 1][j - 1] + 1 < _min:
                    _min = m[i - 1][j - 1] + 1
                    coordinates = (i - 1, j - 1)

                m[i][j] = _min
            o[i][j] = coordinates

    return m[len(x)][len(y)], o


def build_min_edit_instructions(x: str, y: str, o: list) -> list:
    """Interprets the coordinates o (returned as second item of the tuple
    returned by extended_min_edit_distance) and creates a comprehensible list of
    instructions.

    The indices mentioned in the instructions are with respect to the original
    strings x and y and not with respect to the strings after having applied an
    modification, after an instruction."""

    instructions = []  # List for the instructions.

    c = (len(x), len(y))  # Initial coordinates for o.

    while c != (0, 0):
        # 3 cases:
        # 1. Go diagonally (to the left) => replace, if characters are different
        # 2. Go left  => remove from the first string
        # 3. Go up  => remove from the second string

        next_c = o[c[0]][c[1]]

        # Case 1.
        if next_c[0] < c[0] and next_c[1] < c[1]:

            if x[c[0] - 1] != y[c[1] - 1]:
                instructions.append("Replace char at index " + str(c[0] - 1) +
                                    " (" + x[c[0] - 1] + ") from '" + x +
                                    "' with char at index " + str(c[1] - 1) +
                                    " (" + y[c[1] - 1] + ") from '" + y + "'.")
        # Case 3.
        elif next_c[0] == c[0] and next_c[1] < c[1]:
            instructions.append("Insert into '" + x + "' at index " +
                                str(c[1] - 1) + " char at index " +
                                str(c[1] - 1) + " (" + y[c[1] - 1] + ") from '"
                                + y + "'.")

        # Case 2.
        else:  # next_c[0] < c[0] and next_c[1] == c[1]
            instructions.append("Delete from '" + x + "' char at index " +
                                str(c[0] - 1) + " (" + x[c[0] - 1] + ").")

        c = next_c

    instructions.reverse()
    return instructions


if __name__ == "__main__":
    x = "Jazayeri"
    y = "Carzaniga"

    coordinates = extended_min_edit_distance(x, y)[1]
    instructions = build_min_edit_instructions(x, y, coordinates)

    """
    How Jazayeri should be turned into Carzaniga:

    Jazayeri
    Cazayeri
    Carzayeri
    Carzayeri
    Carzaneri
    Carzaniri
    Carzanigi
    Carzaniga
    """

    for i in instructions:
        print(i)
