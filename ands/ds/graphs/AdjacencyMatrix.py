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

from ands.ds.graphs.Graph import Graph


# TODO: support weights
# TODO: add __repr__ to print a nice matrix
# TODO: add method that returns edges
class AdjacencyMatrix(Graph):
    def __init__(self, n: int, value: int = 0):
        # n is the number of nodes.
        # value is the initial value. If value = 0, then all nodes are
        # disconnected.
        assert isinstance(n, int)
        assert isinstance(value, int)
        if n < 1:
            raise ValueError("n should be >= 1 but n = {}".format(n))
        if value not in (0, 1):
            raise ValueError("value should be 0 or 1, but it's " "{}".format(value))
        self.n = n
        # Space complexity: O(n*m)
        self.matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]

    def _check_inputs(self, inputs: list[int]):
        assert all(isinstance(v, int) for v in inputs)
        for v in inputs:
            if not (0 <= v < self.n):
                raise ValueError(
                    "{} is not a valid node; a valid node must "
                    "be an integer in the range "
                    "[0, {})".format(v, self.n)
                )

    def successors(self, v: int):
        # Time complexity: O(n).
        self._check_inputs([v])
        s = []
        for u, value in enumerate(self.matrix[v]):
            if value == 1:
                s.append(u)
        return s

    def add(self, v: int, u: int):
        # Time complexity: O(1).
        self._check_inputs([v, u])
        self.matrix[v][u] = 1

    def delete(self, v: int, u: int):
        # Time complexity: O(1).
        self._check_inputs([v, u])
        self.matrix[v][u] = 0

    def connected(self, v: int, u: int):
        # Time complexity: O(1).
        self._check_inputs([v, u])
        return self.matrix[v][u] == 1


def example():
    g = AdjacencyMatrix(3)
    g.add(0, 1)
    g.add(0, 2)
    g.add(1, 2)

    for s in g.matrix:
        print(*s)


if __name__ == "__main__":
    example()
