#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: Nelson Brochado

Created: 24/08/2015

Updated: 14/03/2022

# Description

An mathematical infix-to-postfix expression parser/converter. It also includes
a calculator that receives a postfix expression.

## Infix, prefix and postfix notations

In infix notation, we place the operators BETWEEN the operands. An example of
an infix notation is

    2+2

In prefix notation (aka Polish notation), we place the operators BEFORE the
operands. Each prefix notation starts with an operator.

Example:

    + 2 2

In postfix notation (aka reverse Polish notation), we place the operators
AFTER the operands.

Example:

    2 2 +

Infix notation is more difficult to parse than prefix and postfix notation by
computers but it's more common among humans. Moreover, in order to determine
the precedence of the operations, in infix notation, it's necessary to define
the priority of the operators or to use parentheses. For example,
multiplication has higher priority than summation. So, 2 * 2 + 2 = (2 * 2) + 2
= 6. In prefix and postfix notation, we don't need to use parentheses, assuming
the operators have a fixed number of inputs (i.e. arity).

## Evaluation

To evaluate the prefix notation, we can use a stack. We first push onto the
stack the first operator (the left-most one in the expression). Successively,
we push as many operands as required by this operator. For example, if we have
the expression * 2 2, we first push * onto the stack, then we push 2 and 2,
because we know that * requires 2 operands, as it's a binary operator.

So, initially, the stack looks like

    +---+
    | * |
    +---+

Successively, it looks like

    +---+
    | 2 |
    +---+
    | 2 |
    +---+
    | * |
    +---+

At this point, we can pop from the stack 2 and 2 and perform the operation *
on then, the push the result onto the stack

    +---+
    | 4 |
    +---+

So, to perform this evaluation, whenever we push an operator onto the stack,
we need to keep track of the number of operands it requires, and then we try
to push that number of operands. If those number of operands are not available,
then the expression is not correct. For example, if you had the expression
* 2, then this is not a valid prefix notation, as * requires to operands, but
we have only 1. So, in general, if an expression is a valid prefix expression,
then, at the end of the evaluation, the stack should contain the result of the
evaluated prefix expression.

The prefix expressions can also be evaluated starting from the right. In this
case, rather than waiting until we have the correct number of operands for a
specific operator, we wait until we find an operator that has an arity equal to
the number of operands already pushed.

# Terminology

- Polish notation and reverse Polish notation refer to the nationality of
Jan Łukasiewicz, who invented the Polish notation.

- Prefix notation is also known as
    - Polish notation
    - normal Polish notation
    - Łukasiewicz notation
    - Warsaw notation
    - Polish prefix notation
- The reverse Polish notatin (RPN) was invented by Arthur Burks, Don Warren,
and Jesse Wright in 1954. Apparently, it was also independently reinvented by
Friedrich L. Bauer and Edsger W. Dijkstra in the early 1960s.

# TODO

- Add complexity analysis.
- Maybe a class could be created?

# References

