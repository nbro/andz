#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Typical BFS algorithm to traverse or search in a graph.
BFS is useful (among other things) to find the shortest path
between a vertex and another (or any other) vertex.

These algorithms were thought to work with the implementation
of the graph in "Graph.py" that you can find under the folder "ds".
The implementation is based on an adjacency list representation of graphs.
"""

from ...ds.Graph import *
from ...ds.BFSQueue import *
from build_shortest_path import *
import __init__


def bfs(g: Graph, s: GraphNode):
    """BFS algorithm.

    We keep track of the predecessor of each node,
    in order to be able to backtrack from a certain node,
    all the way up to the starting_node,
    for example when building the shortest path.

    Running time complexity: O(|N| + |E|),
    where |N| is the number of nodes
    and |E| is the number of edges.
    The complexity is linear in the size of the nodes + edges
    because each node and edge is visited once,
    in other words, each of these visits cost O(1)."""

    if s not in g.nodes:
        raise Exception("'" + s.key + "' not in the graph '" + g.name + "'")

    # Initialisation of all nodes to the default values.
    # This is done because of possible multiple calls to bfs
    # and the values could not be the default ones,
    # and this would affect the calculations that bfs does.

    for u in g.nodes:
        u.distance = INFINITY
        u.predecessor = NIL
        u.color = WHITE

    q = BFSQueue()
    q.enqueue(s)
    s.color = GREY
    s.predecessor = NIL
    s.distance = 0

    while not q.is_empty():

        n = q.dequeue()
        
        for adj_node in n.get_adjacent_nodes():  # update children of n

            # If adj_node has not been visited yet
            # we mark it as visited,
            # and update all other important information...
            if adj_node.color == WHITE:
                adj_node.color = GREY
                adj_node.distance = n.distance + 1
                adj_node.predecessor = n
                q.enqueue(adj_node)

        n.color = BLACK  # mark "n" as completely explored


def find_shortest_path(g: Graph, source: GraphNode, destination: GraphNode) -> list:
    """Find the shortest path from source to destination.
    Note that you don't need to call bfs,
    since it is called automatically by this function.

    build_shortest_path is called
    to build a list containing all the nodes
    of the just found shortest path.

    This function returns an empty list,
    if there's not path from "source" to "destination"."""

    # if "destination" is not in the graph,
    # it does not make sense to continue the procedure
    # note that this check is also done for the source,
    # but it done in the bfs procedure.
    if destination not in g.nodes:
        raise Exception("'" + destination.key + "' not in the graph '" + g.name + "'")

    bfs(g, source)
    return build_shortest_path(destination)


def test_find_shortest_path():
    g = Graph()

    # total_nodes for the graph
    a = GraphNode("A")
    b = GraphNode("B")
    c = GraphNode("C")
    d = GraphNode("D")
    e = GraphNode("E")
    f = GraphNode("F")

    # add the just created total_nodes to the graph
    g.add_node(a)
    g.add_node(b)
    g.add_node(c)
    g.add_node(d)
    g.add_node(e)
    g.add_node(f)

    # establish the connections between total_nodes
    a.add_adjacent_node(b)
    a.add_adjacent_node(d)
    a.add_adjacent_node(c)

    b.add_adjacent_node(a)
    b.add_adjacent_node(e)

    c.add_adjacent_node(d)
    c.add_adjacent_node(f)
    c.add_adjacent_node(a)
    d.add_adjacent_node(a)
    d.add_adjacent_node(c)

    e.add_adjacent_node(b)
    e.add_adjacent_node(f)

    f.add_adjacent_node(e)
    f.add_adjacent_node(c)

    shortest_path = find_shortest_path(g, a, f)
    shortest_path = [x.key for x in shortest_path]
    print(shortest_path)


if __name__ == "__main__":
    test_find_shortest_path()
