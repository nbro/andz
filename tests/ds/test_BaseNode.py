#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Tests for the BaseNode class.
"""

from ands.ds.BaseNode import BaseNode


def test_init():
    try:
        BaseNode(12)
        assert False
    except TypeError:
        pass

    try:
        BaseNode(value=12)
        assert False
    except TypeError:
        pass

    try:
        BaseNode(None, None)
        assert False
    except ValueError:
        pass

    n = BaseNode(12, "Noi")
    assert hash(n) == hash(n.key) + hash(n.value) + id(n)
    assert n.key == 12
    assert n.value == "Noi"
    
    n2 = BaseNode(12, "Noi")
    assert hash(n2) == hash(n2.key) + hash(n2.value) + id(n2)
    assert n2.key == 12
    assert n2.value == "Noi"

    assert n != n2
    
    
if __name__ == "__main__":
    from tools import main
    main(globals().copy(), __name__, __file__)
