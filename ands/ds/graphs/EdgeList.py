#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 16/03/2022

Updated: 16/03/2022

# Description


# References

- https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs

"""

from ands.ds.graphs.Edge import Edge
from ands.ds.graphs.Graph import Graph


class EdgeList(Graph):
    def __init__(self):
        # (v, u, w) is an edge from v to u with weight w.
        # w should be zero, if the graph is unweighted.
        # The space complexity is |E| = the number of edges.
        self.edges: list[Edge] = []

    def add(self, e: Edge):
        assert isinstance(e, Edge)
        self.edges.append(e)

    def contains(self, e: Edge) -> bool:
        assert isinstance(e, Edge)
        # Time complexity: O(|E|).
        return e in self.edges


def example():
    g = EdgeList()
    g.add(Edge(0, 1))
    g.add(Edge(0, 2))
    g.add(Edge(1, 2))
    from pprint import pprint

    pprint(g.edges)


if __name__ == "__main__":
    example()
