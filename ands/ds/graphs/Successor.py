#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 16/03/2022

Updated: 16/03/2022

# Description

# References

"""


class Successor:
    def __init__(self, u: int, w: float = 0.0):
        assert isinstance(u, int) and isinstance(w, float)
        self.u = u
        self.w = w

    def __repr__(self):
        return "{} ({})".format(self.u, self.w)
