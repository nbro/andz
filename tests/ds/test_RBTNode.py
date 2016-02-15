#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 15/02/16

Tests for the RBTNode class.
"""

from ands.ds.RBTNode import *


def test_None():
    try:
        RBTNode(None)
        assert False
    except ValueError:
        pass

def test_init():
    n = RBTNode(12)
    assert n.key == 12 and not n.value
    assert n.color == BLACK
    n.color = RED
    assert n.color == RED
    assert not n.parent and not n.left and not n.right
    n.reset()
    assert n.color == BLACK


if __name__ == "__main__":
    from tools import main
    main(globals().copy(), __name__, __file__)
