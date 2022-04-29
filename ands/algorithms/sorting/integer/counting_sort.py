#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 03/03/2022

Updated: 03/03/2022

# Description

Counting sort (not in-place) algorithm.

## Short Description

In a nutshell, this algorithm determines, for each element in the input list
x ∈ a, the number of elements less than x. It uses this information to place
element x directly into its position in the output list. For example, if 17
elements are less than x, then x should be placed in position 18 in the sorted
list.

Counting sort assumes that each of the n = a.length elements in a is an
integer in the range 0 to k - 1, for some integer k, which is the largest
possible number - 1 in a.

## Long description

More specifically, counting sort keeps an auxiliary list c with k elements, all
initialized to 0. We make one pass through the input list a, and, for each
element x ∈ a that we see, we increment c[x] by 1. After we iterate through the
n elements of a and update c, the value at index i of c corresponds to how
many times i appeared in a.

This step takes Θ(n) time.

Once we have c, we can construct the sorted version b of a by iterating through
c and inserting each element x ∈ a a total of c[x] times into the new list b
(or a itself).

Specifically, we continue from the point where c is a list where c[x] refers to
how many times x appears in a. We transform c to a list where c[x] refers to
how many elements are ≤ x. We do this by iterating through c and adding the
value at the previous index to the value at the current index, since the
number of elements ≤ x is equal to the number of elements ≤ x − 1 (i.e. the
value at the previous index) plus the number of elements = x (i.e. the value
at the current index). The final result is a list c where the value of c[x] is
the number of elements ≤ x in [a].

This step takes Θ(k) time.

We now iterate through a backwards starting from the last element of a.
For each element x we see, we check c[x] to find out how many elements are ≤ x.
From this information, we know exactly where we can put x in the sorted list b.
Once we insert x into the sorted list, we decrement c[x] so that if we see a
duplicate element, we know that we have to insert it right before the previous
x. Once we finish iterating through a, we get a sorted list b.

Note that since we iterate through a backwards and decrement c[x] every time
we see x, we preserve the order of duplicates in a. That is, if there are two
3s in a, we map the first 3 to an index before the second 3. This is the
reason why counting sort is a stable sorting algorithm.

This step takes Θ(n) time.

## Properties

Time complexity: Θ(n + k + n) = Θ(2n + k) = Θ(n + k).

Counting sort beats the lower bound of Ω(n * log(n)) because it is not a
comparison sort, instead, counting sort uses the actual values of the
elements to index into a list.

Counting sort is stable: numbers with the same value appear in the output
list in the same order as they do in the input list a. That is, it breaks
ties between two numbers by the rule that whichever number appears first in a
appears first in the output list.

Normally, the property of stability is important only when "satellite data"
are carried around with the element being sorted.

## Applications

Counting sort is often used as a subroutine in radix sort. The stability of
counting sort is important in order for radix sort to work correctly.

In practice, counting sort is used when k = O(n), where n = a.length, in
which case the running time is Θ(n).

## Example

Initial input and counter lists a and c

    a = [4, 1, 3, 4, 3]
    c = [0, 0, 0, 0, 0]

Auxiliary counter list c after first loop

    c = [0, 1, 0, 2, 2]

Counter list c after second loop

    c = [0, 1, 1, 3, 5]

Counter and final sorted lists c and b after last loop

    c = [0, 0, 1, 1, 3]
    b = [1, 3, 3, 4, 4]

# TODO

- Add in-place version of counting sort.

# References
- http://opendatastructures.org/ods-java/11_2_Counting_Sort_Radix_So.html
- Chapter 8.2, Introduction to Algorithms (3rd edition), by CLRS.
- https://courses.csail.mit.edu/6.006/spring11/rec/rec11.pdf
- https://en.wikipedia.org/wiki/Counting_sort
"""

__all__ = ["counting_sort"]


def counting_sort(a: list, k: int = None) -> list:
    # We may not need this, but for now I will assume this is the case.
    assert isinstance(a, list)
    if not all(isinstance(x, int) for x in a):
        raise TypeError("all elements of a should be integers")
    if len(a) == 0:
        return []
    if not isinstance(k, int):
        k = max(a) + 1
    if k < 0:
        raise ValueError("k must be greater than or equal to 0")
    if not all(0 <= x < k for x in a):
        raise ValueError("all elements of a should be between 0 (included) "
                         "and k (excluded)")

    # An auxiliary counter list of size k with counters initialized to 0.
    c = [0 for _ in range(k)]

    for x in range(len(a)):
        c[a[x]] += 1

    # Now, c[x] contains the number of elements = x.

    for x in range(1, k):
        c[x] += c[x - 1]

    # c[x] now contains the number of elements ≤ x.

    # TODO: I probably don't need to create b, but I can modify a in place.
    b = [None] * len(a)

    # We place each element a[x] into its correct sorted position in b.
    #
    # If all n elements are distinct, then, when we first enter the following
    # line, for each a[x], the value c[a[x]] is the correct final position of
    # a[x] in the output array, since there are c[a[x]] elements less than or
    # equal to a[x].
    #
    # Because the elements might not be distinct, we decrement c[a[x]] each
    # time we place a value a[x] into the b array. Decrementing c[a[x]] causes
    # the next input element with a value equal to a[x], if one exists, to go
    # to the position immediately before a[x] in b.
    for x in range(len(a) - 1, -1, -1):
        c[a[x]] -= 1
        b[c[a[x]]] = a[x]

    return b


if __name__ == '__main__':
    a = []
    print(counting_sort(a))
    a = [0]
    print(counting_sort(a))
    a = [10, 2]
    print(counting_sort(a))
    a = [4, 1, 3, 4, 3]
    print(counting_sort(a))

    # It ignores the non-integer second argument and calculates it based on a.
    a = [2, 12, 3]
    print(counting_sort(a, None))

    # Error, as expected.
    # a = [-1, 10]
    # print(counting_sort(a))
