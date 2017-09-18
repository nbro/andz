#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 09/09/2015

Updated: 20/08/2017

# Description

Merge-sort is a sorting algorithm which follows the divide-and-conquer strategy.

In merge-sort the unsorted list is divided into N sub-lists, each having one element.

A list of one element is by definition sorted. And merging two sorted lists of one element is easy,
since you just need to understand which of the 2 elements from the 2 different lists is greater or smaller.

So once all 1-element lists have been merged in 2-elements lists,
we do the same recursively until we have just 1 list.

## Example

Suppose we have initially the following list L of numbers:

    +-------------------+
    | 5 | 6 | 2 | 9 | 1 |
    +-------------------+

Then we divide this list into 2 sub-lists as follows. Let's call this first sub-list L1:

    +-----------+
    | 5 | 6 | 2 |
    +-----------+

and this second let's call it L2

    +-------+
    | 9 | 1 |
    +-------+

Then we keep diving these two lists in half to obtain sub-lists of at most 1 element.
Let's first divide L1 into other two smaller sub-lists.
The first let's call it L11 and the second L12.

    +-------+
    | 5 | 6 |
    +-------+

and

    +---+
    | 2 |
    +---+

Now we divide L2 in two sub-lists. The first we call it L21 and the second L22.


    +---+
    | 9 |
    +---+

and

    +---+
    | 1 |
    +---+

Now apart from L11, all lists have already just one element.
So, let's further divide L11 in two smaller sub-lists, named respectively L111 and L112.

    +---+
    | 5 |
    +---+

and


    +---+
    | 6 |
    +---+

Now all lists have 1 element and, by definition, they are sorted.
Let's start by merging L111 and L112 into a new list M:

    +-------+
    | 5 | 6 |
    +-------+

Note that this new list M is the same as L11, because L11 was already sorted!

We then merge M and L12 to obtain M1 as follows:

    +-----------+
    | 2 | 5 | 6 |
    +-----------+

We then merge L21 and L22 as follows into a new list called M2 as follows:

    +-------+
    | 1 | 9 |
    +-------+

Now we have two lists which are sorted which we can merge in linear time to obtain the final result:

    +-------------------+
    | 1 | 2 | 5 | 6 | 9 |
    +-------------------+

### The merge procedure

Suppose we have two sorted lists (the ones from the merge of the example above) A and B:

    +-----------+
    | 2 | 5 | 6 |
    +-----------+

and

    +-------+
    | 1 | 9 |
    +-------+

The merge procedure then works in general as follows.
We create a new empty list C, which will contain the final merged and sorted list.

    ++
    ||
    ++

We then iterate through both lists using for each of them different indices,
i for the first one and j for the second.
So the situation looks as follows:

    +-----------+
    | 2 | 5 | 6 |
    +-----------+
      ^
      |

    i = 0

and

    +-------+
    | 1 | 9 |
    +-------+
      ^
      |

    j = 0

We then compare the elements at i and j from both lists and take the smallest one.
In our case, the smallest one is the one at j = 0 from list B.
We take it from B and put it in C, which now looks as follows:

    +---+
    | 1 |
    +---+

Then we increment j, i.e. j = j + 1, so j == 1, that is the situation looks as follows

    +-------+
    | 1 | 9 |
    +-------+
          ^
          |

        j = 1

The situation for A has not changed.
We compare again the elements at position i and j from both lists.
Now element at index i from A, that is 2, is smaller than element at index j from B, that is 9,
so we add 2 two C, and the C now looks like this:

    +-------+
    | 1 | 2 |
    +-------+

and the situation for A now looks as follows:

    +-----------+
    | 2 | 5 | 6 |
    +-----------+
          ^
          |

        i = 1

We do again the same thing: compare elements at indices i and j.
Now element at index i from list A, that is A[i] == 5, is smaller than B[j] == 9,
so we add 5 to list C, and it now looks as follows:


    +-----------+
    | 1 | 2 | 5 |
    +-----------+

and the situation for A looks as follows:

    +-----------+
    | 2 | 5 | 6 |
    +-----------+
              ^
              |

            i = 2

Now I think you have understood the pattern.
We add afterwards 6 (from A) and finally 9 (from B) to C to obtain (as expected):

    +-------------------+
    | 1 | 2 | 5 | 6 | 9 |
    +-------------------+

At the end i == 3 and j == 2.

# TODO

- Implement merge-sort in-place version

# References

- http://www.studytonight.com/data-structures/merge-sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
- http://en.wikipedia.org/wiki/Merge_sort
"""

__all__ = ["merge_sort", "merge", "merge_recursively"]


def merge(left: list, right: list) -> list:
    """Merges 2 sorted lists (`left` and `right`)
    in 1 single list, which is returned at the end.

    Time complexity: O(m), where `m = len(left) + len(right)`."""
    mid = []
    i = 0  # Used to index the left list.
    j = 0  # Used to index the right list.

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mid.append(left[i])
            i += 1
        else:
            mid.append(right[j])
            j += 1

    while i < len(left):
        mid.append(left[i])
        i += 1

    while j < len(right):
        mid.append(right[j])
        j += 1

    return mid


def merge_recursively(left: list, right: list) -> list:
    """Equivalent to `merge`, but using recursion
    and creating new sub-lists at each recursion call.

    You should use `merge` instead of this function,
    because the space complexity of this algorithm is higher,
    since it uses the slice operation, which creates additional unnecessary lists."""
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    elif left[0] < right[0]:
        return [left[0]] + merge_recursively(left[1:], right)
    else:
        return [right[0]] + merge_recursively(left, right[1:])


def _merge_sort_aux(ls: list) -> list:
    """Not-in-place sorting algorithm.

    Splits the original list `ls` until we have many sub-lists
    of one element (which is by the way the base case).

    Note that a list of 1 element is sorted by definition.

    Using the merge algorithm,
    we can easily merge two sorted lists of size 1,
    to obtain a merged sorted list of size 2.
    We keep merging greater sorted lists,
    until we obtain the final sorted list.

    Time complexity: O(n * log(n))"""

    # Base case, where "ls" contains_key either 1 or 0 items,
    # and it is by definition sorted.
    if len(ls) < 2:
        return ls

    # Calls merge_sort on the left half part of ls.
    left = merge_sort(ls[0:len(ls) // 2])

    # Calls merge_sort on the right half part of ls.
    right = merge_sort(ls[len(ls) // 2:])

    # Note that in the previous 2 statements,
    # we are creating new sub-lists using ls[0:len(ls)//2],
    # for the first case, for example.

    # Returns a new sorted list composed of the items in left and right.
    return merge(left, right)


def merge_sort(ls: list) -> list:
    """Merge-sort not-in-place sorting algorithm.

    Returns a new list containing the same elements as `ls` but sorted in increasing order.

    Time complexity

    +-------------+-------------+-------------+
    |    Best     |   Average   |    Worst    |
    +-------------+-------------+-------------+
    | O(n*log(n)) | O(n*log(n)) | O(n*log(n)) |
    +-------------+-------------+-------------+

    Space complexity: O(n).

    Note: space complexity apparently can be improved to O(log(n))."""
    return _merge_sort_aux(ls)
