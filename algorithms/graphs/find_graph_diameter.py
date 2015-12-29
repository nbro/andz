#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 26/08/15

The diameter is defined as the biggest eccentricity
among all the eccentricities of all nodes.

Fact: radius(G) <= diameter(G) <= 2 * radius(G)
"""

from find_eccentricity import *


def find_graph_diameter(graph):
    """Finds the diameter of a graph.

    The diameter is defined as the biggest eccentricity
    among all the eccentricities of all nodes.

    If a node has the eccentricity equal to
    the diameter of the graph to which it belongs,
    then that node is called "peripheral".

    :type graph : Graph
    """
    eccentricities = []

    for u in graph.nodes:
        eccentricity = find_eccentricity(graph, u)
        eccentricities.append(eccentricity)

    return max(eccentricities)


def test_find_graph_diameter():
    g = Graph()

    v1 = GraphNode("v1")
    v2 = GraphNode("v2")
    v3 = GraphNode("v3")
    v4 = GraphNode("v4")
    v5 = GraphNode("v5")

    g.add_node(v1)
    g.add_node(v2)
    g.add_node(v3)
    g.add_node(v4)
    g.add_node(v5)

    v1.add_adjacent_node(v2)
    v2.add_adjacent_node(v1)

    v2.add_adjacent_node(v4)
    v4.add_adjacent_node(v2)

    v2.add_adjacent_node(v3)
    v3.add_adjacent_node(v2)

    v3.add_adjacent_node(v4)
    v4.add_adjacent_node(v3)

    v3.add_adjacent_node(v5)
    v5.add_adjacent_node(v3)

    v4.add_adjacent_node(v5)
    v5.add_adjacent_node(v4)

    print("Diameter of the graph is:", find_graph_diameter(g))


def test_find_graph_diameter2():
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")

    a.add_adjacent_node(b)
    a.add_adjacent_node(c)
    a.add_adjacent_node(d)

    b.add_adjacent_node(a)
    c.add_adjacent_node(a)
    d.add_adjacent_node(a)

    g.add_node(a)
    g.add_node(b)
    g.add_node(c)
    g.add_node(d)

    print("Diameter of the graph is:", find_graph_diameter(g))


if __name__ == "__main__":
    test_find_graph_diameter()
    test_find_graph_diameter2()
