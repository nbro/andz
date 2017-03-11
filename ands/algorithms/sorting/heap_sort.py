#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 09/09/2015

Updated: 10/03/2017

# Description

Heap-sort is one of the best sorting methods being in-place and with no quadratic worst-case scenarios.
Heap-sort algorithm is divided into two basic parts:

1. Creating a heap from a (possibly) unsorted list, then

2. a sorted list is created by repeatedly removing the largest/smallest element from the heap,
and inserting it into the list. The heap is reconstructed after each removal.

Heap-sort is somehow slower in practice on most machines than a well-implemented quick-sort,
but it has the advantage of a more favorable worst-case O(n log n) runtime.
Heap-sort is an in-place algorithm, but it is not a stable sort.

# TODO

- Add ASCII animation of a sorting example using heap-sort!

# References

- [https://en.wikipedia.org/wiki/Binary_heap](https://en.wikipedia.org/wiki/Binary_heap)
- [https://en.wikipedia.org/wiki/Heapsort](https://en.wikipedia.org/wiki/Heapsort)
- [MIT's video lecture on Heaps and Heapsort](http://video.mit.edu/watch/introduction-to-algorithms-lecture-4-heaps-and-heap-sort-14154/)
- [http://www.studytonight.com/data-structures/heap-sort](http://www.studytonight.com/data-structures/heap-sort)
- [https://en.wikipedia.org/wiki/Sorting_algorithm#Stability](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability),
stability in a sorting algorithm

# Resources

- [http://www.stats.ox.ac.uk/__data/assets/pdf_file/0015/4173/heapbuildjalg.pdf]
(http://www.stats.ox.ac.uk/__data/assets/pdf_file/0015/4173/heapbuildjalg.pdf)
- [http://stackoverflow.com/questions/22233532/why-does-heap-sort-have-a-space-complexity-of-o1]
(http://stackoverflow.com/questions/22233532/why-does-heap-sort-have-a-space-complexity-of-o1)
"""

__all__ = ["heap_sort", "build_max_heap", "max_heapify"]


def max_heapify(ls: list, heap_size: int, i: int) -> None:
    """This operation is also sometimes called `push_down`, `shift_down` or `bubble_down`.

    **Time Complexity:** log<sub>2</sub>(n), where n = len(ls)."""
    m = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heap_size and ls[left] > ls[m]:
        m = left
    if right < heap_size and ls[right] > ls[m]:
        m = right
    if i != m:
        ls[i], ls[m] = ls[m], ls[i]
        max_heapify(ls, heap_size, m)


def build_max_heap(ls: list) -> None:
    """The `build_max_heap` converts a list `ls`,
    which can be thought as a binary tree (not a binary-search tree!) with n = len(ls) nodes,
    to a list representing a max-heap by repeatedly using `max_heapify` in a bottom up manner.

    It is based on the observation that the list of elements indexed by floor(n/2) + 1, floor(n/2) + 2, ..., n
    are all leaves for the tree (assuming that indices start at 1), thus each is a 1-element heap.

    `build_max_heap` runs `max_heapify` on each of the remaining tree nodes.

    For more info see: https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap

    This algorithm initially proposed by Robert W. Floyd
    as an improvement to the sub-optimal algorithm to build heaps
    proposed by the inventor of max-heap and of the heap data structure, that is J. Williams.

    **Time Complexity:** O(n), where n = len(ls)."""
    for i in range(len(ls) // 2, -1, -1):
        max_heapify(ls, len(ls), i)


def heap_sort(ls: list) -> None:
    """Heap-sort in-place sorting algorithm.

    **Time complexity**

    +-------------+-------------+-------------+
    |    Best     |   Average   |    Worst    |
    +-------------+-------------+-------------+
    | O(n*log(n)) | O(n*log(n)) | O(n*log(n)) |
    +-------------+-------------+-------------+

    **Space complexity:** O(1)."""
    build_max_heap(ls)
    for i in range(len(ls) - 1, 0, -1):
        ls[i], ls[0] = ls[0], ls[i]
        max_heapify(ls, i, 0)
