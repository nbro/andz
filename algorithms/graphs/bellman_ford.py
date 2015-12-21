#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 26/08/15

Bellman-Ford's single-source shortest path
is an algorithm to find the shortest path from a source node s
to any other node in the graph.

This algorithm works also on negative weighted edges,
and it can also report if there's a negative cycle in the graph.

If you want to know the actual shortest path,
you can use the build_shortest_path function
that you can find in the homonymous module or file.
It requires only that you pass to it the destination node.
"""

from ands.ds.Graph import *
from build_shortest_path import *


def _initialise_single_source(graph: Graph, s: GraphNode):
    for u in graph.nodes:
        u.distance = INFINITY
        u.predecessor = NIL
    s.distance = 0


def _build_negative_cycle(v: GraphNode):
    # TODO (I should definetely do it...)
    pass


def _detect_negative_cycles(graph: Graph):
    """Returns True if there's a negative cycle,
    reachable from the source node.

    After running the loop for |V| - 1 times in the bellman_ford function,
    no further improvement should be possible.
    If we can still lower the distance to a node, then a negative cycle exists."""
    for (u, v), w in graph.edges.items():
        if v.distance > u.distance + w:
            return False
    return True


def _relax(u: GraphNode, v: GraphNode, w):
    if v.distance > u.distance + w:
        v.distance = u.distance + w
        v.predecessor = u


def bellman_ford(graph: Graph, s: GraphNode):
    """Finds shortest paths in a directed weighted graph,
    whose edges' weights can also be negative,
    in contrast to the Dijkstra's algorithm,
    that would not work on that situation."""
    _initialise_single_source(graph, s)

    # Note that a (simple) shortest path
    # can have at most |V| - 1 edges (and |V| vertices),
    # since simple paths cannot have repeated vertices.
    for _ in range(graph.num_of_nodes() - 1):

        # Note that edges returns a dict,
        # where keys are a tuple of the nodes in the edge
        # and the values are the weights of the corresponding edges.
        for (u, v), weight in graph.edges.items():
            _relax(u, v, weight)

    return _detect_negative_cycles(graph)


def test_bellman_ford():
    g = Graph()

    s = GraphNode("S")
    t = GraphNode("T")
    y = GraphNode("Y")
    x = GraphNode("X")
    z = GraphNode("Z")

    s.add_adjacent_node(t, weight=6)
    s.add_adjacent_node(y, weight=7)

    y.add_adjacent_node(z, weight=9)
    y.add_adjacent_node(x, weight=-3)

    t.add_adjacent_node(z, weight=-4)
    t.add_adjacent_node(x, weight=5)
    t.add_adjacent_node(y, weight=8)

    x.add_adjacent_node(t, weight=-2)

    z.add_adjacent_node(x, weight=7)
    z.add_adjacent_node(s, weight=2)

    g.add_nodes((s, t, y, x, z))

    print(bellman_ford(g, s))

    g.show_nodes()

    print("Shortest path from", s, "to", t, "is", build_shortest_path(t), ",  and its distance is:", t.distance)
    print("Shortest path from", s, "to", y, "is", build_shortest_path(y), ",  and its distance is:", y.distance)
    print("Shortest path from", s, "to", z, "is", build_shortest_path(z), ",  and its distance is:", z.distance)
    print("Shortest path from", s, "to", x, "is", build_shortest_path(x), ",  and its distance is:", x.distance)
    print("Shortest path from", s, "to", s, "is", build_shortest_path(s), ",  and its distance is:", s.distance)


def test_bellman_ford_2():
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")

    g.add_directed_edge(a, b, -2)
    g.add_directed_edge(b, c, -3)
    g.add_directed_edge(c, a, -1)

    cycle = bellman_ford(g, a)
    print("Cycle detected:", cycle)


if __name__ == "__main__":
    test_bellman_ford()
    test_bellman_ford_2()
