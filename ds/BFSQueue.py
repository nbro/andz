#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: July, 2015

Simple queue data structure used specifically by BFS.
"""


from ands.ds.BaseQueue import *


class BFSQueue(BaseQueue):
    """Queue for the bfs algorihm."""

    def __init__(self):
        BaseQueue.__init__(self, ls=[])

    def _build_str(self):
        return "[" + ", ".join([u.key for u in self.q]) + "]"

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self._build_str()
