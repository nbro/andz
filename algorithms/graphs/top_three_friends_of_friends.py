#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 05/09/15

Exercise 127.

Consider a social network system that, for each user u,
stores u's friends in a list friends(u).
Implement an algorithm Top-Three-Friends-Of-Friends(u) that,
given a user u, recommends the three other users that are not
already among u's friends but are among
the friends of most of u's friends.
Also, analyze the complexity of the Top-Three-Friends-Of-Friends algorithm.


My idea:
Build the network system as a graph.

But how do we find the 3 friends of friends to suggest to the user u?

Given a user u, we can iterate through its friends.

First, we should create an empty list "suggestions" to store the suggestions.

Then we iterate through each adjacent node w
of each adjacent node "v" of the node "user",
and we check two things:
    1. that w is not adjacent to "user"
    2. w is not already in the list "suggestions".
"""

from pprint import pprint

from ands.ds.Graph import *


def top_three_friends_of_friends(user, k=3):
    """Return a list of suggestions of friends for user.

    Running time complexity:
     - O(n^3) in the worst case
     - O(n^2) in the average case.

    Node that searching for element in a set
    is in average a constant operation,
    but in the worst case it can be linear.

    :type user : GraphNode
    """
    friends = set(user.get_adjacent_nodes())
    suggestions = set()

    for friend in friends:
        for ff in friend.get_adjacent_nodes():
            if ff != user and ff not in friends and \
                            ff not in suggestions and len(suggestions) < k:
                suggestions.add(ff)

    return suggestions


if __name__ == "__main__":
    sn = Graph("Social Network")

    a = GraphNode("a")
    b = GraphNode("b")
    c = GraphNode("c")
    d = GraphNode("d")
    e = GraphNode("e")
    f = GraphNode("f")
    g = GraphNode("g")

    sn.add_nodes((a, b, c, d, e, f, g))

    sn.add_undirected_edge(a, d)
    sn.add_undirected_edge(a, c)
    sn.add_undirected_edge(a, b)
    sn.add_undirected_edge(b, g)
    sn.add_undirected_edge(d, f)
    sn.add_undirected_edge(d, e)

    pprint(top_three_friends_of_friends(a))
