#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 23/09/2017

Updated: 23/09/2017

# Description

Newton's method is an iterative method that can be used to calculate, e.g., (an
approximation of) the square root of a number or the reciprocal of a number. In
general, it used to find the root of a function. If a problem can be formulated
as a root-finding problem, then Newton's method can potentially be used.

Newton's method, also called the Newton–Raphson method, usually converges much
faster than the linearly convergent methods.

To find a root of f(x) = 0, a starting guess x0 is given, and the tangent line
to the function f at x0 is drawn. The tangent line will approximately follow the
function down to the x-axis toward the root. The intersection point of the line
with the x-axis is an approximate root, but probably not exact if f curves.
Therefore, this step is iterated.

The tangent line at x0 has slope given by the derivative f'(x0). One point on
the tangent line is (x0, f(x0)). The point-slope formula for the equation of a
line is y − f(x0) = f'(x0)(x − x0), so that looking for the intersection point
of the tangent line with the x-axis is the same as substituting y = 0 in the
line:

    f'(x0)(x − x0) = 0 - f(x0) <=>
    f'(x0)(x - x0) = -f(x0) <=>
    x - x0 = -(f(x0) / f'(x0)) <=>
    x = x0 - (f(x0) / f'(x0))

Solving for x gives an approximation for the root, which we call x1. Next, the
entire process is repeated, beginning with x1, to produce x2, and so on,
yielding the following iterative formula:

    x0 = initial guess
    xᵢ₊₁ = xᵢ - (f(xᵢ) / f'(xᵢ)), for i = 0, 1, 2, ...

## Examples

### Example 1

Find the Newton's method formula for the equation f(x) = x³ + x − 1 = 0. We find
f'(x) = 3x² + 1. Then we apply the formula above to this f, so we obtain

    xᵢ₊₁ = xᵢ - (xᵢ³ + xᵢ − 1 / 3xᵢ² + 1) <=>
    xᵢ₊₁ = xᵢ - (xᵢ³ + xᵢ − 1 / 3xᵢ² + 1) <=>
    xᵢ₊₁ = ((3xᵢ² + 1)xᵢ - (xᵢ³ + xᵢ − 1)) / (3xᵢ² + 1) <=>
    xᵢ₊₁ = (3xᵢ³ + xᵢ - xᵢ³ - xᵢ + 1) / (3xᵢ² + 1) <=>
    xᵢ₊₁ = (2xᵢ³ + 1) / (3xᵢ² + 1)

# TODO

- Analysis of the convergence of Newton's method.

# References

- https://en.wikipedia.org/wiki/Newton%27s_method
- Dr. prof. Kai Hormann's notes for the Numerical Algorithms course, fall, 2017.
- Chapter 1 of "Numerical Analysis" (2nd ed.) by Sauer.
"""

__all__ = ["newton"]


def newton(
    x0: float,
    f: callable,
    df: callable,
    max_iter: int = 20,
    tolerance: float = 1e-6,
    epsilon: float = 1e-12,
) -> float:
    """Returns an approximation of the closest root to x0 of f, provided that x0
    is "close enough" to one of the roots of f.

    It returns a "garbage" value if either f does not have roots or Newton's
    method does not converge, given the initial guess x0.

    If f or df are not callable, TypeError is raised."""
    if not callable(f) or not callable(df):
        raise TypeError("f and df must be callable objects.")
    x = x0
    for _ in range(max_iter):

        # We don't want to divide by a too small number.
        if abs(df(x)) < epsilon:
            break

        # Newton's computation.
        x_next = x - f(x) / df(x)

        # If the relative error is smaller than a certain tolerance, we exit the
        # loop and return x_next.
        if abs(x_next - x) < tolerance * abs(x_next):
            x = x_next
            break

        x = x_next
    return x
