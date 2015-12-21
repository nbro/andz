#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Graph data structure using adjacency list representation,
but actually using a dictionary.

You can represent a undirected graph (for now ) by adding
each endpoint (node) of an edge to the adjacency list of the other endpoint.
For example, suppose we have node A and B.
To create an undirected graph composed of A and B, you need to do:
    1. A.add_adjacent_node(B)
    2. B.add_adjacent_node(A)

You can also call add_undirected_edge directly.

To create directed graphs, you can simply add the pointed node
to the adjacency list of the starting node.
You could also call add_directed_edge (see its docstrings).

This graph also contains some "utility" functions (reset_nodes)
that can be used in those same algorithms.
"""

import operator
from ands.ds.GraphNode import *


class Graph:
    """Graph data structure using adjacency list representation."""

    def __init__(self, name="Adjacency List Representation"):
        self.nodes = []
        self.name = name

        # Used in the dfs algorithm
        # to keep track of the global time
        # while visiting and exploring nodes.
        self.dfs_global_time = INFINITY

        # Used with the dfs algorithm
        # to create a topological sort
        # of a directed acyclic graph (DAG).
        self.topological_sort = []

        # List of lists, each of them contains
        # the nodes in different connected components.
        self.connected_components = []

    def add_node(self, u: GraphNode):
        """Adds a new node to this graph."""
        self.nodes.append(u)

    def add_nodes(self, ls: list):
        """Adds all GraphNode objects in ls to this Graph object."""
        for u in ls:
            self.nodes.append(u)

    def reset_nodes(self):
        """Make all nodes to assume the default attribute values."""
        for u in self.nodes:
            u.reset()

    def add_undirected_edge(self, u: GraphNode, v: GraphNode, weight=0):
        """Adds v to the adjacency list of u,
        and adds also u to the adjacency list of v,
        creating an "virtual" undirected edge.

        If u is still not a node of this graph,
        it is added first before establish any connection with v.
        The same can be said for v."""
        if u not in self.nodes:
            self.add_node(u)

        if v not in self.nodes:
            self.add_node(v)

        u.add_adjacent_node(v, weight)
        v.add_adjacent_node(u, weight)

    def add_directed_edge(self, u: GraphNode, v: GraphNode, weight=0):
        """Adds v to the adjacency list of u.

        If u is still not a node of this graph,
        it is added first before establish any connection with v.
        The same can be said for v."""
        if u not in self.nodes:
            self.add_node(u)

        if v not in self.nodes:
            self.add_node(v)

        u.add_adjacent_node(v, weight)

    @property
    def edges(self) -> dict:
        """Returns all the edges of this graph as dict,
        where keys are tuples,
        whose first elements are the starting points of the edges,
        and whose second elements are the ending points of the edges.
        Values of these dict represent the weight of the edges.

        Note that if the graph is undirected,
        and suppose there's an edge between node A and B,
        then this function will return both triples:
        (A, B, weight_AB) and (B, A, weight_BA).
        """
        edges = {}
        for node in self.nodes:
            edges.update(node.get_outgoing_edges())
        return edges

    def get_sorted_edges(self, reversed_order=False, undirected=False) -> "list of tuple":
        """Sorts edges, by default, in increasing order."""
        edges = self.edges
        edges_list = sorted(edges.items(), key=operator.itemgetter(1), reverse=reversed_order)
        if undirected:
            return self._remove_double_edges(edges_list)
        else:
            return edges_list

    @staticmethod
    def _remove_double_edges(sorted_edges: list) -> list:
        """If the graph is undirected,
        we don't need to have a double representation of each edge.
        This function serves to this purpose:
        it removes double representations of the same edge,
        in an undirected graph.

        Note that sorted_edges should be the edges returned by get_sorted_edges."""
        i = 0
        while i < len(sorted_edges) - 1:
            if sorted_edges[i][0][0] == sorted_edges[i + 1][0][1] and \
               sorted_edges[i][0][1] == sorted_edges[i + 1][0][0]:
                sorted_edges.remove(sorted_edges[i])
            else:
                i += 1
        return sorted_edges

    def num_of_nodes(self):
        return len(self.nodes)

    def num_of_edges(self):
        return len(self.edges)

    def has_even_degree(self):
        """Returns True, if all vertices have an even degree, False otherwise."""
        for n in self.nodes:
            if n.in_degree != n.out_degree:
                return False
        return True

    @staticmethod
    def weight(node1: GraphNode, node2: GraphNode):
        """
        Returns the weight of the edge connecting node1 to node2.

        It returns None if there's no connection between node1 and node2.

        Note that this method is static,
        because it does not need any field of self
        to check if node1 and node2 are connected somehow.

        So, this method could also be called on total_nodes
        belonging to other graphs, or even belonging to no graph."""
        return node1.get_outgoing_edges().get((node1, node2))

    # PRINT FUNCTIONS

    def show_edges(self, sorted_edges=False):
        ls = []
        if sorted_edges:
            for edge in self.get_sorted_edges():
                ls.append([edge[0][0].key, edge[0][1].key, edge[1]])
        else:
            for edge in self.edges:
                ls.append([edge[0].key, edge[1].key, self.edges[edge]])
        print(tabulate(ls, tablefmt="fancy_grid", headers=("FROM", "TO", "WEIGHT")))

    def show_connected_components(self):
        """This function is useful after finding
        the connected components of this graph.

        You can find the connected components both with bfs or dfs."""
        ls = []
        for i, connected_component in enumerate(self.connected_components):
            a = []
            for j in connected_component:
                a.append(j.key)
            ls.append([i + 1, a])
        print(tabulate(ls, tablefmt="fancy_grid", headers=("CC", "ELEMENTS")))

    def show_nodes(self):
        """Shows nodes' fields."""
        for node in self.nodes:
            node.show()

    def __str__(self):
        return str(self.nodes)

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    g = Graph()

    a = GraphNode("A")
    b = GraphNode("B")
    c = GraphNode("C")

    a.add_adjacent_node(b, 2)
    a.add_adjacent_node(c, 3)

    b.add_adjacent_node(b, 4)
    b.add_adjacent_node(c, 10)

    c.add_adjacent_node(b, 1)

    # Testing add_node
    g.add_node(a)

    # Testing add_nodes
    g.add_nodes((b, c))

    # Testing show_edges (not sorted)
    g.show_edges()

    print("Edge's weight between a and b:", Graph.weight(a, b))
    a.remove_adjacent_node(b)

    # Testing show_nodes edges (sorted)
    g.show_edges(sorted_edges=True)

    # Testing the Graph.weight static function
    print("Edge's weight between a and b:", Graph.weight(a, b))

    # Testing the show_nodes function
    print(g)

    # Function show_connected_components should be tested with bfs or dfs.

    g.show_nodes()
    print("Out-degree of a:", a.out_degree)
    print("In-degree of a:", a.in_degree)

    print("Out-degree of b:", b.out_degree)
    print("In-degree of b:", b.in_degree)

    print("Out-degree of c:", c.out_degree)
    print("In-degree of c:", c.in_degree)

    c.remove_adjacent_node(b)
    a.remove_adjacent_node(c)

    print("Out-degree of c:", c.out_degree)
    print("In-degree of c:", c.in_degree)

    g.show_connected_components()
