#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 29/08/15, 17:57

build_shortest_path can be used
to construct a list of nodes
that represent the shortest path
from a source node to a destination node.

Note that you should call this function
only after an algorithm, such as BFS,
has run on the graph,
i.e. precedecessors are set correctly.
"""


def build_shortest_path(destination):
    """Returns a list with the nodes of the shortest path
    from source to destination (both included).

    source is the node from which the search started.

    This function should be called only after
    an algorithm for calculating the shortest path,
    for example bfs or bellman_ford,
    has calculated and updated the shortest distances
    of every vertex from a source node.

    :type destination : GraphNode
    """

    shortest_path = []
    tmp = destination

    while tmp is not None:
        shortest_path.append(tmp)
        tmp = tmp.predecessor

    shortest_path.reverse()

    return shortest_path
