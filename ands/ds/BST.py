#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 01/07/2015

Updated: 28/09/2017

# Description

A binary search trees (BST), sometimes called ordered or sorted binary trees,
are a particular type of containers: data structures that store "items" (such as
numbers, names, etc.) in memory. They allow fast lookup, addition and removal of
items (if balanced), and can be used to implement either dynamic sets of items,
or lookup tables that allow finding an item by its key (e.g., finding the phone
number of a person by name).

Binary search trees keep their keys in sorted order, so that lookup and other
operations can use the principle of "binary search": when looking for a key in a
tree (or a place to insert a new key), they traverse the tree from the root to a
leaf, making comparisons to keys stored in the nodes of the tree and deciding,
based on the comparison, to continue searching in the left or right subtrees. On
average, this means that each comparison allows the operations to skip about
half of the tree, so that each lookup, insertion or deletion takes time
proportional to the logarithm of the number of items stored in the tree.

This is much better than the linear time required to find items by key in an
(unsorted) array, but slower than the corresponding operations on hash tables.

# TODO

- Add functions "intersection" and "union".
- Implement a recursive version of insert (OPTIONAL).

# References

- https://en.wikipedia.org/wiki/Binary_search_tree
- Introduction to Algorithms (3rd edition), chapter 12, by CLRS
- http://algs4.cs.princeton.edu/32bst/
- http://www.cs.princeton.edu/courses/archive/spr04/cos226/lectures/bst.4up.pdf
- http://algs4.cs.princeton.edu/32bst/BST.java.html
- http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/bst.py
"""

__all__ = ["BST", "is_bst"]


class _BSTNode:
    """Node class to represent a node for the BST class."""

    def __init__(self, key, parent=None, left=None, right=None):
        if key is None:
            raise ValueError("key cannot be None")
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def sibling(self) -> "_BSTNode":
        """Returns the sibling node of this node, which can of course be
        None."""
        if self.parent is not None:
            if self.is_left_child():
                return self.parent.right
            else:
                return self.parent.left

    @property
    def grandparent(self) -> "_BSTNode":
        """Returns the parent of the parent of this node."""
        if self.parent is not None:
            return self.parent.parent

    @property
    def uncle(self) -> "_BSTNode":
        """Returns the uncle node of this node.

        The uncle is the sibling of the parent of this node, if it exists. None
        is returned if it doesn't exist, or the parent or grandparent of this
        node is None."""

        # Implies that also parent is not None.
        if self.grandparent is not None:
            if self.parent == self.grandparent.left:
                return self.grandparent.right
            else:  # self.parent == self.grandparent.right
                return self.grandparent.left

    def is_left_child(self) -> bool:
        if self.parent is not None:
            if self.parent.left is not None:
                return self.parent.left == self
        else:
            raise AttributeError("self does not have a parent")

    def is_right_child(self) -> bool:
        if self.parent is not None:
            if self.parent.right is not None:
                return self.parent.right == self
        else:
            raise AttributeError("self does not have a parent")

    def has_right_child(self) -> bool:
        return self.right is not None

    def has_left_child(self) -> bool:
        return self.left is not None

    def has_parent(self) -> bool:
        return self.parent is not None

    def has_children(self) -> bool:
        """Returns true if self has at least one child, false otherwise."""
        return self.left is not None or self.right is not None

    def has_one_child(self) -> bool:
        """Returns true only if self has exactly one child, false otherwise."""
        return ((self.left is not None and self.right is None) or
                (self.left is None and self.right is not None))

    def has_two_children(self) -> bool:
        """Returns true if self has exactly two children, false otherwise."""
        return self.left is not None and self.right is not None

    def count(self) -> int:
        """Counts the numbers of nodes under self (including self)."""
        if not self.has_children():
            return 1
        else:
            c = 0
            return self._count(self, c)

    def _count(self, u: "_BSTNode", c: int) -> int:
        if u is None:
            return c
        else:
            c += 1
        c = self._count(u.left, c)
        c = self._count(u.right, c)
        return c

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.__str__()


class BST:
    """BST is a class that represents a binary-search tree.

    This implementation does allow duplicate elements.

    It's the responsibility of the client of this class to make sure that keys
    provided to the methods of this class are comparable among them.

    In the time complexity analysis under the methods of this class, h in O(h)
    means the maximum height the algorithm is going to reach. m in O(m) is the
    height of the subtree rooted at the node passed as parameter."""

    def __init__(self):
        self._n = 0
        self._root = None
        assert is_bst(self)

    @property
    def size(self) -> int:
        """Returns the total number of nodes.

        Time complexity: O(1)."""
        assert is_bst(self)
        if self._root is not None:
            assert self._root.count() == self._n
        else:
            assert self._n == 0
        return self._n

    def is_empty(self) -> bool:
        """Returns true if this tree has 0 nodes.

        Time complexity: O(1)."""
        assert is_bst(self)
        return self.size == 0

    def clear(self) -> None:
        """Removes all nodes from this tree.

        Time complexity: O(1)."""
        assert is_bst(self)
        self._root = None
        self._n = 0
        assert is_bst(self)

    def _is_root(self, u: _BSTNode) -> bool:
        """Checks if u is the same object as self.root.

        Time complexity: O(1)."""
        assert is_bst(self)
        if u == self._root:
            if u is not None:
                assert u.parent is None
        return u == self._root

    def insert(self, key: object) -> None:
        """Inserts key into this BST.

        Time complexity: O(h)."""
        assert is_bst(self)

        if key is None:
            raise ValueError("key cannot be None")

        key_node = _BSTNode(key)

        if self._root is None:
            assert self._n == 0
            self._root = key_node
        else:
            c = self._root  # c is the current node.
            p = self._root.parent  # Parent of c.

            while c is not None:
                p = c
                if key_node.key < c.key:
                    c = c.left
                else:
                    c = c.right

            if key_node.key < p.key:
                p.left = key_node
            else:
                p.right = key_node

            key_node.parent = p

        self._n += 1

        assert is_bst(self)

    def contains(self, key: object) -> bool:
        """Returns true if key is in this BST, false otherwise.

        Time complexity: O(h)."""
        assert is_bst(self)
        if key is None:
            raise ValueError("key cannot be None")
        key_node = self._search_key_iteratively(key, self._root)
        assert self._search_key_recursively(key, self._root) == key_node
        assert is_bst(self)
        return key_node is not None

    @staticmethod
    def _search_key_iteratively(key: object, u: _BSTNode) -> _BSTNode:
        """Returns the _BSTNode object c such that c.key == key, or None if no
        such object exists.

        Time complexity: O(m)."""
        c = u  # Current node.
        while c is not None:
            if key == c.key:
                return c
            elif key < c.key:
                c = c.left
            else:
                c = c.right

    def _search_key_recursively(self, key: object, u: _BSTNode) -> _BSTNode:
        """Returns the _BSTNode object c such that c.key == key, or None if no
        such object exists.

        Time complexity: O(m)."""
        if u is None or key == u.key:
            return u
        elif key < u.key:
            return self._search_key_recursively(key, u.left)
        else:
            return self._search_key_recursively(key, u.right)

    def rank(self, key: object) -> int:
        """Returns the number of keys strictly less than key.

        Time complexity: O(h)."""
        assert is_bst(self)
        if not self.contains(key):
            raise LookupError("key was not found")
        return self._rank(self._root, key, 0)

    def _rank(self, u: _BSTNode, key, r: int) -> int:
        if u is None:
            return r
        if u.key < key:
            r += 1
        r = self._rank(u.left, key, r)
        r = self._rank(u.right, key, r)
        return r

    def height(self) -> int:
        """Returns the maximum height of this BST.

        Since this is not a balanced BST, the maximum height may vary during the
        lifetime of this BST.

        Time complexity: O(h)."""
        assert is_bst(self)
        if self._root is None:
            return 0
        else:
            return self._height(self._root)

    def _height(self, u: _BSTNode) -> int:
        if u is None:
            return 0
        return 1 + max(self._height(u.left), self._height(u.right))

    def minimum(self) -> object:
        """Returns the minimum key in this BST, or None if this BST is empty.

        Time complexity: O(h)."""
        assert is_bst(self)
        if self._root is not None:
            m = BST._minimum(self._root)
            assert m == BST._minimum_recursively(self._root)
            assert is_bst(self)
            return m.key if m is not None else None

    @staticmethod
    def _minimum(u: _BSTNode) -> _BSTNode:
        """Returns the node with the minimum key rooted at u."""
        assert u is not None
        while u.has_left_child():
            u = u.left
        return u

    @staticmethod
    def _minimum_recursively(u: _BSTNode) -> _BSTNode:
        """Recursive version of the BST._minimum function."""
        assert u is not None
        if u.has_left_child():
            u = BST._minimum_recursively(u.left)
        return u

    def maximum(self) -> object:
        """Returns the maximum key in this BST, or None if this BST is empty.

        Time complexity: O(h)."""
        assert is_bst(self)
        if self._root is not None:
            m = BST._maximum(self._root)
            assert m == BST._maximum_recursively(self._root)
            assert is_bst(self)
            return m.key if m is not None else None

    @staticmethod
    def _maximum(u: _BSTNode) -> _BSTNode:
        """Returns the node with the maximum key rooted at u."""
        assert u is not None
        while u.has_right_child():
            u = u.right
        return u

    @staticmethod
    def _maximum_recursively(u: _BSTNode) -> _BSTNode:
        """Recursive version of the BST._maximum function."""
        assert u is not None
        if u.has_right_child():
            u = BST._maximum_recursively(u.right)
        return u

    def successor(self, key: object) -> object:
        """Finds the successor of key, i.e. the smallest element greater than
        key, or None if key does not have a successor.

        If key has a right subtree, then the successor of key is the minimum of
        that right subtree.

        Otherwise it is the first ancestor of key, lets call it A, such that key
        falls in the left subtree of A.

        Time complexity: O(h)."""
        assert is_bst(self)
        if key is None:
            raise ValueError("key cannot be None")

        key_node = self._search_key_iteratively(key, self._root)
        if key_node is None:
            raise LookupError("key not in this BST")

        s = BST._successor(key_node)

        assert is_bst(self)

        return s.key if s is not None else None

    @staticmethod
    def _successor(u: _BSTNode) -> _BSTNode:
        """Returns the _BSTNode representing the successor of u."""
        assert u is not None

        if u.has_right_child():
            return BST._minimum(u.right)

        p = u.parent
        while p is not None and p.right == u:
            u = p
            p = u.parent

        return p

    def predecessor(self, key: object) -> object:
        """Finds the predecessor of the node key, i.e. the greatest element
        smaller than key, or None if key does not have a predecessor.

        Time complexity: O(h)."""
        assert is_bst(self)

        if key is None:
            raise ValueError("key cannot be None")

        key_node = self._search_key_iteratively(key, self._root)
        if key_node is None:
            raise LookupError("key not in this BST")

        p = BST._predecessor(key_node)

        assert is_bst(self)

        return p.key if p is not None else None

    @staticmethod
    def _predecessor(u: _BSTNode) -> _BSTNode:
        """Returns the _BSTNode representing the predecessor of u."""
        assert u is not None

        if u.has_left_child():
            return BST._maximum(u.left)

        p = u.parent
        while p is not None and u == p.left:
            u = p
            p = u.parent

        return p

    def remove_max(self) -> None:
        """Removes the greatest element from self.

        Time complexity: O(h)."""
        assert is_bst(self)

        if self.is_empty():
            return

        u = self._root

        # Note that the maximum element is all the way to the right, and it
        # cannot have a right child, but it can still have a left subtree.
        m = BST._maximum(u)

        if m.left is not None:  # m has a left subtree.
            if self._is_root(m):  # m is the root.
                self._root = m.left
                m.left.parent = None  # self.root.parent = None
            else:  # m is NOT the root.
                m.left.parent = m.parent
                m.parent.right = m.left
        else:  # m has NO children
            if self._is_root(m):
                self._root = None
            else:
                m.parent.right = None

        self._n -= 1
        assert is_bst(self)

    def remove_min(self) -> None:
        """Removes the smallest element from self.

        Time complexity: O(h)."""
        assert is_bst(self)

        if self.is_empty():
            return

        u = self._root
        m = BST._minimum(u)

        if m.right is not None:
            if self._is_root(m):
                self._root = m.right
                m.right.parent = None
            else:
                m.right.parent = m.parent
                m.parent.left = m.right
        else:  # m has not right subtree.
            if self._is_root(m):
                self._root = None
            else:  # m is an internal node with no right subtree.
                m.parent.left = None

        self._n -= 1
        assert is_bst(self)

    def delete(self, key: object) -> None:
        """Deletes key from self, if it exists.

        There are 3 cases of deletion:

        1. key has no children,
        2. key has one subtree (or child), and
        3. key has the left and right subtrees (or children).

        Time complexity: O(h)."""
        assert is_bst(self)

        if key is None:
            raise ValueError("key cannot be None")

        key_node = self._search_key_iteratively(key, self._root)
        if key_node is None:
            raise LookupError("key not in this BST")

        self._n -= 1
        self._delete_aux(key_node)
        assert is_bst(self)

    def _delete_aux(self, u: _BSTNode) -> _BSTNode:
        """When deleting a node u from a BST, we have basically to consider 3
        cases:

        1. u has no children, then we simply remove it by modifying its parent
        to replace u with None. If u.parent is None, then u must be the root,
        and thus we simply set the root to None.

        2. u has just one child, but we first need to decide which one (left or
        right). Then we elevate this child to u's position in the tree by
        modifying u's parent to replace u by u's child. But if u's parent is
        None, that means u was the root, and the new root becomes u's child.

        3. u has two children, then we search for u's successor s, (which must
        be in the u's right subtree, and it's the smallest of that subtree)
        which takes u's position in the tree. The rest of the u's subtree
        becomes the s's right subtree, and the u's left subtree becomes the new
        s's left subtree. This case is a little bit tricky, because it matters
        whether s is u's right child.

        Suppose s is the right child of u, then we replace u by s, which might
        or not have a right subtree, but no left subtree.

        Suppose s is not the right child of u, in this case, we replace s by its
        own right child, and then we replace u by s.

        Note that self._delete_when_two_children does not exactly do that, but
        instead it simply replaces the positions of u and s, as if s was u and u
        was s.

        After that, _delete is called again on u, but note that u is now in the
        previous s's position, and thus u has now no left subtree, but at most a
        right subtree."""
        if u.has_two_children():
            self._delete_when_two_children(u)
        else:  # u has at most one child.
            self._delete_when_at_most_one_child(u)

        u.right = u.left = u.parent = None
        return u

    def _delete_when_two_children(self, u: _BSTNode) -> None:
        """Called by _delete_aux when a node has two children."""
        assert u is not None
        # Replace u with its successor s.
        self._switch(u, self._successor(u))
        # u has at most a right child now.
        self._delete_aux(u)

    def _delete_when_at_most_one_child(self, u: _BSTNode) -> None:
        """Removes u from the tree, when u has at most one child.

        This means that u could have 0 or 1 child."""
        assert u is not None
        child = u.right
        if u.left:
            child = u.left
        if not u.has_parent():  # u is the root.
            self._root = child
        else:  # u has a parent, so it is not the root.
            if u.is_left_child():
                u.parent.left = child
            else:
                u.parent.right = child
        # child is None iff u.right and u.left are None.
        if child:
            child.parent = u.parent

    def _switch(self, x: _BSTNode, y: _BSTNode) -> None:
        """"Switches the roles of x and y in the tree by moving references."""
        assert x is not None and y is not None
        assert x != y

        if x.parent == y:
            self._switch_parent_with_child(y, x)
        elif y.parent == x:
            self._switch_parent_with_child(x, y)
        else:
            self._switch_nodes_when_not_parent_child(x, y)

    def _switch_nodes_when_not_parent_child(self, x: _BSTNode,
                                            y: _BSTNode) -> None:
        """x and y are nodes in the tree that are not related by a parent-child.

        Time complexity: O(1)."""
        assert x.parent != y and y.parent != x

        if not x.has_parent():
            self._root = y
            if y.is_left_child():
                y.parent.left = x
            else:
                y.parent.right = x
        elif not y.has_parent():
            self._root = x
            if x.is_left_child():
                x.parent.left = y
            else:
                x.parent.right = y
        else:  # Neither x nor y are the root.
            if x.is_left_child():
                if y.is_left_child():
                    y.parent.left, x.parent.left = x, y
                else:
                    y.parent.right, x.parent.left = x, y
            else:
                if y.is_left_child():
                    y.parent.left, x.parent.right = x, y
                else:
                    y.parent.right, x.parent.right = x, y

        y.parent, x.parent = x.parent, y.parent
        x.left, y.left = y.left, x.left
        x.right, y.right = y.right, x.right

        if x.left:
            x.left.parent = x
        if x.right:
            x.right.parent = x
        if y.left:
            y.left.parent = y
        if y.right:
            y.right.parent = y

    def _switch_parent_with_child(self, p: _BSTNode, c: _BSTNode) -> None:
        """Switches the roles of p and c, where p (parent) is the direct parent
        of c (child)."""
        assert c.parent == p

        if c.is_left_child():
            p.left = c.left
            if c.left:
                c.left.parent = p

            c.left = p

            c.right, p.right = p.right, c.right
            if c.right:
                c.right.parent = c
            if p.right:
                p.right.parent = p
        else:
            p.right = c.right
            if c.right:
                c.right.parent = p

            c.right = p

            c.left, p.left = p.left, c.left
            if c.left:
                c.left.parent = c
            if p.left:
                p.left.parent = p

        if p.parent:
            if p.is_left_child():
                p.parent.left = c
            else:
                p.parent.right = c
        else:  # p is the root.
            self._root = c

        c.parent = p.parent
        p.parent = c

    def in_order_traversal(self) -> None:
        """Prints the elements of the tree in increasing order.

        Time complexity: O(h)."""
        assert is_bst(self)
        self._in_order_traversal(self._root)
        print("\n")

    def _in_order_traversal(self, u: _BSTNode, e=", ") -> None:
        if u is not None:
            self._in_order_traversal(u.left)
            print(u, end=e)
            self._in_order_traversal(u.right)

    def pre_order_traversal(self) -> None:
        """Prints the keys of this tree in pre-order.

        The pre-order consists of recursively printing first a node u, then its
        left child node and then its right child node.

        Time complexity: O(h)."""
        assert is_bst(self)
        self._pre_order_traversal(self._root)
        print("\n")

    def _pre_order_traversal(self, u: _BSTNode, e=", ") -> None:
        if u is not None:
            print(u, end=e)
            self._pre_order_traversal(u.left)
            self._pre_order_traversal(u.right)

    def post_order_traversal(self) -> None:
        """Prints the keys of this tree in post-order. It does the opposite of
        pre_order_traversal.

        Time complexity: O(h)."""
        assert is_bst(self)
        self._post_order_traversal(self._root)
        print("\n")

    def _post_order_traversal(self, u: _BSTNode, e=", ") -> None:
        if u is not None:
            self._post_order_traversal(u.left)
            self._post_order_traversal(u.right)
            print(u, end=e)

    def reverse_in_order_traversal(self) -> None:
        """Prints the keys of this tree in decreasing order. It does the
        opposite of self.in_order_traversal.

        Time complexity: O(h)."""
        assert is_bst(self)
        self._reverse_in_order_traversal(self._root)
        print("\n")

    def _reverse_in_order_traversal(self, u: _BSTNode, e=", ") -> None:
        if u is not None:
            self._reverse_in_order_traversal(u.right)
            print(u, end=e)
            self._reverse_in_order_traversal(u.left)

    def __str__(self):
        if self._root is None:
            return 'Nothing to print: this BST is empty.'
        return '\n'.join(build_pretty_bst(self._root)) + "\n"

    def __repr__(self):
        return self.__str__()


