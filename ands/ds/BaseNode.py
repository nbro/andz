#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Base class for all kind of nodes,
assuming they have a key and a value.
"""


class BaseNode:

    """Base class for all kind of nodes,
    assuming they have a key and a value."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __hash__(self):
        """Returns hash(self.key) + hash(self.value) + id(self)"""
        return hash(self.key) + hash(self.value) + id(self)

    def __str__(self):
        return "{" + str(self.key) + ": " + str(self.value) + "}"
