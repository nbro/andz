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

> t<sub>0</sub> = a

> t<sub>i</sub> = a + i*h,

where `h` = <sup>(b - a)</sup>&frasl;<sub>N</sub> is the step size, for `i = 0, 1, 2, ... N`.
`t` here is called an _independent variable_, `a` and `b` are respectively the beginning and end
of the interval at which we're trying to numerical approximate `y(t)`.

We denote the approximate solution to y(t<sub>i</sub>) by y<sub>i</sub>.
Note that, in general, the step size `h` could be variable, i.e. we could have a h<sub>i</sub>,
but we keep it constant in this explanation and implementation.

Consider the following _**forward difference** formula_:

> y'(t<sub>i</sub>) = <sup>(y(t<sub>i + 1</sub>) - y(t<sub>i</sub>))</sup>&frasl;<sub>h</sub> -
<sup>h</sup>&frasl;<sub>2</sub> * y''(&zeta;<sub>i</sub>)

By the ODE, y'(t<sub>i</sub>) = f(t<sub>i</sub>, y(t<sub>i</sub>)), so,
if we manipulate the expression above to have y(t<sub>i + 1</sub>) isolated in one side,
and we start by multiplying both sides by `h`:

> h * y'(t<sub>i</sub>) = y(t<sub>i + 1</sub>) - y(t<sub>i</sub>) -
 (<sup>h<sup>2</sup></sup>&frasl;<sub>2</sub> * y''(&zeta;<sub>i</sub>))

or, if we rearrange the entries,

> h * y'(t<sub>i</sub>) + y(t<sub>i</sub>) + (<sup>h<sup>2</sup></sup>&frasl;<sub>2</sub> * y''(&zeta; <sub>i</sub>)) =
 y(t<sub>i + 1</sub>)

we further rearrange the entries so that what we're looking for is on the left side of the equals:

> y(t<sub>i + 1</sub>) =
 y(t<sub>i</sub>) + h * y'(t<sub>i</sub>) + (<sup>h<sup>2</sup></sup>&frasl;<sub>2</sub> * y''(&zeta; <sub>i</sub>))

and we replace y'(t<sub>i</sub>) by f(t<sub>i</sub>, y(t<sub>i</sub>))

> y(t<sub>i + 1</sub>) =
 y(t<sub>i</sub>) + h * f(t<sub>i</sub>, y(t<sub>i</sub>)) +
 (<sup>h<sup>2</sup></sup>&frasl;<sub>2</sub> * y''(&zeta; <sub>i</sub>))

dropping the truncation term, i.e.  (<sup>h<sup>2</sup></sup>&frasl;<sub>2</sub> * y''(&zeta; <sub>i</sub>)),
we obtain the forward Euler method, which defines the approximate solution (y<sub>i</sub>)<sub>i=0</sub><sup>N</sup> by:

> y<sub>0</sub> = c

where `c` is the _initial value_.

> y(t<sub>i + 1</sub>) = y(t<sub>i</sub>) + h * f(t<sub>i</sub>, y(t<sub>i</sub>))

for `i = 0 .. N-1`.

This simple formula allow us to march forward into `t`.

In the following implementation we assume that `f` and all other parameters are specified.

## Explicit vs Implicit methods

What happens if we replace the forward difference formula by the **backward formula**

> y'(t<sub>i + 1</sub>) ~ <sup>(y(t<sub>i + 1</sub>) - y(t<sub>i</sub>))</sup>&frasl;<sub>h</sub>

and this leads similarly to the **backward Euler method**:

> y<sub>0</sub> = c

> y<sub>i + 1</sub> = y<sub>i</sub> + h * f(t<sub>i + 1</sub>, y<sub>i + 1</sub>)

for `i = 0 .. N-1`.

There's actually a big difference between this new method and the previous one.
This one to calculate y<sub>i + 1</sub> depends implicitly on y<sub>i + 1</sub> itself!

In general, if a method to calculate y<sub>i + 1</sub> depends implicitly on y<sub>i + 1</sub>,
it's called an implicit method, whereas the forward method is considered a **explicit method**.

# References

- First Course in Numerical Methods, chapter 16,
by Uri M. Ascher and C. Greif

- [Euler's Method program code](https://www.khanacademy.org/math/ap-calculus-bc/diff-equations-bc/eulers-method-bc/v/eulers-method-program-code),
animation program by Khan Academy

"""

from numpy import arange, zeros


def forward_euler(a: float, b: float, n: int, c: float, f: callable) -> tuple:
    """Forward Euler method (which is an explicit method),
    with `y' = f(x, y)`, with initial value `c`, and range `[a, b]`.
    `n` is the number of times to split the range `[a, b]`,
    and is thus used to calculate the step size `h`.

    It returns a tuple, whose first element is the array of abscissas,
    i.e. the values of `t` during the iterations,
    and the second element is the array of ordinates,
    i.e. the values of `y` during the iterations."""
    if a is None or b is None or n is None or c is None:
        raise ValueError("a, b, n and c must not be None.")
    if b < a:
        raise ValueError("b < a, but it should be a <= b.")
    if not callable(f):
        raise TypeError("f should be a callable object.")

    h = (b - a) / n

    # t is an array of abscissas
    t = arange(a, b, h)

    # y is an array of ordinates
    y = zeros(n)
    y[0] = c

    for i in range(n - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y


def forward_euler_approx(a: float, b: float, n: int, c: float, f: callable) -> float:
    """Forward Euler method (which is an explicit method),
    with `y' = f(x, y)`, with initial value `c`, and range `[a, b]`.
    `n` is the number of times to split the range `[a, b]`,
    and is thus used to calculate the step size `h`.

    It returns just `y[b]`.
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
