#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 26/08/15

The eccentricity of a node n is defined as the length
of the longest shortest path from n to any other node.
"""

from ands.ds.Graph import *
from ands.ds.BFSQueue import *


def bfs(graph, starting_node):
    """Breadth-first search algorithm
    used to find the eccentricity of nodes.

    Running time complexity: O(|N| + |E|),
    where |N| is the number of nodes
    and |E| is the number of edges.
    The complexity is linear in the size of the nodes + edges
    because each node and edge is visited once,
    in other words, each of these visits cost O(1).

    :type graph : Graph
    :type starting_node : GraphNode
    """
    distances = []  # used to calculate the eccentricity

    if starting_node not in graph.nodes:
        raise Exception("'" + starting_node.key + "' not in the graph '" + graph.name + "'")

    for u in graph.nodes:
        u.distance = INFINITY
        u.predecessor = NIL
        u.color = WHITE

    # initialisation of bfs with starting_node
    q = BFSQueue()
    q.enqueue(starting_node)
    starting_node.color = GREY
    starting_node.predecessor = NIL
    starting_node.distance = 0

    while not q.is_empty():

        n = q.dequeue()

        for adj_node in n.get_adjacent_nodes():  # update children of n
            if adj_node.color == WHITE:
                adj_node.color = GREY
                adj_node.distance = n.distance + 1
                adj_node.predecessor = n
                q.enqueue(adj_node)

        n.color = BLACK  # mark "n" as completely explored

        # Appending the distance of each explored node
        # to a list of all distances
        # in order to calculate the eccentricity of starting_node
        distances.append(n.distance)

    # Returning the eccentricity of starting_node.
    return max(distances)


def find_eccentricity(graph, n):
    """Finds the eccentricity of node n,
    which is defined as max(d(n, v) | v in graph.nodes),
    or in other words the eccentricity of a node n
    is the length of the longest shortest path
    from n to a node v, for all nodes v in graph.

    The eccentricity of a node n is 1,
    iff n is adjacent to all other nodes in the graph.

    :type graph Graph
    :type n : GraphNode
    """
    return bfs(graph, n)


def test_find_eccentricity():
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

    for node in g.nodes:
        print("Eccentricity of", node.key, ": ", find_eccentricity(g, node))


def test_find_eccentricity2():
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")

    g.add_undirected_edge(a, b)
    g.add_undirected_edge(a, c)
    g.add_undirected_edge(a, d)

    for node in g.nodes:
        print("Eccentricity of", node.key, ": ", find_eccentricity(g, node))


if __name__ == "__main__":
    test_find_eccentricity()
    test_find_eccentricity2()
