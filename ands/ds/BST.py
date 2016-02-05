#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/2016

BST is a class that represents a classical binary search tree.

## Names' Conventions
In general, if a variable name has more than one word,
those words are separated by _ (underscores).
Functions' names should roughly describe what the function does.
Names of functions' local variables are usually short,
and not so self-descriptive, but, on the other hand,
comments are usually provide on the first occurrence of the name,
in order to explain the purpose of such a variable.

### Functions
- Methods that start with _ should not be called.
They are usually helper functions.

- Methods that start with __ should definitely NOT be called.
They are helper functions that usually are not independent from other functions.

### Parameters
- u and v are used to usually indicate that a BSTNode object is expected.
- s is used to indicate that a source node (which is also BSTNode object) is expected.
- x is used when the parameter's expected type can either be a BSTNode object
or any other comparable object to represent keys.
- ls is usually used to indicate that a list or a tuple is expected.

### Local Variables
- c usually indicates some "current" changing variable.
- p is usually c's parent.

### Docstrings
Under methods' signatures, h in O(h) is the height of the tree.
Note that the height of a BST varies
depending on how elements are inserted and removed.

Other names are self-descriptive.
For example, "key" and "value" are self-descriptive.

## Resources

- https://en.wikipedia.org/wiki/Binary_search_tree

- Introduction to Algorithms (3rd edition) by CLRS, chapter 12.

- http://algs4.cs.princeton.edu/32bst/

- http://www.cs.princeton.edu/courses/archive/spr04/cos226/lectures/bst.4up.pdf

- http://algs4.cs.princeton.edu/32bst/BST.java.html

