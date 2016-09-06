#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 05/09/15

Last update: 04/09/16

## Resources

- [Ternary Search Trees](https://www.cs.upc.edu/~ps/downloads/tst/tst.html)
by By Jon Bentley and Bob Sedgewick
- [Fast Algorithms for Sorting and Searching Strings](https://www.cs.princeton.edu/~rs/strings/),
by Jon Bentley and Robert Sedgewick
- [TST.java](http://algs4.cs.princeton.edu/52trie/TST.java.html)
Java implementation by Robert Sedgewick and Kevin Wayne
- [Ternary Search Tries](https://www.youtube.com/watch?v=CIGyewO7868),
video lecture by Robert Sedgewick
- [Ternary search tree](https://en.wikipedia.org/wiki/Ternary_search_tree) at Wikipedia
- [Ternary search tree introduction](https://www.youtube.com/watch?v=xv4oRyqSKiw) by [Balazs Holczer](https://www.udemy.com/user/holczerbalazs/)
- [TernarySearchTree.hh](http://www.keithschwarz.com/interesting/code/?dir=ternary-search-tree),
C++ implementation of a TST by Keith Schwarz, which provides a good analysis of the complexity of the operations of a TST.
- [Remove method for Ternary Search Tree](http://p2p.wrox.com/book-beginning-algorithms/60350-remove-method-ternary-search-tree.html)
at [http://p2p.wrox.com/book-beginning-algorithms](http://p2p.wrox.com/book-beginning-algorithms)
- [How to list in an alphabetical order the words of a ternary search tree?](http://stackoverflow.com/a/27178771/3924118)

## Description
Ternary-search tries (or trees) combine
the time efficiency of other tries
with the space efficiency of binary-search trees.

An advantage compared to hash maps
is that ternary search tries (or trees) support sorting,
but the KEYS of a ternary-search trie can only be STRINGS,
whereas a hash map supports any kind of hashable key.

This TST should NOT allow empty strings to be inserted.
"""


class TSTNode:
    def __init__(self, key, value=None, parent=None, left=None, mid=None, right=None):
        if not key:
            raise ValueError("key must be a string of length >= 1.")
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.mid = mid
        self.right = right

    def is_left_child(self) -> bool:
        if not self.parent:
            raise AttributeError("self does not have a parent.")
        if self.parent.left:
            return self.parent.left == self
        else:
            return False

    def is_right_child(self) -> bool:
        if not self.parent:
            raise AttributeError("self does not have a parent.")
        if self.parent.right:
            return self.parent.right == self
        else:
            return False

    def is_mid_child(self) -> bool:
        if not self.parent:
            raise AttributeError("self does not have a parent.")
        if self.parent.mid:
            return self.parent.mid == self
        else:
            return False

    def has_children(self) -> bool:
        return self.left or self.right or self.mid


class TST:
    def __init__(self, root=None):
        self.n = 0  # number of key/values pairs
        self.root = root

    def size(self):
        return self.n

    def is_root(self, u):
        return self.root == u

    def insert(self, key: str, value: object):
        """Inserts the key-value pair into the symbol table,
        overwriting the old value with the new value,
        if the key is already in the symbol table."""
        if value is None:
            raise TypeError("value cannot be None.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")
        self.root = self._insert(self.root, key, value, 0)

    def _insert(self, node: TSTNode, key: str, value: object, index: int):
        """Inserts key into self starting from node.
        This is helper method and should not be called by any client of TST."""
        if node is None:
            node = TSTNode(key[index])
        if key[index] < node.key:
            node.left = self._insert(node.left, key, value, index)
            node.left.parent = node
        elif key[index] > node.key:
            node.right = self._insert(node.right, key, value, index)
            node.right.parent = node
        else:  # c == node.key
            if index < len(key) - 1:
                # If we're NOT at the end of the key, this is a match,
                # so we recursively call search from index + 1,
                # and we move to the mid node (char) of node.
                # Note that the last index of the key is len(key) - 1.
                node.mid = self._insert(node.mid, key, value, index + 1)
                node.mid.parent = node
            else:
                if not node.value:
                    self.n += 1
                node.value = value
        return node

    def delete(self, key: str):
        """Deletes and returns the value associated with key in this TST.
        This operation does not change the structure of this TST,
        but only merely makes it "forget" that there's a map with key `key`."""
        if not key:
            raise TypeError("key must be a string of length >= 1.")
        return self._delete(self.root, key)

    def _delete(self, node: TSTNode, key: str):
        """Implementation based on the non-recursive implementation of _search."""

        def _delete_fix(u):
            while u and not u.has_children():
                if self.is_root(u):
                    assert u.parent is None
                    self.root = None
                    break
                if u.is_left_child():
                    u.parent.left = None
                elif u.is_right_child():
                    u.parent.right = None
                else:
                    u.parent.mid = None
                p = u.parent
                u.parent = None
                u = p

        if node is None:
            return None

        for i in range(len(key) - 1):
            while node and key[i] != node.key:
                if key[i] < node.key:
                    node = node.left
                else:
                    node = node.right
            if node is None:  # unsuccessful search
                return None
            else:
                # arriving here only if exited from the while loop
                # because the condition key[i] != node.key was false
                node = node.mid
        if not node or node.key != key[-1]:
            return None
        else:
            result = node.value
            node.value = None
            self.n -= 1
            _delete_fix(node)
            return result

    def search_recursively(self, key: str):
        """Returns the value associated with key."""
        if not key:
            raise TypeError("key must be a string of length >= 1.")
        node = self._search_recursively(self.root, key, 0)
        return node.value if node else None

    def _search_recursively(self, node: TSTNode, key: str, index: int):
        """Returns sub-TST corresponding to given key."""
        if node is None:
            return None

        if key[index] < node.key:
            return self._search_recursively(node.left, key, index)
        elif key[index] > node.key:
            return self._search_recursively(node.right, key, index)
        elif index < len(key) - 1:
            return self._search_recursively(node.mid, key, index + 1)
        else:
            return node

    def search(self, key):
        if not key:
            raise TypeError("key must be a string of length >= 1.")
        return TST._search(self.root, key)

    @staticmethod
    def _search(node, key):
        if node is None:
            return None

        for i in range(len(key) - 1):
            while node and key[i] != node.key:
                if key[i] < node.key:
                    node = node.left
                else:
                    node = node.right
            if node is None:  # unsuccessful search
                return None
            else:
                # arriving here only if exited from the while loop
                # because the condition key[i] != node.key was false
                node = node.mid

        if not node or node.key != key[-1]:
            return None
        else:
            return node.value

    def contains(self, key: str):
        """Returns True if the key is in self, False otherwise."""
        return self.search_recursively(key) is not None

    def traverse(self):
        return self._traverse(self.root, "")

    def _traverse(self, node, prefix):
        if node is None:
            return

        self._traverse(node.left, prefix)
        if node.value is not None:
            print(prefix + node.key, "=>", node.value)
        self._traverse(node.mid, prefix + node.key)
        self._traverse(node.right, prefix)

    def count(self):
        """Counts the number of strings in self."""
        return self._count(self.root, 0)

    def _count(self, node, counter):
        if node is None:
            return counter

        counter = self._count(node.left, counter)
        if node.value is not None:
            counter += 1
        counter = self._count(node.mid, counter)
        counter = self._count(node.right, counter)
        return counter
