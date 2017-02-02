#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado
Created: 05/09/2015
Updated: 02/02/2017

# Description

Ternary-search tries (or trees) combine the time efficiency of other tries
with the space efficiency of binary-search trees.

An advantage compared to hash maps is that ternary search tries support sorting,
but the _keys_ of a ternary-search trie can only be _strings_,
whereas a hash map supports any kind of hashable keys.

## TSTs vs Hashing

### Hashing

- Need to examine entire key
- Search miss and hits cost about the same
- Performance relies on hash function
- Does NOT support ordered symbol table operations

### TSTs

- Works only for strings (or digital keys)
- Only examines just enough key characters
- Search miss may involve only a few characters
- Supports ordered symbol table operations:
    - keys-that-match
    - keys-with-prefix
    - longest-prefix-of

### Bottom line

TSTs are:

- faster than hashing (especially for search misses)
- more flexible than red-black trees

# References

- [Ternary Search Trees](https://www.cs.upc.edu/~ps/downloads/tst/tst.html) by By Jon Bentley and Bob Sedgewick
- [Fast Algorithms for Sorting and Searching Strings](https://www.cs.princeton.edu/~rs/strings/), by Jon Bentley and Robert Sedgewick
- [TST.java](http://algs4.cs.princeton.edu/52trie/TST.java.html), Java implementation by Robert Sedgewick and Kevin Wayne
- [Ternary Search Tries](https://www.youtube.com/watch?v=CIGyewO7868), video lecture by Robert Sedgewick
- [Ternary search tree](https://en.wikipedia.org/wiki/Ternary_search_tree) at Wikipedia
- [How to list in an alphabetical order the words of a ternary search tree?](http://stackoverflow.com/a/27178771/3924118)

# Resources

- [Ternary search tree introduction](https://www.youtube.com/watch?v=xv4oRyqSKiw),
by [Balazs Holczer](https://www.udemy.com/user/holczerbalazs/)
- [TernarySearchTree.hh](http://www.keithschwarz.com/interesting/code/?dir=ternary-search-tree),
C++ implementation of a TST by Keith Schwarz, which provides a good analysis of the complexity of the operations of a TST.
- [Remove method for Ternary Search Tree](http://p2p.wrox.com/book-beginning-algorithms/60350-remove-method-ternary-search-tree.html),
at [http://p2p.wrox.com/book-beginning-algorithms](http://p2p.wrox.com/book-beginning-algorithms)
- [Plant your data in a ternary search tree](http://www.javaworld.com/article/2075027/java-app-dev/plant-your-data-in-a-ternary-search-tree.html?page=1)

"""


class TSTNode:
    """A TSTNode has 6 fields:

        - key, which is a character;
        - value, which is None if self is not a terminal node (of an inserted string in the TST);
        - parent, which is a pointer to a TSTNode representing the parent of self;
        - left, which is a pointer to a TSTNode whose key is smaller lexicographically than key;
        - right, which is similarly a pointer to a TSTNode whose key is greater lexicographically than key;
        - mid, which is a pointer to a TSTNode whose key is the following character of key in an inserted string."""

    def __init__(self, key, value=None, parent=None, left=None, mid=None, right=None):
        if not isinstance(key, str):
            raise TypeError("key must be an instance of str.")
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

    def __str__(self):
        return "{0}: {1}".format(self.key, self.value)

    def __repr__(self):
        return self.__str__()


class TST:
    """Methods or fields that start with an underscore _ are considered private,
    so they should not be access and never modified from a client of this class.

    This TST does not allow (through public methods) empty strings to be inserted.

    In general the way the ternary search tree looks like
    depends highly on the order of insertion of the keys,
    that is, inserting the same keys but in different orders
    produces internally a different structure or shape of the TST."""

    def __init__(self):
        self._n = 0
        self._root = None

    def __invariants__(self) -> None:
        """These propositions should always be true at the BEGINNING
        and END of every PUBLIC method of this TST.

        Call this method if you want to ensure the invariants are holding."""
        assert self._n >= 0
        if self._n == 0:
            assert self._root is None
        elif self._n > 0:
            assert isinstance(self._root, TSTNode)
            assert self._root.parent is None

    def _is_root(self, u: TSTNode) -> bool:
        result = (self._root == u)
        if result:
            assert u.parent is None
        else:
            assert u.parent is not None
        return result

    def size(self) -> int:
        return self._n

    def count(self) -> int:
        """Counts the number of strings in self.

        This method recursively passes through all the nodes
        and counts the ones which have a non None value.

        You should clearly use size instead: 
        this method is here only for the fun of writing code!

        **Time complexity:** O(n), where n is the number of nodes in this TST."""
        c = self._count(self._root, 0)
        assert c == self.size()
        return c

    def _count(self, node: TSTNode, counter: int) -> int:
        """Helper method to `self.count`.

        **Time complexity:** O(m), where m is the number of nodes under `node`."""
        if node is None:  # base case
            return counter

        counter = self._count(node.left, counter)
        if node.value is not None:
            counter += 1

        counter = self._count(node.mid, counter)
        counter = self._count(node.right, counter)

        return counter

    def is_empty(self) -> bool:
        """**Time complexity:** O(1)."""
        return self._n == 0

    def insert(self, key: str, value: object):
        """Inserts the `key` into the symbol table and associates with it `value`,
        overwriting an eventual associated old value, if the `key` is already in self.

        If `key` is not an instance of `str`, `TypeError` is raised.
        If `key` is an empty string, `ValueError` is raised.
        If `value` is None, `ValueError` is raised.

        Nodes whose value is not None represent the last character of an inserted word.

        **Time complexity:** O(m + h), where m = length(key),
        which also represents how many times we follow the middle link,
        and h is the number of left and right turns.
        So a lower bound of the complexity would be &Omega(m);."""
        self.__invariants__()
        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")
        if value is None:
            raise ValueError("value cannot be None.")
        self._root = self._insert(self._root, key, value, 0)
        self.__invariants__()

    def _insert(self, node: TSTNode, key: str, value: object, index: int):
        """Inserts `key` with `value` into self starting from `node`."""
        if node is None:
            node = TSTNode(key[index])

        if key[index] < node.key:
            node.left = self._insert(node.left, key, value, index)
            node.left.parent = node
        elif key[index] > node.key:
            node.right = self._insert(node.right, key, value, index)
            node.right.parent = node
        else:  # key[index] == node.key
            if index < len(key) - 1:
                # If we're NOT at the end of the key, this is a match,
                # so we recursively call self._insert from index + 1,
                # and we move to the mid node (char) of node.
                # Note that the last index of the key is len(key) - 1.
                node.mid = self._insert(node.mid, key, value, index + 1)
                node.mid.parent = node
            else:
                if node.value is None:
                    self._n += 1
                node.value = value

        return node

    def search(self, key: str) -> object:
        """Returns the value associated with `key`, if `key` is in self, else None.

        If `key` is not an instance of `str`, `TypeError` is raised.
        If `key` is an empty string, `ValueError` is raised.

        The search in a TST works as follows.

        We start at the root and we compare its character with the first character of key.
            - If they are the same, we follow the middle link of the root node.
            - If the first character of key is smaller lexicographically
            than the key at the root, then we take the left link or pointer.
            We do this because we know that all strings that start with characters
            that are smaller lexicographically than key[0] are on its left subtree.
            - If the first character of key is greater lexicographically
            than the key at the root, we take similarly the right link or pointer.

        We keep applying this idea at every node.
        Moreover, WHEN THERE'S A MATCH, next time we compare the key
        of the next node with the next character of key.

        For example, if there's a match between the first node (the root) and key[0],
        we follow the middle link, and the next comparison is between
        the key of the specific next node and key[1], not key[0]!

        **Time complexity:** O(m + h).
        Check self.insert to see what m and h are."""
        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")

        node = self._search(self._root, key, 0)

        if node is not None:
            assert self.search_iteratively(key) == node.value
            return node.value
        else:
            assert self.search_iteratively(key) is None
            return None

    def _search(self, node: TSTNode, key: str, index: int) -> TSTNode:
        """Searches for the node containing the value associated with `key` starting from `node`.
        If returns None OR a node with value None if there's no such node."""
        if node is None:
            return None

        if key[index] < node.key:
            return self._search(node.left, key, index)
        elif key[index] > node.key:
            return self._search(node.right, key, index)
        elif index < len(key) - 1:  # This is a match, but we're not at the last character of key.
            return self._search(node.mid, key, index + 1)
        else:  # This is a match and we're at the last character of key.
            return node  # node could be None!!

    def search_iteratively(self, key: str) -> object:
        """Iterative alternative to self.search."""
        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")

        node = self._root

        if node is None:
            return None

        # Up to the penultimate index (i.e. len(key) - 1)
        # because if we reach the penultimate character and it's a match,
        # then we follow the mid node (i.e. we end up in what's possibly the last node).
        index = 0

        while index < len(key) - 1:
            while node and key[index] != node.key:
                if key[index] < node.key:
                    node = node.left
                else:
                    node = node.right

            if node is None:  # Unsuccessful search.
                return None
            else:
                # Arriving here only if exited from the while loop
                # because the condition key[i] != node.key was false,
                # that is key[index] == node.key, thus we follow the middle link.
                node = node.mid
                index += 1

        assert index == len(key) - 1

        # If node is not None, then we may still need to go left or right,
        # and we stop when either we find a node which has the same key as the last character of key,
        # or when `node` ends up being set to None, i.e. the key does not exist in this TST.
        while node and key[index] != node.key:
            if key[index] < node.key:
                node = node.left
            else:
                node = node.right

        if node is None:  # Unsuccessful search.
            return None
        else:  # We exit the previous while loop because key[index] == node.key.
            return node.value  # could also be None!!

    def contains(self, key: str) -> bool:
        """Returns True if `key` is in self, False otherwise.

        **Time complexity:** O(m + h).
        See the complexity analysis of self.insert for more info about m and h."""
        return self.search(key) is not None

    def delete(self, key: str) -> TSTNode:
        """Deletes and returns the value associated with `key` in this TST,
        if `key` is in this TST, otherwise it returns None.

        If `key` is not an instance of `str`, `TypeError` is raised.
        If `key` is an empty string, `ValueError` is raised.

        **Time complexity:** O(m + h + k).
        Check self.search to see what m and h are.
        k is the number of "no more necessary" cleaned up
        after deletion of the node associated with `key`.
        Unnecessary nodes are nodes with no children and value equal to None."""
        self.__invariants__()

        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")

        # Note: calling self._search, since self.search does not return a Node,
        # but the value associated with the key passed as parameter.
        node = self._search(self._root, key, 0)

        if node is not None and node.value is not None:
            # If node.value is None, it means
            result = node.value  # forgetting the string tracked by node.
            node.value = None
            self._n -= 1
            self._delete_fix(node)
        else:
            result = None

        self.__invariants__()
        return result

    def _delete_fix(self, u: TSTNode) -> None:
        """Does the clean up of this TST after deletion of node `u`."""
        assert u.value is None

        # While u has no children and his value is None,
        # forget about u and start from his parent.
        # So, this while loop terminates when either u is None,
        # u has at least one child, or u's value is not None.
        while u and not u.has_children() and u.value is None:
            if self._is_root(u):
                assert self._n == 0
                self._root = None
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

        if u.has_children() and u.value is None:
            assert self._count(u, 0) > 0

    def traverse(self) -> None:
        """Traverses all nodes in this TST and prints the key: value associations.

        **Time complexity:** O(n), where n is the number of nodes in self."""
        self._traverse(self._root, "")

    def _traverse(self, node: TSTNode, prefix: str) -> None:
        """Helper method to self.traverse.

        **Time complexity:** O(m), where m is the number of nodes under `node`."""
        if node is None:  # base case
            return

        self._traverse(node.left, prefix)
        if node.value is not None:
            print(prefix + node.key, ": ", node.value)

        self._traverse(node.mid, prefix + node.key)
        self._traverse(node.right, prefix)

    def keys_with_prefix(self, prefix: str) -> list:
        """Returns all keys in this TST that start with `prefix`.

        If `prefix` is not an instance of `str`, `TypeError` is raised.
        If `prefix` is an empty string, then all keys in this TST
        that start with an empty string, thus all keys are returned."""
        if not isinstance(prefix, str):
            raise TypeError("prefix must be an instance of str!")

        kwp = []

        if not prefix:
            self._collect(self._root, [], kwp)
        else:
            node = self._search(self._root, prefix, 0)

            if node is not None:
                if node.value is not None:
                    # A `key` equals to prefix was found in the TST with an associated value.
                    kwp.append(prefix)

                self._collect(node.mid, list(prefix), kwp)

        return kwp

    def _collect(self, node: TSTNode, prefix_list: list, kwp: list) -> None:
        """Returns all keys rooted at `node` given the prefix given as a list of characters `prefix_list`."""
        if node is None:
            return

        self._collect(node.left, prefix_list, kwp)

        if node.value is not None:
            kwp.append("".join(prefix_list + [node.key]))

        prefix_list.append(node.key)
        self._collect(node.mid, prefix_list, kwp)

        prefix_list.pop()
        self._collect(node.right, prefix_list, kwp)
