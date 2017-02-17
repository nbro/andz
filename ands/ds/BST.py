#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 01/07/2015

Updated: 16/02/2017

# Description

### Coding Conventions

In general, if a variable name has more than one word,
those words are separated by _ (underscores).
Functions' names should roughly describe what the function does.
Names of functions' local variables are usually short,
and not so self-descriptive, but, on the other hand,
comments are usually provide on the first occurrence of the name,
in order to explain the purpose of such a variable.

#### Functions

- Methods that start with _ should not be called,
because they might either be "helper" or private functions.

#### Parameters

- `u`, `v`, `z` and `w` are used to indicate that a general `BSTNode` object is expected.

- `s` is used to indicate that a source node is expected.

- `x` is used when the parameter's expected type can either be a `BSTNode` object
or any other comparable object to represent keys.

- `ls` is usually used to indicate that a list or a tuple is expected.

#### Local Variables

- `c` usually indicates some "current" changing variable.

- `p` is usually `c`'s parent.

#### Docstrings

Under methods' signatures, h in O(h) is the height of the tree.
Note that the height of a BST varies depending on how elements
are inserted and removed.
m in O(m) is the height of the subtree rooted at the node passed
as parameter.

Other names are self-descriptive.
For example, "key" and "value" are self-descriptive.

# TODO

