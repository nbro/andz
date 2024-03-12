"""
# Meta-info

Author: Nelson Brochado

Created: 04/08/2018

Updated: 05/08/2018

# Description

Unit tests for the functions in the andz.algorithms.ds.change_making module.
"""

import unittest

from andz.algorithms.dp.change_making import *


class TestChangeMaking(unittest.TestCase):
    """We test both functions change_making and extended_change_making
    together."""

    def test_no_coins(self):
        self.assertRaises(ValueError, change_making, [], 10)
        self.assertRaises(ValueError, extended_change_making, [], 10)

    def test_n_is_negative(self):
        self.assertRaises(ValueError, change_making, [1, 2, 5], -1)
        self.assertRaises(ValueError, extended_change_making, [1, 2, 5], -1)

    def test_some_coin_is_negative(self):
        self.assertRaises(ValueError, change_making, [1, 5, -3], 6)
        self.assertRaises(ValueError, extended_change_making, [1, 5, -3], 6)

    def test_n_is_zero(self):
        self.assertEqual(change_making([7, 2, 5], 0), 0)
        self.assertEqual(extended_change_making([7, 2, 5], 0), [])

    def test_n_is_one(self):
        # Note: the list of coins doesn't contain 1, but the algorithms assume
        # the existence of the denomination 1.
        self.assertEqual(change_making([7, 2, 5], 1), 1)
        self.assertEqual(extended_change_making([7, 2, 5], 1), [1])

    def arbitrary_list_of_coins_and_n(
        self, coins=(1, 2, 5, 10, 20, 50), n=19, optimal=[2, 2, 5, 10]
    ):
        # https://www.sciencedirect.com/science/article/pii/S0195669809001292
        self.assertEqual(change_making(coins, n), len(optimal))
        self.assertEqual(sorted(extended_change_making(coins, n)), optimal)

    def test_1(self):
        self.arbitrary_list_of_coins_and_n()

    def test_2(self):
        # https://www.sciencedirect.com/science/article/pii/S0195669809001292
        self.arbitrary_list_of_coins_and_n((1, 5, 9, 16), 18, [9, 9])
