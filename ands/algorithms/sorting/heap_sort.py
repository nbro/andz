#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 09/09/15

Modified: 01/07/16

### Resources
- [Heap Sort](https://en.wikipedia.org/wiki/Heapsort), Wiki's article
- [MIT's video lecture on Heaps and Heapsort](http://video.mit.edu/watch/introduction-to-algorithms-lecture-4-heaps-and-heap-sort-14154/)
"""


def max_heapify(ls: list, heap_size: int, i: int):
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


def build_max_heap(ls: list):
    for i in range(len(ls) // 2, -1, -1):
        max_heapify(ls, len(ls), i)
    return ls


def heap_sort(ls: list):
    """In-place sorting algorithm.
    Returns a reference to `ls`.

    **Time Complexity:** O(n*log<sub>2</sub>(n))."""
    build_max_heap(ls)
    for i in range(len(ls) - 1, 0, -1):
        ls[i], ls[0] = ls[0], ls[i]
        max_heapify(ls, i, 0)
    return ls
