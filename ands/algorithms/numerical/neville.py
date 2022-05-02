#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 30/09/2017

Updated: 08/10/2017

# Description

## Polynomial curves

In the context of curve design, which in turn is a key ingredient of
Computer-Aided Design (CAD) and used in the ship-building, aircraft, and
automobile industry, we are interested in polynomial curves P : R → Rᵈ in d
dimensions, where d is usually 2 or 3, although the theory works for arbitrary
d.

Using the monomial basis, a polynomial curve P of degree at most u can be
written as

    P(t) = Aᵤ * tᵘ + Aᵤ₋₁ * tᵘ⁻¹ + ... + A₁ * t + A₀ =                       (1)
         = ∑ᵢ₌₀ᶦ⁼ᵘ Aᵢ * tᶦ,

where the coefficients A₀, A₁, ..., Aᵤ ∈ Rᵈ are now d-dimensional points (or
vectors, if you prefer).

### Find point in a polynomial curve using Horner's method

P(t) can be computed efficiently using Horner's scheme (or method).

## Find interpolating polynomial curve of a set of points

Often we are interested in finding an interpolating polynomial curve. That is,
we are given u + 1 interpolation points P₀, P₁, ..., Pᵤ and parameter values t₀,
t₁, ..., tᵤ, and want to determine the polynomial curve P of degree at most u
which satisfies

    P(tᵢ) = Pᵢ

for i = 0, ..., u.

Using (1), these u + 1 conditions can be written as the linear system:

    V * A = P                                                                (2)

where

    A = (A₀, A₁, ..., Aᵤ)ᵀ ∈ R⁽ᵘ⁺¹⁾ˣ¹

is the column vector of unknown coefficients,

    P = (P₀, P₁, ..., Pᵤ)ᵀ ∈ R⁽ᵘ⁺¹⁾ˣ¹

is the column vector of interpolation points, and

    |  1  |  t₀ | t₀² | ... | t₀ᵘ |
    |  1  |  t₁ | t₁² | ... | t₁ᵘ |
    |  .  |  .  |  .  | .   |  .  |
V = |  .  |  .  |  .  |  .  |  .  | ∈ R⁽ᵘ⁺¹⁾ˣ⁽ᵘ⁺¹⁾
    |  .  |  .  |  .  |   . |  .  |
    |  1  |  tᵤ | tᵤ² | ... | tᵤᵘ |

is the Vandermonde matrix.

In general, solving a linear system like (2) has complexity O(n³), but the
special structure of the Vandermonde matrix can be used to design an O(n²)
algorithm (EXPLAIN FURTHER!!!).

## Neville's algorithm

The interpolation problem can be handled in a more direct way.

We can actually compute the interpolating polynomial P(t) at some t ∈ R without
explicitly determining the coefficients Aᵢ of the monomial representation by
using Neville's algorithm, which is based on the following observation:

The constant polynomial curves (of degree 0)

    Qᵢ⁰(t) = Pᵢ, for i = 0 , ..., u,

surely interpolate the given interpolations points Pᵢ at tᵢ, one at a time, and
they can be used to define polynomial curves of degree 1 (i.e., lines),

    Qᵢ¹(t) = (tᵢ₊₁ - t) / (tᵢ₊₁ - tᵢ) * Qᵢ⁰(t) +
             (t - tᵢ)   / (tᵢ₊₁ - tᵢ) * Qᵢ₊₁⁰(t)

for i = 0 , ..., u.

It should immediately be clear that Qᵢ¹(t) is a linear combination of Qᵢ⁰(t) and
Qᵢ₊₁⁰(t) where the first weight is α = (tᵢ₊₁ - t) / (tᵢ₊₁ - tᵢ) and the second
weight is β = (t - tᵢ)  /  (tᵢ₊₁ - tᵢ). So, the previous expression can be
written in a more compact way as follows:

    Qᵢ¹(t) = α * Qᵢ⁰(t) + β * Qᵢ₊₁⁰(t)

Moreover, we also have

    α + β = (tᵢ₊₁ - t) / (tᵢ₊₁ - tᵢ) + (t - tᵢ)  /  (tᵢ₊₁ - tᵢ) <=>
    α + β = ((tᵢ₊₁ - t) + (t - tᵢ))  /  (tᵢ₊₁ - tᵢ) <=>
          = (tᵢ₊₁ - tᵢ) / (tᵢ₊₁ - tᵢ)
          = 1

Hence Qᵢ¹(t) is also an affine combination.

Qᵢ¹(t) basically interpolates the points Pᵢ and Pᵢ₊₁ at tᵢ and tᵢ₊₁,
respectively.

### Recursion in Neville's algorithm

This construction of polynomial curves to interpolate points can be applied
recursively, for any number of points.

