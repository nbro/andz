#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 26/08/15

Utility functions related to connected components of a graph.
"""

from ands.ds.Graph import *
from ands.ds.Queue import BFSQueue


def bfs(g: Graph, s: GraphNode):
    """BFS algorithm implemented specifically
    to find the connected components of a graph.

    Time complexity: O(number of nodes + number of edges),

    The complexity is linear in the size of the nodes + edges
    because each node and edge is visited once,
    in other words, each of these visits cost O(1)."""

    # Adding a new empty list to represent this connected component
    g.connected_components.append([])

    s.color = GREY

    q = BFSQueue()
    q.enqueue(s)

    while not q.is_empty():

        u = q.dequeue()

        for v in u.get_adjacent_nodes():
            if v.color == WHITE:
                v.color = GREY
                q.enqueue(v)

        u.color = BLACK

        # Each Graph object contains a field, a list of lists,
        # each of them containing the nodes of different connected components,
        # basically each of these lists is a connected component.
        g.connected_components[-1].append(u)

        # Each node contains also a field called "connected_component",
        # which represents the connected component to which they belong.
        u.connected_component = len(g.connected_components)


def find_connected_components(g: Graph):
    """Finds the connected components in graph using bfs.

    Connected components of graph are sub-graphs of graph
    that are not connected together by an edge.

    This procedure is useful for:
        - checking if a network is disconnected
        - visualising the parts of a graph
        - ..."""

    # Clearing possible previous calculations
    g.connected_components.clear()

    for u in g.nodes:
        u.color = WHITE
        u.connected_component = NIL

    for v in g.nodes:
        # If a node is still WHITE, that means it has not yet been visited,
        # either because this is the first iteration
        # or because v belongs to a different connected component
        # than the ones of the previous found.
        if v.color == WHITE:
            bfs(g, v)

    return g.connected_components


def dfs(g: Graph, u: GraphNode):
    u.color = GREY

    for v in u.get_adjacent_nodes():
        if v.color == WHITE:
            dfs(g, v)

    u.color = BLACK


def count_connected_components(g: Graph):
    """Find connected components using dfs."""
    cc = 0

    for u in g.nodes:
        u.color = WHITE

    for u in g.nodes:
        if u.color == WHITE:
            dfs(g, u)
            cc += 1

    return cc


def is_connected(g: Graph):
    """Returns true if g has only one connected component,
    which would also imply that it is connected."""
    return count_connected_components(g) == 1


if __name__ == "__main__":
    graph = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")
    e = GraphNode("e")
    f = GraphNode("f")

    graph.add_undirected_edge(a, b)
    graph.add_undirected_edge(b, c)
    graph.add_undirected_edge(a, c)
    # graph.add_undirected_edge(b, d)
    graph.add_undirected_edge(e, f)
    # graph.add_undirected_edge(e, d)

    graph.add_nodes((a, b, c, d, e, f))

    print(count_connected_components(graph))
    print(find_connected_components(graph))

    graph.show_connected_components()
