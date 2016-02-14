#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: August, 2015

How to find MST of a weighted graph using Prim's algorithm:
https://www.youtube.com/watch?v=YyLaRffCdk4
"""

from ands.ds.Graph import *
from ands.ds.MinPriorityQueue import *


def _nodes_and_values(g):
    """Returns a list of tuples,
    each of them having 2 items:
    t_i[0] = reference to the node i
    t_i[1] = value (in this case is the priority) of node i.

    This method was created as a utility
    for the Prim's algorithm to find a MST.
    """
    ls = []
    for node in g.nodes:
        ls.append((node, node.value))
    return ls


def _initialise_prim_mst(g: Graph, s: GraphNode):
    for u in g.nodes:
        u.predecessor = NIL
        u.value = INFINITY
    s.value = 0


def prim_mst(g: Graph, s: GraphNode):
    """Creates a MST.

    During execution of this algorithm,
    nodes that are NOT yet in the tree,
    reside in the min priority queue,
    which is based on the "value" attribute.

    For each vertex v in the g,
    the attribute v.value is the minimum weight of any edge
    connecting v to a vertex in the tree.
    The attribute v.predecessor names the parent of v in the tree.

    The algorithm implicitly maintains a set A:
    A = {(v, v.predecessor) : v in V - {r} - Q}

    When the algorithm terminates, the mpq is empty,
    and A = {(v, v.predecessor) : v in V - {r}}."""

    _initialise_prim_mst(g, s)

    q = MinPriorityQueue(_nodes_and_values(g))

    last_node_added = s

    while not q.is_empty():

        u = q.extract_min()  # Returns the minimum element

        for v in u.get_adjacent_nodes():
            if q.contains_element(v) and g.weight(u, v) < v.value:
                v.value = g.weight(u, v)
                v.predecessor = u
                q.change_priority(v, new_priority=v.value)

        last_node_added = u

    return last_node_added


def print_prim_mst(last):
    while last is not None:
        print("Node:", last)
        print("Edge's weight:", last.value)
        print("Predecessor:", last.predecessor, end="\n\n")
        last = last.predecessor


def build_prim_mst(last):
    mst = Graph()

    while last is not None:
        n = GraphNode(last, last.value)
        if last.predecessor is not None:
            n.add_adjacent_node(last.predecessor, last.value)
            n.predecessor = last.predecessor
        mst.add_node(n)
        last = last.predecessor

    return mst


if __name__ == "__main__":
    graph = Graph()

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")
    e = GraphNode("e")
    f = GraphNode("f")
    g = GraphNode("g")
    h = GraphNode("h")
    i = GraphNode("i")

    a.add_adjacent_node(b, 4)
    a.add_adjacent_node(h, 8)

    b.add_adjacent_node(a, 4)
    b.add_adjacent_node(h, 11)
    b.add_adjacent_node(c, 8)

    c.add_adjacent_node(b, 8)
    c.add_adjacent_node(i, 2)
    c.add_adjacent_node(d, 7)
    c.add_adjacent_node(f, 4)

    d.add_adjacent_node(c, 7)
    d.add_adjacent_node(f, 14)
    d.add_adjacent_node(e, 9)

    e.add_adjacent_node(d, 9)
    e.add_adjacent_node(f, 10)

    f.add_adjacent_node(e, 10)
    f.add_adjacent_node(d, 14)
    f.add_adjacent_node(c, 4)
    f.add_adjacent_node(g, 2)

    g.add_adjacent_node(f, 2)
    g.add_adjacent_node(h, 1)
    g.add_adjacent_node(i, 6)

    i.add_adjacent_node(g, 6)
    i.add_adjacent_node(c, 2)
    i.add_adjacent_node(h, 7)

    h.add_adjacent_node(a, 8)
    h.add_adjacent_node(g, 1)
    h.add_adjacent_node(i, 7)
    h.add_adjacent_node(b, 11)

    graph.add_nodes((a, b, c, d, e, f, g, h, i))

    build_prim_mst(prim_mst(graph, a)).show_nodes()
