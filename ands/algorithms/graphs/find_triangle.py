#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 05/09/15

Exercise 112.
"""

from ands.ds.Graph import *


edges = {}


def is_an_edge(u, v):
    """Returns true if v is an adjacent node to u.

    Running time complexity: O(number of adjacent nodes to u).

    :type u : GraphNode
    :type v : GraphNode
    """
    if (u, v) not in edges:
        edges[(u, v)] = w in u.get_adjacent_nodes()
    return edges[(u, v)]


def find_triangle(g):
    """Returns true if there's a triangle in g.

    A triangle in a graph is a triple of vertices u, v and w,
    such that all three edges  (u, v), (v, w) and (u, w) are in the graph.

    Note that a triangle is not composed of the edges (u, v), (v, w) and (w, u)!

    :type g : Graph
    """
    for u in g.nodes:
        for v in u.get_adjacent_nodes():
            for w in g.nodes:
                if is_an_edge(v, w) and is_an_edge(u, w):
                    return True
    return False


def improved_find_triangle(g):
    for e in g.edges:  # e = (u, v)
        for w in g.nodes:
            if is_an_edge(e[1], w) and is_an_edge(e[0], w):
                return True
    return False


if __name__ == "__main__":
    g = Graph()

    u = GraphNode("u")
    w = GraphNode("w")
    v = GraphNode("v")
    z = GraphNode("z")

    u.add_adjacent_node(v)
    u.add_adjacent_node(w)  # comment this line to remove the triangle

    v.add_adjacent_node(w)
    v.add_adjacent_node(z)

    # w.add_adjacent_node(u)
    w.add_adjacent_node(z)

    g.add_nodes((u, v, w, z))

    print(g)

    print(find_triangle(g))
    print(improved_find_triangle(g))
