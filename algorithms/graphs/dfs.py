#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Implementation of depth-first search,
which uses starting and ending times of visiting nodes,
and keeps also track of the predecessor of each node,
in order to be able to backtrack from a node to the source, if necessary.
"""

from ands.ds.Graph import *


dfs_global_time = INFINITY


def dfs_iterative(graph):
    # TODO (eventually because it's complex...)
    pass

def dfs_aux(graph: Graph, n: GraphNode):
    """This function is called by dfs to further explore child nodes."""
    global dfs_global_time

    n.color = GREY
    dfs_global_time += 1
    n.start = dfs_global_time

    for v in n.get_adjacent_nodes():

        if v.color == WHITE:
            v.predecessor = n
            dfs_aux(graph, v)

    n.color = BLACK
    dfs_global_time += 1
    n.end = dfs_global_time


def dfs(graph: Graph):
    """Typical dfs algorithm that traverses all nodes
    that have not been explored yet,
    and keeps track of the visited and finished times."""
    global dfs_global_time

    for node in graph.nodes:
        node.predecessor = NIL
        node.starting_time = INFINITY
        node.ending_time = INFINITY
        node.color = WHITE

    dfs_global_time = 0  # global time for dfs

    for n in graph.nodes:
        if n.color == WHITE:  # if it is not visited
            dfs_aux(graph, n)

# TESTS

def test_dfs():
    g = Graph()

    # total_nodes for the graph
    A = GraphNode("A")
    B = GraphNode("B")
    C = GraphNode("C")
    D = GraphNode("D")
    E = GraphNode("E")
    F = GraphNode("F")

    # add the just created total_nodes to the graph
    g.add_node(A)
    g.add_node(B)
    g.add_node(C)
    g.add_node(D)
    g.add_node(E)
    g.add_node(F)

    # establish the connections between total_nodes
    A.add_adjacent_node(B)
    A.add_adjacent_node(D)
    A.add_adjacent_node(C)

    B.add_adjacent_node(A)
    B.add_adjacent_node(E)

    C.add_adjacent_node(D)
    C.add_adjacent_node(F)
    C.add_adjacent_node(A)

    D.add_adjacent_node(A)
    D.add_adjacent_node(C)

    E.add_adjacent_node(B)
    E.add_adjacent_node(F)

    F.add_adjacent_node(E)
    F.add_adjacent_node(C)

    # g.show_nodes()

    dfs(g)

    g.show_nodes()


def test_dfs2():
    g = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")
    e = GraphNode("e")
    f = GraphNode("f")

    g.add_node(a)
    g.add_node(b)
    g.add_node(c)
    g.add_node(d)
    g.add_node(e)
    g.add_node(f)

    a.add_adjacent_node(b)
    b.add_adjacent_node(e)
    b.add_adjacent_node(c)

    c.add_adjacent_node(a)

    d.add_adjacent_node(c)

    e.add_adjacent_node(d)

    f.add_adjacent_node(a)
    f.add_adjacent_node(e)

    dfs(g)

    g.show_nodes()


if __name__ == "__main__":
    test_dfs()
    # test_dfs2()
