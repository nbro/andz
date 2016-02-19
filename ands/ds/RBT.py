#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 19/02/16

Contains the class RBT for representing red-black trees.

## Red-black tree property

1. Every node is either red or black.

2. The root is black.

3. Every NIL or leaf node is black.

4. If a node is red, then both its children are black,
in other words, there cannot be two red nodes in a row.

5. For every node x, each path from x to its descendent leaves
has the same number of black nodes, i.e. bh(x).

## Lemma

The height `h(x)` of a red-black tree with `n = size(x)` internal nodes
is at most 2 * log<sub>2</sub>(n + 1), that is, h(x) <= 2 * log<sub>2</sub>(n + 1),
which is equivalent to h(x)/2 <= log<sub>2</sub>(n + 1), which is equivalent to
n >= 2<sup>h(x)/2</sup> - 1. If you don't understand exactly why this last statements
are equivalent, then do the reversed reasoning:

* n >= 2<sup>h(x)/2</sup> - 1

* n + 1 >= 2<sup>h(x)/2</sup>

Now we log both parts

* log<sub>2</sub>(n + 1) >= log<sub>2</sub>(2<sup>h(x)/2</sup>)

* log<sub>2</sub>(n + 1) >= h(x)/2 * log<sub>2</sub>(2)

* log<sub>2</sub>(n + 1) >= h(x)/2 * 1

* 2 * log<sub>2</sub>(n + 1) >= h(x)


### Proof

1. Prove that for all `x`, size(x) >= 2<sup>bh(x)</sup> - 1 by induction.

    1.1. **Base case**: `x` is a leaf, so `size(x) = 0` and `bh(x) = 0`.

    1.2. **Induction step**: consider y<sub>1</sub>, y<sub>2</sub>,
    and `x` such that y<sub>1</sub>.parent = y<sub>2</sub>.parent = x,
    and assume (induction) that size(y<sub>1</sub>) >= 2<sup>bh(y<sub>1</sub>)</sup> - 1
    and size(y<sub>2</sub>) >= 2<sup>bh(y<sub>2</sub>)</sup> - 1.
    Prove that size(x) >= 2<sup>bh(x)</sup> - 1.

    **Proof**:

    size(x) = size(y<sub>1</sub>) + size(y<sub>2</sub>) + 1 >= (2<sup>bh(y<sub>1</sub>)</sup> - 1)
    + (2<sup>bh(y<sub>2</sub>)</sup> - 1) + 1

    Since bh(x) = {

        bh(y), if color(y) = red
        
        bh(y) + 1, if color(y) = black
    }
    
    size(x) >= (2<sup>bh(x) - 1</sup> - 1) + (2<sup>bh(x) - 1</sup> - 1) + 1
    = (2<sup>bh(x)</sup> - 1).

    Since every red node has black children,
    in every path from `x` to a leaf node,
    at least half the nodes are black, thus bh(x) >= h(x)/2.
    So, n = size(x) >= 2<sup>h(x)/2</sup> - 1. Therefore
    h(x) <= 2 * log<sub>2</sub>(n + 1).

    A red-black tree works as a binary-search tree for search,
    insert, etc, so the complexity of those operations is T(n) = O(h),
    that is T(n) = O(log<sub>2</sub> n), which is also the worst case complexity.

## TODO
- Override needed methods inherited from BST.

## References

