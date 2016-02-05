#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 25/08/15

Find a shortest path between a node and any other,
using a topological sort for a DAG.
"""

from top_sort import *


def dag_shortest_path(dag, s):
    """This function calculates the shortest paths
    between s and any other node a DAG.

    Note that this algorithm only works for DAGs!

    This algorithm first creates a topological sort of dag,
    and, if dag contains a path from u to v,
    then u will come before v in the topological sort.

    Running time complexity: O(|V| + |E|),
    because of dfs.

    :type dag : Graph
    :type s : GraphNode
    """

    topological_sort = top_sort(dag)

    # Initialisation
    for node in topological_sort:
        node.predecessor = NIL
        node.distance = INFINITY

    s.distance = 0

    # Note that there's no need to explore
    # the last node in topological_sort
    # because it has no outgoing edges,
    # and thus we do not need to "_relax" anything.
    for u in topological_sort:
        for v in u.get_adjacent_nodes():
            # relaxation step
            if v.distance > dag.weight(u, v) + u.distance:
                v.distance = dag.weight(u, v) + u.distance
                v.predecessor = u

def test_dag_shortest_path():
    g = Graph()

    r = GraphNode("r")
    s = GraphNode("s")
    t = GraphNode("t")
    x = GraphNode("x")
    y = GraphNode("y")
    z = GraphNode("z")

    r.add_adjacent_node(s, 5)
    r.add_adjacent_node(t, 3)

    s.add_adjacent_node(x, 6)
    s.add_adjacent_node(t, 2)

    t.add_adjacent_node(y, 4)
    t.add_adjacent_node(x, 7)
    t.add_adjacent_node(z, 2)

    x.add_adjacent_node(y, -1)
    x.add_adjacent_node(z, 1)

    y.add_adjacent_node(z, -2)

    g.add_node(r)
    g.add_node(s)
    g.add_node(t)
    g.add_node(x)
    g.add_node(y)
    g.add_node(z)

    dag_shortest_path(g, s)

    g.show_nodes()


if __name__ == "__main__":
    test_dag_shortest_path()
