#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 30/09/2017

Updated: 30/09/2017

# Description

## Polynomials

The most common way of expressing a polynomial p: R → R of degree at most u is
to use the monomial basis {1, x, x², ..., xᵘ} and to write p as

    p(x) = aᵤ * xᵘ + aᵤ₋₁ * xᵘ⁻¹ + ... + a₁ * x + a₀ = ∑ᵢ₌₀ᶦ⁼ᵘ aᵢ * xᶦ

with coefficients a₀, a₁, ..., aᵤ₋₁, aᵤ ∈ R. Using this representation, one can
show that:

    p'(x) = u * aᵤ * xᵘ⁻¹ + (u − 1) * aᵤ₋₁ * xᵘ⁻² + ... + 2 * a₂ * x + a₁ =
          = ∑ᵢ₌₀ᶦ⁼ᵘ⁻¹ (i + 1) * aᵢ₊₁ * xᶦ,

and

    p⁽ᶦ⁾(0) = i! * aᵢ, for i = 0, ..., u,

and

    p⁽ᵘ⁺¹⁾(x) = 0.

## Horner's method to compute polynomials

Horner's method (a.k.a. Horner scheme or Horner's rule) is an algorithm for
calculating polynomials. It consists of transforming the monomial form of p into
a computationally efficient form.

Suppose we want to evaluate the polynomial p at a specific value of x, say x₀.

We now transform the monomial (usual) form of p into an equivalent form, which
allows us to efficiently evaluate p at x₀:

    p(x) = aᵤ * xᵘ + aᵤ₋₁ * xᵘ⁻¹ + ... + a₁ * x + a₀                        <=>
    p(x) = (aᵤ * xᵘ⁻¹ + aᵤ₋₁ * xᵘ⁻² + ... + a₁) * x + a₀                    <=>
    p(x) = ((aᵤ * xᵘ⁻² + aᵤ₋₁ * xᵘ⁻³ + ... + a₂) * x + a₁) * x + a₀         <=>

If we continue this process, we end up with the following formula:

    p(x) = (((aᵤ₋₁ + aᵤ * x) * x + ... + a₂) * x + a₁) * x + a₀

We now calculate p at x₀ by replacing x with x₀ in the general form

    p(x₀) = (((aᵤ₋₁ + aᵤ * x₀) * x₀ + ... + a₂) * x₀ + a₁) * x₀ + a₀

### Why would this allow us to evaluate p at x₀ efficiently?

If, for simplicity, we perform the following changes of variables

    bᵤ   := aᵤ
    bᵤ₋₁ := aᵤ₋₁ + bᵤ * x₀
          .
          .
          .
    b₀   := a₀ + b₁ * x₀

And replace these new variables (or alias) in the evaluation of p at x₀, that is

    p(x₀) = (((aᵤ₋₁ + bᵤ * x₀) * x₀ + ... + a₂) * x₀ + a₁) * x₀ + a₀        <=>
    p(x₀) = (((bᵤ₋₁) * x₀ + ... + a₂) * x₀ + a₁) * x₀ + a₀                  <=>
          .
          .
          .
    p(x₀) = a₀ + b₁ * x₀                                                    <=>
    p(x₀) = b₀

We see that we end up, at the end, to discover that the result of p(x₀) is b₀.

### How many changes of variables do we perform?

This can easily be seen from the subscripts of the variables b. We have u
changes of variables, where u is the original degree of the polynomial p.

### In each change of variable, how many additions and multiplications do we
perform?

Excluding bᵤ := aᵤ, which we assume to be a constant-time operation, all other u
changes of variables perform one addition and one multiplication.

### How many operations have we performed in total?

So, we have u additions and u multiplications, plus a constant-time operation.

### Notes

- When evaluating p(x₀) with the changes of variables, we are only performing
the operations in the changes of variables.

### Optimality of Horner's method

Horner's method is optimal, in the sense that any algorithm to evaluate an
arbitrary polynomial must use at least as many operations.

## Computing polynomials by implementing Horner's method

p(x₀), a u-degree polynomial, can computed efficiently using Horner's scheme, in
O(n) operations, as follows

    function HORNER({a₀, a₁, ..., aᵤ₋₁, aᵤ}, x₀):
        p := aᵤ
        for i from u − 1 to 0 by −1 do:
            p := p * x₀ + aᵢ
        return p

From the previous pseudo-code, we can easily see that this is a O(n) algorithm,
since we have u iterations of the for loop and provided that multiplications and
additions can be performed in O(1), w.r.t. u.

### Notes

- HORNER basically implements the changes of variables explained above.

# References

- Dr. prof. Kai Hormann's notes for the Numerical Algorithms course, fall, 2017.
- https://en.wikipedia.org/wiki/Horner%27s_method
"""


def horner(coefficients: list, x0: float) -> float:
    """A function that implements the Horner's method for evaluating a
    polynomial, with coefficients, at x = x0."""
    p = 0
    for coefficient in coefficients:
        p = p * x0 + coefficient
    return p
