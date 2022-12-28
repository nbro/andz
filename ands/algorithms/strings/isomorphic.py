#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 15/03/2022

Updated: 15/03/2022

# Description

See the doc-strings of the isomorphic function below.

# References

- https://www.programcreek.com/2014/05/leetcode-isomorphic-strings-java/

"""

__all__ = ["isomorphic"]


def isomorphic(a: str, b: str) -> bool:
    """Returns true if a and b are isomorphic.

    Two strings a and b are isomorphic if there's a 1-to-1 mapping between the
    chars in a and the chars in b. In other words, we need to replace all
    occurrences of the char x in a with the same char x'. It doesn't matter
    which x' we choose, as long as it makes a become b, and x' was not already
    chosen to replace another x'' in a.

    Example of isomorphic strings:
        - a = "egg"
        - b = "add"
    Explanation: replace "e" with "a" and "g" with "d".

    Example of non-isomorphic strings
        - a = "foo"
        - b = "bar"
    Explanation: we need to replace "o" with "a", but then we need to replace
    "o" with "r", so there is not a 1-to-1 mapping.

    Time complexity: O(n).

    Space complexity: O(n)."""
    assert isinstance(a, str) and isinstance(b, str)

    if len(a) != len(b):
        return False

    a_map = {}
    b_map = {}

    for x, y in zip(a, b):

        # If x is already in a_map, then x already appeared in a. So, we
        # already mapped x to some char, i.e. a_map[x]. If a_map[x] is
        # different from y, then it means that we would need to create another
        # mapping for x, so these strings would not be isomorphic.
        if x in a_map:
            if a_map[x] != y:
                return False
        else:  # x is not in a_map
            # x not in a_map
            if y in b_map:
                # If y in b_map, it ALSO means that there's another char in
                # a_map that maps to y, because we always add both mappings
                # x -> y and y -> x. So, if y in b_map, then we previously
                # added another char to a_map that maps to y, and that char
                # is not x. So, we cannot map x to y now. That means that
                # these strings are not isomorphic.
                assert b_map[y] != x
                return False
            # x is not in a_map and y is not in b_map
            a_map[x] = y
            b_map[y] = x

    return True


def test1():
    # Yes
    a = ""
    b = ""
    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))

    # Yes
    a = "x"
    b = "x"
    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))

    # Yes
    a = "x"
    b = "y"
    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))

    # No
    a = "xx"
    b = "yz"
    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))

    # Yes
    a = "egg"
    b = "add"
    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))

    # Yes. Replace e with a. Replace a with b. Replace o with r.
    a = "eao"
    b = "abr"

    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))

    # No
    a = "foo"
    b = "bar"
    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))

    # Yes.
    a = "acab"
    b = "xcxy"
    print("isomorphic({}, {}) = {}".format(a, b, isomorphic(a, b)))


if __name__ == "__main__":
    test1()
