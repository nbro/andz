#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 03/03/2022

Updated: 07/03/2022

# Description

Counting sort (not in-place) algorithm.

## Short Description

Counting sort determines, for each element in the input list x ∈ a, the number
of elements less than x. It uses this information to place element x directly
into its position in the output list. For example, if 17 elements are less
than x, then x should be placed in position 18 in the sorted list.

Counting sort assumes that each of the n = len(a) elements in a is an
integer in the range 0 to k - 1, for some integer k, which is the largest
possible number - 1 (although some descriptions and implementations assume
that k is the largest possible) in a. However, note that these integers,
sometimes called "keys" in this context, can have other associated data
(values).

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
the number of elements ≤ x in a.

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

The 2nd and 3rd loop can be combined if the keys don't have any other
associated data, because, in that case, the same numbers are really
indistinguishable, so if have, say, three 5s, we can simply put them their
correct position without caring with 5 we place before another.

## Properties

Time complexity: Θ(n + k + n) = Θ(2n + k) = Θ(n + k).

If k = O(n), then the time complexity is Θ(n), so counting sort because a
linear-time sorting algorithm. Thomas H. Cormen et al. state that, in practice,
counting sort is used when k = O(n).

Counting sort beats the lower bound of Ω(n * log(n)) because it is not a
comparison sort, instead, counting sort uses the actual values of the
elements to index into a list.

Counting sort is stable: numbers with the same value (e.g. two 2s) appear in
the output list in the same order as they do in the input list a. So, for
example, if we have an initial list a = [1, 2, 3, 2]. The first 2 at index
x = 1 will appear before the second 2 at index x = 3 in the sorted list b.

The stability of a sorting algorithm can be important for multiple reasons.
For example, let's say that we want to sort the array
[(1, "no"), (0, "ok"), (1, "yes")]. If we sort this array according to
the first elements of the tuples, then (1, "no") would still come before
(1, "yes") in the sorted list, i.e. the sorted list would be
[(0, "ok"), (1, "no"), (1, "yes")] and not [(0, "ok"), (1, "yes"), (1, "no")].
If this property is important, then counting sort can be useful.

## Example

Initial input list a that we want to sort.

    a = [4, 1, 3, 4, 3]

Create the counter list and initialise all elements to zero.

    c = [0, 0, 0, 0, 0]

After the first loop, the auxiliary counter list c looks as follows.

        Number of times 4 appears in a
                     ^
                     |
    c = [0, 1, 0, 2, 2]
               |
               v
    number of times 2 appears in a


So, the index i in c correspond to the number i in the sequence {0,.. k - 1}.

After the second loop, the counter list c is

       number of elements <= to number 3
       in fact, there is one 1 and two 3s, so c[3] = 1 + 2 = 3.
                  ^
                  |
    c = [0, 1, 1, 3, 5]
            |
            v
    number of elements <= to number 1
    in fact, there's only one 1 and no zero, so c[1] = 1

Final loop

   b = [None, None, None, None, None]

Iteration x = n - 1 = 4, where n = 5.

    a = [4, 1, 3, 4, 3]
                     |
                     x

    // There are 3 numbers <= 3
    c[x] = c[3] = 3
    c = [0, 1, 1, 3, 5]

    // The position of x=3 is at c[3] - 1 = 2
    // We decrement first c[3] because the indices are shifted by 1,
    // and the maximum value in c is k = n + 1.
    c[3] <- c[3] - 1 = 2
    c = [0, 1, 1, 2, 5]

    b[c[3]] = b[2] <- a[x] = 3
    b = [None, None, 3, None, None]

Iteration x = n - 2 = 3.

    a = [4, 1, 3, 4, 3]
                  |
                  x

    // There are 5 numbers <= 4
    c[x] = c[4] = 5
    c = [0, 1, 1, 2, 5]

    // The position of x=4 is at c[4] - 1 = 4
    c[4] <- c[4] - 1 = 4
    c = [0, 1, 1, 2, 4]

    b[c[4]] = b[4] <- a[x] = 4
    b = [None, None, 3, None, 4]

