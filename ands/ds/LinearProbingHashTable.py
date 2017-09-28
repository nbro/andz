#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 01/06/2015

Updated: 28/09/2017

# Description

## What's a hash map (or hash table)?

A hash map is a data structure which is used to implement the so-called
associative array, which is an abstract data type composed of a collection of
(key, value) pairs, such that each possible key appears at most once in the
collection.

## Hash function

To map keys to values, a hash function is used when implementing a hash map. A
hash function is any function that can be used to map data of arbitrary size to
data of fixed size.

A perfect hash function is a function that assigns each key a unique bucket in
the the data structure, but most hash table designs employ an imperfect hash
function, which might cause hash collisions, where the hash function generates
the same index (i.e. the same position or bucket) for more than one key. Such
collisions must be resolved or accommodated in some way.

## Resolving collisions

There are different ways to resolve collisions, where the most famous techniques
are "separate chaining" and "open addressing".

# TODO

- Add complexity analysis to operations

- No difference between non-existence of a key in the table and existence of a
key with None as associated value: maybe we want to differentiate the two cases?

- Resizing the hash table only whenever we reach a full table may not be the
best option in terms of performance...

- Should a client of this class be able to specify its custom hash function?

- Size could be implemented as a counter.

- Improve is_hash_table function

# References

