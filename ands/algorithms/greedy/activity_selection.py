#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Consider a set of requests for a room.

Only one person can reserve the room at a time,
and you want to allow the maximum number of requests.

The requests for periods (si=start time for i, fi=finish time for i) are:

(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)

Where for example in (1, 4), s1 = 1 and f1 = 4.

Which ones should we schedule?

We can solve this problem using dynamic programming,
but it we can also solve it using a simple greedy algorithm.

The algorithm consists of basically choosing the next activity
with the smallest finish time.
So, to do this, we need first to sort the activities by finish time.
This algorithm is a top-down algorithm,
in the sense that we can start by choosing an activity,
the one with the earliest finish time,
and then we can do the same for the remaining sub-problems.
"""

import operator

from tabulate import tabulate

activities = [["a", 12, 14], ["b", 0, 6], ["c", 2, 13], ["d", 3, 5],
              ["e", 5, 7], ["f", 1, 4], ["g", 5, 9], ["h", 3, 8],
              ["i", 12, 14], ["j", 6, 10], ["k", 8, 11]]


def ask_activities():
    print("Welcome to the Activity Selection problem!\n\n" +
          "You tell me your activities and their starting\n" +
          "and ending times, and I will tell you which\n" +
          "activities are compatible, and should take place.")

    print("=" * 48, end="\n\n")
    activities.clear()

    while True:
        name = input("Enter name of the activity: ")
        starting_time = int(input("Enter the starting time of " + name + ": "))
        ending_time = int(input("Enter the ending time of " + name + ": "))
        activities.append([name, starting_time, ending_time])

        a = input("\nType q if you don't have more activities: ")

        if a.lower() == "q":
            break
        else:
            print("-" * 48, end="\n\n")


def activity_selector(activities, verbose=True):
    # sorting activities by finish time
    activities.sort(key=operator.itemgetter(2))

    if verbose:
        print("\nAll activities ordered by finish time:")
        print(tabulate(activities,
                       headers=(
                           "Activity's Name",
                           "Starting Time",
                           "Ending Time"),
                       tablefmt="grid"))

    last_selected_activity = activities[0]

    selected_activities = [activities[0]]

    for i in range(1, len(activities)):
        # if the starting time of the ith activity
        # is greater or equal to the ending time
        # of the last selected activity
        # then add the ith activity to the selected activities.
        if activities[i][1] >= last_selected_activity[2]:
            selected_activities.append(activities[i])
            last_selected_activity = activities[i]

    if verbose:
        print("\n\nYou should schedule your activities in the following way:")
        print(tabulate(selected_activities,
                       headers=(
                           "Activity's Name",
                           "Starting Time",
                           "Ending Time"),
                       tablefmt="grid"))

    return selected_activities


if __name__ == "__main__":
    # ask_activities()  # uncomment this line if you want to choose your
    # activities manually
    sa = activity_selector(activities)
    print(sa)
