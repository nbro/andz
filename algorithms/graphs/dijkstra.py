#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Implementation of a typical Dijkstra's single-source shortest path algorithm.
It uses the min priority queue implementation found in MinPriorityQueue.py.

Want to know more about Dijkstra's single-source shortest path algorithm?
- http://interactivepython.org/courselib/static/pythonds/Graphs/DijkstrasAlgorithm.html
- https://www.youtube.com/watch?v=elUoBUwIlpQ (Computer Networks 5-3: Dijkstra's Algorithm)
"""

from ands.ds.Graph import *
from ands.ds.MinPriorityQueue import *


def _initialise_single_source(graph, source_node):
    """Initialisation step for Dijkstra's
    single source shortest path algorithm.

    :type graph : Graph
    :type source_node : GraphNode
    """
    for u in graph.nodes:
        u.distance = INFINITY
        u.predecessor = NIL

    source_node.distance = 0


def _relax(u: GraphNode, v: GraphNode, w: "function", q: MinPriorityQueue):
    """Relaxes the distance to v from u, using the weight function w.

    u is the current node.

    v is the adjacent node to u that we want to _relax.

    w is the weight function.

    q is the MinPriorityQueue object containing v,
    that we need to change v's priority within it,
    if eventually we _relax v's distance to the source node."""
    if v.distance > u.distance + w(u, v):
        v.distance = u.distance + w(u, v)
        v.predecessor = u

        # Raises an error if v is no more in q
        # This is nice because this only happens
        # where there's a negative weighted edge.
        q.change_priority(v, u.distance + w(u, v))


def _nodes_and_distances(g: Graph):
    ls = []
    for node in g.nodes:
        ls.append((node, node.distance))
    return ls


def dijkstra(g: Graph, s: GraphNode):
    """
    Dijkstra's algorithm to calculate since-source shortest paths,
    that is to calculate the shortest path between source_node and
    any other node in graph, which should be a directed weighted graph.

    This algorithm maintains tha invariant  Q = V - S,
    where Q is the min priority queue (set),
    V is the set of vertices in the graph,
    and S is the set of visited nodes,
    whose distances have already been determined.

    Note that the algorithm never inserts nodes in q (Q),
    after it is initialised with the nodes of the graph,
    but priorities are changed only.

    Note also that each vertex that is extracted from Q,
    is added to the set of visited_nodes exactly once.

    Since this algorithm always chooses the lightest edge from Q to add to S,
    we say that this algorithm uses a greedy strategy.

    Greedy strategies not always yield an optimal solution,
    but in the case of this algorithm, it does.

    This algorithm does not work when edges have negative weights.
    Lets look at an example that illustrates this.

    Suppose we have a graph of 3 nodes like the following:

    Adjacency lists:

    S = [(A, 3), (B, 2)]
    A = [(S, 3), (B, -2)]
    B = [(S, 2), (A, -2)]

    Edges = [(S, A, 3), (S, B, 2), (A, B, -2)]

    Note that the previous graph is an undirected graph,
    where basically, if A and B are connected,
    then A contains a tuple representing its connection to B,
    and vice-versa, B contains a tuple representing its connection to A.
    In the set of edges, we can see more clearly these undirected edges.

    Now, suppose we start this algorithm from S.
    The first thing to do is to update the current shortest path to A and B.
    We set A.distance = 3 and B.distance = 2.
    Then we visit B. We update A's distance to 0.

    Why doesn't this algorithm work on this graph?

    If you start from S and then go to A and finally to B,
    we obtain a shortest path of length 1,
    but note that this algorithm gave us a shortest path to B of 2,
    which is incorrect!"""

    _initialise_single_source(g, s)

    # This set will contain the vertices of graph,
    # whose shortest path weights from source_node have already been determined.
    visited_nodes = set()

    # Creation of a MinPriorityQueue object that takes into account as priorities
    # the distances of the nodes in the graph from source_node.
    # get_node_with_distances returns a list of tuples,
    # whose first item is a HeapNode and the second its distance from source_node,
    # that at this point (initially) is set to INFINITY by _initialise_single_source.
    q = MinPriorityQueue(_nodes_and_distances(g))

    while q.is_not_empty():
        # u has the estimated shortest path in the set V - S
        # Note that the first element being pulled is the source_node.
        u = q.extract_min()

        # {u} is a set with one element
        # The following operation (in this case)
        # is equivalent to: visited_nodes.add(u)
        visited_nodes = visited_nodes.union({u})

        for v in u.get_adjacent_nodes():
            # In the implementation of the graph data structure in Graph.py,
            # the weight of an edge between two connected nodes
            # can be found by calling the static method weight,
            # by passing to it the two nodes of the edge.

            _relax(u, v, g.weight, q)

    return visited_nodes


def test_dijkstra():
    g = Graph()

    s = GraphNode("S")
    t = GraphNode("T")
    y = GraphNode("Y")
    x = GraphNode("X")
    z = GraphNode("Z")

    s.add_adjacent_node(t, weight=10)
    s.add_adjacent_node(y, weight=5)

    y.add_adjacent_node(t, weight=3)
    y.add_adjacent_node(z, weight=2)
    y.add_adjacent_node(x, weight=9)

    t.add_adjacent_node(y, weight=2)
    t.add_adjacent_node(x, weight=1)

    x.add_adjacent_node(z, weight=4)

    z.add_adjacent_node(x, weight=6)
    z.add_adjacent_node(s, weight=7)

    g.add_nodes((s, t, y, x, z))

    visited_updated_nodes = dijkstra(g, s)

    print(visited_updated_nodes)

    for n in visited_updated_nodes:
        print("Node:", n, ",Distance:", n.distance)


def test_dijkstra2():
    g = Graph()

    s = GraphNode("s")
    a = GraphNode("a")
    b = GraphNode("b")

    g.add_undirected_edge(s, a, 3)
    g.add_undirected_edge(a, b, 1)
    g.add_undirected_edge(s, b, 2)

    dijkstra(g, s)

    g.show_nodes()

if __name__ == "__main__":
    # test_dijkstra()
    test_dijkstra2()
