#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 21/02/16

Test the HashTable class.
"""

import string
import collections
from random import sample, shuffle, randint, uniform
from ands.ds.HashTable import HashTable, has_duplicates, find_duplicates


def test_put_and_get_1():
    """Testing that errors are raised."""
    t = HashTable()
    try:
        t.put(None)
        assert False
    except TypeError:
        pass

    try:
        t.get(None)
        assert False
    except TypeError:
        pass
        
def test_put_and_get_2(n=100):
    """Testing that the same elements inserted
    multiple times in the same order,
    but always with different values associated with them."""
    t = HashTable()
    ls = list(string.ascii_lowercase)

    for i in range(1, n + 1):        
        for j, letter in enumerate(ls):

            if i == 1:
                assert t.get(letter) is None
            else:
                assert t.get(letter) == (i - 1) + j

            t.put(letter, i + j)

        assert t.size == len(ls)
        assert not has_duplicates(t.keys)

    for i, letter in enumerate(ls):
        assert t.get(letter) == ls.index(letter) + n
        assert t.size == len(ls)
        assert not has_duplicates(t.keys)        
            
def test_put_and_get_3(n=100):
    """Testing insertion of permutations of the same items
    and possibly different values associated with them."""
    t = HashTable()
    a = list(string.printable)
    
    p = None
    a = sample(a, len(a))

    for i in range(1, n + 1):        
        for j, letter in enumerate(a):

            if i == 1:
                assert t.get(letter) is None
                assert p is None
            else:
                assert p is not None
                assert t.get(letter) == (i - 1) + p.index(letter)

            t.put(letter, i + j)
            
        p = a
        a = sample(a, len(a))

        assert t.size == len(a)
        assert not has_duplicates(t.keys)

    for i, letter in enumerate(a):
        assert t.get(letter) == p.index(letter) + n
        assert t.size == len(a)
        assert not has_duplicates(t.keys)

def put_and_get_floats(random_func=randint, n=100):
    t = HashTable()
    
    a = [random_func(-100, 100) for _ in range(100)]
    p = None

    def find_all_indices(a, ls):
        return [i for i, item in enumerate(ls) if item == a]
    
    for i in range(1, n + 1):
        for j, num in enumerate(a):

            if i == 1:
                assert p is None
            else:
                assert p is not None
                try:
                    find_all_indices(num, p).index(t.get(num))
                except ValueError:
                    find_all_indices(num, a).index(t.get(num))
                    
            t.put(num, a.index(num))
            
        p = a
        a = sample(a, len(a))
        assert not has_duplicates(t.keys)

    for i, num in enumerate(a):
        try:
            find_all_indices(num, p).index(t.get(num))
        except ValueError:
            find_all_indices(num, a).index(t.get(num))
        assert not has_duplicates(t.keys)

def test_put_and_get_4():
    put_and_get_floats()

def test_put_and_get_5():
    put_and_get_floats(uniform)

def test_put_and_get_6():
    """Test adding strings"""
    pass

def test_delete(n=100):
    t = HashTable()
    ls = list(string.ascii_lowercase)

    for i in range(1, n + 1):        
        for j, letter in enumerate(ls):
            if i == 1:
                assert t[letter] is None
            else:
                assert t[letter] == (i - 1) + j
            t[letter] = i + j
        assert t.size == len(ls)
        assert not has_duplicates(t.keys)

    for i, letter in enumerate(ls):
        assert t[letter] == ls.index(letter) + n
        assert t.size == len(ls)
        assert not has_duplicates(t.keys)

    for i, letter in enumerate(ls):
        v = t.delete(letter)
        assert v is not None
        assert not has_duplicates(t.keys)
        assert t.size == len(ls) - (i + 1)

    assert t.size == 0
    assert not has_duplicates(t.keys)

def test_empty_hash_table_capacity():
    h = HashTable()
    assert h.capacity == 11

    h = HashTable(capacity=47)
    assert h.capacity == 47

        
if __name__ == "__main__":
    from tools import main
    main(globals().copy(), __name__, __file__)
