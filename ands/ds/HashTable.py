#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 01/06/2015

Updated: 13/02/2017

# Description

Hash table that re-sizes if no more slots are available.
The process of re-sizing doubles the current capacity of the hash table each time (for now).
It uses [linear probing](https://en.wikipedia.org/wiki/Linear_probing) when there's a collision.
The hash function uses both the Python's built-in `hash` function and the `%` operator.
You can access and put an item in the hash table by using the same convenient notation
that is used by the Python's standard `dict` class, that is:

    h = HashTable()
    h[12] = 3
    print(h[12])

# References

- [http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html](http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html)
- [http://stackoverflow.com/questions/279539/best-way-to-remove-an-entry-from-a-hash-table](http://stackoverflow.com/questions/279539/best-way-to-remove-an-entry-from-a-hash-table)
- [http://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-a-list](http://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-a-list)
- [http://stackoverflow.com/questions/1541797/check-for-duplicates-in-a-flat-list](http://stackoverflow.com/questions/1541797/check-for-duplicates-in-a-flat-list)

"""

from collections import Counter

from tabulate import tabulate

__all__ = ["HashTable", "has_duplicates_ignore_nones", "find_duplicates_ignore_nones"]


class HashTable:
    def __init__(self, capacity: int = 11):
        assert isinstance(capacity, int)
        self._n = capacity
        self._keys = [None] * self._n
        self._values = [None] * self._n

    @property
    def size(self):
        """Returns the number of pairs key-value in this map."""
        assert len(self._keys) == len(self._values) == self._n
        return sum(k is not None for k in self._keys)

    @property
    def capacity(self):
        """Returns the size of the internal buffers that store the keys and the values."""
        assert len(self._keys) == len(self._values) == self._n
        return len(self._keys)

    def hash_code(self, key, size: int) -> int:
        """Returns a hash code (an int) between 0 and `size` (excluded).

        `size` must be the size of the buffer based on which
        this function should return a hash value."""
        return hash(key) % size

    def rehash(self, old_hash: int, size: int) -> int:
        """Returns a new hash value based on the previous one called `old_hash`.

        `size` must be the size of the buffer based on which
        we want to have a new hash value from the old hash value."""
        return (old_hash + 1) % size

    def put(self, key: object, value: object) -> None:
        """Inserts the pair `key`/`value` in this map.

        If `key` is `None`, a `TypeError` is raised, because keys cannot be `None`."""
        if key is None:
            raise TypeError("key cannot be None.")

        assert not has_duplicates_ignore_nones(self._keys)
        self._put(key, value, self._n)
        assert not has_duplicates_ignore_nones(self._keys)

    def _put(self, key: object, value: object, size: int) -> None:
        """Helper method of `self.put` and thus it's considered PRIVATE."""

        assert not has_duplicates_ignore_nones(self._keys)

        hash_value = self.hash_code(key, size)

        # No need to allocate new space.
        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = value

        # If self already contains key, then its value is overridden.
        elif self._keys[hash_value] == key:
            self._values[hash_value] = value

        # Collision: there's already a key-value pair
        # at the slot dedicated to this key-value pair,
        # according to the self.hash_code function.
        # We need to rehash, i.e. find another slot for this key-value pair.
        else:
            next_slot = self.rehash(hash_value, size)
            rehashed = False

            while self._keys[next_slot] is not None and self._keys[next_slot] != key:

                next_slot = self.rehash(next_slot, size)

                # Allocate new buffer of length len(self.keys)*2 + 1
                if next_slot == hash_value:
                    rehashed = True

                    keys = self._keys
                    values = self._values

                    new_size = len(self._keys) * 2 + 1
                    self._keys = [None] * new_size
                    self._values = [None] * new_size

                    # Rehashing and putting all elements again
                    # Note that the following call to self._put
                    # will never reach this statement
                    # because there will be slots available
                    for k in keys:
                        v = self._get(k, keys, values, self._n)
                        self._put(k, v, new_size)

                    self._put(key, value, new_size)
                    self._n = new_size

            # We exited the loop either because
            # we have found a free slot or a slot containing our key.
            # (and not after having re-sized the table!)
            if not rehashed:
                if self._keys[next_slot] is None:
                    self._keys[next_slot] = key
                    self._values[next_slot] = value
                else:
                    assert self._keys[next_slot] == key
                    self._values[next_slot] = value

        assert not has_duplicates_ignore_nones(self._keys)

    def get(self, key: object) -> object:
        """Returns the value associated with `key`.

        If `key` is `None`, a `TypeError` is raised, because keys cannot be None."""
        if key is None:
            raise TypeError("key cannot be None.")
        return self._get(key, self._keys, self._values, self._n)

    def _get(self, key: object, keys: list, values: list, size: int) -> object:
        """Helper method of `self.get` and thus it's considered PRIVATE."""
        assert not has_duplicates_ignore_nones(keys)

        hash_value = self.hash_code(key, size)

        data = None
        stop = False
        found = False
        position = hash_value

        while keys[position] is not None and not found and not stop:

            if keys[position] == key:
                found = True
                data = values[position]
            else:
                # Find a new possible position by rehashing
                position = self.rehash(position, size)

                # We are at the initial slot,
                # and thus nothing was found.
                if position == hash_value:
                    stop = True

        assert not has_duplicates_ignore_nones(keys)
        return data

    def delete(self, key) -> object:
        """Deletes the mapping between `key` and its corresponding associated value.
        If there's no mapping, nothing is done."""
        try:
            i = self._keys.index(key)
            v = self._values[i]
            self._keys[i] = self._values[i] = None
            return v
        except ValueError:
            pass

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
        return str([(k, v) for k, v in zip(self._keys, self._values) if k is not None])

    def __repr__(self):
        return self.__str__()


def has_duplicates_ignore_nones(ls: list) -> bool:
    """Returns `True` if `ls` does contain duplicate elements, `False` otherwise.

    None items in `ls` are not considered."""
    ls = [item for item in ls if item is not None]
    return len(ls) != len(set(ls))


def find_duplicates_ignore_nones(ls: list) -> list:
    """"Returns a list with the items from `ls` which appear more than once in the same list.

    None items in `ls` are ignored in this procedure."""
    return [item for item, count in Counter(ls).items() if (count > 1 and item is not None)]
