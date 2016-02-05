#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 06/09/15

My solution to exercise 146 from the series of exercise by prof. A. Carzaniga

Write an algorithm called Four-Cycle(G)
that takes a directed graph represented with its adjacency matrix G,
and that returns true if and only if G contains a 4-cycle.

A 4-cycle is a sequence of four distinct vertexes a, b, c, d
such that there is an arc from a to b, from b to c, from c to d,
and from d to a.

Also, analyze the complexity of Four-Cycle(G).
"""

from ands.ds.Graph import *


def is_an_edge(u, v):
    return v in u.get_adjacent_nodes()


def four_cycle(g):
    """Detects a four cycle in a graph represented as an adjacency list.

    Running time complexity(O^5),
    but using a adjacency matrix representation,
    it would only be O(n^4),
    because checking if there's an edge is a constant operation.

    :type g : Graph
    """
    for a in g.nodes:
        for b in a.get_adjacent_nodes():
            for c in b.get_adjacent_nodes():
                for d in c.get_adjacent_nodes():
                    if is_an_edge(d, a):
                        return True

    return False


if __name__ == "__main__":
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")

    g.add_directed_edge(a, b)
    g.add_directed_edge(b, c)
    g.add_directed_edge(c, a)  # change a to d, i.e. (c, d) to form a 4-cycle
    g.add_directed_edge(d, a)

    print(four_cycle(g))
