#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

Created: 10/09/2016

Updated: 19/02/2017

# Description

The forward Euler's method for solving ODEs is the easiest method
for approximately solving a _initial value_ ODE problem.
Hence it's used, in general, as a vehicle for studying
several important and basic notions on numerical ODE methods.

## Euler's method derivation

We first consider finding an approximate solution for
a scalar initial value ODE problem at equidistant abscissae.
Thus, we define the points:

  t<sub>0</sub> = a

  t<sub>i</sub> = a + i*h,

where h = <sup>(b - a)</sup>&frasl;<sub>N</sub> is the step size.
We denote the approximate solution to y(t<sub>i</sub>) by yi.
Note that, in general, the step size h could change.

Consider the following forward difference formula:

<sup>15</sup>&frasl;<sub>16</sub>

 y'(t<sub>i</sub>) = (y(t<sub>i + 1</sub>) - y(t<sub>i</sub>)) / h - ((h / 2) * y''(zeta<sub>i</sub>))

By the ODE, y'(t<sub>i</sub>) = f(t<sub>i</sub>, y(t<sub>i</sub>)), so,
if we manipulate the expression above to have y(t<sub>i + 1</sub>) isolated in one side,
and we start by multiplying both sides by h:

 h * y'(t<sub>i</sub>) = y(t<sub>i + 1</sub>) - y(t<sub>i</sub>) - ((h^2) / 2 * y''(zeta<sub>i</sub>))

 h * y'(t<sub>i</sub>) + y(t<sub>i</sub>) + ((h^2) / 2 * y''(zeta<sub>i</sub>)) = y(t<sub>i + 1</sub>)

or

 y(t<sub>i + 1</sub>) = y(t<sub>i</sub>) + h * y'(t<sub>i</sub>) + ((h^2) / 2 * y''(zeta<sub>i</sub>))

we replace y'(t<sub>i</sub>) by f(t<sub>i</sub>, y(t<sub>i</sub>))

 y(t<sub>i + 1</sub>) = y(t<sub>i</sub>) + h * f(t<sub>i</sub>, y(t<sub>i</sub>)) + ((h^2) / 2 * y''(zeta<sub>i</sub>))


dropping the truncation term, we obtain the forward Euler method,
which defines the approximate solution (y<sub>i</sub>)<sub>i=0</sub><sup>N</sup> by:

 y<sub>0</sub> = c (initial value)

 y(t<sub>i + 1</sub>) = y(t<sub>i</sub>) + h * f(t<sub>i</sub>, y(t<sub>i</sub>)), i=0..N-1

This simple formula allow us to march forward into t.

In the following function we assume that f
and all other parameters are specified.

## Explicit vs Implicit methods

What happens if we replace the forward difference formula
by the backward formula

 y'(t<sub>i + 1</sub>) ~~ (y(t<sub>i + 1</sub>) - y(t<sub>i</sub>)) / h

and this leads similarly to the backward Euler method:

 y<sub>0</sub> = c

 y<sub>i + 1</sub> = y<sub>i</sub> + h * f(t<sub>i + 1</sub>, y<sub>i + 1</sub>), i=0..N

There's actually a big difference between this new method
and the previous one. This one to calculate y<sub>i + 1</sub>
depends implicitly on y<sub>i + 1</sub> itself!

In general, if a method to calculate y<sub>i + 1</sub> depends implicitly on y<sub>i + 1</sub>,
it's called an implicit method,
whereas the forward method is considered a explicit method.

# References

- First Course in Numerical Methods, chapter 16,
by Uri M. Ascher and C. Greif

- [Euler's Method program code](https://www.khanacademy.org/math/differential-equations/first-order-differential-equations/eulers-method-tutorial/p/eulers-method-program-code),
animation program by Khan Academy

"""

import numpy as np


def forward_euler(a: float, b: float, n: int, c: float, f) -> tuple:
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

    for _ in range(n - 1):
        y += h * f(t, y)
        t += h

    return y
