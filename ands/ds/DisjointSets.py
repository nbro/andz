#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 08/03/2017

Updated: 06/04/2018

# Description

Module which contains the abstract class from which DisjointSetsForest derives.

The reason to have this abstract class is that a disjoint-sets data structure
can possibly be implemented in different ways.
"""

from abc import ABC, abstractmethod

__all__ = ["DisjointSets"]


class DisjointSets(ABC):
    """Abstract class from which DisjointSetsForest derives.

    A DisjointSets data structure is sometimes also called DisjointSet,
    UnionFind or MergeSet."""

    @abstractmethod
    def make_set(self, x) -> None:
        pass

    @abstractmethod
    def find(self, x):
        pass

    @abstractmethod
    def union(self, x, y):
        pass
