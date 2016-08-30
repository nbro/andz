#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 05/09/15

Last update: 01/07/16

Resources:

- https://www.cs.upc.edu/~ps/downloads/tst/tst.html
- http://algs4.cs.princeton.edu/52trie/TST.java.html
- https://www.youtube.com/watch?v=CIGyewO7868
- https://en.wikipedia.org/wiki/Ternary_search_tree
- https://www.youtube.com/watch?v=xv4oRyqSKiw

Description:
Ternary-search tries (or trees) combine
the time efficiency of other tries
with the space efficiency of binary-search trees.

An advantage compared to hash maps
is that ternary search tries support sorting,
but the keys of a ternary-search trie can only be strings,
whereas a hash map supports any kind of hashable key.

# TODO
- Delete operation
"""


class TSTNode:

    def __init__(self, key, value=None, parent=None,
                 left=None, mid=None, right=None):
        if key is None:
            raise ValueError("key cannot be None")

        self.key = key
        self.value = value

        self.parent = parent  # not used so far...
        self.left = left
        self.mid = mid
        self.right = right


class TST:
    # Ternary Search Trie

    def __init__(self, root=None):
        self.n = 0  # Size of the ternary search tree
        self.root = root

    def size(self):
        return self.n

    def contains(self, key: str):
        """Returns True if the key is in self, False otherwise."""
        return self.search_recursively(key) is not None

    def search_recursively(self, key: str):
        """Returns the value associated with key."""
        if not key:
            raise TypeError("key must be a string of length >= 1")

        node = TST._search_recursively(self.root, key, 0)

        if node:
            return node.value

    @staticmethod
    def _search_recursively(node: TSTNode, key: str, index: int):
        """Returns sub-TST corresponding to given key."""
        if not key:
            raise TypeError("key must be a string of length >= 1")

        if node is None:
            return None

        c = key[index]  # char of key at index

        if c < node.key:
            return TST._search_recursively(node.left, key, index)
        elif c > node.key:
            return TST._search_recursively(node.right, key, index)
        elif index < len(key) - 1:
            return TST._search_recursively(node.mid, key, index + 1)
        else:
            return node

    def search(self, key):
        return TST._search(self.root, key)

    @staticmethod
    def _search(node, key):

        if node is None or not key:
            return None

        for i in range(len(key) - 1):

            while node and key[i] != node.key:
                if key[i] < node.key:
                    node = node.left
                else:
                    node = node.right

            if node is None:  # Unsuccessful search
                return None
            else:
                node = node.mid

        # In case the length of the key is 1
        return node.value if node.key == key else None

    def insert(self, key: str, value: object):
        """Inserts the key-value pair into the symbol table,
        overwriting the old value with the new value,
        if the key is already in the symbol table."""
        if value is None:
            raise TypeError("'value' cannot be None.")

        if not self.contains(key):
            self.n += 1

        self.root = TST._insert(self.root, key, value, 0)

    @staticmethod
    def _insert(node: TSTNode, key: str, value: object, index: int):
        """Inserts key into self starting from node."""
        c = key[index]

        if node is None:
            node = TSTNode(c)

        if c < node.key:
            node.left = TST._insert(node.left, key, value, index)
        elif c > node.key:
            node.right = TST._insert(node.right, key, value, index)
        elif index < len(key) - 1:
            """if we're not at the end of the key,
            this is a match, so we recursively call search from index + 1,
            and we move to the mid node (char) of node."""
            node.mid = TST._insert(node.mid, key, value, index + 1)
        else:
            node.value = value

        return node

    def traverse(self):
        return TST._traverse(self.root, "")

    @staticmethod
    def _traverse(node, prefix):
        """Based on: http://stackoverflow.com/a/27178771/3924118"""
        if node is None:
            return

        TST._traverse(node.left, prefix)

        if node.value is not None:
            print(prefix + node.key, "=>", node.value)

        TST._traverse(node.mid, prefix + node.key)
        TST._traverse(node.right, prefix)

    def count(self):
        """Counts the number of strings in self.
        You should call instead self.size(),
        whose time complexity is constant.
        """
        return self._count(self.root, 0)

    @staticmethod
    def _count(node, counter):
        if node is None:
            return counter

        counter = TST._count(node.left, counter)

        if node.value is not None:
            counter += 1

        counter = TST._count(node.mid, counter)

        counter = TST._count(node.right, counter)

        return counter


if __name__ == "__main__":
    tst = TST()

    tst.insert("M", 12)
    tst.insert("Nelson", 28)
    tst.insert("Mamma", 1)
    tst.insert("Anna", 12)

    # print(tst.search_r("Me"))

    print(tst.search("M"))
    print(tst.search_recursively("M"))
    # print(tst.search("Nelson"))
    # print(tst.size())

    tst.traverse()

    print(tst.count())
