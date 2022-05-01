#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 10/09/2016

Updated: 07/03/2018

# Description

The forward Euler's method is the easiest method for approximately solving an
initial value ODE problem. In practice, it's used as a vehicle for studying
several important and basic notions on numerical ODE methods.

## Euler's method derivation

We first consider finding an approximate solution for a scalar initial value ODE
problem at equidistant abscissae. Thus, we define the points:

    t₀ = a

    tᵢ = a + i * h,

where h = (b - a) / N is the step size, for i = 0, 1, 2, ... N. t here is called
an "independent variable", a and b are respectively the beginning and end of the
interval at which we're trying to numerical approximate y(t).

We denote the approximate solution to y(tᵢ) by yᵢ.
Note: in general, the step size h could be variable, i.e. we could have a hᵢ,
but we keep it constant in this explanation and implementation.

Consider the following "forward difference" formula:

    y'(tᵢ) = (y(tᵢ₊₁) - y(tᵢ)) / h - h / 2 * y''(Ζᵢ)

By the ODE, y'(tᵢ) = f(tᵢ, y(tᵢ)). So, we manipulate the expression above to
have y(tᵢ₊₁) isolated in one side. We start by multiplying both sides by h:

    h * y'(tᵢ) = y(tᵢ₊₁) - y(tᵢ) - (h² / 2 * y''(Ζᵢ))

or, if we rearrange the entries,

    h * y'(tᵢ) + y(tᵢ) + (h² / 2 * y''(Ζᵢ)) = y(tᵢ₊₁)

we further rearrange the entries so that what we're looking for is on the left
side of the equals:

    y(tᵢ₊₁) = y(tᵢ) + h * y'(tᵢ) + (h² / 2 * y''(Ζᵢ))

and we replace y'(tᵢ) by f(tᵢ, y(tᵢ))

    y(tᵢ₊₁) = y(tᵢ) + h * f(tᵢ, y(tᵢ)) + (h² / 2 * y''(Ζᵢ))

dropping the truncation term, i.e. (h² / 2 * y''(Ζᵢ)), we obtain the forward
Euler method, which defines the approximate solution (yᵢ){ᵢ₌₀}^{N} by:

    y₀ = c

where c is the initial value.

    y(tᵢ₊₁) = y(tᵢ) + h * f(tᵢ, y(tᵢ))

for i = 0, ..., N - 1.

This simple formula allow us to march forward into t.

### Notes

In the following implementation, we assume that f and all other parameters are
specified.

## Explicit vs Implicit methods

What happens if we replace the forward difference formula by the backward
formula

    y'(tᵢ₊₁) ~ (y(tᵢ₊₁) - y(tᵢ)) / h

and this leads similarly to the backward Euler method:

    y₀ = c
    yᵢ₊₁ = yᵢ + h * f(tᵢ₊₁, yᵢ₊₁)

for i = 0, ..., N - 1.

There's actually a big difference between this new method and the previous one.
This one to calculate yᵢ₊₁ depends implicitly on yᵢ₊₁ itself.

In general, if a method to calculate yᵢ₊₁ depends implicitly on yᵢ₊₁, it's
called an implicit method, whereas the forward method is considered a explicit
method.

# References

- First Course in Numerical Methods, chapter 16, by Uri M. Ascher and C. Greif
- https://www.khanacademy.org/math/ap-calculus-bc/diff-equations-bc/eulers-method-bc/v/eulers-method-program-code
"""

__all__ = ["forward_euler", "forward_euler_approx"]

from numpy import arange, zeros


def forward_euler(a: float, b: float, n: int, c: float, f: callable) -> tuple:
    """Forward Euler method, with y = f(x, y), with initial value c, and range
    [a, b]. n is the number of times to split the range [a, b], and is thus used
    to calculate the step size h.

    It returns a tuple, whose first element is the array of abscissas, i.e. the
    values of t during the iterations, and the second element is the array of
    ordinates, i.e. the values of y during the iterations."""
    if a is None or b is None or n is None or c is None:
        raise ValueError("a, b, n and c must not be None.")
    if b < a:
        raise ValueError("b < a, but it should be a <= b.")
    if not callable(f):
        raise TypeError("f should be a callable object.")

    h = (b - a) / n

    # t is an array of abscissas.
    t = arange(a, b, h)

    # y is an array of ordinates.
    y = zeros(n)
    y[0] = c

    for i in range(n - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y


def forward_euler_approx(a: float,
                         b: float,
                         n: int,
                         c: float,
                         f: callable) -> float:
    """Forward Euler method, with y = f(x, y), with initial value c, and range
    [a, b]. n is the number of times to split the range [a, b], and is thus used
    to calculate the step size h.

    It returns just y[b].

    Use this function in case space requirements are a must."""

    if a is None or b is None or n is None or c is None:
        raise ValueError("a, b, n and c must not be None.")
    if b < a:
        raise ValueError("b < a, but it should be a <= b")
    if not callable(f):
        raise TypeError("f should be a callable object")

    t = a
    y = c
    h = (b - a) / n

    for _ in range(n - 1):
        y += h * f(t, y)
        t += h

    return y
