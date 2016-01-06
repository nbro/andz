#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max_num_dups(A):
    """Find the maximum number of duplicated numbers.

    A must be sorted!!
    """
    m = 0
    c = 1
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            c += 1
        elif c > m:
            m = c
            c = 1
    return m


def test():
    ls = [12, 12, 12, 92, 92]
    print("List:", ls)
    print("Max number of duplicates:", max_num_dups(ls))
    
if __name__ == '__main__':
    test()
