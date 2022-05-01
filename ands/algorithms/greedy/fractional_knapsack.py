#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 09/07/2015

Updated: 07/03/2018

# Description

The time complexity of the fractional knapsack is O(n * log(n)), because of the
call to sort the items by value/weight ratio.

# TODO

- Add complexity analysis.
- Create a non-interactive version.
"""

import operator

from tabulate import tabulate

__all__ = ["interactive_fractional_knapsack"]


def ask_objects():
    objects = []
    print("Welcome to the Fractional Knapsack problem!\n\n" +
          "You will tell me the objects that you have,\n" +
          "their value and weight.\n\n" +
          "After that, you should also tell me\n"
          "how much weight you can carry with you.\n\n" +
          "I will then tell you which items or\n" +
          "fraction of items you should take.\n")

    input("When you are ready, press ENTER.\n" + "=" * 40 + "\n\n")

    while True:
        name = input("Enter the name of the object: ")
        cost = int(input("Enter the value of " + name + ": "))
        weight = int(input("Enter the weight (in grams) of " + name + ": "))
        objects.append([name, cost, weight])
        yn = input("\nDo you have other items (y/n)? ")

        if yn.lower() in ("n", "no"):
            break
        else:
            print("-" * 40, end="\n\n")

    for obj in objects:
        # Adding as forth property of each object its path_cost/weight ratio.
        obj.append(obj[1] / obj[2])

    objects.sort(key=operator.itemgetter(3), reverse=True)

    print("\n\nThe following are the items that you have:\n")
    print(tabulate(objects, tablefmt="grid",
                   headers=("Name", "Value", "Weight", "Value/Weight Ratio")))
    capacity = int(
        input("\nEnter the maximum weight you can bring (in grams): "))

    return objects, capacity


def output_fractional_knapsack(knapsack_objects, objects):
    s = "You should take "

    for i, item in enumerate(knapsack_objects):

        if not isinstance(item, tuple):
            s += str(objects[item][2]) + " gram(s) of " + objects[item][0]

            if i < len(knapsack_objects) - 1:
                s += ", "
        else:
            s += " and " + str(item[1]) + " gram(s) of " + objects[item[0]][
                0] + "."

    print("\n\n" + s)


def interactive_fractional_knapsack():
    objects, capacity = ask_objects()
    current_weight = 0
    knapsack_objects = []

    for i, obj in enumerate(objects):
        if obj[2] + current_weight <= capacity:
            current_weight += obj[2]
            knapsack_objects.append(i)
        else:
            remaining_weight = capacity - current_weight
            knapsack_objects.append((i, remaining_weight))
            break

    output_fractional_knapsack(knapsack_objects, objects)


if __name__ == "__main__":
    interactive_fractional_knapsack()
