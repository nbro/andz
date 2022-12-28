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

from collections import defaultdict

from ands.ds.graphs.Edge import Edge
from ands.ds.graphs.Graph import Graph
from ands.ds.graphs.Successor import Successor


class AdjacencyList(Graph):
    def __init__(self):
        # TODO: should I expect |V|=n to be pre-defined?
        # A map from nodes to a list of its successors. u is a successor of v
        # if there's an edge from v to u.
        # Space complexity: O(|V| + |E|). |V| is the space used to store the
        # keys.
        self.nodes: dict[int, list[Successor]] = defaultdict(list[Successor])

    def add(self, v: int, s: Successor):
        # Time complexity: O(1).
        assert isinstance(v, int) and isinstance(s, Successor)
        self.nodes[v].append(s)

    def successors(self, v: int) -> list[Successor]:
        # Time complexity: O(1).
        return self.nodes[v]

    def connected(self, v: int, u: int):
        # Time complexity: O(d), where d is the degree of v.
        return u in self.nodes[v]

    def edges(self) -> list[Edge]:
        # Time complexity: O(|V| + |E|).
        e = []
        for v, ss in self.nodes.items():
            for s in ss:
                u = s.u
                w = s.w
                e.append(Edge(v, u, w))
        return e


def example():
    g = AdjacencyList()
    g.add(0, Successor(1))
    g.add(0, Successor(2))
    g.add(1, Successor(2))
    g.add(1, Successor(4))
    g.add(2, Successor(4))
    g.add(4, Successor(5))
    g.add(3, Successor(5))
    from pprint import pprint

    pprint(g.nodes)
    print(g.edges())


if __name__ == "__main__":
    example()
