#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 24/07/2015

Updated: 19/09/2017

# Description

Consider a set of requests for a room. Only one person can reserve the room at a
time, and you want to allow the maximum number of requests.

The requests for periods (sᵢ=start time for i, fᵢ=finish time for i) are:

    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (3, 8),
    (5, 9),
    (6, 10),
    (8, 11),
    (8, 12),
    (2, 13),
    (12, 14)

Where for example in (1, 4), s₁ = 1 and f₁ = 4. Which ones should we schedule?

We can solve this problem using dynamic programming, but it we can also solve it
using a simple greedy algorithm.

The algorithm consists of basically choosing the next activity with the smallest
finish time. To do this, we need first to sort the activities by finish time.

This algorithm is a top-down algorithm, in the sense that we can start by
choosing an activity, the one with the earliest finish time, and then we can do
the same for the remaining sub-problems.

# TODO

- Add complexity analysis.
"""

import operator


def activity_selector(activities: list) -> list:
    # Sorting activities by finish time, i.e. 2.
    activities.sort(key=operator.itemgetter(2))

    last_selected_activity = activities[0]

    selected_activities = [activities[0]]

    for i in range(1, len(activities)):
        # If the starting time of the ith activity is greater or equal to the
        # ending time of the last selected activity, then add the ith activity
        # to the selected activities.
        if activities[i][1] >= last_selected_activity[2]:
            selected_activities.append(activities[i])
            last_selected_activity = activities[i]

    return selected_activities


if __name__ == "__main__":
    # The first element of each sub-list is the name of the activity.
    # The second element is the starting time. The last element is the end time.
    activities = [["a", 12, 14],
                  ["b", 0, 6],
                  ["c", 2, 13],
                  ["d", 3, 5],
                  ["e", 5, 7],
                  ["f", 1, 4],
                  ["g", 5, 9],
                  ["h", 3, 8],
                  ["i", 12, 14],
                  ["j", 6, 10],
                  ["k", 8, 11]]
    print("Selected activities:", activity_selector(activities))
