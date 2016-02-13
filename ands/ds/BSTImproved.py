#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 13/02/2016

Binary-search tree that provides somehow randomness at insertion.

## TODO
- Improve the "randomness" of insertion into the bst.
"""

from ands.ds.BST import *
from random import randint


class BSTImproved(BST):
    
    def __init__(self, root=None, name="BSTImproved"):
        BST.__init__(self, root, name)

    def insert(self, u, value=None):
        """Inserts `x` into this tree.

        `x` can either be a `BSTNode` object,
        or it can be a _key_ of any other type,
        but it should be comparable with the other keys,
        and these keys should be comparable objects.

        Note that the height of a `BST` varies
        depending on how elements are inserted and removed.
        For example, if we insert a list of numbers in increasing order,
        the resulting `BST` object will look like a chain with height **n - 1**,
        where `n` is the number of elements inserted.
        In general, the optimal height is logarithmic on the number of nodes,
        and to get closer to the optimal height,
        randomly insertion of numbers is usually used.

        If we have `n` keys to insert, there are `n!` (n-factorial)
        ways of inserting those `n` keys into the binary search tree.
        When we randomly insert them, those permutations are equally likely.

        So, the expected height of a tree created with randomly insertions is O(log<sub>2</sub>(n)).
        For a proof, see chapter 12 of Introduction to Algorithms (3rd ed.) by CLRS.

        This function does a pseudo-random insertion of keys."""
        r = randint(0, self.size() * 3 // 8)  # * 3 // 8 is just a random operation...
        if r == 0:
            self.root_insert(x, value)
        else:
            self.tail_insert(x, value)


    def tail_insert(self, x, value=None):
        """Inserts (normally) `x` into this BST object.

        **Time Complexity**: O(h)."""
        if x is None:
            raise ValueError("x cannot be None.")

        if not isinstance(x, BSTNode):
            x = BSTNode(x, value)

        if x.left or x.right or x.parent:
            raise ValueError("x cannot have left or right children, or parent.")

        if self.root is None:
            self._initialise(x)
        else:
            c = self.root  # c is the current node
            p = self.root.parent  # parent of c

            while c is not None:
                p = c
                if x.key < c.key:
                    c = c.left
                else:
                    c = c.right
            if x.key < p.key:
                p.left = x
            else:
                p.right = x

            x.parent = p
            self.n += 1

    def root_insert(self, x, value=None):
        """Inserts `x` as the root of this tree.

        **Time Complexity**: O(h)."""
        def _root_insert(u: BSTNode, v: BSTNode):
            """Helper method for `self.root_insert`."""
            if u is None:
                return v
            if v.key < u.key:
                u.left = _root_insert(u.left, v)
                u = self.right_rotate(u)
            else:
                u.right = _root_insert(u.right, v)
                u = self.left_rotate(u)
            return u

        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, BSTNode):
            x = BSTNode(x, value)
        if x.left or x.right or x.parent:
           raise ValueError("x cannot have left or right children, or parent.")
        if self.root is None:
            self._initialise(x)
        else:
            _root_insert(self.root, x)
            self.n += 1


if __name__ == "__main__":
    pass
