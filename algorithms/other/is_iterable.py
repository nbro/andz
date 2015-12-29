#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
"""

def is_iterable(obj):
    """Simple way to check if an object is iterable."""
    try:
        iter(obj)
        return True
    except TypeError:
        return False
