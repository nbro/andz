#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 16/03/2022

Updated: 16/03/2022

# Description

# References

- https://en.wikipedia.org/wiki/Depth-first_search
"""

from ands.ds.graphs.AdjacencyList import AdjacencyList
from ands.ds.graphs.Successor import Successor


def iterative_dfs(graph: AdjacencyList, v: int):
    # visited = set()
    visited = []
    stack = [v]
    while len(stack) != 0:
        u = stack.pop()
        # Note that we check first if we visited a node. In BFS, we first go
        # through the successors and then check if we visited a node.
        if u not in visited:
            # print("u = {}".format(u))
            # visited.add(u)
            visited.append(u)
            for s in graph.successors(u):
                stack.append(s.u)
    return visited


def _dfs(graph: AdjacencyList, v: int, visited: list):
    visited.append(v)
    for s in graph.successors(v):
        if s.u not in visited:
            _dfs(graph, s.u, visited)


def dfs(graph: AdjacencyList, v: int):
    visited = []
    _dfs(graph, v, visited)
    return visited


def example():
    g = AdjacencyList()
    g.add(0, Successor(1))
    g.add(0, Successor(2))
    g.add(1, Successor(2))
    g.add(1, Successor(4))
    g.add(2, Successor(4))
    g.add(4, Successor(5))

    from pprint import pprint

    visited = iterative_dfs(g, 0)
    pprint(visited)

    visited = dfs(g, 0)
    pprint(visited)


if __name__ == "__main__":
    example()