def build_pretty_bst(node: _BSTNode, only_list: bool = True):
    """Pretty-prints this BST object."""
    if not isinstance(_BSTNode):
        raise TypeError("node must be an instance of _BSTNode")
    if not isinstance(only_list, bool):
        raise TypeError("only_list must be a bool")

    if node is None:
        if only_list:
            return []
        else:
            return [], 0, 0

    fill = "_"

    left_lines, left_pos, left_width = build_pretty_bst(node.left)
    right_lines, right_pos, right_width = build_pretty_bst(node.right)
    middle = max(right_pos + left_width - left_pos + 1, len(node.key), 2)
    pos = left_pos + middle // 2
    width = left_pos + middle + right_width - right_pos

    while len(left_lines) < len(right_lines):
        left_lines.append(' ' * left_width)

    while len(right_lines) < len(left_lines):
        right_lines.append(' ' * right_width)

    if ((middle - len(node.key)) % 2 == 1 and node.parent is not None and
            node is node.parent.left and len(node.key) < middle):
        node.key += fill

    node.key = node.key.center(middle, fill)

    if node.key[0] == fill:
        node.key = ' ' + node.key[1:]

    if node.key[-1] == fill:
        node.key = node.key[:-1] + ' '

    lines = [' ' * left_pos + node.key + ' ' * (right_width - right_pos),
             ' ' * left_pos + '/' + ' ' * (middle - 2) +
             '\\' + ' ' * (right_width - right_pos)] + \
            [left_line + ' ' * (width - left_width - right_width) +

             right_line

             for left_line, right_line in zip(left_lines, right_lines)]

    if only_list:
        return lines
    else:
        return lines, pos, width