- Improve the "randomness" of insertion into the BSTImproved class.
- Add functions "intersection" and "union".
- Implement a recursive version of insert (OPTIONAL).
- implement "is balanced" function (http://codereview.stackexchange.com/questions/108459/binary-tree-data-structure)

- Fix inconsistencies because allowing both keys and BSTNodes to be inserted, searched and deleted,
and because the BST allows duplicate elements: if, e.g., the user tries to search using a BSTNode,
there's!!!
Allow duplicates and when deleting returning values, probably doesn't make sense,
since the values could be different for nodes with same key,
and we could return one whereas the user expects another!!

# References

- [https://en.wikipedia.org/wiki/Binary_search_tree](https://en.wikipedia.org/wiki/Binary_search_tree)
- [Introduction to Algorithms (3rd edition)](https://mitpress.mit.edu/books/introduction-algorithms) by CLRS, chapter 12
- [http://algs4.cs.princeton.edu/32bst/](http://algs4.cs.princeton.edu/32bst/)
- [http://www.cs.princeton.edu/courses/archive/spr04/cos226/lectures/bst.4up.pdf](http://www.cs.princeton.edu/courses/archive/spr04/cos226/lectures/bst.4up.pdf)
- [http://algs4.cs.princeton.edu/32bst/BST.java.html](http://algs4.cs.princeton.edu/32bst/BST.java.html)
- [http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/bst.py](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/bst.py)

"""

from random import randint

__all__ = ["BST", "BSTNode", "is_bst", "BSTImproved", "build_pretty_bst", "has_bst_property", "all_bst_nodes"]


class BSTNode:
    """Class to represent a BST's node."""

    def __init__(self, key, value=None, parent=None, left=None, right=None):
        if key is None:
            raise ValueError("key cannot be None")
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        # Used for printing purposes.
        self.label = "[" + str(self.key) + "]"

    @property
    def sibling(self):
        """Returns the sibling node of this node,
        which can of course be `None`."""
        if self.parent is not None:
            if self.is_left_child():
                return self.parent.right
            else:
                return self.parent.left

    @property
    def grandparent(self):
        """Returns the parent of the parent of this node."""
        if self.parent is not None:
            return self.parent.parent

    @property
    def uncle(self):
        """Returns the uncle node of this node.
        The uncle is the sibling of the parent of this node,
        if it exists. `None` is returned if it doesn't exist,
        or the parent or grandparent of this node is `None`."""
        if self.grandparent is not None:  # implies that also parent is not None
            if self.parent == self.grandparent.left:
                return self.grandparent.right
            else:  # self.parent == self.grandparent.right:
                return self.grandparent.left

    def reset(self) -> None:
        self.parent = None
        self.left = None
        self.right = None

    def is_left_child(self) -> bool:
        if self.parent is not None:
            if self.parent.left is not None:
                return self.parent.left == self
        else:
            raise AttributeError("self does not have a parent.")

    def is_right_child(self) -> bool:
        if self.parent is not None:
            if self.parent.right is not None:
                return self.parent.right == self
        else:
            raise AttributeError("self does not have a parent.")

    def has_children(self) -> bool:
        """Returns `True` if `self` has at least one child. `False` otherwise."""
        return self.left is not None or self.right is not None

    def has_one_child(self) -> bool:
        """Returns `True` only if `self` has exactly one child. `False` otherwise."""
        return (self.left is not None and self.right is None) or \
               (self.left is None and self.right is not None)

    def has_two_children(self) -> bool:
        """Returns `True` if self has exactly two children. `False` otherwise."""
        return self.left is not None and self.right is not None

    def count(self) -> int:
        """Counts the numbers of nodes under `self` (including `self`)."""

        def _count(u, c: int):
            if u is None:
                return c
            else:
                c += 1
            c = _count(u.left, c)
            c = _count(u.right, c)
            return c

        if not self.has_children():
            return 1
        else:
            c = 0
            return _count(self, c)

    def __fields(self):
        return [["key", self.key],
                ["value", self.value],
                ["parent", self.parent],
                ["left", self.left],
                ["right", self.right],
                ["sibling", self.sibling],
                ["grandparent", self.grandparent],
                ["uncle", self.uncle]]

    def __str__(self):
        return "{" + str(self.key) + ": " + str(self.value) + "}"

    def __repr__(self):
        return self.__str__()
        # return tabulate(self.__fields(), tablefmt="fancy_grid")


class BST:
    """`BST` is a class that represents a classical binary search tree."""

    def __init__(self, root=None):
        if root is not None:
            if not isinstance(root, BSTNode):
                raise TypeError("root must be an instance of BSTNode")
            if root.parent is not None:
                raise ValueError("the parent of root must be None")
            if not all_bst_nodes(root):
                raise TypeError("not all objects under root are instances of BSTNode")
            if not has_bst_property(root):
                raise TypeError("tree rooted at root does not have the binary-search tree property")
            self._n = root.count()
        else:
            self._n = 0

        self.root = root
        assert is_bst(self)

    def _initialise_if_empty(self, u: BSTNode) -> None:
        """Sets `u` as the new root and unique node of this tree."""
        assert self.root is None
        self.root = u
        self.root.parent = None
        self.root.left = None
        self.root.right = None
        self._n = 1
        assert is_bst(self)

    def clear(self) -> None:
        """Removes all nodes from this tree.

        **Time Complexity**: O(1)."""
        assert is_bst(self)
        self.root = None
        self._n = 0
        assert is_bst(self)

    def size(self) -> int:
        """Returns the total number of nodes.

        **Time Complexity**: O(1)."""
        assert is_bst(self)
        if self.root is not None:
            assert self.root.count() == self._n
        else:
            assert self._n == 0
        return self._n

    def is_empty(self) -> bool:
        """Returns `True` if this tree has 0 nodes.

        **Time Complexity**: O(1)."""
        assert is_bst(self)
        return self.size() == 0

    def is_root(self, u: BSTNode) -> bool:
        """Checks if `u` is the same object as `self.root`.

        **Time Complexity**: O(1)."""
        assert is_bst(self)
        if u == self.root:
            if u is not None:
                assert u.parent is None
        return u == self.root

    def insert(self, x: object, value=None) -> None:
        """Inserts (normally) `x` into this BST object.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, BSTNode):
            x = BSTNode(x, value)
        if x.left is not None or x.right is not None or x.parent is not None:
            raise ValueError("x cannot have left or right children, or parent.")

        if self.root is None:
            self._initialise_if_empty(x)
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
            self._n += 1

        assert is_bst(self)

    def insert_many(self, ls: list) -> None:
        """Calls `self.insert` for all elements of `ls`.
        Therefore the elements of `ls` should either be
        `BSTNode` objects or they should represent keys.

        **Time Complexity**: O(len(ls)*h)."""
        assert is_bst(self)
        if not isinstance(ls, list):
            raise TypeError("ls must be an instance of list")
        for elem in ls:
            self.insert(elem)
        assert is_bst(self)

    def search(self, key: object) -> BSTNode:
        """Searches for the key in the tree.

        `key` must be a comparable object of the same type as the other keys.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        if key is None:
            raise ValueError("key cannot be None.")
        return self.search_key_iteratively(key)

    def search_key_iteratively(self, key: object) -> BSTNode:
        """Searches iteratively for key starting from the root.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        result = BST._search_key_iteratively(key, self.root)
        assert result == self.search_key_recursively(key)
        return result

    @staticmethod
    def _search_key_iteratively(key: object, u: BSTNode) -> BSTNode:
        """Searches iteratively for key in the subtree rooted at `u`.

        **Time Complexity**: O(m)."""
        c = u  # c is the current node
        while c is not None:
            if key == c.key:
                return c
            elif key < c.key:
                c = c.left
            else:
                c = c.right

    def search_key_recursively(self, key: object) -> BSTNode:
        """Searches recursively for `key` starting from `self.root`.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        return self._search_key_recursively(key, self.root)

    def _search_key_recursively(self, key: object, u: BSTNode) -> BSTNode:
        """Searches recursively for `key` in the subtree rooted at `u`.

        `key` must be a comparable object of the same type as the other keys.

        **Time Complexity**: O(m),
        where `m` is the height of the subtree rooted at `u`,
        if `u` is not `None`. Else the time complexity is O(1)."""
        if u is None or key == u.key:
            return u
        elif key < u.key:
            return self._search_key_recursively(key, u.left)
        else:
            return self._search_key_recursively(key, u.right)

    def contains_key(self, key: object) -> bool:
        """Returns `True` if a `BSTNode` object with `key` exists in the tree.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        return self.search_key_iteratively(key) is not None

    def rank(self, key: object) -> int:
        """Returns the number of keys strictly less than `key`.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        if key is None:
            raise ValueError("key cannot be None.")
        if not self.contains_key(key):
            raise LookupError("key was not found.")
        return self._rank(self.root, key, 0)

    def _rank(self, u: BSTNode, key, r: int) -> int:
        if u is None:
            return r
        if u.key < key:
            r += 1
        r = self._rank(u.left, key, r)
        r = self._rank(u.right, key, r)
        return r

    def height(self) -> int:
        """Returns the maximum depth or height of the tree.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        if self.root is None:
            return 0
        return self._height(self.root)

    def _height(self, u: BSTNode) -> int:
        if u is None:
            return 0
        return 1 + max(self._height(u.left), self._height(u.right))

    def minimum(self) -> BSTNode:
        """Calls `BST._minimum_r(self.root)` if `self.root` is evaluated to `True`.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        if self.root is not None:
            m = BST._minimum(self.root)
            assert m == BST._minimum_r(self.root)
            return m

    @staticmethod
    def _minimum_r(u: BSTNode) -> BSTNode:
        """Recursive version of the `BST._minimum(u)` function."""
        if u.left is not None:
            u = BST._minimum_r(u.left)
        return u

    @staticmethod
    def _minimum(u: BSTNode) -> BSTNode:
        """Returns the node (rooted at u) with the minimum key."""
        while u.left is not None:
            u = u.left
        return u

    def maximum(self) -> BSTNode:
        """Calls `BST._maximum_r(self.root)` if `self.root` is evaluated to `True`.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if self.root is not None:
            m = BST._maximum(self.root)
            assert m == BST._maximum_r(self.root)
            return m

    @staticmethod
    def _maximum_r(u: BSTNode) -> BSTNode:
        """Recursive version of `BST._maximum`."""
        if u.right is not None:
            u = BST._maximum_r(u.right)
        return u

    @staticmethod
    def _maximum(u: BSTNode) -> BSTNode:
        """Returns the node (rooted at u) with the maximum key."""
        while u.right is not None:
            u = u.right
        return u

    def successor(self, x: object) -> BSTNode:
        """Finds the successor of `x`,
        i.e. the smallest element greater than `x`.

        If `x` has a right subtree,
        then the successor of `x` is the minimum of that right subtree.

        Otherwise it is the first ancestor of `x`, lets call it `A`,
        such that `x` falls in the left subtree of `A`.

        `x` can either be a reference to an actual `BSTNode` object,
        or it can be a key of a supposed node in self.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if not isinstance(x, BSTNode):
            x = self.search_key_iteratively(x)
            if x is None:
                raise LookupError("no node was found with key=x.")
        else:
            if not self.contains_key(x.key):
                raise LookupError("x does not belong to this tree")

        if x.right is not None:
            return BST._minimum(x.right)

        p = x.parent
        while p is not None and p.right == x:
            x = p
            p = x.parent
        return p

    def predecessor(self, x: object) -> BSTNode:
        """Finds the predecessor of the node `x`,
        i.e. the greatest element smaller than `x`.

        `x` can either be a reference to an actual `BSTNode` object,
        or it can be a key of a supposed node in self.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if not isinstance(x, BSTNode):
            x = self.search_key_iteratively(x)
            if x is None:
                raise LookupError("No node was found with key=x.")
        else:
            if not self.contains_key(x.key):
                raise LookupError("x does not belong to this tree")

        if x.left is not None:
            return BST._maximum(x.left)

        p = x.parent
        while p is not None and x == p.left:
            x = p
            p = x.parent
        return p

    def _left_rotate(self, x: object) -> BSTNode:
        """Left rotates the subtree rooted at node `x`.

        `x` can be a `BSTNode` object, and in that case,
        this function performs in constant time O(1);
        else, if node is not a `BSTNode` object,
        it tries to search for a `BSTNode` object with key=x,
        and, in that case, it performs in O(h) time.

        Returns the node which is at the previous position of `x`,
        that is it returns the parent of `x`.

        **Time Complexity**: O(1)."""
        if not isinstance(x, BSTNode):
            c = self.search_key_iteratively(x)
            if c is None:
                raise LookupError("key node was not found in the tree.")
        else:
            c = x

        # To left rotate a node, its right child must exist.
        if c.right is None:
            raise ValueError("left rotation cannot be performed on " + str(c) +
                             " because it does not have a right child.")

        c.right.parent = c.parent

        # Only the root has a None parent.
        if c.parent is None:
            self.root = c.right

        # Checking if c is a left or a right child,
        # in order to set the new left
        # or right child respectively of its parent.
        elif c.is_left_child():
            c.parent.left = c.right
        else:
            c.parent.right = c.right

        c.parent = c.right

        # The new right child of c becomes what is
        # the left child of its previous right child.
        c.right = c.parent.left

        # Set c to be the parent of its new right child.
        if c.right is not None:
            c.right.parent = c

        # Set c to be the new left child of its new parent.
        c.parent.left = c
        return c.parent

    def _right_rotate(self, x: object) -> BSTNode:
        """Right rotates the subtree rooted at node `x`.
        See doc-strings of `self._left_rotate`.

        **Time Complexity**: O(1)."""
        if not isinstance(x, BSTNode):
            c = self.search_key_iteratively(x)
            if c is None:
                raise LookupError("key node was not found in the tree.")
        else:
            c = x

        if c.left is None:
            raise ValueError("right rotation cannot be performed on " + str(c) +
                             " because it does not have a left child.")

        c.left.parent = c.parent

        if c.parent is None:
            self.root = c.left
        elif c.is_left_child():
            c.parent.left = c.left
        else:
            c.parent.right = c.left

        c.parent = c.left
        c.left = c.parent.right

        if c.left is not None:
            c.left.parent = c

        c.parent.right = c
        return c.parent

    def remove_max(self) -> BSTNode:
        """Removes and returns the maximum element of the tree, if it is not empty.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if self.is_empty():
            return

        u = self.root

        # Note that the maximum element is all the way to the right,
        # and it cannot have a right child, but it can still have a left subtree.
        m = BST._maximum(u)

        if m.left is not None:  # m has a left subtree.
            if self.is_root(m):  # m is the root.
                self.root = m.left
                m.left.parent = None  # self.root.parent = None
            else:  # m is NOT the root.
                m.left.parent = m.parent
                m.parent.right = m.left
        else:  # m has NO children
            if self.is_root(m):
                self.root = None
            else:
                m.parent.right = None

        m.parent = m.left = None
        self._n -= 1
        assert is_bst(self)
        return m

    def remove_min(self) -> BSTNode:
        """Removes and returns the minimum element of the tree, if it is not empty.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if self.is_empty():
            return

        u = self.root
        m = BST._minimum(u)

        if m.right is not None:
            if self.is_root(m):
                self.root = m.right
                m.right.parent = None
            else:
                m.right.parent = m.parent
                m.parent.left = m.right
        else:  # m has not right subtree.
            if self.is_root(m):
                self.root = None
            else:  # m is an internal node with no right subtree.
                m.parent.left = None

        m.right = m.parent = None
        self._n -= 1
        assert is_bst(self)
        return m

    def delete(self, x: object) -> BSTNode:
        """Deletes `x` from self (if it exists).

        There are 3 cases of deletion:
            1. `x` has no children
            2. `x` has one subtree (or child)
            3. `x` has the left and right subtrees (or children).

        `x` can either be a reference to an actual `BSTNode` object,
        or it can be a key of a supposed node in `self`.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if x is None:
            raise ValueError("x cannot be None.")

        if not isinstance(x, BSTNode):
            x = self.search_key_iteratively(x)
            if x is None:
                raise LookupError("no node was found with key=x.")
        else:
            if not self.contains_key(x.key):
                raise LookupError("x does not belong to this tree")

        # Not calling self.is_root because it contains some assertions,
        if x.parent is None and x != self.root:
            raise ValueError("x does not have parent but it's the root")
        if x == self.root and x.parent is not None:
            raise ValueError("x has parent and is the root")

        self._n -= 1
        elem = self._delete(x)

        assert is_bst(self)

        return elem

    def _delete(self, u: BSTNode) -> BSTNode:
        """This is a helper method to the delete method,
        thus it should not be called by clients.

        When deleting a node u from a BST, we have basically to consider 3 cases:
        1. u has no children
        2. u has one child
        3. u has two children

        1. u has no children, then we simply remove it
        by modifying its parent to replace u with None.
        If u.parent is None, then u must be the root,
        and thus we simply set the root to None.

        2. u has just one child,
        but we first need to decide which one (left or right).
        Then we elevate this child to u's position in the tree
        by modifying u's parent to replace u by u's child.
        But if u's parent is None, that means u was the root,
        and the new root becomes u's child.

        3. u has two children, then we search for u's successor s,
        (which must be in the u's right subtree,
        and it's the smallest of that subtree)
        which takes u's position in the tree.
        The rest of the u's subtree becomes the s's right subtree,
        and the u's left subtree becomes the new s's left subtree.
        This case is a little bit tricky,
        because it matters whether s is u's right child.

        Suppose s is the right child of u, then we replace u by s,
        which might or not have a right subtree, but no left subtree.

        Suppose s is not the right child of u,
        in this case, we replace s by its own right child,
        and then we replace u by s.

        Note that "delete_two_children" does NOT exactly do that,
        but instead it simply replaces the positions of u and s,
        as if s was u and u was s.

        After that, delete_helper is called again on u,
        but note that u is now in the previous s's position,
        and thus u has now no left subtree, but at most a right subtree."""

        def delete_at_most_one_child(v: BSTNode) -> None:
            """Removes v from the tree, when v has at most one child.
            This means that v could have 0 or 1 child."""
            child = v.right
            if v.left:
                child = v.left
            if v.parent is None:  # v is the root.
                self.root = child
            else:  # v has a parent, so it is not the root.
                if v.is_left_child():
                    v.parent.left = child
                else:
                    v.parent.right = child
            # child is None iff v.right and v.left are None.
            if child:
                child.parent = v.parent

        def delete_two_children(v: BSTNode) -> None:
            """Called by `delete_helper` when a node has two children."""
            # Replace v with its successor s.
            self._switch(v, self.successor(v))
            # v has at most a right child now.
            self._delete(v)

        if u.has_two_children():
            delete_two_children(u)
        else:  # u has at most one child
            delete_at_most_one_child(u)

        u.right = u.left = u.parent = None
        return u

    def _switch(self, u: BSTNode, v: BSTNode) -> None:
        """"Switches the roles of `u` and `v` in the tree by moving references.

        This is a PRIVATE method, and clients should therefore NOT use it directly!"""

        def switch_parent_child(p: BSTNode, c: BSTNode) -> None:
            """Switches the roles of p and c, where p (parent) is the direct parent of c (son)."""
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
            else:  # p is the root
                self.root = c

            c.parent = p.parent
            p.parent = c

        def switch_not_parent_child(z: BSTNode, w: BSTNode) -> None:
            """`z` and `w` are nodes in the tree that are not related by a parent-child.

            **Time Complexity**: O(1)."""
            assert z.parent != w and w.parent != z

            if not z.parent:
                self.root = w
                if w.is_left_child():
                    w.parent.left = z
                else:
                    w.parent.right = z
            elif not w.parent:
                self.root = z
                if z.is_left_child():
                    z.parent.left = w
                else:
                    z.parent.right = w
            else:  # neither z nor w is the root
                if z.is_left_child():
                    if w.is_left_child():
                        w.parent.left, z.parent.left = z, w
                    else:
                        w.parent.right, z.parent.left = z, w
                else:
                    if w.is_left_child():
                        w.parent.left, z.parent.right = z, w
                    else:
                        w.parent.right, z.parent.right = z, w

            w.parent, z.parent = z.parent, w.parent
            z.left, w.left = w.left, z.left
            z.right, w.right = w.right, z.right

            if z.left:
                z.left.parent = z
            if z.right:
                z.right.parent = z
            if w.left:
                w.left.parent = w
            if w.right:
                w.right.parent = w

        if u is None:
            raise ValueError("u cannot be None.")
        if v is None:
            raise ValueError("v cannot be None.")
        if u == v:
            raise ValueError("u cannot be equal to v.")

        assert self.contains_key(u.key) and self.contains_key(v.key)

        if u.parent == v:
            switch_parent_child(v, u)
        elif v.parent == u:
            switch_parent_child(u, v)
        else:
            switch_not_parent_child(u, v)

    def in_order_traversal(self) -> None:
        """Prints the elements of the tree in increasing order.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        self._in_order_traversal(self.root)
        print("\n")

    def _in_order_traversal(self, u: BSTNode, e=", ") -> None:
        if u is not None:
            self._in_order_traversal(u.left)
            print(u, end=e)
            self._in_order_traversal(u.right)

    def pre_order_traversal(self) -> None:
        """Prints the keys of this tree in pre-order.
        The pre-order consists of recursively printing first a node `u`,
        then its left child node and then its right child node.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        self._pre_order_traversal(self.root)
        print("\n")

    def _pre_order_traversal(self, u: BSTNode, e=", ") -> None:
        if u is not None:
            print(u, end=e)
            self._pre_order_traversal(u.left)
            self._pre_order_traversal(u.right)

    def post_order_traversal(self) -> None:
        """Prints the keys of this tree in post-order.
        It does the opposite of `pre_order_traversal`.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        self._post_order_traversal(self.root)
        print("\n")

    def _post_order_traversal(self, u: BSTNode, e=", ") -> None:
        if u is not None:
            self._post_order_traversal(u.left)
            self._post_order_traversal(u.right)
            print(u, end=e)

    def reverse_in_order_traversal(self) -> None:
        """Prints the keys of this tree in decreasing order.

        It does the opposite of `self.in_order_traversal`.

        **Time Complexity**: O(h)."""
        assert is_bst(self)
        self._reverse_in_order_traversal(self.root)
        print("\n")

    def _reverse_in_order_traversal(self, u: BSTNode, e=", ") -> None:
        if u is not None:
            self._reverse_in_order_traversal(u.right)
            print(u, end=e)
            self._reverse_in_order_traversal(u.left)

    def __str__(self):
        if self.root is None:
            return 'Nothing to print: this BST is empty.'
        return '\n'.join(build_pretty_bst(self.root)) + "\n"

    def __repr__(self):
        return self.__str__()


class BSTImproved(BST):
    """Binary-search tree that provides somehow randomness at insertion."""

    def __init__(self, root=None):
        BST.__init__(self, root)

    def insert(self, x: object, value=None) -> None:
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
        assert is_bst(self)
        r = randint(0, self.size() * 3 // 8)  # random operation for now!!
        if r == 0:
            self.root_insert(x, value)
        else:
            self.tail_insert(x, value)
        assert is_bst(self)

    def tail_insert(self, x: object, value=None) -> None:
        """Inserts (normally) `x` into this BST object.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, BSTNode):
            x = BSTNode(x, value)
        if x.left is not None or x.right is not None or x.parent is not None:
            raise ValueError("x cannot have left or right children, or parent.")

        if self.root is None:
            self._initialise_if_empty(x)
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
            self._n += 1

        assert is_bst(self)

    def root_insert(self, x: object, value=None) -> None:
        """Inserts `x` as the root of this tree.

        **Time Complexity**: O(h)."""
        assert is_bst(self)

        def _root_insert(u: BSTNode, v: BSTNode):
            """Helper method for `self.root_insert`."""
            if u is None:
                return v
            if v.key < u.key:
                u.left = _root_insert(u.left, v)
                u = self._right_rotate(u)
            else:
                u.right = _root_insert(u.right, v)
                u = self._left_rotate(u)
            return u

        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, BSTNode):
            x = BSTNode(x, value)
        if x.left is not None or x.right is not None or x.parent is not None:
            raise ValueError("x cannot have left or right children, or parent.")

        if self.root is None:
            self._initialise_if_empty(x)
        else:
            _root_insert(self.root, x)
            self._n += 1

        assert is_bst(self)


def build_pretty_bst(node: BSTNode, only_list: bool = True):
    """Pretty-prints this BST object."""
    if not isinstance(BSTNode):
        raise TypeError("node must be an instance of BSTNode")
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
    middle = max(right_pos + left_width - left_pos + 1, len(node.label), 2)
    pos = left_pos + middle // 2
    width = left_pos + middle + right_width - right_pos

    while len(left_lines) < len(right_lines):
        left_lines.append(' ' * left_width)

    while len(right_lines) < len(left_lines):
        right_lines.append(' ' * right_width)

    if (middle - len(node.label)) % 2 == 1 and node.parent is not None and \
                    node is node.parent.left and len(node.label) < middle:
        node.label += fill

    node.label = node.label.center(middle, fill)

    if node.label[0] == fill:
        node.label = ' ' + node.label[1:]

    if node.label[-1] == fill:
        node.label = node.label[:-1] + ' '

    lines = [' ' * left_pos + node.label + ' ' * (right_width - right_pos),
             ' ' * left_pos + '/' + ' ' * (middle - 2) +
             '\\' + ' ' * (right_width - right_pos)] + \
            [left_line + ' ' * (width - left_width - right_width) +

             right_line

             for left_line, right_line in zip(left_lines, right_lines)]

    if only_list:
        return lines
    else:
        return lines, pos, width


def has_bst_property(n: BSTNode) -> bool:
    """Check if the tree under n has the binary-search tree property,
    i.e., for each node `u`, all nodes in its left sub-tree are smaller than `u`,
    and all nodes in its right sub-tree are greater than `u`.

    It also checks that parent pointers are correctly set up."""
    if n is not None:
        if n.left and n.key < n.left.key:
            return False
        if n.right and n.key > n.right.key:
            return False

        # Asserting n.left and n.right have n as parent
        if n.left:
            if n.left.parent != n:
                return False
        if n.right:
            if n.right.parent != n:
                return False

        return has_bst_property(n.left) and has_bst_property(n.right)

    return True


def all_bst_nodes(n: BSTNode) -> bool:
    """Returns `True` if all nodes under `n` (including `n`)
    are instances of `BSTNode`, `False` otherwise."""
    if n is not None:
        # If either n or its parent are not instances of BSTNode
        if not isinstance(n, BSTNode) or (n.parent is not None and not isinstance(n.parent, BSTNode)):
            return False
        return all_bst_nodes(n.left) and all_bst_nodes(n.right)
    return True


def is_bst(t: BST) -> bool:
    """Returns `True` if `t` is a valid `BST` object. `False` otherwise.

    Invariant: for each node `n` in `t`,
    if `n.left` exists, then `n.left <= n`,
    and if `n.right` exists, then `n.right >= n`."""
    if not isinstance(t, BST):
        return False
    if t.root and t.root.parent is not None:
        return False
    return all_bst_nodes(t.root) and has_bst_property(t.root)
