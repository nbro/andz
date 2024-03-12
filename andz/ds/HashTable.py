#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 13/02/2017

Updated: 06/04/2018

# Description

Since a hash table (or map) can be implemented in many ways, mostly because
these ways reflect the way collisions are handled, where the most famous
techniques are "separate chaining" and "open addressing", it is convenient to
have this abstract class from which all implementations should derive, and they
should all implement at least two methods: put and get.

# References

- https://stackoverflow.com/q/13646245/3924118
"""

from abc import ABC, abstractmethod

__all__ = ["HashTable"]


class HashTable(ABC):
    """Abstract class from which classes such as LinearProbingHashTable
    derive."""

    @abstractmethod
    def put(self, key: object, value: object) -> None:
        """
        Add the key: value pair to the hash table.
        """

    @abstractmethod
    def get(self, key: object) -> object:
        """
        Get the value associated with the key.
        """
