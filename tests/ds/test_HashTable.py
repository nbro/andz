#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 21/02/16

Last update: 28/08/16

Test the HashTable class.
"""

import string
import unittest
from random import sample, randint, uniform, choice

from ands.ds.HashTable import HashTable, has_duplicates


def gen_rand_str(size):
    return "".join(choice(string.printable) for _ in range(size))


def put_and_get_numbers(random_func=randint, n=100):
    t = HashTable()

    a = [random_func(-100, 100) for _ in range(100)]
    p = None

    def find_all_indices(a, ls):
        return [i for i, item in enumerate(ls) if item == a]

    for i in range(1, n + 1):
        for _, num in enumerate(a):

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


class TestHashTable(unittest.TestCase):

    def test_put_and_get_1(self):
        """Testing that errors are raised."""
        t = HashTable()
        try:
            t.put(None, 12)
            assert False
        except TypeError:
            pass

        try:
            t.get(None)
            assert False
        except TypeError:
            pass

    def test_put_and_get_2(self, n=100):
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

    def test_put_and_get_3(self, n=100):
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

    def test_put_and_get_ints(self):
        put_and_get_numbers()

    def test_put_and_get_floats(self):
        put_and_get_numbers(uniform)

    def test_put_and_get_strings(self, n=100):
        """Test adding different permutations of a list of the same strings."""
        t = HashTable()
        a = [gen_rand_str(10) for _ in range(100)]
        p = None

        for i in range(1, n + 1):
            for j, string in enumerate(a):
                if i == 1:
                    assert t.get(string) is None
                    assert p is None
                else:
                    assert p is not None
                    assert t.get(string) == (i - 1) + p.index(string)

                t.put(string, i + j)

            p = a
            a = sample(a, len(a))

            assert t.size == len(a)
            assert not has_duplicates(t.keys)

        for i, string in enumerate(a):
            assert t.get(string) == p.index(string) + n
            assert t.size == len(a)
            assert not has_duplicates(t.keys)

    def test_put_and_get_non_hashable_type(self):
        t = HashTable()

        def put_type_error(a):
            try:
                t.put(a, 12)
                assert False
            except TypeError:
                pass

        def get_type_error(a):
            t.put(12, "Noi")
            try:
                t.get(a)
                assert False
            except TypeError:
                pass

        put_type_error([])
        put_type_error({})
        get_type_error({})
        get_type_error({})

    def test_delete_letters(self, n=100):
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

    def test_empty_hash_table_capacity(self):
        h = HashTable()
        assert h.capacity == 11
        assert h.size == 0

        h = HashTable(capacity=47)
        assert h.capacity == 47
        assert h.size == 0


if __name__ == "__main__":
    unittest.main(verbosity=2)