The general formula for a polynomial of degree j, that is Qᵢʲ, which
interpolates points Pᵢ, ...,Pᵢ₊ⱼ at tᵢ, ..., tᵢ₊ⱼ, looks like

    Qᵢʲ(t) = (tᵢ₊ⱼ - t) / (tᵢ₊ⱼ - tᵢ) * Qᵢʲ⁻¹(t) +                           (3)
             (t - tᵢ)   / (tᵢ₊ⱼ - tᵢ) * Qᵢ₊₁ʲ⁻¹(t)

for i = 0, ..., u - j and j = 1, ..., u. Remember: j is the degree of the
polynomial.

We have

    α = (tᵢ₊ⱼ - t) / (tᵢ₊ⱼ - tᵢ)

and

    β = (t - tᵢ) / (tᵢ₊ⱼ - tᵢ)

So, (3) can be written more compactly as follows

    Qᵢʲ(t) = α * Qᵢʲ⁻¹(t) + β * Qᵢ₊₁ʲ⁻¹(t)

Clearly, α +  β = 1, so this is still an affine combination.

In particular, Qᵤ⁰ is the interpolating polynomial curve that we were looking
for.

### Schematic interpretation of Neville's algorithm

Suppose u = 1. Then, we can represent graphically (as a tree or pyramid) the
previously mentioned recursive procedure (Neville's algorithm) as follows:

                                    Q₀¹(t)
                                ↗            ↖
         (t₁ - t) / (t₁ - t₀) ↗                ↖ (t - t₀) / (t₁ - t₀)
                            ↗                    ↖
                      Q₀⁰(t) = P₀            Q₁⁰(t) = P₁

As we can see, the labels attached to the arrows correspond to the weights of
the affine combinations (3).

### Pseudo-code of Neville's algorithm

    function NEVILLE({P₁, ..., Pᵤ}):
        for i from 0 to u by 1 do:
            Qᵢ = Pᵢ

        for j from 1 to u by 1 do:
            for i from 0 to u − j by 1 do:
                Qᵢ = ((tᵢ₊ⱼ - t) * Qᵢ + (t - tᵢ) * Qᵢ₊₁) / (tᵢ₊ⱼ - tᵢ)

        return Q₀

#### Analysis of Neville's algorithm

The previous algorithm takes O(n²) operations. It is clearly not as efficient as
Horner's method (but it solves the interpolation problem "on-the-fly").

### Notes

- The main idea of Neville's algorithm is to approximate the value of a
polynomial at a particular point without having to first find all of the
coefficients of the polynomial.

# References

- Dr. prof. Kai Hormann's notes for the Numerical Algorithms course, fall, 2017.
- https://en.wikiversity.org/wiki/Numerical_Analysis/Neville%27s_algorithm_examples
- https://en.wikipedia.org/wiki/Vandermonde_matrix
- https://www.cse.wustl.edu/~furukawa/cse452/slides/16_interpolation.pdf
- http://people.math.sfu.ca/~kam33/teaching/316-10.09/neville.pdf
- https://mail.scipy.org/pipermail/scipy-user/2003-August/001864.html
- https://people.clas.ufl.edu/maia/files/Lecture3.1.pdf
"""

__all__ = ["neville"]


def neville(xs: list, ys: list, x0: float) -> float:
    """Given n points xs[i], for i = 0, ..., n - 1, ys[i] = f(xs[i]), where f is
    some function.

    Neville's algorithm approximates the value of a polynomial q (of degree
    n - 1) at a particular point x0, i.e. it approximates q(x0), without having
    to first find all the coefficients of the polynomial associated with a
    monomial basis.

    This polynomial q interpolates the n points xs[i] of f, that is,
    f(xs[i]) = ys[i] = q(xs[i]), for i = 0, ..., n - 1. So, at these points, the
    error of the approximation of the function f using the polynomial q is zero.
    However, at other points k of the domain of f, q(k) may be very different
    from f(k), that is the error of the approximation of the function using the
    polynomial varies from point to point of the domain of f. We define the
    error as e(k) = f(k) – q(k). In general, we are most interested in the
    maximum of |e| over the domain of f. This maximum is called "error bound".

    Time complexity: O(n²)."""
    if len(xs) != len(ys):
        raise ValueError("Lists xs and ys have different lengths.")

    n = len(xs)
    q = n * [0]

    for j in range(n):
        for i in range(n - j):
            if j == 0:  # Base case: Qᵢ = Pᵢ
                q[i] = ys[i]
            else:
                # Qᵢʲ(x0) = (tᵢ₊ⱼ - x0) / (tᵢ₊ⱼ - tᵢ) * Qᵢʲ⁻¹(x0) +
                #          (x0 - tᵢ)   / (tᵢ₊ⱼ - tᵢ) * Qᵢ₊₁ʲ⁻¹(x0)
                q[i] = (((x0 - xs[i + j]) * q[i] + (xs[i] - x0) * q[i + 1]) /
                        (xs[i] - xs[i + j]))

    return q[0]  # Q₀
