#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 15/02/16

Base class for all kind of nodes,
assuming they have a key and a value.
"""

class BaseNode:

    def __init__(self, key, value):
        if key is None:
            raise ValueError("key cannot be None.")
        self.key = key
        self.value = value

    def __hash__(self):
        """Returns hash(self.key) + hash(self.value) + id(self)"""
        return hash(self.key) + hash(self.value) + id(self)

    def __str__(self):
        return "{" + str(self.key) + ": " + str(self.value) + "}"
