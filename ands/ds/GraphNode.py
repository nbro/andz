#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/16


GraphNode for the `Graph` data structure defined in `Graph.py`.
Nodes contain many fields that are used in the 2 main graph algorithms:
- `bfs`
- `dfs`
These fields are for example `self.predecessor`, `self.distance`, etc.

Nodes keep also track of the edges of which they are the starting point.
These edges are represented as a list of 3 items:

    edge = [self, pointed_node, edge_weight]

where:
- `self` is the reference to the node itself,
- `pointed_node` is the ending node of the edge
- `edge_weigh` is the eventual weight of the edge.
"""

import sys
from tabulate import tabulate
from ands.ds.BaseNode import BaseNode


__all__ = ["GraphNode", "WHITE", "BLACK", "GREY", "INFINITY", "NIL"]


WHITE = "WHITE"
BLACK = "BLACK"
GREY = "GREY"
INFINITY = sys.maxsize
NIL = None


class GraphNode(BaseNode):

    def __init__(self, key, value=None):
        BaseNode.__init__(self, key, value)

        # Attributes used mostly in algorithms for graphs, such as in bfs or dfs.
        self.predecessor = NIL
        self.distance = INFINITY
        self.color = WHITE  # To keep track if a node has been or not visited yet.

        self.adjacent_nodes = []
        self.outgoing_edges = {}  # [(self, other), w]

        self.cc = NIL
        """This variable can be used to keep track of which
        connected component this node in the graph belongs to.

        For example, we could name the possible different
        connected components using simply numbers:
        the first connected component is 1, the second is 2,
        the third is 3, and so on.

        When searching for connected components,
        we can use this variable to associate this node
        with a connected component:
        if we set it to 1, that would mean that this node
        belongs to the connected component 1."""

        # These variables are useful for dfs
        # to keep track when a node is first visited
        # and when we finish visiting it,
        # and we start backtracking.
        self.start = INFINITY
        self.end = INFINITY

        self.in_degree = 0
        self.out_degree = 0

    def get_adjacent_nodes(self) -> list:
        """Returns the adjacent nodes to self."""
        return self.adjacent_nodes

    def get_outgoing_edges(self) -> dict:
        """Returns a dictionary containing the edges outgoing from this node.
        Edges are of the form (self, other): weight."""
        return self.outgoing_edges

    def add_adjacent_node(self, u, weight=0):
        """Adds u as adjacent node to self.

        Creates a directed edge from self to u."""
        self.adjacent_nodes.append(u)
        self.outgoing_edges[(self, u)] = weight
        self.out_degree += 1
        u.in_degree += 1

    def remove_adjacent_node(self, u):
        """Removes u's reference from the adjacent_nodes list of self.

        It also removes the directed edge from self to u."""
        self.adjacent_nodes.remove(u)
        w = self.outgoing_edges.pop((self, u))
        self.out_degree -= 1
        u.in_degree -= 1
        return w

    def reset(self, clear_nodes=False):
        """Make self assume the default attribute values.

        If clear_nodes=True, then all connections with other nodes are removed.
        """
        self.color = WHITE
        self.predecessor = NIL
        self.distance = INFINITY
        self.cc = NIL
        self.start = INFINITY
        self.end = INFINITY
        if clear_nodes:
            self.clear_adjacent_nodes()

    def clear_adjacent_nodes(self):
        self._fix_degrees_before_clearing()
        self.adjacent_nodes.clear()
        self.outgoing_edges.clear()

    def _fix_degrees_before_clearing(self):
        for n in self.adjacent_nodes:
            n.in_degree -= 1
        self.out_degree = 0

    def get_str_repr_of_adj_nodes(self):
        """Returns a string representing all the adjacent total_nodes."""
        str_repr = "["
        for node in self.get_adjacent_nodes():
            str_repr += str(node.key) + ", "
        return "[]" if not str_repr[:-2] else str_repr[:-2] + "]"

    def _get_list_of_attributes(self):
        a = [["Name", self.key],
             ["Adjacent nodes", self.get_str_repr_of_adj_nodes()],
             ["Color", self.color],
             ["Distance", self.distance],
             ["Connected component", self.cc],
             ["Starting visit time", self.start],
             ["Ending visit time", self.end]]

        if self.predecessor is not None:
            a.append(["Predecessor", self.predecessor.key])
        else:
            a.append(["Predecessor", NIL])

        return a

    def show(self):
        """Prints the current status of this node."""
        print(tabulate(self._get_list_of_attributes(), tablefmt="fancy_grid", headers=("ATTRIBUTES", "VALUES")))

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.__str__() + " => " + self.get_str_repr_of_adj_nodes()

    def __eq__(self, other):
        return self.value == other.value and self.key == other.key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.key) + id(self)