def has_bst_property(n: _BSTNode) -> bool:
    """Check if the tree under n has the binary-search tree property, i.e., for
    each node u, all nodes in its left sub-tree are smaller than u, and all
    nodes in its right sub-tree are greater than u.

    It also checks that parent pointers are correctly set up."""
    if n is not None:
        if n.left and n.key < n.left.key:
            return False
        if n.right and n.key > n.right.key:
            return False

        # Asserting n.left and n.right have n as parent.
        if n.left:
            if n.left.parent != n:
                return False
        if n.right:
            if n.right.parent != n:
                return False

        return has_bst_property(n.left) and has_bst_property(n.right)

    return True


def all_bst_nodes(n: _BSTNode) -> bool:
    """Returns true if all nodes under n (including n) are instances of _BSTNode,
    false otherwise."""
    if n is not None:
        # If either n or its parent are not instances of _BSTNode.
        if (not isinstance(n, _BSTNode) or
                (n.parent is not None and not isinstance(n.parent, _BSTNode))):
            return False
        return all_bst_nodes(n.left) and all_bst_nodes(n.right)
    return True


def is_bst(t: BST) -> bool:
    """Returns true if t is a valid BST object, false otherwise.

    Invariant: for each node n in t, if n.left exists, then n.left <= n, and if
    n.right exists, then n.right >= n."""
    if not isinstance(t, BST):
        return False
    if t._root and t._root.parent is not None:
        return False
    return all_bst_nodes(t._root) and has_bst_property(t._root)
