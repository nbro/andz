#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 21/02/2016

Updated: 08/03/2017

# Description

A disjoint-set (forests) or union-find data structure is a data structure which keeps track of a set of elements
partitioned into disjoint (non-overlapping, i.e. their intersection is the empty set) sets.
The usual operations supported by this data structure are:

  1. make-set(x): creates a single-element set containing x, and x is the representative of that set.

  2. find(x): returns the "representative" of the set where the element x is.
    If the data structure is implemented a tree, the representative is the root of the tree.

  3. union(x, y): unions the sets where x and y are (if they do not belong already to the same set).

`DisjointSetsForest` uses two heuristics that improve the performance with respect to a naive implementation.

  1. Union by rank: attach the smaller tree to the root of the larger tree

  2. Path compression: is a way of flattening the structure of the tree whenever find is used on it.

These two techniques complement each other: applied together, the amortized time per operation is only O(α(n)).

# TODO

- Deletion operation (OPTIONAL, since it's usually not part of the interface of a disjoint-set data structure)
- Pretty-print(x), for some element x in the disjoint-set data structure.
- Implement the version explained [here](http://algs4.cs.princeton.edu/15uf/)
- Add complexity analysis for print_set

# References

- Introduction to algorithms, 3rd, by C.L.R.S., chapter 21.3
- [https://en.wikipedia.org/wiki/Disjoint-set_data_structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
- [http://orionsword.no-ip.org/blog/wordpress/?p=246](http://orionsword.no-ip.org/blog/wordpress/?p=246)
- [http://stackoverflow.com/a/22945492/3924118](http://stackoverflow.com/a/22945492/3924118)
- [http://stackoverflow.com/q/23055236/3924118](http://stackoverflow.com/q/23055236/3924118)
- [https://www.cs.usfca.edu/~galles/JavascriptVisual/DisjointSets.html](https://www.cs.usfca.edu/~galles/JavascriptVisual/DisjointSets.html)
to visualize how disjoint-_sets work.

"""

from ands.ds.DisjointSets import DisjointSets

__all__ = ["DisjointSetsForest"]


class DSFNode:
    """DSFNode is the node used internally by `DisjointSetsForest`
    to represent nodes in the disjoint trees (or sets).

    Clients should NOT need to use this class."""

    def __init__(self, x, rank=0):
        # This attribute can contain any hashable value.
        self.value = x

        # The rank of node x only changes in one specific union(x, y) case:
        # when x is the representative of its set
        # and the representative of the set where y resides has the same rank as x.
        # In the DisjointSetsForest implementation below, if a situation as just described occurs,
        # then the x.rank is increased by 1.
        self.rank = rank

        # Reference to the representative of the set where this node resides
        # Since DisjointSetsForest actually implements a tree,
        # self.parent is also the root of that tree.
        self.parent = self

        # Reference used to help printing all nodes
        # belonging to the set to which this node belongs in O(m) time,
        # where m is the size of the mentioned set.
        self.next = self

    def is_root(self) -> bool:
        """A DSFNode x is a root or representative of a set
        whenever its parent pointer points to himself.
        Of course this is only true if x is already in a DisjointSetsForest object."""
        return self.parent == self

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        if self.parent == self:
            return "(value: {0}, rank: {1}, parent: self)".format(self.value, self.rank)
        else:
            return "(value: {0}, rank: {1}, parent: {2})".format(self.value, self.rank, self.parent)


class DisjointSetsForest(DisjointSets):
    """Disjoint-set forests is a collection of disjoint sets.

    Two sets A and B are disjoint if they have no element in common,
    or, in other words, their intersection is the empty set.

    It's called forest because the way the disjoint set data structure is implemented,
    that is it's implemented by representing a forest of trees.
    A disjoint-set data structure can be implemented differently.

    This data structure does not allow duplicates."""

    def __init__(self):
        # keeps tracks of the DSNodes in this disjoint-set forests.
        self._sets = {}
        self._n = 0

    def make_set(self, x: object) -> None:
        """Creates a set object for `x`.

        If `x` is already in self, then `ValueError` is raised."""
        assert 0 <= self.sets <= self.size
        if self.contains(x):
            raise LookupError("x is already in self")
        self._sets[x] = DSFNode(x)
        self._n += 1
        assert 0 <= self.sets <= self.size

    @property
    def size(self) -> int:
        """Returns the number of elements in this DisjointSetsForest."""
        return len(self._sets)

    @property
    def sets(self) -> int:
        """Returns the number of disjoint sets in `self`."""
        return self._n

    def contains(self, x: object) -> bool:
        """Returns True if x is in self, False otherwise."""
        return x in self._sets

    def _find(self, x: DSFNode) -> DSFNode:
        """Finds and returns the representative (or root) of `x`.
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

        **Time complexity:** O(α(n)), where α(n) is the inverse of the function
        n = f(x) = A(x, x), and A is the extremely fast-growing Ackermann function.
        Since α(n) is the inverse of this function,
        α(n) is less than 5 for all remotely practical values of n.
        Thus, the amortized running time per operation is effectively a small constant."""
        assert x is not None
        if x.parent != x:
            x.parent = self._find(x.parent)
        return x.parent

    @staticmethod
    def _find_iteratively(x: DSFNode) -> DSFNode:
        """This version is just an iterative alternative to the find method."""
        assert x is not None

        y = x

        # find the representative of the set where x resides
        while y != y.parent:
            y = y.parent

        # now y is the representative of x,
        # but we also want to do a path compression,
        # i.e. connect all nodes in the path from x to y directly to y.
        while x != x.parent:
            p = x.parent
            x.parent = y
            x = p

        return y

    def find(self, x: object) -> object:
        """Finds and returns the representative (or root) of `x`.

        Raises a `LookupError` if `x` does not belong to this `DisjointSetsForest`.

        **Time complexity:** O(α(n))."""
        if not self.contains(x):
            raise LookupError("x is not in self")
        x_root = self._find(self._sets[x]).value
        assert x_root == DisjointSetsForest._find_iteratively(self._sets[x]).value
        return x_root

    def union(self, x: object, y: object) -> object:
        """"Union by rank" 2 sets into one by attaching
        the root of one to the root of the other.

        Returns the root object representing the representative of
        the set resulted from the union of the sets containing `x` and `y`.
        It returns None if `x` and `y` are already in the same set.

        "Union by rank" consists of attaching the smaller tree
        to the root of the larger tree.

        Since it is the depth of the tree that affects the running time,
        the tree with smaller depth gets added under the root of the deeper tree,
        which only increases the depth if the depths were equal.

        In the context of this algorithm, the term _rank_ is used instead of depth,
        since it stops being equal to the depth if path compression is also used.

        The rank is an upper bound on the height of the node.

        One-element trees are defined to have a rank of zero,
        and whenever two trees of the same rank `r` are united,
        the rank of the result is `r + 1`.

        **Time complexity:** O(α(n)), where α(n) is the inverse of the function
        n = f(x) = A(x, x), and A is the extremely fast-growing Ackermann function.

        Since α(n) is the inverse of this function,
        α(n) is less than 5 for all remotely practical values of n.
        Thus, the amortized running time per operation is effectively a small constant."""
        assert 0 <= self.sets <= self.size
        
        if not self.contains(x):
            raise LookupError("x is not in self")
        if not self.contains(y):
            raise LookupError("y is not in self")

        x_node = self._sets[x]
        y_node = self._sets[y]

        x_root = self._find(x_node)
        y_root = self._find(y_node)

        # x and y are already joined.
        if x_root == y_root:
            return

        # Exchanging the next pointers of x_node and y_node.
        # This is needed in order to print the elements of a set in O(m) time,
        # where m is the size of the same set, in self.print_set.
        # Check here: http://stackoverflow.com/a/22945492/3924118.
        x_node.next, y_node.next = y_node.next, x_node.next

        self._n -= 1
        assert 0 <= self.sets <= self.size

        # x and y are not in the same set, therefore we merge them.
        if x_root.rank < y_root.rank:
            x_root.parent = y_root
            return y_root.value
        else:
            y_root.parent = x_root
            if x_root.rank == y_root.rank:
                x_root.rank += 1
            return x_root.value

    def print_set(self, x: object) -> None:
        if not self.contains(x):
            raise LookupError("x is not in self")

        x_node = self._sets[x]
        y = x_node

        print("{0} -> {{{1}".format(x_node, x_node), end="")
        while y.next != x_node:
            print(",", y.next, end="")
            y = y.next
        print("}")

    def __str__(self):
        return str(self._sets)
