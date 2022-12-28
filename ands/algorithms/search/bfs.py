#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 16/03/2022

Updated: 16/03/2022

# Description

# References

- https://en.wikipedia.org/wiki/Breadth-first_search
"""

from collections import deque

from ands.ds.graphs.AdjacencyList import AdjacencyList
from ands.ds.graphs.Successor import Successor


def bfs(graph: AdjacencyList, v: int):
    # It does not keep track of paths.
    # visited = set()  # aka closed set, discovered set
    q = deque([v])
    visited = [v]
    while len(q) != 0:
        print("q = {}".format(q))
        u = q.popleft()
        print("u = {}".format(u))
        for s in graph.successors(u):
            # print(s)
            if s.u not in visited:
                # visited.add(s.u)
                visited.append(s.u)
                q.append(s.u)
    return visited


def bfs_find_paths(graph: AdjacencyList, v: int):
    # Alternative: keep track of the parent of each node, so that we can
    # then backtrack.
    # It keeps track of parents.
    q = deque([[v]])
    all_paths = [[v]]
    while len(q) != 0:
        path = q.popleft()
        u = path[-1]
        for s in graph.successors(u):
            # Make a copy of path, one for each successor
            new_path = list(path)
            new_path.append(s.u)
            q.append(new_path)
            all_paths.append(new_path)
    return all_paths


def example():
    g = AdjacencyList()
    g.add(0, Successor(1))
    g.add(0, Successor(2))
    g.add(1, Successor(2))
    g.add(1, Successor(4))
    g.add(2, Successor(4))
    g.add(4, Successor(5))

    from pprint import pprint

    visited = bfs(g, 0)
    pprint(visited)

    all_paths = bfs_find_paths(g, 0)
    pprint(all_paths)


if __name__ == "__main__":
    example()