## TODO
- Improve the "randomness" of insertion into the bst.
- Implement a recursive version of insert_key (OPTIONAL).
- add functions "intersection" and "union"
- implement "is balanced" function (http://codereview.stackexchange.com/questions/108459/binary-tree-data-structure)
"""

from ands.ds.BSTNode import BSTNode
from random import randint


__all__ = ["BST"]


class BST:
    """Represents a classical binary search tree."""

    def __init__(self, root=None, name="BST"):
        self.root = root
        self.name = name
        self.n = 0  # number of nodes
        
        if root is not None:
            self._initialise(root)

    # INITIALISE

    def _initialise(self, u: BSTNode):
        """Sets u as the new root and unique node of this tree."""
        self.root = u
        self.root.parent = None
        self.root.left = None
        self.root.right = None
        self.n = 1

    def size(self):
        """Returns the total number of nodes."""
        return self.n

    def is_empty(self):
        """Returns True if this tree has 0 nodes."""
        return self.size() == 0

    def is_the_root(self, u):
        """Checks if u is a reference pointing to the root object."""
        return u == self.root
    
    def clear(self):
        """Removes all nodes from this tree."""
        self.root = None
        self.n = 0

    # INSERTIONS

    def insert(self, x, value=None):
        """Inserts x into this tree.

        x can either be a BSTNode object,
        or it can be a key of any other type,
        but it should be of the same type of the other keys,
        and these keys should be comparable objects.

        Note that the height of a BST varies
        depending on how elements are inserted and removed.
        For example, if we insert a list of numbers in increasing order,
        the resulting BST object will look like a chain with height n - 1,
        where n is the number of elements inserted.
        In general, the optimal height is logarithmic,
        and to get closer to the optimal height,
        randomly insertion of numbers usually is used.

        If we have n keys to insert, there are n! (n-factorial)
        ways of inserting those n keys into the binary search tree.
        When we randomly insert them, those permutations are equally likely.

        So, the expected height of a tree created with randomly insertions is O(log_2(n)).
        For a proof, see chapter 12 of Introduction to Algorithms (3rd ed.) by CLRS.

        This function does a pseudo-random insertion of keys."""
        r = randint(0, self.size() * 3 // 8)  # * 3 // 8 is just a random operation...
        if r == 0:
            self.root_insert(x, value)
        else:
            self.tail_insert(x, value)

    def insert_many(self, ls):
        """Calls self.tail_insert for all elements of ls.

        Therefore the elements of ls should either be
        BSTNode objects or they should represent keys.

        Time complexity: O(len(ls)*h)"""
        for i in ls:
            self.insert(i)

    def tail_insert(self, x, value=None):
        """Inserts x into this BST object.

        x can either be a BSTNode object,
        or it can be a key of any other type,
        but it should be of the same type of the other keys,
        and these keys should be comparable objects.
        Note that if you tail_insert x as a key,
        you can also pass a value to associate with x.

        Time complexity: O(h)"""
        if x is None:
            raise ValueError("x cannot be None.")

        if not isinstance(x, BSTNode):
            x = BSTNode(x, value)

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
        """Inserts x as the root of this tree.

        x can either be a key or a BSTNode object.
        In the former case, a BSTNode object is first created to host x.
        If x is a key, you can also provide a value,
        which is then associated with the BSTNode object with key x.

        Time complexity: O(h)"""
        if x is None:
            raise ValueError("x cannot be None.")
        if not isinstance(x, BSTNode):
            x = BSTNode(x, value)
            
        if self.root is None:
            self._initialise(x)
        else:
            self._root_insert(self.root, x)
            self.n += 1

    def _root_insert(self, u: BSTNode, v: BSTNode):
        """Helper method for self.root_insert

        Time complexity: O(h)"""
        if u is None:
            return v
        if v.key < u.key:
            u.left = self._root_insert(u.left, v)
            u = self.right_rotate(u)
        else:
            u.right = self._root_insert(u.right, v)
            u = self.left_rotate(u)
        return u

    # SEARCH

    def search(self, key, s: BSTNode=None) -> BSTNode:
        """Searches for the key in the tree.
        If s is specified, then this procedure starts searching from s.

        key must be a comparable object of the same type as the other keys.

        Time complexity: O(h)"""
        if key is None:
            raise ValueError("key cannot be None.")
        if s is None:
            return self.search_i(key)
        else:
            return BST._search_i(key, s)

    def search_r(self, key) -> BSTNode:
        """Searches recursively for key starting from the root.
        
        Time complexity: O(h)"""
        return self._search_r(key, self.root)

    def _search_r(self, key, s: BSTNode) -> BSTNode:
        """Searches recursively for key in the subtree rooted at s.

        key must be a comparable object of the same type as the other keys.

        Time complexity: O(m),
        where m is the height of the subtree rooted at s,
        if s is not None. Else the time complexity is O(1)."""
        if s is None or key == s.key:
            return s
        elif key < s.key:
            return self._search_r(key, s.left)
        else:
            return self._search_r(key, s.right)

    def search_i(self, key) -> BSTNode:
        """Searches iteratively for key starting from the root.

        Time complexity: O(h)"""
        return BST._search_i(key, self.root)

    @staticmethod
    def _search_i(key, s: BSTNode):
        """Searches iteratively for key in the subtree rooted at root_node.

        Time complexity: O(m),
        where m is the height of the subtree rooted at s,
        if s is not None. Else the time complexity is constant."""
        c = s  # c is the current node
        while c:
            if key == c.key:
                return c
            elif key < c.key:
                c = c.left
            else:
                c = c.right

    # CONTAINS

    def contains(self, key):
        """Returns True if a BSTNode object with key exists in the tree."""
        return self.search_r(key) is not None

    # SELECT

    def rank(self, key):
        """Returns the number of keys strictly less than key."""
        if key is None:
            raise ValueError("key cannot be None.")
        if not self.search(key):
            raise LookupError("key was not found.")
        if self.root is None:
            return 0
        else:
            r = 0
            return self._rank(self.root, key, r)

    def _rank(self, u: BSTNode, key, r: int):
        if u is None:
            return r
        if u.key < key:
            r += 1
        r = self._rank(u.left, key, r)
        r = self._rank(u.right, key, r)
        return r

    def height(self):
        """Returns the maximum depth or height of the tree."""
        if self.root is None:
            return 0
        return self._height(self.root)

    def _height(self, u: BSTNode):
        if u is None:
            return -1
        return 1 + max(self._height(u.left), self._height(u.right))

    # TRAVERSALS

    def in_order_traversal(self):
        """See BST._in_order_traversal"""
        self._in_order_traversal(self.root)
        print("\n")

    def _in_order_traversal(self, u: BSTNode, e=", "):
        """Prints the elements of the tree in increasing order.

        Time complexity: theta(m),
        where m is the number of elements rooted under u (included)."""
        if u:
            self._in_order_traversal(u.left)
            print(u, end=e)
            self._in_order_traversal(u.right)

    def pre_order_traversal(self):
        """See BST._pre_order_traversal"""
        self._pre_order_traversal(self.root)
        print("\n")

    def _pre_order_traversal(self, u: BSTNode, e=", "):
        """Prints the keys in pre-order starting from u.
        In other words, it prints first u,
        then its left child node and then its right child node.
        It keeps doing this recursively.

        Time complexity: theta(m),
        where m is the number of elements rooted under u (included)."""
        if u:
            print(u, end=e)
            self._pre_order_traversal(u.left)
            self._pre_order_traversal(u.right)

    def post_order_traversal(self):
        """See self._post_order_traversal"""
        self._post_order_traversal(self.root)
        print("\n")

    def _post_order_traversal(self, u: BSTNode, e=", "):
        """Prints the keys in post-order.

        It does the opposite of BST._pre_order_traversal

        Time complexity: theta(m),
        where m is the number of elements rooted under u (included)."""
        if u:
            self._post_order_traversal(u.left)
            self._post_order_traversal(u.right)
            print(u, end=e)

    def reverse_in_order_traversal(self):
        """See self._reverse_in_order_traversal"""
        self._reverse_in_order_traversal(self.root)
        print("\n")

    def _reverse_in_order_traversal(self, u: BSTNode, e=", "):
        """Prints the keys in decreasing order.

        It does the opposite of BST._in_order_traversal

        Time complexity: theta(m),
        where m is the number of elements rooted under u (included)."""
        if u:
            self._reverse_in_order_traversal(u.right)
            print(u, end=e)
            self._reverse_in_order_traversal(u.left)

    # ROTATIONS

    def left_rotate(self, x):
        """Left rotates the subtree rooted at node x.

        x can be a BSTNode object, and in that case,
        this function performs in constant time O(1);
        else, if node is not a BSTNode object,
        it tries to search for a BSTNode object with key=x,
        and, in that case, it performs in O(h) time.

        Returns the node which is at the previous position of x,
        that is it returns the parent of x."""

        c = None  # It will rotate the subtree rooted at c.

        if not isinstance(x, BSTNode):
            c = self.search(x)
            if c is None:
                raise LookupError("key node was not found in the tree.")
        else:  # x should be a BSTNode object
            c = x

        if c is None:
            raise ValueError("x cannot be None.")
        
        # To left rotate a node, its right child must exist.
        if c.right is None:
            raise ValueError("Left rotation cannot be performed on " + str(c) +
                            " because it does not have a right child.")

        c.right.parent = c.parent

        # If the following expression is evaluated to True,
        # then this implies that c is the root
        # and the new root becomes the right child.
        if c.parent is None:
            self.root = c.right

        # Checking if c is a left or a right child,
        # in order to set the new left or right child (respectively) of its parent.
        elif c.is_left_child():
            c.parent.left = c.right

        else:  # c.is_right_child():
            c.parent.right = c.right

        # Setting the new parent of c,
        # which is its right child.
        c.parent = c.right

        # Setting the new right child of c
        # Note that the current parent of c
        # is what was its previous right child
        # So, basically, the new right child of c
        # becomes what is the left child of its previous right child.
        c.right = c.parent.left

        # Checking if the new right child of c is None,
        # because, if it is not, we need to set its parent to be c
        if c.right is not None:
            c.right.parent = c

        # Now, we can set c to be the new left child
        # of its new parent (which was its previous right child).
        c.parent.left = c

        return c.parent

    def right_rotate(self, x):
        """Right rotates the subtree rooted at node x.
        See doc-strings of left_rotate."""
        c = None

        if not isinstance(x, BSTNode):
            c = self.search(x)
            if c is None:
                raise LookupError("key node was not found in the tree.")
        else:
            c = x

        if c is None:
            raise ValueError("x cannot be None.")
        if c.left is None:
            raise ValueError("Right rotation cannot be performed on " + str(c) +
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

    # MINIMUM AND MAXIMUM

    def minimum(self):
        """Calls BST._minimum_r(self.root) if self.root is not None."""
        if self.root:
            return BST._minimum_r(self.root)

    @staticmethod
    def _minimum_r(u: BSTNode):
        """Recursive version of the BST._minimum(u) function.

        Time complexity: O(h)"""
        if u.left:
            u = BST._minimum_r(u.left)
        return u

    @staticmethod
    def _minimum(u: BSTNode):
        """Returns the node (rooted at u) with the minimum key."""
        while u.left:
            u = u.left
        return u

    def maximum(self):
        """Calls BST._maximum_r(self.root) if self.root is not None."""
        if self.root:
            return BST._maximum_r(self.root)

    @staticmethod
    def _maximum_r(u: BSTNode):
        """Recursive version of BST._maximum.

        Time complexity: O(h)"""
        if u.right:
            u = BST._maximum_r(u.right)
        return u

    @staticmethod
    def _maximum(u: BSTNode):
        """Returns the node (rooted at u) with the maximum key."""
        while u.right:
            u = u.right
        return u

    # SUCCESSOR AND PREDECESSOR

    def successor(self, u):
        """Finds the successor of u.
        If u has a right subtree,
        then the successor of u is the minimum of that right subtree.

        Otherwise it is the first ancestor, lets call it A, of u
        such that u falls in the left subtree of A.

        u can either be a reference to an actual BSTNode object,
        or it can be a key of a supposed node in self.

        Time complexity: O(h)"""
        if not isinstance(u, BSTNode):
            u = self.search(u)
            if not u:
                raise LookupError("No node was found with key=u.")

        if u.right:
            return BST._minimum_r(u.right)

        p = u.parent

        # The comparison node == p.right
        # compares basically if they are the same object.
        # See the BaseNode class.
        while p and p.right == u:
            u = p
            p = u.parent
        return p

    def predecessor(self, u):
        """Finds the successor of the node u.
        Opposite operation of successor(u).
        
        u can either be a reference to an actual BSTNode object,
        or it can be a key of a supposed node in self.

        Time complexity: O(h)"""
        if not isinstance(u, BSTNode):
            u = self.search_r(u)
            if u is None:
                raise LookupError("No node was found with key=u.")
        if u.left:
            return BST._maximum_r(u.left)

        p = u.parent

        # The comparison node == p.left
        # compares basically if they are the same object,
        # See the BaseNode class.
        while p and u == p.left:
            u = p
            p = u.parent
        return p

    # REMOVALS AND DELETIONS

    # REMOVALS

    def remove_max(self):
        """Removes and returns the maximum element of the tree, if it is not empty."""
        if self.n > 0:
            return self._remove_max(self.root)

    def _remove_max(self, u: BSTNode):
        """Removes the maximum element of the subtree rooted at u.

        Note that the maximum element is all the way to the right,
        and it cannot have a right child,
        but it can still have a left subtree.

        If u is None, exceptions will be thrown.

        Time complexity: O(h)"""
        m = BST._maximum_r(u)
        
        if m.left:  # m has a left subtree.
            if self.is_the_root(m):  # m is the root.
                self.root = m.left
                m.left.parent = None  # self.root.parent = None
            else:  # m is NOT the root.
                m.left.parent = m.parent
                m.parent.right = m.left
        else:  # m has NO children
            if self.is_the_root(m):
                self.root = None
            else:
                m.parent.right = None
                
        m.parent = m.left = None
        self.n -= 1
        return m

    def remove_min(self):
        """Removes and returns the minimum element of the tree, if it is not empty."""
        if self.n > 0:
            return self._remove_min(self.root)

    def _remove_min(self, u: BSTNode):
        """Removes and returns the minimum element of the subtree rooted at u.

        If u is None, exceptions will be thrown.

        Time complexity: O(h)"""

        m = BST._minimum_r(u)

        if m.right:
            if self.is_the_root(m):
                self.root = m.right
                m.right.parent = None
            else:
                m.right.parent = m.parent
                m.parent.left = m.right
        else:  # m has not right subtree.
            if self.is_the_root(m):
                self.root = None
            else:  # m is an internal node with no right subtree.
                m.parent.left = None

        m.right = m.parent = None
        self.n -= 1
        return m

    # DELETIONS

    def delete(self, u):
        """Deletes u from self (if it exists).

        There are 3 cases of deletion:
            1. the node has no children
            2. the node has one subtree (or child)
            3. the node has the left and right subtrees (or children).
            
        u can either be a reference to an actual BSTNode object,
        or it can be a key of a supposed node in self.

        Time complexity: O(h)"""
        if u is None:
            raise ValueError("u cannot be None.")
        
        if not isinstance(u, BSTNode):
            u = self.search_r(u)
            if u is None:
                raise LookupError("No node was found with key=u.")

        if u.parent is None and u != self.root:
            raise ValueError("u is not a valid node.")

        self.n -= 1
        return self.__delete(u)

    def __delete(self, u: BSTNode):
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
        
        Note that "self.__delete__two_children" does NOT exactly do that,
        but instead it simply replaces the positions of u and s,
        as if s was u and u was s.
        
        After that, self.__delete is called again on u,
        but note that u is now in the previous s's position,
        and thus u has now no left subtree, but at most a right subtree."""
        def __delete__at_most_one_child(v: BSTNode):
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
                
        def __delete__two_children(v: BSTNode):
            """Call by __delete when a node has two children."""
             # Replace v with its successor s.
            self._switch(v, self.successor(v))
            # Recursively calls the function that should have called this function.
            # This is done because v is now in a new position,
            # where it simply has at most one right subtree.
            self.__delete(v)
        
        if u.has_two_children():
            __delete__two_children(u)
        else:  # u has at most one child
            __delete__at_most_one_child(u)
        u.right = u.left = u.parent = None
        return u

    def _switch(self, x: BSTNode, y: BSTNode, search_first=False):
        if not x:
            raise ValueError("x cannot be None.")
        if not y:
            raise ValueError("y cannot be None.")
        if x == y:
            raise ValueError("x cannot be equal to y")

        if search_first:
            if not self.search(x.key) or not self.search(y.key):
                raise LookupError("x or y not found.")
        
        def switch_1(p, s):
            """Switches the roles of p and s,
            where p (parent) is the direct parent of s (son)."""
            assert s.parent == p
            
            if s.is_left_child():
                p.left = s.left
                if s.left:
                    s.left.parent = p
            
                s.left = p
                
                s.right, p.right = p.right, s.right
                if s.right:
                    s.right.parent = s
                if p.right:
                    p.right.parent = p
            else:
                p.right = s.right
                if s.right:
                    s.right.parent = p
                    
                s.right = p

                s.left, p.left = p.left, s.left
                if s.left:
                    s.left.parent = s
                if p.left:
                    p.left.parent = p
            
            if p.parent:
                if p.is_left_child():
                    p.parent.left = s 
                else:
                    p.parent.right = s
            else:  # p is the root
                self.root = s
                
            s.parent = p.parent
            p.parent = s

        def switch_2(u, v):
            """u and v are nodes in the tree
            that are not related by a parent-son
            or a grandparent-son relantionships."""
            assert u.parent != v and v.parent != u
            
            if not u.parent:
                self.root = v
                if v.is_left_child():
                    v.parent.left = u
                else:
                    v.parent.right = u
            elif not v.parent:
                self.root = u
                if u.is_left_child():
                    u.parent.left = v
                else:
                    u.parent.right = v
            else:  # neither u nor v is the root                
                if u.is_left_child():
                    if v.is_left_child():                   
                        v.parent.left, u.parent.left = u, v
                    else:
                        v.parent.right, u.parent.left = u, v
                else:
                    if v.is_left_child():                   
                        v.parent.left, u.parent.right = u, v
                    else:
                        v.parent.right, u.parent.right = u, v                    
                    
            v.parent, u.parent = u.parent, v.parent
            u.left, v.left = v.left, u.left
            u.right, v.right = v.right, u.right

            if u.left:
                u.left.parent = u
            if u.right:
                u.right.parent = u
            if v.left:
                v.left.parent = v
            if v.right:
                v.right.parent = v
        
        if x.parent == y:
            switch_1(y, x)            
        elif y.parent == x:
            switch_1(x, y)
        else:
            switch_2(x, y)

    def show(self):
        """Calls self.__str__()"""
        print(self)

    def __str__(self):
        if self.root is None:
            return 'Nothing to print: this BST is empty.'
        return '\n'.join(BSTPrinter.print_1(self.root)[0]) + "\n"

    def __repr__(self):
        return self.__str__()


class BSTPrinter:
    """Based on: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/bst.py"""

    @staticmethod
    def print_1(node):
        """Pretty-prints this BST object."""
        if node is None:
            return [], 0, 0

        fill = "_"

        left_lines, left_pos, left_width = BSTPrinter.print_1(node.left)
        right_lines, right_pos, right_width = BSTPrinter.print_1(node.right)
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
        return lines, pos, width


# TESTS

def bst_invariant(bst):
    """Invariant: for each node n in bst,
    if n.left exists, then n.left <= n,
    and if n.right exists, then n.right >= n."""
    return check_helper(bst.root)

def check_helper(n):
    while n is not None:
        if n.left is not None and n.key < n.left.key:
            return False
        if n.right is not None and n.key > n.right.key:
            return False
        if n.left:
            assert n.left.parent == n
        if n.right:
            assert n.right.parent == n
        return check_helper(n.left) and check_helper(n.right)        
    return True

def assert_consistencies(bst):
    """Call only when bst.root is not None"""
    assert bst.root.count() == bst.n == bst.size()
    assert bst.root.parent is None

def test_empty(b):
    assert not b.root
    assert b.size() == b.n == 0
    print("test_empty finished.")

def test_empty_size():
    b = BST()
    test_empty(b)
    assert bst_invariant(b)
    print("test_empty_size finished.")

def test_empty_contains():
    b = BST()
    for i in range(-10, 11):
        assert not b.contains(i)
    print("test_empty_contains finished.")

def test_one_size():
    b = BST()
    b.insert(12)
    assert b.size() == b.n == b.root.count() == 1
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_one_size finished.")

def test_one_contains():
    b = BST()
    b.insert(12)
    for i in range(-10, 11):
        assert not b.contains(i)
    assert b.contains(12)
    print("test_one_contains finished.")

def test_many_size():
    b = BST()
    size = 0
    for i in range(-10, 11):
        b.insert(i)
        size += 1
        assert size == b.size() == b.n == b.root.count()
        assert bst_invariant(b)
        assert_consistencies(b)
    print("test_many_size finished.")

def test_many_contains():
    b = BST()
    for i in range(-10, 11):
        b.insert(i)
    for i in range(-10, 11):
        assert b.contains(i)
    print("test_many_contains finished.")

def test_structure_many():
    b = BST()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(7)
    b.insert(20)
    b.insert(18)
    b.insert(14)
    b.insert(14)
    b.insert(12)
    b.insert(3)
    b.insert(4)
    assert 11 == b.size() == b.n == b.root.count()
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_structure_many finished.")
    
def test_delete_not_found():
    b = BST()
    try:
        b.delete(12)
        raise Exception("test_delete_not_found not passed")
    except LookupError as e:
        pass
    print("test_delete_not_found finished.")

def test_delete_one_size():
    b = BST()
    b.insert(12)    
    b.delete(12)
    assert not b.contains(12)
    test_empty(b)
    assert bst_invariant(b)
    print("test_delete_one_size finished.")

def test_multiple_remove1():
    b = BST()
    for i in range(15):
        b.insert(i)
    for i in range(0, 15, 2):
        b.delete(i)
        assert not b.contains(i)
    for i in range(1, 15, 2):
        assert b.contains(i)
    assert b.size() == b.n == b.root.count() == 7
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_multiple_remove1 finished.")

def test_multiple_remove2():
    b = BST()
    for i in range(0, 15, 2):
        b.insert(i)
    for i in range(-1, 15, 2):
        try:
            b.delete(i)
        except LookupError:
            pass
        assert not b.contains(i)
    for i in range(0, 15, 2):
        assert b.contains(i)
    assert b.size() == b.n == b.root.count() == 8
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_multiple_remove2 finished.")

def test_multiple_remove3():
    b = BST()
    test_empty()
    b.insert(5)
    b.insert(3)
    b.insert(4)
    b.insert(10)
    b.insert(7)
    b.insert(6)
    b.insert(8)
    b.insert(9)
    b.insert(12)
    b.insert(11)
    assert b.size() == b.n == b.root.count() == 10
    assert bst_invariant(b)
    assert_consistencies(b)
    b.delete(3)
    b.delete(10)
    b.delete(12)
    assert b.size() == b.n == b.root.count() == 7
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_multiple_remove3 finished.")

def test_search():
    b = BST()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    try:
        b.search(None)
        raise Exception("test_search failed")
    except ValueError:
        pass
    assert not b.search(12)
    assert b.search(5)
    assert b.search(10)
    assert b.search(15)
    assert b.size() == b.n == b.root.count() == 3
    assert bst_invariant(b)
    assert_consistencies(b)
    b.delete(10)
    assert not b.search(10)
    assert b.size() == b.n == b.root.count() == 2
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_search finished.")
    
def test_remove_min_and_max():
    b = BST()
    assert not b.remove_min()
    assert not b.remove_max()    
    b.insert(14)
    b.insert(12)
    b.insert(28)
    
    m = b.remove_min()
    assert m and m.key == 12
    assert b.size() == b.n == b.root.count() == 2
    assert bst_invariant(b)
    assert_consistencies(b)

    M = b.remove_max()
    assert M and M.key == 28
    assert b.size() == b.n == b.root.count() == 1
    assert bst_invariant(b)
    assert_consistencies(b)
    print("test_remove_min_and_max finished.")

def test_predecessor_and_successor():
    b = BST()
    b.insert(12)
    b.insert(14)
    b.insert(28)
    assert not b.successor(28)
    assert b.successor(12) == b.search(14)
    assert not b.predecessor(12)
    assert b.predecessor(14) == b.search(12)
    try:
        b.successor(7)
        b.predecessor(6)
        raise Exception("test_predecessor_and_successor failed")
    except LookupError as e:
        pass
    print("test_predecessor_and_successor finished.")

def test_rank():
    b = BST()
    try:
        b.rank(None)
        raise Exception("test_rank failed.")
    except ValueError:
        pass
    try:
         b.rank(12)
         raise Exception("test_rank failed.")
    except LookupError:
        pass
    b.insert(12)
    assert b.rank(12) == 0
    b.insert(14)
    b.insert(28)
    b.insert(10)
    b.insert(7)
    assert b.rank(12) == 2
    assert b.rank(7) == 0
    assert b.rank(28) == 4
    print("test_rank finished.")

def test_switch():
    b = BST()
    b.tail_insert(12)
    b.tail_insert(20)
    b.tail_insert(28)
    b.tail_insert(8)
    b.tail_insert(16)
    b.tail_insert(10)
    b.tail_insert(4)
    b.tail_insert(2)
    b.tail_insert(5)
    b.tail_insert(9)
    b.tail_insert(11)
    b.tail_insert(14)
    b.tail_insert(18)
    b.tail_insert(22)
    b.tail_insert(30)

    def asserts():
        print("\nroot =", b.root, end="\n\n")
        print(b)
        bst_invariant(b)
        assert_consistencies(b)

    try:
        b._switch(b.search(12), b.search(12))
    except ValueError as e:
        print(e)
    try:
        b._switch(b.search(12), None)
    except ValueError as e:
        print(e)

    try:
        b._switch(b.search(12), BSTNode(100), search_first=True)
    except LookupError as e:
        print(e)

    asserts()

    b._switch(b.search(8), b.search(12))
    assert b.root == b.search(8)
    assert not b.root.parent    
    b._switch(b.search(8), b.search(8).left)
    asserts()

    b._switch(b.search(20), b.search(12))
    assert b.root == b.search(20)
    assert not b.root.parent    
    b._switch(b.search(20), b.search(20).right)
    asserts()
    
    b._switch(b.search(4), b.search(10))
    assert b.root == b.search(12)
    #print(b)
    b._switch(b.search(8).left, b.search(8).right)
    asserts()

    b._switch(b.search(8), b.search(20))
    assert b.root == b.search(12)
    #print(b)
    b._switch(b.search(12).left, b.search(12).right)
    asserts()
    
    b._switch(b.search(8), b.search(28))
    assert b.root == b.search(12)
    #print(b)
    b._switch(b.search(12).left, b.search(20).right)
    asserts()

    b._switch(b.search(8), b.search(14))
    assert b.root == b.search(12)
    #print(b)
    b._switch(b.search(12).left, b.search(12).right.left.left)
    asserts()
    
    b._switch(b.search(2), b.search(28))
    assert b.root == b.search(12)
    #print(b)
    b._switch(b.search(12).left.left.left, b.search(12).right.right)
    asserts()
    assert b.search(2).left is None
    assert b.search(2).right is None
    assert b.search(28).left == b.search(22)
    assert b.search(28).right == b.search(30)

    b._switch(b.search(8), b.search(5))
    assert b.root == b.search(12)
    #print(b)
    b._switch(b.search(12).left, b.search(12).left.left.right)
    asserts()

    b._switch(b.search(8), b.search(2))
    assert b.root == b.search(12)
    #print(b)
    b._switch(b.search(12).left, b.search(12).left.left.left)
    assert not b.search(12).left.left.left.left
    assert not b.search(12).left.left.left.right
    assert b.search(12).left.left.left.parent == b.search(12).left.left
    #asserts()

    b._switch(b.search(12), b.search(10))
    assert b.root == b.search(10)
    assert not b.root.parent
    #print(b)
    b._switch(b.search(10), b.search(10).left.right)
    asserts()
    print("test_switch finished.")


def run_tests():
    test_empty_size()
    test_empty_contains()
    test_one_size()
    test_one_contains()
    test_many_size()
    test_many_contains()
    test_structure_many()
    test_delete_not_found()
    test_delete_one_size()
    test_multiple_remove1()
    test_multiple_remove2()
    test_search()
    test_remove_min_and_max()
    test_predecessor_and_successor()
    test_rank()
    test_switch()


if __name__ == "__main__":
    run_tests()
