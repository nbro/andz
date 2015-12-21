#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 14/10/2017

Updated: 26/10/2017

# Description

An implementation of the gradient descent method for finding local minima of
single-variable functions.

# References

- https://en.wikipedia.org/wiki/Gradient_descent
"""

__all__ = ["gradient_descent"]


def gradient_descent(
    x0: float,
    df: callable,
    step_size: float = 0.01,
    max_iter: int = 100,
    tol: float = 1e-6,
):
    """Finds a local minimum of a function whose derivative is df starting from
    an initial guess x0 using a step size = step_size."""
    if not callable(df):
        raise TypeError("df must be a callable object.")

    x = x0

    for i in range(max_iter):
        x_next = x - step_size * df(x)  # Gradient descent step.

        if abs(x_next - x) < tol * abs(x_next):
            x = x_next
            break

        x = x_next

    return x
