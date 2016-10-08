#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado
Creation: 10/09/2016

## References

- First Course in Numerical Methods, chapter 16,
by Uri M. Ascher and C. Greif

- [Euler's Method program code](https://www.khanacademy.org/math/differential-equations/first-order-differential-equations/eulers-method-tutorial/p/eulers-method-program-code),
animation program by Khan Academy

## Description

Forward Euler's method for solving ODEs.
This is the easiest method for approximately solving
a initial value ODE problem.
Hence it's used, in general, as a vehicle for studying
several important and basic notions on numerical ODE methods.

### Euler's method derivation

We first consider finding an approximate solution for
a scalar initial value ODE problem at equidistant abscissae.
Thus, we define the points:

    t_0 = a, t_i = a + i*h,

where h = (b - a) / N is the step size.
We denote the appoximate solution to y(t_i) by yi.
Note that, in general, the step size h could change.

Consider the following forward difference formula:

    y'(t_i) = (y(t_{i + 1}) - y(t_i)) / h - ((h / 2) * y''(zeta_i))

By the ODE, y'(t_i) = f(t_i, y(t_i)), so,
if we manipulate the expression above to have y(t_{i + 1}) isolated in one side,
and we start by multiplying both sides by h:

    h * y'(t_i) = y(t_{i + 1}) - y(t_i) - ((h^2) / 2 * y''(zeta_i))

    h * y'(t_i) + y(t_i) + ((h^2) / 2 * y''(zeta_i)) = y(t_{i + 1})

or

    y(t_{i + 1}) = y(t_i) + h * y'(t_i) + ((h^2) / 2 * y''(zeta_i))

we replace y'(t_i) by f(t_i, y(t_i))

    y(t_{i + 1}) = y(t_i) + h * f(t_i, y(t_i)) + ((h^2) / 2 * y''(zeta_i))


dropping the truncation term, we obtain the forward Euler method,
which defines the approximate solution {y_i}_{i=0}^{N} by:

    y_0 = c (initial value)

    y(t_{i + 1}) = y(t_i) + h * f(t_i, y(t_i)), i=0..N-1

This simple formula allow us to march forward into t.

In the following function we assume that f
and all other parameters are specified.

### Explicit vs Implicit methods

What happens if we replace the forward difference formula
by the backward formula

    y'(t_{i+1}) ~~ (y(t_{i+1}) - y(t_i)) / h

and this leads similarly to the backward Euler method:

    y_0 = c
    y_{i+1} = y_i + h * f(t_{i+1}, y_{i+1}), i=0..N

There's actually a big difference between this new method
and the previous one. This one to calculate y_{i+1}
depends implicitly on y_{i+1} itself!

In general, if a method to calculate y_{i+1} depends implicitly on y_{i+1},
it's called an implicit method,
whereas the forward method is considered a explicit method.
"""

import numpy as np


def forward_euler(a: float, b: float, n: int, c: float, f):
    """
    a is the start of the range
    b is the end of the range
    n is the number of "times"
    c is the initial value
    f is y' = f(x, y)
    """
    if a is None or b is None or n is None or c is None:
        raise ValueError("a, b, n and c must not be None.")
    if b < a:
        raise ValueError("b < a, but it should be a <= b.")
    if not callable(f):
        raise TypeError("f should be a callable object.")

    h = (b - a) / n

    # t is an array of abscissas
    t = np.arange(a, b, h)

    # y is an array of ordinates
    y = np.zeros(n)
    y[0] = c

    for i in range(n - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y


def forward_euler_approx(a: float, b: float, n: int, c: float, f):
    """Returns just y[b].
    Use this function in case you just need y[b]
    and space requirements are a must."""

    if a is None or b is None or n is None or c is None:
        raise ValueError("a, b, n and c must not be None.")
    if b < a:
        raise ValueError("b < a, but it should be a <= b")
    if not callable(f):
        raise TypeError("f should be a callable object")

    t = a
    y = c
    h = (b - a) / n

    for i in range(n - 1):
        y += h * f(t, y)
        t += h

    return y