- [https://en.wikipedia.org/wiki/Red%E2%80%93black_tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)

- Slides by prof. A. Carzaniga

- Chapter 13 of [Introduction to Algorithms (3rd ed.)](https://mitpress.mit.edu/books/introduction-algorithms) by CLRS
"""

import math
from ands.ds.BST import BST, is_bst
from ands.ds.RBTNode import RBTNode, RED, BLACK


__all__ = ["RBT", "is_rbt", "bh", "upper_bound_height"]


class RBT(BST):

    def __init__(self, root=None, name="RBT"):
        BST.__init__(self, root, name)

    def insert(self, x, value=None):
        """Inserts `x` into this `RBT`.

        This operation is similar to the `insert` operation of a classical `BST`,
        but, in this case, the red-black tree property must be maintained,
        so addional work is needed.    

        There are several cases of inserting into a RBT to handle:

        1. `x`  is the root node (first node).

        2. `x.parent` is `BLACK`.

        3. `x.parent` and the uncle of `x` are `RED`.

            The uncle of `x` will be the left child of `x.parent.parent`,
        if `x.parent` is the right child of `x.parent.parent`,
        otherwise (`x.parent` is the left child of `x.parent.parent`)
        the uncle will be the right child of `x.parent.parent`.

        4. x.parent is RED, but x.uncle is BLACK (or None). x.grandparent exists because x.parent is RED.

            4.1. `x` is added to the right of a left child of `x.parent.parent` (grandparent)

            4.2. or `x` is added to the left of a right child of `x.parent.parent`.

            4.3. `x` is added to the left of a left child of `x.parent.parent`.

            4.4. or `x` is added to the right of a right child of `x.parent.parent`.

        `_fix_insertion` handles these cases in the same order as just presented above.

        **Time Complexity:** O(log<sub>2</sub>(n))."""
        if x is None:
            raise ValueError("x cannot be None.")

        if not isinstance(x, RBTNode):
            x = RBTNode(x, value)

        if x.left or x.right or x.parent:
            raise ValueError("x cannot have left or right children, or parent.")

        c = self.root  # Current node
        p = None  # Current node's parent

        while c is not None:
            p = c
            if x.key < c.key:
                c = c.left
            else:  # x.key >= c.key
                c = c.right

        x.parent = p

        # The while loop was not executed even once.
        # Case 1: node is inserted as root.
        if p is None:
            self.root = x
        elif p.key > x.key:
            p.left = x
        else:  # p.key < x.key:
            p.right = x

        x.color = RED
        self.n += 1
        self._fix_insertion(x)

    def _fix_insertion(self, u: RBTNode):
        # u is the root and we color it BLACK.
        if u.parent is None:
            u.color = BLACK

        elif u.parent.color == BLACK:
            return
        
        elif u.parent.color == RED and (u.uncle is not None and u.uncle.color == RED):
            u.parent.color = BLACK
            u.uncle.color = BLACK
            u.grandparent.color = RED
            self._fix_insertion(u.grandparent)

        elif u.parent.color == RED and (u.uncle is None or u.uncle.color == BLACK):
            
            # u is added as a right child to a node that is the left child.
            if u.parent.is_left_child() and u.is_right_child():
                
                # left_rotation does not violate the property:
                # all paths from any given node to its leaf nodes
                # contain the same number of black nodes.
                self.left_rotate(u.parent)

                # With the previous left_rotate call,
                # u.parent has become the left child of u,
                # or, u bas become the parent of what before was u.parent
                # We can pass to case 5, where we have 2 red nodes in a row,
                # specifically, u.parent and u,
                # which are both left children of their parents.

                self._fix_insertion(u.left)

            # u is added as a left child to a node that is the right child.
            elif u.parent.is_right_child() and u.is_left_child():
                self.right_rotate(u.parent)
                self._fix_insertion(u.right)

            # u is added as a left child to a node that is the left child.
            elif u.parent.is_left_child() and u.is_left_child():
                # Note that grandparent is known to be black,
                # since its former child could not have been RED
                # without violating property 4.
                self.right_rotate(u.grandparent)
                u.parent.color = BLACK
                u.parent.right.color = RED

            # u is added as a right child to a node that is the right child.
            elif u.parent.is_right_child() and u.is_right_child():
                self.left_rotate(u.grandparent)
                u.parent.color = BLACK
                u.parent.left.color = RED
                
            else:
                assert False

    def delete(self, x):
        """Delete `x` from this `RBT` object.

        `x` can either be a `RBTNode` object or a key.
        
        If a key, then a search is performed first
        to find the corresponding `RBTNode` object.
        An exception is raised if a `RBTNode` object
        with a key=x is not found.
        
        If `x` is a `RBTNode` object, the only check
        that is performed is that if it hasn't a parent,
        then it must be the root. Similarly,
        a node that isn't the root must have a parent.
        If `x` has a parent, therefore it cannot be the root,
        but there's no way of knowing if this node
        really belongs to this `RBT` object,
        because no search is performed (for now).
        
        If it doesn't belong to this `RBT` object,
        then the behaviour of this method is undefined (for now).

        **Time Complexity:** O(log<sub>2</sub>(n))."""
        def delete_case1(v):
            if v.parent is not None:
                delete_case2(v)

        def delete_case2(v):
            if v.sibling.color == RED:

                assert v.parent.color == BLACK

                v.sibling.color = BLACK
                v.parent.color = RED

                if v.is_left_child():
                    self.left_rotate(v.parent)
                else:
                    self.right_rotate(v.parent)
                    
                assert v.sibling.color == BLACK

            delete_case3(v)

        def delete_case3(v):
            # not sure if the children of v.sibling can be None
            if (v.parent.color == BLACK and v.sibling.color == BLACK and
                ((v.sibling.left and v.sibling.left.color == BLACK) or not v.sibling.left) and
                ((v.sibling.right and v.sibling.right.color == BLACK) or not v.sibling.right)):

                v.sibling.color = RED
                delete_case1(v.parent)
            else:
                delete_case4(v)

        def delete_case4(v):
            # not sure if the children of v.sibling can be None
            if (v.parent.color == RED and v.sibling.color == BLACK and
                ((v.sibling.left and v.sibling.left.color == BLACK) or not v.sibling.left) and
                ((v.sibling.right and v.sibling.right.color == BLACK) or not v.sibling.right)):

                v.sibling.color = RED
                v.parent.color = BLACK
            else:
                delete_case5(v)

        def delete_case5(v):
            assert v.sibling is not None

            if v.sibling.color == BLACK:
                if (v.is_left_child() and
                    (not v.sibling.right or v.sibling.right.color == BLACK) and
                    v.sibling.left.color == RED):

                    v.sibling.color = RED
                    v.sibling.left.color = BLACK
                    self.right_rotate(v.sibling)
                    
                elif (v.is_right_child() and
                      (not v.sibling.left or v.sibling.left.color == BLACK) and
                      v.sibling.right.color == RED):

                    v.sibling.color = RED
                    v.sibling.right.color = BLACK
                    self.left_rotate(v.sibling)

            delete_case6(v)

        def delete_case6(v):
            assert v.sibling is not None

            v.sibling.color, v.parent.color = v.parent.color, v.sibling.color
            
            if v.is_left_child():
                assert v.sibling.right
                v.sibling.right.color = BLACK
                self.left_rotate(v.parent)
            else:
                assert v.sibling.left
                v.sibling.left.color = BLACK
                self.right_rotate(v.parent)
                
        if x is None:
            raise ValueError("x cannot be None.")

        if not isinstance(x, RBTNode):
            x = self.search(x)
            if x is None:
                raise LookupError("No node was found with key=x.")

        if x.parent is None and not self.is_root(x):
            raise ValueError("x is not a valid node.")

        # If x has two non-leaf children, then replace x with its successor.
        if x.left is not None and x.right is not None:
            s = self.successor(x)
            self._switch(x, s)
            x.color, s.color = s.color, x.color

        # At least one of the children must be None.
        assert x.left is None or x.right is None

        # Case 1
        # If `x` is a red node, we simply replace it with its child `c`,
        # which must be black by property 4, if any.
        # This can only occur when `x` has two leaf children,
        # because if the red node `x` had a black non-leaf child on one side,
        # but just a leaf child on the other side,
        # then the count of black nodes on both sides would be different,
        # thus the tree would violate property 5.
        # All paths through the deleted node
        # will simply pass through one fewer red node,
        # and both the deleted node's parent and child must be black,
        # so property 3 (all leaves are black) and property 4
        # (both children of every red node are black) still hold.
        if x.color == RED:
            assert x.left is None and x.right is None
            assert not self.is_root(x)

            if x.is_left_child():
                x.parent.left = None
            else:
                x.parent.right = None

        else:  # x.color == BLACK

            # One of the children of x is RED.
            # Simply removing a black node (x) could break properties 4,
            # i.e., both children of every red node are black,
            # because x.parent could be RED (e.g.), and 5,
            # i.e. all paths from any given node to its leaf nodes
            # contain the same number of black nodes),
            # but if we repaint `c` BLACK,
            # both of these properties are preserved.
            if x.left is not None and x.left.color == RED:
                if not self.is_root(x):
                    if x.is_left_child():
                        x.parent.left = x.left
                    else:
                        x.parent.right = x.left

                x.left.parent = x.parent
                x.left.color = BLACK

                if self.is_root(x):
                    self.root = x.left

            elif x.right is not None and x.right.color == RED:
                if not self.is_root(x):
                    if x.is_left_child():
                        x.parent.left = x.right
                    else:
                        x.parent.right = x.right

                x.right.parent = x.parent
                x.right.color = BLACK

                if self.is_root(x):
                    self.root = x.right

            # The complex case is when both `x` and `c` are BLACK.
            # This can only occur when deleting a black node
            # which has two leaf children, because if the black node `x`
            # had a black non-leaf child on one side
            # but just a leaf child on the other side,
            # then the count of black nodes on both sides would be different,
            # thus the tree would have been an invalid red–black tree
            # by violation of property 5.
            elif x.left is None and x.right is None:
                # 6 cases
                if not self.is_root(x):
                    assert x.sibling is not None
                    
                    # Note that x.sibling cannot be None,
                    # because otherwise the substree containing it
                    # would have fewer black nodes
                    # than the subtree containing x.
                    # Specifically, the subree containing x
                    # would have a black height of 2,
                    # whereas the one containing the sibling
                    # would have a black height of 1.

                    delete_case1(x)

                    # We begin by replacing x with its child c.
                    # Note that both children of x are null-leaf children,
                    # as we observed
                    if x.is_left_child():
                        x.parent.left = None
                    else:
                        x.parent.right = None
                else:
                    self.root = None                
            else:
                assert False

        # Ensures that x has no reference to any node of this RBT.
        self.n -= 1
        x.parent = x.left = x.right = None
        return x

    def remove_max(self):
        """Removes and returns the element with the greatest value from `self`.

        **Time Complexity:** O(log<sub>2</sub>(n))."""
        if self.root:
            m = self.maximum()
            assert m
            return self.delete(m)

    def remove_min(self):
        """Removes and returns the element with the smallest value from `self`.

        **Time Complexity:** O(log<sub>2</sub>(n))."""        
        if self.root:
            m = self.minimum()
            assert m
            return self.delete(m)


def bh(n):
    """Returns the black-height of the node `n`."""
    if n is None:
        return 1
    
    left_bh = bh(n.left)
    right_bh = bh(n.right)
    
    if left_bh != right_bh:
        return -1
    else:
        return left_bh + (1 if n.color == BLACK else 0)

def upper_bound_height(t):
    return t.height() <= 2 * math.log2(t.n + 1)

def is_rbt(rbt):
    """Returns `True` if `rbt` is a valid `RBT` object. `False` otherwise."""
    
    def prop_1(t):
        """Returns `True` if all colors are either `RED` or `BLACK`."""
        def h(n):            
            if n:
                if n.color != BLACK and n.color != RED:
                    return False               
                return h(n.right) and h(n.left)
            return True
        return h(t.root)

    def prop_2(t):
        """Returns `True` if the root is `BLACK` (or it is `None`),
        `False` otherwise."""
        if t.root:
            return t.root.color == BLACK
        return True

    def prop_3(t):
        # leaves are represented with Nones,
        # so there's not need to check this property.
        return True

    def prop_4(t):
        def h(n):
            if n:
                if n.parent and n.color == RED and n.parent.color == RED:
                    return False
                if not n.parent and n.color == RED:
                    return False
                return h(n.left) and h(n.right)
            return True 
        return h(t.root)

    def prop_5(t):        
        return bh(t.root) != -1

    def all_rbt_nodes(t):
        def h(n):            
            if n is not None:
                if not isinstance(n, RBTNode):
                    return False
                return h(n.left) and h(n.right)
            return True
        return h(t.root)

    if not is_bst(rbt):
        return False

    if not isinstance(rbt, RBT):
        return False

    if not all_rbt_nodes(rbt):
        return False    

    return prop_1(rbt) and prop_2(rbt) and prop_4(rbt) and prop_5(rbt)
