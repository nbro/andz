#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/16


Disjoint Set data structure for Kruskal's algorithm
to find a minimum-spanning tree of a undirected weighted graph.
"""

class SetElement:
    def __init__(self, value):
        self.value = value
        self.r = None

    @property
    def representative(self):
        return self.r

    @representative.setter
    def representative(self, new_representative):
        if self.r is None or new_representative != self.r:
            self.r = new_representative

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value) + " => " + str(self.r)

    def __eq__(self, other):
        """:type other SetElement"""
        return self.value == other.value

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.value)


class Set:
    def __init__(self):
        self.set = set()
        self.r = None

    @property
    def representative(self):
        return self.r

    @representative.setter
    def representative(self, new_representative: SetElement):
        if self.representative is None or self.representative != new_representative:
            self.r = new_representative

    def add(self, set_element: SetElement):
        """Adds a new SetElement to self"""
        # set_element becomes the representative of self
        self.representative = set_element
        self.set.add(set_element)
        self.update_representatives()

    def update_representatives(self):
        """Updates the representative reference of all items in self.set"""
        for set_element in self.set:
            set_element.representative = self.representative

    def union(self, other_set):
        for set_element in other_set.set:
            if set_element not in self.set:
                self.add(set_element)
        return self.representative

    def __repr__(self):
        return str(self.set)

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        return iter(self.set)


class SameSetException(Exception):
    pass


class DisjointSet:
    def __init__(self):
        # keys = representatives
        # values = sets
        self.ds = {}

    def create_set(self, set_element: SetElement):
        s = Set()
        s.add(set_element)  # s contains just one SetElement object!
        self.ds[s.representative] = s

    def show(self, message="", end=""):
        print(message, end=end)
        for representative in self.ds.keys():
            print(self.ds[representative], "=>", representative)

    @staticmethod
    def find_set(set_element: SetElement):
        """set_element must be an object of type SetElement"""
        return set_element.representative

    def merge_sets(self, se1, se2, raise_error=True):
        """set_element1 and set_element2 must belong to sets already in self.
        If set_element1 and set_element2 belong to the same set,
        a SameSetException is raised."""
        repr1 = DisjointSet.find_set(se1)
        repr2 = DisjointSet.find_set(se2)

        if repr1 != repr2 and repr1 in self.ds.keys() and repr2 in self.ds.keys():
            new_representative = self.ds[repr1].union(self.ds.pop(repr2))
            self.ds[new_representative] = self.ds.pop(repr1)

            return new_representative

        elif raise_error:
            raise SameSetException(str(se1.value) + " and " + str(se2.value) + " cannot belong to the same set.")

    def __str__(self):
        return str(self.ds)

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    ds = DisjointSet()

    se1 = SetElement(12)
    se2 = SetElement(14)
    se3 = SetElement(28)
    se4 = SetElement(10)

    a = SetElement(12)
    ds.create_set(a)

    # print(a == se1)

    elements = [se1, se2, se3, se4]

    for i in elements:
        ds.create_set(i)

    ds.show(message="Disjoint Set", end="\n")

    ds.merge_sets(se1, se2)
    ds.show(message="Disjoint Set", end="\n")

    ds.merge_sets(se1, se3)
    ds.show(message="Disjoint Set", end="\n")

    ds.merge_sets(se1, se4)

    ds.show(message="Disjoint Set", end="\n")
