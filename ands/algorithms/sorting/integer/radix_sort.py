#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 05/03/2022

Updated: 09/03/2022

# Description

## Short Description

Radix sort is a non-comparison sorting algorithm that uses the stable
counting sort as a subroutine. The stability of counting sort is essential for
radix sort to work properly.

## Long Description

Radix-sort assumes that the given list contains integers, each of which has
a w-bit binary representation (for example, w = 32). It sorts the list by
calling w / d times the counting sort algorithm. In the first iteration, it
sorts (with counting sort) the list of integers according to the least
significant d bits of each integer. In the next iteration, it sorts according
to the next least significant d bits. This continues until the last iteration,
where the integers are sorted according to the most significant d bits.

If w / d is not an integer, we can increase w to d⌈w/d⌉, where ⌈⌉ is the
ceiling operation.

## Example

In reality, radix sort can also be applied to non-binary representations.
For example, consider 3-digit decimal numbers: for example, 356, which has 3
digits, each of which can range from 0 to 9. Now, here's an example of how
radix sort would work on a list of 3-digit decimal numbers (this example is
taken from Figure 8.3 of CLRS book, p. 198). Here's the initial list.
list.

            329
            457
            657
            839
            436
            720
            355

We now sort these numbers according to the least significant digit.

            720
            355
            436
            457
            657
            329
            839
              |
    Least significant digit

You can see that the least significant digits, i.e. 0, 5, 6, 7, 7, 9, 9, are
sorted.

We now sort these numbers according to the second least significant digit, so
we obtain

            720
            329
            436
            839
            355
            457
            657
             |
Second least significant digit

You can see that the 2nd least significant digits, 2, 2, 3, 3, 5, 5, 5 are
sorted. However, note that the least significant digits are no longer sorted.
Nevertheless, note that, if we consider the last 2 digits, we have a sorted
list, i.e. 20, 29, 36, 39, 55, 57, 57.

Finally, we sort the numbers according to the most significant digit, to obtain

            329
            355
            436
            457
            657
            720
            839
            |
  Most significant digit

So, the most significant digits are sorted, 3, 3, 4, 4, 6, 7, 8.

So, in this example, we performed 3 iterations of the stable sorting algorithm,
e.g. counting sort.

## Properties

- Non-comparison (integer) sorting algorithm
- Stable (because of the stability of the counting sort, which is used as a
subroutine)
- Not-in-place (at least the implementation below)

## Applications

- Sort records of information that are keyed by multiple fields.
    - Example: sort dates by three keys: year, month, and day.

# Invention

- According to Wikipedia, radix-sort dates back to 1887 to the work of
Herman Hollerith on tabulating machines. It came into come use in 1923 as a
way to sort punched cards. Harold H. Seward, in 1954, developed the first
memory-efficient version.

# Terminology

- Robert Sedgewick and Kevin Wayne in their book "Algorithms" (4th edition),
section 5.1, page 706, call a version of radix-sort applied to strings
"least-significant-digit first (LSD) string sort". There are other similar
algorithms or variations. For example, there's the most-significant-digit first
(MSD) radix sort.

- The "radix" refers to the base of the numbers that are given as input to the
algorithm.

# TODO

- The code used for counting sort here is really very similar to the standalone
counting sort algorithm in the module counting_sort.py, so we might want to
reuse that code.
- Add time and space complexity
- Is it in place?

# References

