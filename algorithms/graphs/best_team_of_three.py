#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 06/09/15, 12:37

My solution to exercise 139 from the series of exercises by prof. A. Carzaniga

Consider a weighted undirected graph G = (V, E)
representing a group of programmers and their affinity for team work,
such that the weight w(e) of an edge e = (u, v) is a number
representing the ability of programmers u and v
to work together on the same project.

Write an algorithm Best-Team-Of-Three
that outputs the best team of three programmers.

The value of a team is considered to be the lowest affinity level
between any two members of the team.

So, the best team is the group of programmers
for which the lowest affinity level between members of the group is maximal.

Ideas:
Basically we are going to have graph with weighted edges.
The weight of these edges represents the affinity
between the nodes (or programmers) of the edge.

As far as I have understood, two programmers work best together,
if their affinity or the weight of the edge between them is high.
But the overall affinity of the group is the smallest of the affinities.

We need to find some kind of triangle in an undirected graph.
A triangle can be found using dfs.
"""

from ands.ds.Graph import *


def is_an_edge(u, v):
    return v in u.get_adjacent_nodes()


def best_team_of_three(g):
    """Returns a set of programmers (nodes) with the best affinity.

    :type g : Graph
    """
    best_3 = set()
    max_lowest_affinity = -sys.maxsize

    for u in g.nodes:

        for v in u.get_adjacent_nodes():

            for z in v.get_adjacent_nodes():

                if is_an_edge(z, u):

                    triple = (u, v, z)

                    x = min(g.weight(u, v), g.weight(v, z), g.weight(z, u))

                    if x > max_lowest_affinity:
                        max_lowest_affinity = x
                        best_3.clear()
                        best_3 = best_3.union(triple)
    return best_3


if __name__ == "__main__":
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")
    e = GraphNode("e")

    g.add_undirected_edge(a, d, 1)
    g.add_undirected_edge(a, b, 2)
    g.add_undirected_edge(a, c, 2)

    g.add_undirected_edge(d, b, 3)
    g.add_undirected_edge(b, c, 3)

    g.add_undirected_edge(d, e, 4)
    g.add_undirected_edge(e, b, 5)

    print(best_team_of_three(g))
