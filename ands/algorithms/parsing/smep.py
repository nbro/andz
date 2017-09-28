#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 24/08/2015

Updated: 19/09/2017

# Description

An mathematical infix-to-postfix expression parser/converter.

Includes also a calculator that receives a postfix expression.

# TODO

- Add complexity analysis.
- Maybe a class could be created?

# References

- https://www.youtube.com/watch?v=vXPL6UavUeA
- http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
"""

import operator
import re

# Higher number => higher precedence.
OPERATORS = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "%": 2,
    "^": 3
}

# Associates symbols with functions.
OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "^": operator.pow
}

PARENTHESIS = {"(", ")"}

REGEX = re.compile(r"(\d+|\w+|[-+*/^%()])")


def string_to_infix(e: str, regex=REGEX) -> list:
    """Parses a string expression `e` into a infix representation list."""
    return regex.findall(e)


def list_to_string(ls: list) -> str:
    return " ".join(ls)


def infix_to_postfix(infix: list) -> list:
    """Return a list representing the postfix representation of the list
    infix."""
    stack = []
    postfix = []

    # Used for counting the number of opening and closing parenthesis, which
    # should be the same.
    opening_paren = 0
    closing_paren = 0

    for i, c in enumerate(infix):
        if c in OPERATORS:
            if i > 0 and infix[i - 1] in OPERATORS:
                raise SyntaxError("No two operators can be in a row.")

            if len(stack) > 0:
                top = stack[-1]

                if top in OPERATORS:
                    if OPERATORS[c] > OPERATORS[top]:
                        stack.append(c)
                    else:
                        while (top in OPERATORS and
                                       OPERATORS[top] >= OPERATORS[c]):
                            op = stack.pop()
                            postfix.append(op)
                            if len(stack) > 0:
                                top = stack[-1]
                            else:
                                break
                        stack.append(c)
                else:
                    stack.append(c)
            else:
                stack.append(c)

        elif c in PARENTHESIS:
            if c == ")":
                if len(stack) > 0:
                    top = stack[-1]
                    while top != "(":
                        try:
                            # pop throws an IndexError if the list is empty
                            r = stack.pop()
                            # Adding what's in between ( ) to the postfix list
                            postfix.append(r)
                            top = stack[-1]
                        except IndexError:
                            raise SyntaxError("'(' not found when popping.")

                    stack.pop()  # Removes ( from the top of the stack
                else:
                    raise SyntaxError(
                        "')' cannot be added to the stack if it is empty.")
                closing_paren += 1
            else:
                stack.append(c)  # c == '('
                opening_paren += 1
        else:  # All the rest is considered an operand
            if i > 0 and infix[i - 1] not in OPERATORS and infix[
                        i - 1] not in PARENTHESIS:
                raise SyntaxError("No two operands can be in a row.")

            postfix.append(c)

    if opening_paren != closing_paren:
        raise SyntaxError(
            "number of opening and closing parenthesis do not match.")

    while len(stack) > 0:
        top = stack.pop()
        if top in OPERATORS:
            postfix.append(top)

    return postfix


def smep_calculator(postfix: list) -> list:
    """Simple mathematical postfix expression calculator."""
    stack = []

    for c in postfix:

        if c not in OPERATORS:
            stack.append(c)
        else:
            top = int(stack.pop())
            top2 = int(stack.pop())
            stack.append(OPS[c](top2, top))

    return stack


if __name__ == "__main__":
    def test1():
        # ifx = "a+b/c*(d+e)-f"
        # ifx = "(12)^3 * x^3 +  (4  * 3)^3 + ()"
        # ifx = "a+b*c"
        # ifx = "3 + 2 * 2 ^ 3 % 3"
        # ifx = "(((3 + 2) * 4))"

        ifx = "((12*2^3+44*3)*3)"
        print("Infix:", ifx)

        ls = string_to_infix(ifx)
        print("Infix list:", ls)

        # ls = ['(', '(', '(', '3', '+', '2', '(', ')', ')', '*', '4', ')', ')']
        # print("Infix:", list_to_string(ls))

        pfx = infix_to_postfix(ls)
        print("Postfix list:", pfx)
        print("Calculated:", smep_calculator(pfx))

        pfx_str = list_to_string(pfx)
        print("Postfix:", pfx_str)


    test1()
