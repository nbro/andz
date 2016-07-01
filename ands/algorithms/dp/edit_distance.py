#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 31/08/15

Calculate the edit distance between two strings.

Based on:
- https://github.com/dossan/interview/blob/master/src/com/interview/dynamic/EditDistance.java
- https://www.youtube.com/watch?v=We3YDTzNXEk
"""

from pprint import pprint


def _get_edit_distance_matrix(s1, s2):
    """Returns a len(s2) + 1 by len(s1) + 1 matrix,
    where the first row and column are filled with 0s,
    the rest is filled with -1s.

    :type s1 : str
    :type s2 : str
    """
    matrix = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for j in range(len(matrix[0])):
        matrix[0][j] = j

    for i in range(len(matrix)):
        matrix[i][0] = i

    return matrix


def _get_coordinates_matrix(s1, s2):
    return [[(0, 0) for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]


def min_edit_distance(s1, s2, return_matrix=False):
    """Returns the edit distance of s1 to s2.

    The edit distance is the minimum number of operations,
    among insertion, deletion and substitution,
    that we need to turn s1 into s2.

    If return_matrix = True,
    the matrix used to calculate the edit distance is returned,
    instead of the edit distance.

    This algorithm uses a dynamic programming solution.

    Running time complexity: O(m * n),
    where m is the length of s1 and n is the length of s2.

    :type s1 : str
    :type s2 : str
    """
    m = _get_edit_distance_matrix(s1, s2)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):
            # How do we obtain the m[i][j] value?
            # We need to look at three positions while iterating:
            # 1. m[i - 1][j -1]
            # 2. m[i][j - 1]
            # 3. m[i - 1][j]

            # s1[i - 1] and s2[j - 1] are the characters

            # (node that i and j start from 1!)
            # that we are currently comparing.
            # If the characters are equal,
            # we don't need to perform any of the operations:
            # insertion, deletion or substitution,
            # and the minimum edit distance to convert s1[i - 1] to s2[j - 1]
            # is the same as the one to convert s1[i] to s[j],
            # because, as stated above, s1[i - 1] and s2[j - 1] are equal,
            # so we don't have to perform any other operation.
            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1]
            else:
                m[i][j] = min(m[i - 1][j - 1] + 1, m[i - 1]
                              [j] + 1, m[i][j - 1] + 1)

        # pprint(m)
        # input()
        # print()

    return m[len(s1)][len(s2)] if not return_matrix else m


def extended_min_edit_distance(s1, s2):
    """Returns a tuple whose first item is the minimum edit distance,
    and the second item is a list of lists containing the instructions
    (in the language of coordinates) to convert a string to another.

    Running time complexity: O(m * n),
    where m is the length of s1 and n is the length of s2.

    :type s1 : str
    :type s2 : str
    """
    m = _get_edit_distance_matrix(s1, s2)

    o = _get_coordinates_matrix(s1, s2)

    for i in range(1, len(s1) + 1):

        for j in range(1, len(s2) + 1):

            coordinates = (i - 1, j - 1)

            if s1[i - 1] == s2[j - 1]:
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

    return m[len(s1)][len(s2)], o


def build_min_edit_instructions(s1, s2, o):
    """Interprets the coordinates o
    and creates a comprehensible list of instructions.

    :type s1 : str
    :type s2 : str
    :type o : list
    """

    i = []  # List for the instructions

    c = (len(s1), len(s2))  # Initial coordinates for o

    while c != (0, 0):
        # Three Cases:
        # 1. Go diagonally (to the left) => Replace, if characters are different
        # 2. Go left  => Remove from the first string
        # 3. Go up  => Remove from the second string

        next_c = o[c[0]][c[1]]

        # Case 1
        if next_c[0] < c[0] and next_c[1] < c[1]:

            if s1[c[0] - 1] != s2[c[1] - 1]:
                i.append("Replace char at index " + str(c[0] - 1) + " (" + s1[c[0] - 1] + ") from '" + s1 +
                         "' with char at index " + str(c[1] - 1) + " (" + s2[c[1] - 1] + ") from '" + s2 + "'.")
        # Case 3
        elif next_c[0] == c[0] and next_c[1] < c[1]:
            i.append("Insert into '" + s1 + "' at index " + str(c[1] - 1) + " char at index "
                     + str(c[1] - 1) + " (" + s2[c[1] - 1] + ") from '" + s2 + "'.")

        # Case 2
        else:  # next_c[0] < c[0] and next_c[1] == c[1]
            i.append("Delete from '" + s1 + "' char at index " +
                     str(c[0] - 1) + " (" + s1[c[0] - 1] + ").")

        c = next_c

    i.reverse()
    return i


def convert(str1, str2):
    print("Edit distance:", min_edit_distance(str1, str2))
    print()

    print("Matrix:")
    pprint(min_edit_distance(str1, str2, return_matrix=True))
    print()

    instructions = build_min_edit_instructions(
        str1, str2, extended_min_edit_distance(str1, str2)[1])

    for i in instructions:
        print(i)


if __name__ == "__main__":
    str1 = "Jazayeri"
    str2 = "Carzaniga"

    str3 = "BANA"
    str4 = "ANA"

    convert(str1, str2)
    convert("kitten", "sitting")
    convert(str3, str3)  # nothing will be indicated to do!
    convert(str3, str4)