Iteration x = n - 3 = 2.

    a = [4, 1, 3, 4, 3]
               |
               x

    c[x] = c[3] = 2
    c = [0, 1, 1, 2, 4]

    c[3] <- c[3] - 1 = 1
    c = [0, 1, 1, 1, 4]

    b[c[3]] = b[1] <- a[x] = 3
    b = [None, 3, 3, None, 4]


Iteration x = n - 4 = 1.

    a = [4, 1, 3, 4, 3]
            |
            x

    c[x] = c[1] = 1
    c = [0, 1, 1, 1, 4]

    c[1] <- c[1] - 1 = 0
    c = [0, 0, 1, 1, 4]

    b[c[1]] = b[0] <- a[x] = 1
    b = [1, 3, 3, None, 4]

Iteration x = n - 5 = 0.

    a = [4, 1, 3, 4, 3]
         |
         x

    c[x] = c[4] = 4
    c = [0, 1, 1, 1, 4]

    c[4] <- c[4] - 1 = 3
    c = [0, 0, 1, 1, 3]

    b[c[4]] = b[3] <- a[x] = 4
    b = [1, 3, 3, 4, 4]

The final sorted list b and the counter are

    b = [1, 3, 3, 4, 4]

    c = [0, 0, 1, 1, 3]

# Applications

- Counting sort is often used as a subroutine in radix sort.
    - The stability of counting sort is important in order for radix sort to
    work correctly.
- sort strings by the first (second, third, etc.) letter
- sort phone numbers by area code

# Invention

Counting sort was invented by Harold H. Seward in 1954 in the paper
"Information sorting in the application of electronic digital computers to
business operations", section "2.4.6 Internal Sorting by Floating Digital
Sort", according to Donald Knuth.

# Terminology

- Counting sort is also called "key-indexed counting" by Robert Sedgewick and
Kevin Wayne in their book "Algorithms" (4th edition), section 5.1, page 703,
but it's in the context of sorting strings.

- k is also called "radix"; this terminology will clarify why radix-sort,
which uses counting sort as a subroutine, is called radix-sort. In Sedgewick
and Wayne's book, k is denoted by R to remind us that it refers to the radix.

# References

