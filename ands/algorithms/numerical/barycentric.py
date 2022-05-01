#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 09/10/2017

Updated: 02/04/2018

# Description

Given a set P = {(x₁, y₁), ..., (xᵢ, yᵢ)} of 2-dimensional points, then the
so-called problem of "polynomial interpolation" consists in finding the
polynomial of smallest degree which goes through these points, that is, a
polynomial which "interpolates" these points.

# References

- Dr. prof. Kai Hormann's notes for the Numerical Algorithms course, fall, 2017.
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.barycentric_interpolate.html
- https://en.wikipedia.org/wiki/Lagrange_polynomial
"""

__all__ = ["barycentric", "compute_weights"]


def compute_weights(xs: list) -> list:
    """Computes and returns the weights (as a list) used in the barycentric form
    of the Lagrange polynomial.

    This function avoids checking if the input list xs is well-formed for
    performance reasons.

    Time complexity: O(n²)."""
    n = len(xs)
    ws = [1] * n
    for i in range(n):
        for j in range(n):
            if j != i:
                ws[i] *= 1 / (xs[i] - xs[j])
    return ws


def barycentric(xs: list, ys: list, x0: float, ws: list = None) -> float:
    """Evaluates, at x coordinate x0, the polynomial that interpolates 2d points
    (xs[i], ys[i]), for i=0, ..., len(xs) - 1 == len(ys) - 1. In other words,
    this function returns the y value corresponding to the x coordinate x0 of
    the polynomial which interpolates the points (xs[i], ys[i]).

    For reasons of numerical stability, this function does not compute the
    coefficients of the polynomial.

    This function uses a "barycentric interpolation" method that treats the
    problem as a special case of rational function interpolation. This algorithm
    is quite stable, numerically, but even in a world of exact computation,
    unless the x coordinates are chosen very carefully, polynomial interpolation
    itself is a very ill-conditioned process due to the Runge phenomenon.

    The construction of the interpolation weights is a relatively slow process:
    it takes O(n²) time. If you want to call this many times with the same x
    coordinates (but possibly varying the corresponding y values or x0), you can
    first calculate the weights, using e.g. the function compute_weights in this
    same module, and then pass them as the parameter ws. If ws is None, then the
    weights are computed by this function at every call. If ws is not None, it
    should be a list of the same length as xs and ys and should clearly
    represent the weights as computed by the function compute_weights in this
    same module.

    Time complexity: O(n²), if ws is None, else O(n)."""
    if len(xs) != len(ys):
        raise ValueError("Lists xs and ys have different lengths.")

    if ws is None:
        ws = compute_weights(xs)
    else:
        if len(xs) != len(ws):
            raise ValueError("Lists xs and ws have different lengths.")

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
