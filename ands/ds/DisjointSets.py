#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 08/03/2017

Updated: 08/03/2017

# Description

Module which contains the abstract class from which DisjointSetsForest derives.

The reason to have this abstract class is because a disjoint-sets data structure
can possibly be implemented in different ways.
"""

from abc import ABCMeta, abstractmethod

__all__ = ["DisjointSets"]


class DisjointSets(metaclass=ABCMeta):
    """Abstract class from which DisjointSetsForest derives.

    A DisjointSets data structure is sometimes also called DisjointSet,
    UnionFind or MergeSet."""

    @abstractmethod
    def make_set(self, x: object) -> None:
        pass

    @abstractmethod
    def find(self, x: object) -> object:
        pass

    @abstractmethod
    def union(self, x: object, y: object) -> object:
        pass