- http://opendatastructures.org/ods-java/11_2_Counting_Sort_Radix_So.html
- Chapter 8.2, "Introduction to Algorithms" (3rd edition), by CLRS.
- Section 5.1, p. 703, "Algorithms" (4th edition), by Robert Sedgewick and
Kevin Wayne
- "31 2 Key Indexed Counting"
(https://www.youtube.com/watch?v=WrPm-Eqoicg&ab_channel=ComputerScience) video
lesson on "key-indexed counting" by Robert Sedgewick.
- https://courses.csail.mit.edu/6.006/spring11/rec/rec11.pdf
- https://en.wikipedia.org/wiki/Counting_sort
- https://www.ime.usp.br/~yoshi/Sedgewick/Algs4th/Slides/51StringSorts.pdf
"""

__all__ = ["counting_sort"]

def counting_sort(a: list,
                  k: int = None,
                  key: callable = lambda x: x,
                  sedgewick_wayne: bool = False) -> list:
    """Counting sort algorithm, which is a stable algorithm. So, if
    a[i] == a[j] and i < j, then a[i] still appears before a[j] in the sorted
    list. It's also not in-place.

    Time complexity

    +-------------+-------------+-------------+
    |    Best     |   Average   |    Worst    |
    +-------------+-------------+-------------+
    |             |  Θ(n + k)   |  Θ(n + k)   |
    +-------------+-------------+-------------+

    Space complexity: Θ(n + k)."""
    assert isinstance(a, list)
    assert isinstance(sedgewick_wayne, bool)

    n = len(a)

    # If a is empty, return an empty list, and it does not check the
    # correctness of any other argument.
    if n == 0:
        return []

    if not callable(key):
        raise TypeError("key should be a function")

    try:
        for x in a:
            key(x)
    except Exception:
        raise KeyError("key is not valid")

    if not all(isinstance(key(x), int) for x in a):
        raise TypeError("the key attribute of each element of a should be an "
                        "int")

    # In Sedgewick and Wayne's book, k is denoted by R.
    if not isinstance(k, int):
        k = key(max(a, key=key)) + 1

    if k < 0:
        raise ValueError("k must be greater than or equal to 0")

    if not all(0 <= key(x) < k for x in a):
        raise ValueError("the key of each element in a should be between 0 "
                         "(included) and k (excluded)")

    # In Sedgewick and Wayne's book, b is denoted by aux.
    b = [None] * n

    def sw():
        # This implementation follows closely Sedgewick and Wayne's book.
        # In Sedgewick and Wayne's book, c is denoted by count.
        # c[0] will always be 0.
        c = [0] * (k + 1)

        # Compute frequency counts.
        for x in range(n):
            c[key(a[x]) + 1] += 1

        # Transform counts to indices.
        for x in range(k):
            c[x + 1] += c[x]

        # Distribute the records.
        for x in range(n):
            b[c[key(a[x])]] = a[x]
            c[key(a[x])] += 1

    def default():
        # This implementation is based on
        # http://opendatastructures.org/ods-java/11_2_Counting_Sort_Radix_So.html.

        # An auxiliary counter list of size k with counters initialized to 0.
        c = [0] * k

        for x in range(n):
            c[key(a[x])] += 1

        # Now, c[x] contains the number of elements = x.

        for x in range(1, k):
            c[x] += c[x - 1]

        # c[x] now contains the number of elements ≤ x.

        # We place each element a[x] into its correct sorted position in b.
        #
        # If all n keys are distinct, then, when we first enter the
        # following line, for each key(a[x]), the value c[key(a[x])] is the
        # correct final position of key(a[x]) in the output list, since there
        # are c[key(a[x])] elements less than or equal to a[x].
        #
        # Because the elements might not be distinct, we decrement
        # c[key(a[x])] each time we place a value a[x] into the list b.
        # Decrementing c[key(a[x])] causes the next input element with a value
        # equal to a[x], if one exists, to go to the position immediately
        # before a[x] in b.
        #
        # If we started the loop from 0 to n - 1, this implementation
        # would still produce a sorted list, but it would not be stable. We
        # can easily see this from the example given in the doc-strings above.
        # However, R. Sedgewick and K. Wayne (section 5.1, p. 703, of
        # "Algorithms" (4th edition)) implement it slightly differently. See
        # the function sw().
        for x in range(n - 1, -1, -1):
            c[key(a[x])] -= 1
            b[c[key(a[x])]] = a[x]

    if sedgewick_wayne:
        sw()
    else:
        default()

    return b


def example1():
    a: list = []
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


def example2():
    # Example taken from R. Sedgewick and K. Wayne's book "Algorithms"
    # (4th edition), section 5.1, p. 703.
    a = [
        (2, "Anderson"),
        (3, "Brown"),
        (3, "Davis"),
        (4, "Garcia"),
        (1, "Harris"),
        (3, "Jackson"),
        (4, "Johnson"),
        (3, "Jones"),
        (1, "Martin"),
        (2, "Martinez"),
        (2, "Miller"),
        (1, "Moore"),
        (2, "Robinson"),
        (4, "Smith"),
        (3, "Taylor"),
        (4, "Thomas"),
        (4, "Thompson"),
        (2, "White"),
        (3, "Williams"),
        (4, "Wilson"),
    ]

    from pprint import pprint

    key = lambda x: x[0]

    b = counting_sort(a, key=key)
    pprint(b)
    assert b is not a

    pprint(counting_sort(a, key=key))


def example3():
    a = [(1, "no"), (0, "ok"), (1, "yes")]
    from pprint import pprint

    key = lambda x: x[0]
    b = counting_sort(a, key=key, sedgewick_wayne=True)
    pprint(b)


def example4():
    # Raises an exception (as expected).
    a = [(1, "no"), (0, "ok"), (1, "yes")]
    from pprint import pprint

    key = lambda x: x[3]
    b = counting_sort(a, key=key, sedgewick_wayne=True)
    pprint(b)


if __name__ == '__main__':
    example1()
    example2()
    example3()
    example4()
