#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Meta info

Author: Nelson Brochado

Creation: 21/02/16

Last update: 03/01/16

## Description

A disjoint-set (forests) or union-find data structure is a data structure which keeps track of a set of elements
partitioned into disjoint (non-overlapping, i.e. their intersection is the empty set) sets.
The usual operations supported by this data structure are:

  1. make-set(x): creates a single-element set containing x, and x is the representative of that set.

  2. find(x): returns the "representative" of the set where the element x is.
    If the data structure is implemented a tree, the representative is the root of the tree.

  3. union(x, y): unions the sets where x and y are (if they do not belong already to the same set).

`DSForests` uses two heuristics that improve the performance with respect to a naive implementation.

  1. Union by rank: attach the smaller tree to the root of the larger tree

  2. Path compression: is a way of flattening the structure of the tree whenever find is used on it.

These two techniques complement each other: applied together, the amortized time per operation is only O( &alpha; (n)).

## References

- Introduction to algorithms (by C.L.R.S.), chapter 21.3

- [https://en.wikipedia.org/wiki/Disjoint-set_data_structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

- [http://orionsword.no-ip.org/blog/wordpress/?p=246](http://orionsword.no-ip.org/blog/wordpress/?p=246)

- [http://stackoverflow.com/a/22945492/3924118](http://stackoverflow.com/a/22945492/3924118)

- [http://stackoverflow.com/q/23055236/3924118](http://stackoverflow.com/q/23055236/3924118)

- [https://www.cs.usfca.edu/~galles/JavascriptVisual/DisjointSets.html](https://www.cs.usfca.edu/~galles/JavascriptVisual/DisjointSets.html)
to visualize how disjoint-sets work.

## TODO

- Deletion operation (OPTIONAL, since it's usually not part of the interface of a disjoint-set data structure)

- Pretty-print(x), for some element x in the disjoint-set data structure.

- Implement the version explained [here](http://algs4.cs.princeton.edu/15uf/)

"""


class DSNode:

    def __init__(self, x, rank=0):
        # This attribute can contain any hashable value.
        self.value = x

        # The rank of node x only changes in one specific union(x, y) case:
        # when x is the representative of its set
        # and the representative of the set where y resides has the same rank as x.
        # In the DSForests implementation below, if a situation as just described occurs,
        # then the x.rank is increased by 1.
        self.rank = rank

        # Reference to the representative of the set where this node resides
        # Since DSForests actually implements a tree,
        # self.parent is also the root of that tree.
        self.parent = self

        # Reference used to help printing all nodes
        # belonging to where this node belongs in O(m) time,
        # where m is the size of the mentioned set.
        self.next = self

    def is_root(self):
        """A DSNode x is a root or representative of a set
        whenever its parent pointer points to himself.
        Of course this is only true if x is already in a DSForests object."""
        return self.parent == self

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        if self.parent == self:
            return "(value: {0}, rank: {1}, parent: self)".format(self.value, self.rank)
        else:
            return "(value: {0}, rank: {1}, parent: {2})".format(self.value, self.rank, self.parent)


class DSForests:

    def __init__(self):
        # keys tracks of the DSNodes in this disjoint-set
        self.sets = {}

    def make_set(self, x) -> DSNode:
        """Creates a set object for `x`."""
        assert x not in self.sets
        self.sets[x] = DSNode(x)
        return self.sets[x]

    def find(self, x: DSNode) -> DSNode:
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

        **Time Complexity:** O*(&alpha; (n)),
        where &alpha; (n) is the inverse of the function n = f(x) = A(x, x),
        and A is the extremely fast-growing **Ackermann** function.
        Since &alpha; (n) is the inverse of this function,
        &alpha; (n) is less than 5 for all remotely practical values of n.
        Thus, the amortized running time per operation
        is effectively a small constant."""
        assert x
        if x.parent != x:
            x.parent = self.find(x.parent)
        return x.parent

    def find_iteratively(self, x: DSNode) -> DSNode:
        """This version is just an iterative alternative to the find method."""
        assert x

        y = x

        # find the representative of the set where x resides
        while y != y.parent:
            y = y.parent

        # post-condition
        assert y == self.find(x)

        # now y is the representative of x,
        # but we also want to do a path compression,
        # i.e. connect all nodes in the path from x to y directly to y.
        while x != x.parent:
            p = x.parent
            x.parent = y
            x = p

        return y

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

        # Since the original values x and y are not used afterwards,
        # and what we actually need in two places of this algorithm are the corresponding DSNodes
        # we set x and y to be respectively their DSNode counter-part.
        x = self.sets[x]
        y = self.sets[y]

        x_root = self.find(x)
        y_root = self.find(y)

        # x and y are already joined.
        if x_root == y_root:
            return

        # Exchanging the next pointers of x and y.
        # This is needed in order to print the elements of a set in O(m) time,
        # where m is the size of the same set.
        # Check here: http://stackoverflow.com/a/22945492/3924118.
        x.next, y.next = y.next, x.next

        # x and y are not in the same set, therefore we merge them.
        if x_root.rank < y_root.rank:
            x_root.parent = y_root
            return y_root
        else:
            y_root.parent = x_root
            if x_root.rank == y_root.rank:
                x_root.rank += 1
            return x_root

    def print_set(self, x) -> None:
        assert x in self.sets

        x = self.sets[x]
        y = x

        print("{0} -> {{{1}".format(x, x), end="")
        while y.next != x:
            print(",", y.next, end="")
            y = y.next
        print("}")

    def __str__(self):
        return str(self.sets)