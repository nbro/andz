#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 16/03/2022

Updated: 16/03/2022

# Description

# References

"""


class Edge:
    def __init__(self, v: int, u: int, w: float = 0.0):
        assert isinstance(v, int) and isinstance(u, int)
        assert isinstance(w, (int, float))
        self.v = v
        self.u = u
        self.w = w

    def __repr__(self):
        return "({}, {}, {})".format(self.v, self.u, self.w)
