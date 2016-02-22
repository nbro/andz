#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015
"""

from ands.ds.Graph import *
from ands.ds.Queue import BFSQueue


def bfs(graph, s):
    """BFS algorithm implemented specifically
    to check if a graph is bipartite or not.

    Running time complexity: O(|N| + |E|),
    where |N| is the number of nodes
    and |E| is the number of edges.
    The complexity is linear in the size of the nodes + edges
    because each node and edge is visited once,
    in other words, each of these visits cost O(1).

    :type graph : Graph
    :type s : GraphNode
    """

    if s not in graph.nodes:
        raise Exception("'" + s.key + "' not in the graph '" + graph.name + "'")

    for u in graph.nodes:
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

        for adj_node in n.get_adjacent_nodes():

            # When checking if a graph is bipartite,
            # it is sufficient to check if all adjacent nodes
            # are note GREY and they have not the same distance
            # as the node that is being explored.
            # Why?
            # Since BFS proceeds the exploration of a graph by levels,
            # when exploring a node n at a certain level i,
            # all the nodes of that level can either be GREY or BLACK
            # and their distances must be the same as the distance of n,
            # the node being explored.
            # If one of the adjacent nodes happens to be GREY
            # that would mean that it is in the same level
            # and its distance should also be equal to n's distance.
            # Note that if the color of an adjacent node is BLACK,
            # it cannot be in the same level,
            # because the first node in the level that detects this cycle
            # to a node in the same level,
            # would always find first un unexplored node GREY.
            # If the adjacent node is BLACK,
            # that means the node has already been completely explored
            # and is in a previous level,
            # It could not even be in the previous level of the previous current level,
            # because that would mean that the current node n
            # should have a different distance. Can you see why?

            if adj_node.color == GREY and adj_node.distance == n.distance:
                return False

            if adj_node.color == WHITE:
                adj_node.color = GREY
                adj_node.distance = n.distance + 1
                adj_node.predecessor = n
                q.enqueue(adj_node)

        n.color = BLACK  # mark "n" as completely explored

    return True  # graph is bipartite


# Idea: https://www.youtube.com/watch?v=r1-8p11fSPw&list=PLBF3763AF2E1C572F&index=26

def is_bipartite(graph, verbose=False):
    """Check if the graph is bipartite.
    A graph is bipartite, if every node A in a certain level i
    is connected to another node B in either a level i - 1 or i + 1, or,
    in other words, nodes in the same level cannot be connected together.

    :type graph : Graph
    """
    starting_node = graph.nodes[0]

    if verbose:
        print("Starting bfs from", starting_node.key)

    return bfs(graph, starting_node)


def test_is_bipartite():
    g = Graph()

    # nodes for the graph
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

    A.add_adjacent_node(E)
    A.add_adjacent_node(D)

    B.add_adjacent_node(D)
    B.add_adjacent_node(F)

    C.add_adjacent_node(E)

    D.add_adjacent_node(A)
    D.add_adjacent_node(B)
    D.add_adjacent_node(E)

    E.add_adjacent_node(A)
    E.add_adjacent_node(C)
    E.add_adjacent_node(D)

    F.add_adjacent_node(B)

    print("Is bipartite:", is_bipartite(g, verbose=True))


def test_is_bipartite2():
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

    a.add_adjacent_node(d)
    d.add_adjacent_node(a)

    a.add_adjacent_node(e)
    e.add_adjacent_node(a)

    b.add_adjacent_node(d)
    d.add_adjacent_node(b)
    b.add_adjacent_node(f)
    f.add_adjacent_node(b)

    c.add_adjacent_node(e)
    e.add_adjacent_node(c)

    c.add_adjacent_node(f)
    f.add_adjacent_node(c)

    print("Is bipartite:", is_bipartite(g, verbose=True))


if __name__ == "__main__":
    test_is_bipartite()
    test_is_bipartite2()
