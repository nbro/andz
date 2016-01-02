#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

A very simple example of recursion: factorial

Resources:

- http://www.math.uah.edu/stat/foundations/Structures.html#com2
"""

def factorial(n):
    """Returns the factorial of n.
    Assumes that n >= 0"""
    if n == 0:
        return 1
    elif n == 1 or n == 2:
        return n
    else:
        return n * factorial(n - 1)

def n_choose_k(n, k):
    """'n choose k' returns you the number of ways
    of choosing k elements, disregarding their order,
    from a set of n elements."""
    if n >= 0 and k >= 0:
        if n == k or k == 0:
            return 1
        if k > n:
            return 0

    if n >= 0 and k < 0:
        return 0
    
    return factorial(n) / (factorial(k) * factorial(n - k))

def n_choose_k_2(n, k):
    """n choose k can be recursively defined as:
    'n - 1 choose k - 1' + 'n - 1 choose k',
    for all integers n and k, such that 1 <= k <= n - 1.

    Proof:
    Suppose that we have n persons, one named Fred,
    and that we want to select a committee of size k.
    There are 'n choose k' different committees.
    On the other hand, there are 'n - 1 choose k - 1' committees
    with Fred as a member, and 'n - 1 choose k' committees
    without Fred as a member.
    The sum of these two numbers is also the number of committees.    
    """
    return n_choose_k(n - 1, k - 1) + n_choose_k(n - 1, k)

def n_choose_k_3(n, k):
    """Proof this formula is equivalent to the one in n_choose_k:

    Note that if we select a subset of size k
    from a set of size n, then we leave a subset
    of size n − k behind (the complement).
    Thus A -> A^c is a one-to-one correspondence
    between subsets of size k and subsets of size n − k."""
    return n_choose_k(n, n - k)

def a_plus_b_all_to_n(a, b, n):
    """Solve polynomials of the form (a + b)^n"""
    s = 0
    for k in range(0, n + 1):
        s += n_choose_k(n, k) * (a**k) * (b**(n - k))
    return s

def sum_first_m_pos_nat_nums(m):
    """Sum first m natural numbers (starting from 1).

    sum_{j=1}^{m} j = 'm + 1 choose 2' = ((m + 1)*m)/(2)"""
    return n_choose_k_2(m + 1, 2)


def sum_first_m_pos_nat_nums_2(m):
    """Sum first m natural numbers (starting from 1).

    sum_{j=1}^{m} j = 'm + 1 choose 2' = ((m + 1)*m)/(2)"""
    return ((m + 1)*m)/(2)
    
def sum_first_m_pos_nat_nums_3(m):
    """Sum first m natural numbers (starting from 1).

    sum_{j=1}^{m} j = 'm + 1 choose 2' = ((m + 1)*m)/(2)"""
    s = 0
    for i in range(m):
        s += (i + 1)
    return s

        
if __name__ == "__main__":
    for i in range(10):
        print(factorial(i))

    print(factorial(8))
    print(factorial(12))
    
    print(n_choose_k(5, 5))
    print(n_choose_k(5, 0))
    print(n_choose_k(5, 2))
    print(n_choose_k_2(5, 2))
    print(n_choose_k_3(5, 2))
    
    print(a_plus_b_all_to_n(2, 3, 2))
    
    print(sum_first_m_pos_nat_nums(1))
    print(sum_first_m_pos_nat_nums_2(1))
    print(sum_first_m_pos_nat_nums_3(1))
    
    print(sum_first_m_pos_nat_nums(0))    
    print(sum_first_m_pos_nat_nums_2(0))    
    print(sum_first_m_pos_nat_nums_3(0))    

    print(sum_first_m_pos_nat_nums(10))
    print(sum_first_m_pos_nat_nums_2(10))
    print(sum_first_m_pos_nat_nums_3(10))
