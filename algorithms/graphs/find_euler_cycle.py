#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 05/09/15

Euler cycle in a graph is a cycle
that goes through each edge exactly once.
It turns out that a Euler cycle exists if:
    1. the graph is connected
    2. Every node has an even degree, for undirected graphs,
    or every node has in-degree equal to the out-degree,
    for directed graphs.

So, how do we find a Euler cycle?
"""

from pprint import pprint
from random import choice

from connected_components import *


def _is_self_loop(edge):
    return edge[0] == edge[1]


def _dfs_aux(g, u, visited, cycle):
    """Called once by dfs to traverse the graph

    :type g : Graph
    :type u : GraphNode
    :type visited : dict
    :type cycle : list
    """

    for v in u.get_adjacent_nodes():
        edge = (u, v)

        if edge not in visited:
            visited[edge] = True

            if not _is_self_loop(edge):
                visited[(v, u)] = True

            cycle.append(edge)

            _dfs_aux(g, v, visited, cycle)

    return cycle


def dfs(g):
    """DFS for the find_euler_cycle procedure.

    :type g : Graph
    """
    visited = {}
    cycle = []  # Edges in the Euler cycle

    s = choice(list(g.nodes))

    return _dfs_aux(g, s, visited, cycle)


def find_euler_cycle(g):
    """
    :type g : Graph
    """
    if not is_connected(g) or not g.has_even_degree():
        return None

    return dfs(g)


def test_find_euler_cycle():
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")
    e = GraphNode("e")
    f = GraphNode("f")

    a.add_adjacent_node(b)
    a.add_adjacent_node(c)
    a.add_adjacent_node(e)
    a.add_adjacent_node(f)

    b.add_adjacent_node(a)
    b.add_adjacent_node(d)

    c.add_adjacent_node(d)
    c.add_adjacent_node(a)

    d.add_adjacent_node(b)
    d.add_adjacent_node(c)

    e.add_adjacent_node(a)
    e.add_adjacent_node(f)

    f.add_adjacent_node(e)
    f.add_adjacent_node(a)

    g.add_nodes((a, b, c, d, e, f))

    pprint(find_euler_cycle(g))


def test_find_euler_cycle_2():
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")

    a.add_adjacent_node(b)
    b.add_adjacent_node(c)
    c.add_adjacent_node(d)
    d.add_adjacent_node(a)

    g.add_nodes((a, b, c, d))

    pprint(find_euler_cycle(g))


if __name__ == "__main__":
    test_find_euler_cycle()
    test_find_euler_cycle_2()
