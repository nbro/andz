#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta info

Author: Nelson Brochado

Created: 13/02/2017

Updated: 14/02/2017

# Description

Since a hash table (or map) can be implemented in many ways,
mostly because these ways reflect the way collisions are handled,
where the most famous techniques are **separate chaining** and **open addressing**,
I decided to create this abstract class from which all implementations should derive,
and they should all implement at least two methods: put and get.

# References

- [http://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python](http://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python)

"""

from abc import ABCMeta, abstractmethod


class HashTable(metaclass=ABCMeta):
    """Abstract class from which classes such as LinearProbingHashTable derive."""

    @abstractmethod
    def put(self, key: object, value: object) -> None:
        pass

    @abstractmethod
    def get(self, key: object) -> None:
        pass
