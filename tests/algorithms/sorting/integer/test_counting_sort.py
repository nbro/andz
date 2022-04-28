#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 03/03/2022

Updated: 07/03/2022

# Description

Unit tests for the functions in the
ands.algorithms.sorting.integer.counting_sort module.
"""

import random
import string
import unittest

from ands.algorithms.sorting.integer.counting_sort import counting_sort
from tests.algorithms.sorting.base_tests import SortingAlgorithmTests


def gen_random_string(k=5):
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=k))


def gen_random_key_indexed_list(n=100, a=0, b=1000):
    return [(random.randint(a, b), gen_random_string()) for _ in range(n)]


def make_test(sedgewick_wayne=False):
    class TestCountingSort(unittest.TestCase, SortingAlgorithmTests):
        def __init__(self, method_name="__init__"):
            unittest.TestCase.__init__(self, method_name)
            SortingAlgorithmTests.__init__(self,
                                           counting_sort,
                                           in_place=False,
                                           start=0,
                                           end=10000)

        def test_raises_when_not_all_int(self):
            self.assertRaises(TypeError, self.sorting_algorithm, [1, "1"],
                              sedgewick_wayne=sedgewick_wayne)

        def test_raises_when_k_is_not_non_negative(self):
            self.assertRaises(ValueError, self.sorting_algorithm, [1], -1,
                              sedgewick_wayne=sedgewick_wayne)

        def test_raises_when_not_all_elements_are_less_than_k(self):
            self.assertRaises(ValueError, self.sorting_algorithm, [10, 1], 3,
                              sedgewick_wayne=sedgewick_wayne)

        def test_raises_when_not_all_elements_are_non_negative(self):
            self.assertRaises(ValueError, self.sorting_algorithm, [10, -1],
                              sedgewick_wayne=sedgewick_wayne)

        def test_raises_when_key_is_not_callable(self):
            self.assertRaises(TypeError, self.sorting_algorithm, [3, 2], key=3,
                              sedgewick_wayne=sedgewick_wayne)

        def test_raises_when_bad_key(self):
            class A:
                def __init__(self, y=2):
                    self.y = y

            self.assertRaises(KeyError, self.sorting_algorithm,
                              [A(), ("zero", 0)], key=lambda x: x.y,
                              sedgewick_wayne=sedgewick_wayne)

        def test_raises_when_non_int_key(self):
            self.assertRaises(TypeError, self.sorting_algorithm,
                              [("zero", 0), ("one", 1)], key=lambda x: x[0],
                              sedgewick_wayne=sedgewick_wayne)

        def test_key_indexed_list(self):
            a = gen_random_key_indexed_list()
            key = lambda x: x[0]
            b = self.sorting_algorithm(a, key=key)
            b1 = sorted(a, key=key)

            # Python's sorted is guaranteed to be stable. If that wasn't the
            # case, we couldn't use it to test the correctness of counting
            # sort.
            # https://stackoverflow.com/q/1915376/3924118
            assert b == b1

    return TestCountingSort


test_sw_counting_sort = make_test(sedgewick_wayne=True)
test_counting_sort = make_test(sedgewick_wayne=False)

if __name__ == '__main__':
    unittest.main()
