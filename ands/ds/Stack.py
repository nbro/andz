#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 05/07/2015

Updated: 04/02/2017

# Description

A stack is one of the most simple and, at the same time, useful abstract data types in computer science.

An abstract data type (or, in short, ADT) is a logical description or specification
of a certain way of viewing and/or organizing data, and which values and operations are allowed on this data.
An ADT is, as the same suggests, an abstract concept or mathematical model;
thus an ADT can be implemented as a data structure in many ways.
Essentially, ADTs is all about ideas or concepts of representing and manipulating data,
whereas a data structure is an implementation of a specific ADTs;
hence there can be more than one data structure for the same ADT.

What defines a stack is the order of insertion and removal of elements from it:
a stack is a "last in, first out" (or, as an acronym, LIFO) abstract data type,
that is, the last element inserted into the stack is the first to be removed.
Since this is an ADT, we don't care how the elements are stored in memory,
or how we manipulate them so that the last element inserted is the first to be removed.
The insertion of an element is usually called "push", whereas the removal is usually called "pop".
There's also another operation (i.e. "peek" or "top")
which consists in looking at the last element inserted into the stack.
Of course other operations, such as "size of the stack" (i.e. how many elements in the stack)
or "is empty" (i.e. checking if the stack contains elements or not) may also useful.

# References

- [http://interactivepython.org/runestone/static/pythonds/Introduction/WhyStudyDataStructuresandAbstractDataTypes.html](http://interactivepython.org/runestone/static/pythonds/Introduction/WhyStudyDataStructuresandAbstractDataTypes.html)
- [http://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python](http://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python),
for the time complexity analysis of the pop operation of the last element on lists.
- [http://stackoverflow.com/questions/1115313/cost-of-len-function](http://stackoverflow.com/questions/1115313/cost-of-len-function),
for the time complexity analysis of the size operation.
- [http://stackoverflow.com/questions/12342457/what-is-the-big-o-notation-for-the-len-function-in-python](http://stackoverflow.com/questions/12342457/what-is-the-big-o-notation-for-the-len-function-in-python),
for other time complexity analysis of the list class.

"""

from collections import Iterable

from tabulate import tabulate

__all__ = ["Stack"]


class Stack:
    """This is a wrapper class around the Python's list to represent a stack data structure.

    It doesn't allow you to insert None elements through the public methods.
    It returns None whenever you try to pop from or peek at the stack, but it's empty.

    The data structure can be initialized with an iterable object with not None values.
    A copy of the given iterable is made, so the original iterable is not affected when performing operations."""

    def __init__(self, s=None):
        if s is not None:
            if not isinstance(s, Iterable):
                raise TypeError("s must be an instance of Iterable")
            if any(elem is None for elem in s):
                raise ValueError("all elements of s must be not None")
        else:
            s = []
        self._stack = list(s)

    def push(self, elem: object) -> None:
        """Pushes `elem` on top of this stack.

        If `elem` is None`, `ValueError` is raised.

        **Time complexity:** O(1)."""
        if elem is None:
            raise ValueError("elem cannot be None")
        self._stack.append(elem)

    def pop(self) -> object:
        """Returns the top of this stack, or `None` if the stack is empty.

        **Time complexity:** O(1)."""
        return None if self.is_empty() else self._stack.pop()

    def size(self) -> int:
        """Returns the size of this stack.

        **Time complexity:** O(1)."""
        return len(self._stack)

    def is_empty(self) -> bool:
        """Returns `True` if this stack is empty, `False` otherwise.

        **Time complexity:** O(1)."""
        return self.size() == 0

    def top(self) -> object:
        """Returns but does **not** pop the top of the stack.

        If the stack is empty, `None` is returned.

        This operation is also called "peek".

        **Time complexity:** O(1)."""
        return None if self.is_empty() else self._stack[-1]

    def __str__(self):
        return tabulate([[e] for e in reversed(self._stack)], tablefmt="grid")

    def __repr__(self):
        return self.__str__()
