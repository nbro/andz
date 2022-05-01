#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 09/10/2017

Updated: 11/10/2017

# Description

Approximate value of polynomial at an x-coordinate using the barycentric form.

# TODO

- Add a more detailed description of the barycentric form of the Lagrange
polynomials for polynomial interpolation.

# References

- Dr. prof. Kai Hormann's notes for the Numerical Algorithms course, fall, 2017.
"""

__all__ = ["barycentric"]


def _compute_weights(xs: list) -> list:
    """Computes the weights used in the barycentric form of the Lagrange
    polynomial.

    Time complexity: O(n²)."""
    n = len(xs)
    ws = [1] * n
    for i in range(n):
        for j in range(n):
            if j != i:
                ws[i] *= 1 / (xs[i] - xs[j])
    return ws


def barycentric(xs: list, ys: list, x0: float) -> float:
    """Evaluates the polynomial that interpolates points (xs[i], ys[i]), for
    i=0, ..., len(xs) - 1 == len(ys) - 1, at point x0.

    Time complexity: O(n²)."""
    if len(xs) != len(ys):
        raise ValueError("Lists xs and ys have different lengths.")

    ws = _compute_weights(xs)

    n = 0  # Numerator
    d = 0  # Denominator: sum of all weights.

    for i in range(len(xs)):
        if x0 == xs[i]:
            return ys[i]
        else:
            w = ws[i] / (x0 - xs[i])
            n += w * ys[i]
            d += w
    return n / d
