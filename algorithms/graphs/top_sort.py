#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 25/08/15

Notes: To reduce dependencies between modules,
I decided to included a clean version of dfs here,
specifically for the top_sort algorithm.

Explanation:
A topological ordering (or sorting, sort, order) of a directed graph with no cycles (DAG),
is an order of the vertices, such that all the directed edges only go forward.

Knowing the topological ordering of a DAG can be useful
for example when we want to schedule certain tasks,
where some tasks have higher precedence respect to others:
in this example, vertices of the graph represent the tasks,
and a directed edge from a certain node A to node B
represents the fact that A must be "computed" or "executed" before B,
A has higher precedence respect to B.

When does a graph have a topological sorting?

A graph has a topological sorting if and only if it has no cycles.

The fact that a graph with a topological order
has no cycles is quite easy to understand:
Suppose a graph G has a cycle,
then when searching for a topological ordering in the cycle,
we are going at some point to return to a node that we have already visited,
and this would mean that there's an edge that goes backward,
which contradicts the fact that G has a topological ordering,
by the definition of topological ordering.

What if we don't have a cycle, do we always have a topological ordering?
Yes [missing proof].

We can find a topological ordering:
1. without dfs (the straightforward solution)
2. with depth-first search
3. another solution

1. Topological ordering without dfs (the straightforward solution)

First, we need to have the notion of a "sink vertex",
which simply is a vertex with no outgoing edges.

Lemma: Every DAG must have a sink vertex.
Proof: Suppose DAG g has no sink vertex and it has a finite number of vertices,
then, when you are searching on the graph,
you will always find at least one outgoing edge from every vertex.
Since g has a finite number of vertices,
we will find at some point a vertex that we have already visited,
which would contradict the assumptions that g is a directed graph with no cycles (DAG).

PSEUDO-CODE:

TOP-SORT(DAG):
    top_sort_list = []

    create a copy of DAG called g

    while g is not empty:
        // the next sink vertex is also removed from g,
        // so its size is decreased at each iteration.
        top_sort_list.add(g.get_next_sink_vertex())

    return top_sort_list

Note that by removing a node from a DAG, we will never create a cycle,
and thus we will always be able to find a sink vertex.


2. Topological ordering with dfs
Check the function implemented below. You should also check the function dfs.

But using dfs should be as easy as the following pseudo-code shows:

TOPOLOGICAL-SORT(G):
    DFS(G)
    output vertices V in reversed order of finish times.


3. TOPOLOGICAL-SORT-SOL-3(G):
    1. Find an vertex v with no incoming edges
    2. Remove outgoing edge from v
    3. Go back to step 1

To improve the performance of this algorithm,
- we can pre-compute the number of incoming edges of each vertex.
- insert_key all nodes with degree of 0 into a queue
- repeat the following until the queue is not empty
    * Take u from the queue
    * for each v adj[u]:
        decrement deg[v] (essentially removing edge u - v
        if deg[v] == 0:
            insert_key v into the queue


PROOF OF CORRECTNESS:
We basically need to show_nodes that, if (u, v) is a directed edge from u to v,
then u comes before v in the topological sort.

We have 2 cases:
1. u is visited by dfs before v
2. v is visited by dfs before u

Assume that u is visited before v (1).
Then there's nothing to prove,
because v will be set explored (and therefore at the right of u) before u.

So assume that v is visited before u (2).
This is only true if v was visited from another vertex
(and note that u has not yet been visited).
v will be therefore set as explored before even visiting u,
and thus v will be to the right of u in the topological order,
since u will be added to the topological order only when it is completely explored.

"""

from ands.ds.Graph import *


def dfs_visit(graph: Graph, n: GraphNode):
    """This function is called by dfs to further explore child nodes."""

    n.color = GREY

    for v in n.get_adjacent_nodes():
        if v.color == WHITE:
            dfs_visit(graph, v)

    n.color = BLACK

    # adding the just explored node to the list
    # which represents the topological sort
    graph.topological_sort.append(n)


def dfs(graph: Graph):
    """Typical dfs algorithm that traverses
    all nodes that have not been explored yet
    and keeps track of the visited and finished times."""

    for n in graph.nodes:
        n.color = WHITE

    for n in graph.nodes:
        if n.color == WHITE:
            dfs_visit(graph, n)


# TODO: DETECT CYCLE IN A "SUPPOSED" DAG

def top_sort(dag: Graph):
    """dag = DAG = Direct A-cycle Graph

    If dag is not really a directed graph with no cycles (DAG),
    the behaviour of this function is undefined.

    This algorithm creates a topological sort
    by using the ending visited times of each node:
    once a node has been completely explored,
    it is added to a list representing the topological sort.

    Time complexity: O(|V| + |E|)"""
    dfs(dag)

    # dag.top_sort_with_dfs is an object of type TopologicalSortStack,
    # so the first element of this object
    # is the element at the bottom of the stack
    # and the last element is the element at the top
    dag.topological_sort.reverse()

    return dag.topological_sort



def test_topological_sort():
    g = Graph()

    a = GraphNode("A")
    b = GraphNode("B")
    c = GraphNode("C")
    d = GraphNode("D")

    a.add_adjacent_node(b)
    a.add_adjacent_node(c)

    b.add_adjacent_node(d)

    c.add_adjacent_node(d)

    g.add_node(a)
    g.add_node(b)
    g.add_node(c)
    g.add_node(d)

    ts = top_sort(g)
    ts = [x.key for x in ts]
    print(ts)


# https://en.wikipedia.org/wiki/Topological_sorting
def test_topological_sort2():
    g = Graph()

    n7 = GraphNode(7)
    n5 = GraphNode(5)
    n3 = GraphNode(3)
    n11 = GraphNode(11)
    n8 = GraphNode(8)
    n2 = GraphNode(2)
    n9 = GraphNode(9)
    n10 = GraphNode(10)

    g.add_node(n2)
    g.add_node(n7)
    g.add_node(n5)
    g.add_node(n3)
    g.add_node(n11)
    g.add_node(n8)
    g.add_node(n9)
    g.add_node(n10)

    n7.add_adjacent_node(n11)
    n7.add_adjacent_node(n8)

    n5.add_adjacent_node(n11)

    n3.add_adjacent_node(n8)
    n3.add_adjacent_node(n10)

    n11.add_adjacent_node(n2)
    n11.add_adjacent_node(n9)
    n11.add_adjacent_node(n10)

    n8.add_adjacent_node(n9)

    ts = top_sort(g)
    ts = [x.key for x in ts]
    print(ts)


if __name__ == "__main__":
    test_topological_sort()
    test_topological_sort2()