- http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
- http://stackoverflow.com/questions/279539/best-way-to-remove-an-entry-from-a-hash-table
- http://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-a-list
- http://stackoverflow.com/questions/1541797/check-for-duplicates-in-a-flat-list
- https://en.wikipedia.org/wiki/Associative_array
- https://en.wikipedia.org/wiki/Hash_table
- https://en.wikipedia.org/wiki/Hash_function
- https://en.wikipedia.org/wiki/Linear_probing
- https://en.wikipedia.org/wiki/Open_addressing
"""

from collections import Hashable

from tabulate import tabulate

from ands.ds.HashTable import HashTable

__all__ = ["LinearProbingHashTable", "has_duplicates_ignore_nones",
           "is_hash_table"]


class LinearProbingHashTable(HashTable):
    """Resizable hash table which uses linear probing, which is a specific
    "open addressing" technique, to resolve collisions.

    The process of resizing consists in doubling the current capacity of the
    hash table each time.

    The hash function uses both the Python's built-in hash function and the %
    operator.

    You can access and put an item in the hash table by using the same
    convenient notation that is used by the Python's standard dict class:

        h = LinearProbingHashTable()
        h[12] = 3
        print(h[12])"""

    def __init__(self, capacity: int = 11):
        if not isinstance(capacity, int):
            raise TypeError("capacity must be an instance of int")
        if capacity < 1:
            raise ValueError("capacity must be greater or equal to 1")
        self._n = capacity  # self._n holds the size of the buffers.
        self._keys = [None] * self._n
        self._values = [None] * self._n

    @property
    def size(self) -> int:
        """Returns the number of pairs key-value in this map."""
        assert is_hash_table(self)
        return sum(k is not None for k in self._keys)

    @property
    def capacity(self) -> int:
        """Returns the number of allocated cells in memory."""
        assert is_hash_table(self)
        return len(self._keys)

    @staticmethod
    def _hash_code(key, size: int) -> int:
        """Returns a hash code (an int) between 0 and size (excluded).

        size must be the size of the buffer based on which this function should
        return a hash value."""
        return hash(key) % size

    @staticmethod
    def _rehash(old_hash: int, size: int) -> int:
        """Returns a new hash value based on the previous one called old_hash.

        size must be the size of the buffer based on which we want to have a new
        hash value from the old hash value."""
        return (old_hash + 1) % size

    def put(self, key: object, value: object) -> None:
        """Inserts the pair (key: value) in this map.

        If key is None, a TypeError is raised, because keys cannot be None."""
        assert is_hash_table(self)

        if key is None:
            raise TypeError("key cannot be None.")

        self._put(key, value, self._n)

        assert is_hash_table(self)

    def _put(self, key: object, value: object, size: int) -> None:
        """Helper method of self.put."""
        hash_value = LinearProbingHashTable._hash_code(key, size)

        # No need to allocate new space.
        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = value

        # If self already contains_key key, then its value is overridden.
        elif self._keys[hash_value] == key:
            self._values[hash_value] = value

        # Collision: there's already a (key: value) pair at the slot dedicated
        # to this (key: value) pair, according to the self._hash_code function.
        # We need to _rehash, i.e. find another slot for this (key: value) pair.
        else:
            next_slot = LinearProbingHashTable._rehash(hash_value, size)
            rehashed = False

            while (self._keys[next_slot] is not None and
                           self._keys[next_slot] != key):

                next_slot = LinearProbingHashTable._rehash(next_slot, size)

                # Allocate new buffer of length len(self.keys) * 2 + 1.
                if next_slot == hash_value:
                    rehashed = True

                    keys = self._keys
                    values = self._values

                    new_size = len(self._keys) * 2 + 1
                    self._keys = [None] * new_size
                    self._values = [None] * new_size

                    # Rehashing and putting all elements in the new bigger
                    # buffer.
                    #
                    # Note: the calls to self._put in the following loop will
                    # never reach these statements, because there will be slots
                    # available, and because the way hashing and rehashing is
                    # currently implemented.
                    for k in keys:
                        v = LinearProbingHashTable._get(k, keys, values,
                                                        self._n)
                        self._put(k, v, new_size)

                    # After resizing the buffers, we insert the original
                    # (key: value) pair.
                    self._put(key, value, new_size)
                    self._n = new_size

            # We exited the loop either because we have found a free slot or a
            # slot containing our key, and not after having re-sized the table.
            if not rehashed:
                if self._keys[next_slot] is None:
                    self._keys[next_slot] = key
                    self._values[next_slot] = value
                else:
                    assert self._keys[next_slot] == key
                    self._values[next_slot] = value

    def get(self, key: object) -> object:
        """Returns the value associated with key.

        If key is None, a TypeError is raised, because keys cannot be None."""
        assert is_hash_table(self)

        if key is None:
            raise TypeError("key cannot be None.")
        value = LinearProbingHashTable._get(key, self._keys, self._values,
                                            self._n)

        assert is_hash_table(self)

        return value

    @staticmethod
    def _get(key: object, keys: list, values: list, size: int) -> object:
        """Helper method of self.get."""
        hash_value = LinearProbingHashTable._hash_code(key, size)

        data = None
        stop = False
        found = False
        position = hash_value

        while keys[position] is not None and not found and not stop:

            if keys[position] == key:
                found = True
                data = values[position]
            else:
                # Find a new possible position by rehashing.
                position = LinearProbingHashTable._rehash(position, size)

                # We are at the initial slot, and thus nothing was found.
                if position == hash_value:
                    stop = True

        return data

    def delete(self, key: object) -> object:
        """Deletes the mapping between key and its associated value.

        If there's no mapping, nothing is done."""
        assert is_hash_table(self)

        if key is None:
            raise TypeError("key cannot be None.")
        if not isinstance(key, Hashable):
            raise TypeError("key must be an instance of a hashable type")

        try:
            i = self._keys.index(key)
            v = self._values[i]
            self._keys[i] = self._values[i] = None
            return v
        except ValueError:
            pass
        finally:
            assert is_hash_table(self)

    def show(self) -> None:
        """Prints this hash table in table-like format."""
        c = 0
        data = []
        for i in range(len(self._keys)):
            if self._keys[i] is not None:
                c += 1
                data.append([c, self._keys[i], self._values[i]])
        print(tabulate(data, headers=["#", "Keys", "Values"], tablefmt="grid"))

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __str__(self):
        return str([(k, v) for k, v in zip(self._keys, self._values)
                    if k is not None])

    def __repr__(self):
        return self.__str__()


def has_duplicates_ignore_nones(ls: list) -> bool:
    """Returns true if ls does contain duplicate elements, false otherwise.

    None items in ls are not considered."""
    ls = [item for item in ls if item is not None]
    return len(ls) != len(set(ls))


def is_hash_table(t: HashTable) -> bool:
    """Returns true if t is a valid HashTable, false otherwise."""
    if not isinstance(t, HashTable):
        return False
    if len(t._keys) != len(t._values) or len(t._keys) != t._n:
        return False
    return not has_duplicates_ignore_nones(t._keys)