- "Introduction to Algorithms" (3rd edition), by CLRS, chapter 8.3
- "Algorithms in C", R. Sedgewick, chapter 10, p. 133
- "Algorithms" (4th edition), by Robert Sedgewick and Kevin Wayne
- http://opendatastructures.org/ods-java/11_2_Counting_Sort_Radix_So.html
- https://www.youtube.com/watch?v=YXFI4osELGU
- http://www.allisons.org/ll/AlgDS/Sort/Radix/
- https://wiki.python.org/moin/BitwiseOperators
- https://en.wikipedia.org/wiki/Radix_sort
- https://brilliant.org/wiki/radix-sort/
"""

__all__ = ["radix_sort"]

import math
import sys


def lsd(
    a: list,
    w: int = None,
    # length of strings; we assume fixed-length strings here
    # The value of k can make a big difference in performance. If we can
    # assume e.g. that we're using only ASCII chars, then we know that k
    # is quite small.
    k: int = sys.maxunicode,
    # TODO: support a more general key
    #  other we may need to assume that the first parameter is always a
    #  string (or something that we can index) and index would be the index
    key: callable = lambda string, index: ord(string[index]),
) -> list:
    """The least-significant-digit first (LSD) string sort, which stably sorts
    fixed-length strings.

    This implementation is based on the pseudocode and information given in
    section 5.1 of the book "Algorithms" (4th edition), by Robert Sedgewick and
    Kevin Wayne.

    Time complexity

    +-------------+---------------+---------------+
    |    Best     |     Average   |     Worst     |
    +-------------+---------------+---------------+
    |             | Θ(2*w(n + k)) | Θ(2*w(n + k)) |
    +-------------+---------------+---------------+

    Space complexity: Θ(n + k)."""
    if len(a) == 0:
        return []
    if not isinstance(w, int):
        w = len(a[0])
    if w < 0:
        raise ValueError("w must be >= 0")
    if not all(len(x) == w for x in a):
        raise ValueError(
            "the length of each string in a should be equal to " "w = {}".format(w)
        )

    # TODO: check correctness of key.
    # TODO: check correctness of k, maybe as an assertion, because we may
    #  get index out of range
    # TODO: support also the sort of integers (probably we need to convert them
    #  to strings): see CLRS.
    # TODO: this is in-place, but the algorithm below is not.

    n = len(a)

    b = [None] * n

    for d in range(w - 1, -1, -1):
        # Sort by key-indexed counting on dth char.
        c = [0] * (k + 1)  # In the book, it's denoted by "count"

        # Compute frequency counts.
        for x in range(n):
            c[key(a[x], d) + 1] += 1

        # Transform counts to indices.
        for x in range(k):
            c[x + 1] += c[x]

        # Distribute.
        for x in range(n):
            b[c[key(a[x], d)]] = a[x]
            c[key(a[x], d)] += 1

        # Copy back.
        for x in range(n):
            a[x] = b[x]


# TODO: deal with the case where w is not divisible by d; don't forget the
#  test cases.
# TODO: deal with wrong values for w and d.
# TODO: this implementation of radix-sort fails to sort if e.g. we try to sort
#  numbers that cannot be represented as w-bit integers. For example, if we
#  assume w=8, then we assume 8-bit integers, so integers up to 2^8 = 256. In
#  the tests, we need to take this into account, otherwise, the tests may fail.
def radix_sort(
    a: list,
    w: int = 14,  # We assume 8-bit integers.
    d: int = 8,  # We will sort the integers 1 bit at a time
) -> list:
    """Radix-sort algorithm that sorts w-bit integers with w // d rounds of
    the stable counting sort. At each round, we sort the list according to d
    bits.

    Time complexity

    +--------------+--------------+--------------+
    |    Best      |   Average    |    Worst     |
    +--------------+--------------+--------------+
    |              | Θ(d*(n + k)) | Θ(d*(n + k)) |
    +--------------+--------------+--------------+

    """
    assert isinstance(a, list)
    assert isinstance(w, int)
    assert isinstance(d, int)

    if not all(isinstance(x, int) for x in a):
        raise TypeError("all elements of a should be integers")
    if not all(x >= 0 for x in a):
        raise ValueError("all elements be >= 0")

    if not (1 <= w <= int(math.log2(sys.maxsize)) + 1):
        raise ValueError(
            "w should be an integer in the range "
            "[1, {}]".format(int(math.log2(sys.maxsize)) + 1)
        )

    for x in a:
        if not (0 <= x < 2**w):
            raise ValueError(
                "element {} of 'a' cannot be represented with {} " "bits".format(x, w)
            )

    # We need to consider at least 1 and at most w digit at a time.
    if not (1 <= d <= w):
        raise ValueError("d should be an integer in the range [1, w]")

    if w % d != 0:
        # We could also set w to int(math.floor(w / d)) * d, as suggested here
        # http://opendatastructures.org/ods-java/11_2_Counting_Sort_Radix_So.html
        d = 1

    assert w % d == 0

    # If d == 1, then 1 << d == 1 << 1 == 10 (in binary) == 2 (in decimal).
    k = 1 << d

    def key(x: int, p: int) -> int:
        # x is an element of a
        # p is the current iteration number
        # if d == 1, then p is just the current digit/bit's position/index.

        # (x >> d * p) & (k - 1) is the integer whose binary
        # representation is given by bits
        # (p + 1) * d - 1, ..., p * d of x, where x = a[i].
        #
        # Example
        #
        # Let x = 3, d = 2 and p = 0.
        # Then (x >> d * p) & ((1 << d) - 1) = (3 >> 2 * 0) & ((1 << 2) - 1) =
        # (3 >> 0) & (4 - 1) = 3 & 3 = 3.
        #
        # Let x = 7, d = 2 and p = 1.
        # Then (x >> d * p) & ((1 << d) - 1) = (7 >> 2 * 1) & ((1 << 2) - 1) =
        # (7 >> 2) & (4 - 1) = 1 & 3 = 1.

        # If k == 2, then k - 1 == 1.
        # So, x & 1 means that the output is 1 only if the last digit of the
        # binary representation of x is 1, else it's 0.
        # For example, let x = 3. In binary, 3 == 11, so x & 1 == 3 & 1 ==
        # 11 & 01 = 1. Let x = 2, then 10 & 01 == 0, where 10 is the binary
        # representation of 2. In general, r can be as big as k - 1. In this
        # case, given that k = 2, then as big as 1.
        r = (x >> d * p) & (k - 1)
        assert r in list(range(k))
        return r

    n = len(a)

    # w // d of counting sort.
    for p in range(w // d):
        # This block of code is an adaptation of the counting sort algorithm
        # for this radix sort algorithm.

        # The auxiliary counter list of size k.
        c = [0] * k

        for i in range(n):
            c[key(a[i], p)] += 1

        for i in range(1, k):
            c[i] += c[i - 1]

        # The result list for iteration p.
        b = [None] * n

        for i in range(n - 1, -1, -1):
            c[key(a[i], p)] -= 1
            b[c[key(a[i], p)]] = a[i]

        a = b

    return b


# pylint: disable=missing-function-docstring
def example1():
    a: list = []
    b = radix_sort(a)
    print(b)

    a = [2]
    b = radix_sort(a)
    print(b)

    a = [10, 2]
    b = radix_sort(a)
    print(b)

    # a = [10, 2, -3]
    # b = radix_sort(a)
    # print(b)


# pylint: disable=missing-function-docstring
def example2():
    # Example taken from Sedgewick and Wayne's book, p. 706.
    a = [
        "4PGC938",
        "2IYE230",
        "3CIO720",
        "1ICK750",
        "1OHV845",
        "4JZY524",
        "1ICK750",
        "3CIO720",
        "1OHV845",
        "1OHV845",
        "2RLA629",
        "2RLA629",
        "3ATW723",
    ]

    lsd(a, 7)
    from pprint import pprint  # pylint: disable=import-outside-toplevel

    pprint(a)


if __name__ == "__main__":
    example1()
    example2()
