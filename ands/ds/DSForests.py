#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 21/02/16

DSForests (DisjointSetForests) uses two heuristics that improve the performance with respect to a naive implementation.

    1. Union by rank: attach the smaller tree to the root of the larger tree

    2. Path compression: is a way of flattening the structure of the tree whenever find is used on it.

These two techniques complement each other;
applied together, the amortized time per operation is only O( &alpha; (n))
Time complexity analysis based on Wiki's article.

## References:

- Chapter 21 (specifically paragraph 3, i.e. 21.3)

- http://orionsword.no-ip.org/blog/wordpress/?p=246

- https://en.wikipedia.org/wiki/Disjoint-set_data_structure

## Other Readings

- http://code.activestate.com/recipes/215912-union-find-data-structure/

- http://python-algorithms.readthedocs.org/en/latest/_modules/python_algorithms/basic/union_find.html
"""


class DSNode:
    def __init__(self, x, rank=0):
        self.value = x
        self.rank = rank
        self.parent = self

    def __repr__(self):
        if self.parent == self:
            return "(value: {0}, rank: {1}, parent: self)".format(
                self.value, self.rank)
        else:
            return "(value: {0}, rank: {1}, parent: {2})".format(
                self.value, self.rank, self.parent)


class DSForests:
    def __init__(self):
        self.sets = {}

    def make_set(self, x) -> None:
        """Creates a set object for `x`."""
        assert x not in self.sets
        self.sets[x] = DSNode(x)
        return self.sets[x]

    def find(self, x: DSNode) -> DSNode:
        """Finds and returns the representative of `x`.
        It follows parent nodes until it reaches
        the root of the tree (set) to which `x` belongs.

        It also uses a technique called "path compression",
        which is a way of flattening the structure of the tree.

        The idea is that each node visited on the way to a root node
        may as well be attached directly to the root node;
        they all share the same representative.

        To effect this, as `self.find` recursively traverses up the tree,
        it changes each node's parent reference
        to point to the root that it found.

        The resulting tree is much flatter,
        speeding up future operations not only on these elements
        but on those referencing them, directly or indirectly.

        This algorithm does not change any ranks of the `Set` objects.

        **Time Complexity:** O*(&alpha; (n)),
        where &alpha; (n) is the inverse of the function n = f(x) = A(x, x),
        and A is the extremely fast-growing **Ackermann** function.
        Since &alpha; (n) is the inverse of this function,
        &alpha; (n) is less than 5 for all remotely practical values of n.
        Thus, the amortized running time per operation
        is effectively a small constant."""
        if x.parent != x:
            x.parent = self.find(x.parent)
        return x.parent

    def union(self, x, y) -> DSNode:
        """"Union by rank" 2 trees (sets) into one by attaching
        the root of one to the root of the other.
        Returns the `DSNode` object representing the representative of
        the set resulted from the union of the sets containing `x` and `y`.

        "Union by rank" consists of attaching the smaller tree
        to the root of the larger tree.

        Since it is the depth of the tree that affects the running time,
        the tree with smaller depth gets added
        under the root of the deeper tree,
        which only increases the depth if the depths were equal.

        In the context of this algorithm,
        the term _rank_ is used instead of depth,
        since it stops being equal to the depth
        if path compression is also used.

        The rank is an upper bound on the height of the node.

        One-element trees are defined to have a rank of zero,
        and whenever two trees of the same rank `r` are united,
        the rank of the result is `r + 1`.

        **Time Complexity:** O*(&alpha; (n)),
        where &alpha; (n) is the inverse of the function n = f(x) = A(x, x),
        and A is the extremely fast-growing **Ackermann** function.
        Since &alpha; (n) is the inverse of this function,
        &alpha; (n) is less than 5 for all remotely practical values of n.
        Thus, the amortized running time per operation
        is effectively a small constant."""
        assert x in self.sets and y in self.sets

        x_root = self.find(self.sets[x])
        y_root = self.find(self.sets[y])

        # x and y are already joined.
        if x_root == y_root:
            return x_root

        # x and y are not in the same set, therefore we merge them.
        if x_root.rank < y_root.rank:
            x_root.parent = y_root
            return y_root
        else:
            y_root.parent = x_root
            if x_root.rank == y_root.rank:
                x_root.rank += 1
            return x_root

    def __str__(self):
        return str(self.sets)