- https://en.wikipedia.org/wiki/Infix_notation
- https://en.wikipedia.org/wiki/Polish_notation
- https://en.wikipedia.org/wiki/Reverse_Polish_notation
- [Evaluation of Prefix expression | Examples | Data Structures | Lec-21 | Bhanu Priya](https://www.youtube.com/watch?v=op_NxwPY61I)
- [3. Infix to Postfix Conversion The Easy Way](https://www.youtube.com/watch?v=vXPL6UavUeA)
- [Prefix to Infix Conversion | Examples | Data Structures | Lec-18 | Bhanu Priya](https://www.youtube.com/watch?v=b6m4f2xwRjM)
- http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
"""

__all__ = ["infix_to_postfix"]

# TODO: check if the implementations below are correct
# TODO: infix_to_prefix
# TODO: prefix_to_postfix
# TODO: support also - (negative/negation)

import operator
import re


class Op:
    def __init__(self, func: callable, arity: int, precedence: int):
        assert callable(func)
        assert isinstance(arity, int)
        assert isinstance(precedence, int)
        if arity < 1:
            raise ValueError("operator should have at least 1 operand")
        if precedence < 1:
            raise ValueError("precedence should be at least 1")
        self.func = func
        self.arity = arity
        self.precedence = precedence


# A map from an operator symbol to a tuple (function, arity, precedence), where
# function is the corresponding function of the operator, arity is the number
# of operands that this operator requires, and precedence determines the
# precedence of the operator wrt others, where a higher number means a higher
# precedence.
OPERATORS: dict[str, Op] = {
    "+": Op(operator.add, 2, 1),
    "-": Op(operator.sub, 2, 1),
    "*": Op(operator.mul, 2, 2),
    "/": Op(operator.truediv, 2, 2),
    "%": Op(operator.mod, 2, 2),
    "^": Op(operator.pow, 2, 3),
}

PARENTHESIS = {"(", ")"}

_REGEX = re.compile(r"(\d+|\w+|[-+*/^%()])")


def _str_to_infix(e: str, regex=_REGEX) -> list:
    """Parses a string expression `e` into an infix representation list."""
    return regex.findall(e)


def _list_to_str(ls: list) -> str:
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
                    if OPERATORS[c].precedence > OPERATORS[top].precedence:
                        stack.append(c)
                    else:
                        while (
                            top in OPERATORS
                            and OPERATORS[top].precedence >= OPERATORS[c].precedence
                        ):
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
                        "')' cannot be added to the stack if it is empty."
                    )
                closing_paren += 1
            else:
                stack.append(c)  # c == '('
                opening_paren += 1
        else:  # All the rest is considered an operand
            if (
                i > 0
                and infix[i - 1] not in OPERATORS
                and infix[i - 1] not in PARENTHESIS
            ):
                raise SyntaxError("No two operands can be in a row.")

            postfix.append(c)

    if opening_paren != closing_paren:
        raise SyntaxError("number of opening and closing parenthesis do not match.")

    while len(stack) > 0:
        top = stack.pop()
        if top in OPERATORS:
            postfix.append(top)

    return postfix


# TODO: devise a more robust way to support not just float?
def str_to_num(s: str):
    assert isinstance(s, str)
    try:
        operand = int(s)
        if not s.isdigit():
            assert operand < 0
    except ValueError:
        # TODO: This should raise if s is not convertable to a float. Is this
        #  a good thing, or should we handle this case differently?
        operand = float(s)
    return operand


def prefix_to_infix(prefix: list, verbose=True) -> list:
    evaluation = []

    for c in reversed(prefix):
        if c in OPERATORS:
            operand1 = evaluation.pop()
            operand2 = evaluation.pop()

            operation = ["("]
            if isinstance(operand1, list):
                operation.extend(operand1)
            else:
                assert isinstance(operand1, str) and operand1 not in OPERATORS
                operation.append(operand1)

            operation.append(c)

            if isinstance(operand2, list):
                operation.extend(operand2)
            else:
                assert isinstance(operand2, str) and operand2 not in OPERATORS
                operation.append(operand2)

            operation.append(")")

            if OPERATORS[c].arity == 2:
                evaluation.append(operation)
            else:
                raise NotImplementedError("only binary operators are " "supported")
        else:
            evaluation.append(c)

        if verbose:
            print("evaluation =", evaluation)

    if len(evaluation) != 1:
        raise ValueError("invalid prefix expression")

    return evaluation[-1]


def evaluate_prefix(prefix: list, from_left=True, verbose=False) -> float:
    if from_left:
        return evaluate_prefix_from_left(prefix, verbose=verbose)
    else:
        return evaluate_prefix_from_right(prefix, verbose=verbose)


def evaluate_prefix_from_right(prefix: list, verbose=False) -> float:
    evaluation = []
    for c in reversed(prefix):
        if c in OPERATORS:
            operands = []
            for _ in range(OPERATORS[c].arity):
                operand = evaluation.pop()
                operand = str_to_num(operand)
                operands.append(operand)
            result = OPERATORS[c].func(*operands)
            evaluation.append(str(result))
        else:
            evaluation.append(c)

        if verbose:
            print("evaluation =", evaluation)

    if len(evaluation) != 1:
        raise ValueError("invalid prefix expression")

    return evaluation[-1]


def evaluate_prefix_from_left(prefix: list, verbose=True) -> float:
    # Based on https://stackoverflow.com/a/3206901/3924118
    # It uses 2 stacks.

    # A stack that holds the operators (e.g. * or +) and operands (e.g. 1 or
    # 2).
    evaluation = []

    # A stack that holds a tuple of size 2, where the first element is the
    # number of operands left to be seen, while the second element is the
    # expected number of operators of an operator (i.e. its arity).
    count = []

    def evaluate_top():
        # If the number of elements to be seen in the top tuple in count is
        # zero,
        # - we pop that tuple,
        # - pop the expected number operands from the evaluation stack (we
        # know this from the second element of the just popped tuple from
        # count), and the operator,
        # - evaluate the expression, and
        # - push the result onto evaluation, and
        # - modify the now top tuple of count accordingly.
        # Then continue in the same fashion.
        if count[-1][0] == 0:
            count.pop()
            op_arity = top_count[1]

            operands = []
            for _ in range(op_arity):
                operand = evaluation.pop()
                operand = str_to_num(operand)
                operands.append(operand)

            # TODO: do I need to reverse the list?
            operands.reverse()

            op = evaluation.pop()
            assert op in OPERATORS
            assert OPERATORS[op].arity == top_count[1]

            result = OPERATORS[op].func(*operands)
            evaluation.append(str(result))

            if len(count) > 0:
                # Given that we pushed the result, we update the top count by
                # decrementing the first element.
                new_top_tuple = count.pop()
                count.append((new_top_tuple[0] - 1, new_top_tuple[1]))
            else:
                assert len(count) == 0 and len(evaluation) == 1

    for c in prefix:
        if c in OPERATORS:
            # Every time we see an operator, we push it onto the evaluation
            # stack, and we also push a tuple onto count (operator.arity,
            # operator.arity).
            evaluation.append(c)
            op = OPERATORS[c]
            count.append((op.arity, op.arity))
        else:
            # We assume that c is an operand.

            # Every time we see an operand, we check the top tuple in count,
            # and decrement the first element.
            top_count = count.pop()
            count.append((top_count[0] - 1, top_count[1]))

            # Of course, we also push it onto the evaluation stack.
            evaluation.append(c)

        if verbose:
            print("evaluation =", evaluation)
            print("count =", count)

        evaluate_top()

        if verbose:
            print("evaluation (after evaluate_top) =", evaluation)
            print("count (after evaluate_top) =", count)
            print("-" * 60)

    while len(evaluation) > 1:
        evaluate_top()
        if verbose:
            print("evaluation (after evaluate_top) =", evaluation)
            print("count (after evaluate_top) =", count)

    return evaluation[-1]


def test1():
    ifx = "((12*2^3+44*3)*3)"
    print("Infix:", ifx)

    ls = _str_to_infix(ifx)
    print("Infix list:", ls)

    # TODO: this does not err, but should!?
    # ls = ['(', '(', '(', '3', '+', '2', '(', ')', ')', '*', '4', ')', ')']

    print("Infix:", _list_to_str(ls))


# TODO: why this fails?
def test2():
    ifx = "2.0 + 2*3"
    ls = _str_to_infix(ifx)
    pfx = infix_to_postfix(ls)
    print("Postfix list:", pfx)


def test3():
    # ifx = "a+b/c*(d+e)-f"
    # ifx = "(12)^3 * x^3 +  (4  * 3)^3 + ()"
    # ifx = "a+b*c"
    # ifx = "3 + 2 * 2 ^ 3 % 3"
    # ifx = "(((3 + 2) * 4))"

    ifx = "((12*2^3+44*3)*3)"
    print("Infix:", ifx)

    ls = _str_to_infix(ifx)
    print("Infix list:", ls)

    pfx = infix_to_postfix(ls)
    print("Postfix list:", pfx)

    pfx_str = _list_to_str(pfx)
    print("Postfix:", pfx_str)


def test4():
    prefixes = [
        ["*", "-", "1", "2", "3"],
        ["+", "3", "+", "4", "/", "20", "4"],
        # _str_to_infix("((12*2^3+44*3)*3)")
    ]

    for prefix in prefixes:
        result = evaluate_prefix(prefix, from_left=False)
        print(result)
        result = evaluate_prefix(prefix, from_left=True)
        print(result)
        infix = prefix_to_infix(prefix)
        print(infix)
        print(" ".join(infix))


if __name__ == "__main__":
    test1()
    # test2()  # fails, why? I don't remember.
    test3()
    test4()
