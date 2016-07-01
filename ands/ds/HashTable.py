#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: June, 2015

Last update: 21/02/16

Hash table that re-sizes if no more slot is available.
The process of re-sizing doubles the current capacity of the hash table each time (for now).
It uses [linear probing](https://en.wikipedia.org/wiki/Linear_probing) when there's a collision.
The hash function uses both the Python's built-in `hash` function and the `%` operator.
You can access and put an item in the hash table by using the same convinient notation
that is used by the Python's standard `dict` class, that is:

    h = HashTable()
    h[12] = 3
    print(h[12])

## References
- [http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html](http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html)

- [http://stackoverflow.com/questions/279539/best-way-to-remove-an-entry-from-a-hash-table](http://stackoverflow.com/questions/279539/best-way-to-remove-an-entry-from-a-hash-table)
"""


from tabulate import tabulate


__all__ = ["HashTable", "has_duplicates", "find_duplicates"]


class HashTable:

    def __init__(self, capacity: int=11):
        self.n = capacity
        self.keys = [None] * self.n
        self.values = [None] * self.n

    # HASH FUNCTIONS

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

    # PUT

    def put(self, key: object, value: object):
        """Inserts the pair `key`-`value` in this map.

        If `key` is `None`, a `TypeError` is raised,
        because keys cannot be `None`."""
        if key is None:
            raise TypeError("key cannot be None.")

        assert not has_duplicates(self.keys)
        a = self._put(key, value, self.n)
        assert not has_duplicates(self.keys)
        return a

    def _put(self, key, value, size):
        assert not has_duplicates(self.keys), "precondition in _put"

        hash_value = self.hash_code(key, size)

        # No need to allocate new space.
        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
            self.values[hash_value] = value

        # If self already contains key, then its value is overridden.
        elif self.keys[hash_value] == key:
            self.values[hash_value] = value

        # Collision: there's already a key-value pair
        # at the slot dedicated to this key-value pair,
        # according to the self.hash_code function.
        # We need to rehash, i.e. find another slot for this key-value pair.
        else:
            next_slot = self.rehash(hash_value, size)
            rehashed = False

            while self.keys[next_slot] is not None and self.keys[
                    next_slot] != key:

                next_slot = self.rehash(next_slot, size)

                # Allocate new buffer of length len(self.keys)*2 + 1
                if next_slot == hash_value:
                    rehashed = True

                    keys = self.keys
                    values = self.values

                    new_size = len(self.keys) * 2 + 1
                    self.keys = [None] * new_size
                    self.values = [None] * new_size

                    # Reashing and putting all elements again
                    # Note that the following call to self._put
                    # will never reach this statement
                    # because there will be slots available
                    for k in keys:
                        v = self._get(k, keys, values, self.n)
                        self._put(k, v, new_size)

                    self._put(key, value, new_size)
                    self.n = new_size

            # We exited the loop either because
            # we have found a free slot or a slot containing our key.
            # (and not after having re-sized the table!)
            if not rehashed:
                if self.keys[next_slot] is None:
                    self.keys[next_slot] = key
                    self.values[next_slot] = value
                else:
                    assert self.keys[next_slot] == key
                    self.values[next_slot] = value

        if has_duplicates(self.keys):
            find_duplicates(self.keys)

        assert not has_duplicates(self.keys), "postcondition in _put"

    def get(self, key):
        """Returns the value associated with `key`.
        It returns `None` if there's no value associated with `key`.

        If `key` is `None`, a `TypeError` is raised,
        because keys cannot be None."""
        if key is None:
            raise TypeError("key cannot be None.")
        return self._get(key, self.keys, self.values, self.n)

    def _get(self, key, keys, values, size):
        assert not has_duplicates(keys), "precondition in _get"

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

        assert not has_duplicates(keys), "postcondition _get"
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def delete(self, key):
        """Deletes the mapping (if any) between `key`
        and its corresponding associated value.
        If there's no mapping, `None` is returned."""
        try:
            i = self.keys.index(key)
            v = self.values[i]
            self.keys[i] = self.values[i] = None
            return v
        except ValueError:
            return None

    @property
    def size(self):
        """Returns the number of pairs key-value in this map."""
        assert len(self.keys) == len(self.values) == self.n
        return sum(k is not None for k in self.keys)

    @property
    def capacity(self):
        """Returns the size of the internal buffers that store the keys and the values."""
        assert len(self.keys) == len(self.values) == self.n
        return len(self.keys)

    def show(self):
        """Pretty-prints (using `tabulate.tabulate()`) this table."""
        c = 0
        data = []
        for i in range(len(self.keys)):
            if self.keys[i] is not None:
                c += 1
                data.append([c, self.keys[i], self.values[i]])
        print(tabulate(data, headers=["#", "Keys", "Values"], tablefmt="grid"))

    def __str__(self):
        return str([(k, v)
                    for k, v in zip(self.keys, self.values) if k is not None])

    def __repr__(self):
        return self.__str__()


def has_duplicates(ls):
    ls = [item for item in ls if item is not None]
    return len(ls) != len(set(ls))


def find_duplicates(ls):
    return [item for item, count in collections.Counter(
        ls).items() if (count > 1 and item is not None)]
