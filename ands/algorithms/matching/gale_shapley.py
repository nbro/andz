#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# Meta-info

Author: Nelson Brochado

Created: 19/09/2017

Updated: 29/09/2017

# Description

The Gale-Shapley algorithm for the stable matching problem, which is a discrete
problem.

Given n men and n women and a list of preferences for each man and woman,
regarding who they want to stay with.

A "perfect matching" is an one-to-one assignment of each man to exactly one
woman, so that no man or woman remains unmatched (or "alone").

An unstable match occurs when man M prefers woman W and woman W prefers man M,
but man M is matched with another woman W' and woman W is with another man M'.

A "stable matching" is a perfect matching with no unstable pairs.

Stable matching problem: find a stable matching (if one exists).

Clearly, domains could be different. Instead of women and men we could have
for example people and servers, medical school graduates and hospitals, intern
to companies, etc.

How do find matches so that no men or women remain alone and no unstable match
exists?

We can use the Gale-Shapley algorithm (proposed 1962) to solve this problem,
whose pseudo-code is as follows:

function GALE_SHAPLEY:
    Initialize all m ∈ M and w ∈ W to free
    while ∃ free man m who still has a woman w to propose to:
        w = first woman on m’s list to whom m has not yet proposed
        if w is free:
            (m, w) become engaged
        else some pair (m', w) already exists:
            if w prefers m to m':
                m' becomes free
                (m, w) become engaged
            else:
                (m', w) remain engaged

## Examples

Suppose we have the following preferences lists for men.

|        | 1st    | 2nd    | 3rd   |
|--------|--------|--------|-------|
| Xavier | Amy    | Bertha | Clare |
| Yancey | Bertha | Amy    | Clare |
| Zeus   | Amy    | Bertha | Clare |

And the following one for women.

|        | 1st    | 2nd    | 3rd  |
|--------|--------|--------|------|
| Amy    | Yancey | Xavier | Zeus |
| Bertha | Xavier | Yancey | Zeus |
| Clare  | Xavier | Yancey | Zeus |

Then assignments Xavier to Clare, Yancey to Bertha and Zeus to Amy are unstable,
because Bertha prefers Xavier to Yancey and Xavier prefers Bertha to Clare.

The assignments Xavier to Amy, Yancey to Bertha and Zeus to Clare are stable.

## Notes

1. Men propose to women in decreasing order of preference.
2. Once a woman is matched, she never becomes unmatched: she only "trades up."

## Complexity analysis of the Gale-Shapley algorithm

Gale-Shapley terminates with a stable matching after at most n² iterations of
the while loop. In particular, n * (n - 1) + 1 proposals may be required.

### Algorithm terminates after at most n² iterations of while loop.

#### Proof

- There are n² pairs (m, w).

- At each iteration of the while loop, one man proposes to one woman.

- Once a man proposes to a woman, he will never propose to her again (note 1).
Thus, a man does at most n proposals.

- Thus, after at most n² iterations, no one is left to propose to (algorithm
must terminate).

### All men and women get matched (we have a perfect matching)

- Suppose (by contradiction) that there is a man, Z, who is not matched upon
termination of algorithm.

- Then there must be a woman, say A, who is not matched upon termination.
Remember there are n men and n women!

- Then, by note 2, A was never proposed to.

- But, Z proposes to everyone, since he ends up unmatched. Thus, he must have
proposed to A, a contradiction.

### No unstable pairs (stable matching)

Suppose we have the following pairs (Xavier-Clare), (Yancey-Bertha) and
(Zeus-Amy). And suppose Xavier prefers Bertha to Clare and Bertha prefers Xavier
to Yancey, i.e. Xavier and Bertha would hook up with each other after the given
assignments. So we have an unstable pair in a Gale-Shapley matching S.

Then there are two possible cases:

1. Xavier never proposed to Bertha.
    => Xavier prefers his partner to Bertha in S.
        => S is stable.

2. Xavier proposed to Bertha.
    => Bertha rejected Xavier (right away or later).
    Remember: women only trade up.
        => Bertha prefers her current partner to Xavier.
            => S is stable.

In both cases 1 and 2, we reach a contradiction.

▪

## How to implement the Gale-Shapley algorithm so that its complexity is O(n²)?

Since there are at most n² iterations, each iteration should take constant time.

We denote men and women from 0 to n - 1.

We maintain two lists wife[m] and husband[w]. wife[m] or husband[w] is None if m
does still not have a woman and w does still not have a husband, respectively.
Initially, all wife[i] and husband[i], for i = 0, ..., n - 1, is None.

For each man, maintain a list of women, ordered by preference.

Maintain a list count[m] that counts the number of proposals made by man m.

Idea: for each woman, create the inverse of her preference list. For example,
if the preference list of woman w is:

     0  1  2    <- preferences
    [2, 0, 1]   <- men


where 2 is w's most preferred man and 1 the least preferred. Then we build the
following inverse list

     0  1  2    <- men
    [2, 1, 0]   <- preferences

where the number 0 represents the highest preference and the number 2 the
smallest one.

To build the inverse preference list, it takes n time.

Suppose we have an n x n matrix, where each row i represents the preferences
list of man (or woman) i. Then, we can invert those preferences lists as follows:

    inverses := empty n x n matrix
    for i = 0 to n - 1:
        for p = 0 to n - 1:
            inverses[preferences[i][p]] = p

### Conclusions

We have n men + n women = 2 * n. But we also have as input the preferences lists
of men and women. Each of them occupies n² space. So, the input is N = 2 * n².
It actually follows that the Gale-Shapley algorithm is a O(N) algorithm, i.e. a
linear-time algorithm, where N is the size of the input.

## Further Notes

- In practical applications, the input size may be linear as the preference list
may be limited to a constant (say 5 < n), where n is the number of men (or
women).

- With the previous restriction, the algorithm may fail to find a stable
matching.

- In practice, a "reasonably" stable matching is sufficient.

- The previous algorithm assumed we have the same number of men as women.

## Understanding the Solution produced by Gale-Shapley algorithm.

TODO

# TODO

- is_stable function

# References

- Slides of prof. E. Papadopoulou for her course "Algorithms & Complexity" at
USI, fall 2017, master in AI.

- https://en.wikipedia.org/wiki/Stable_marriage_problem
"""

__all__ = ["gale_shapley"]


def _validate_inputs(men_preferences: list, women_preferences: list, n: int):
    if len(men_preferences) != len(women_preferences):
        raise ValueError("Preferences lists should be of the same size.")

    for m, w in zip(men_preferences, women_preferences):
        if len(m) != len(set(m)) or len(w) != len(set(w)):
            raise ValueError("A preference list has duplicate entries.")
        if len(m) != n or len(w) != n:
            raise ValueError("Preferences matrix should be n x n.")

        possible_values = set(range(n))
        for p1, p2 in zip(m, w):
            if p1 not in possible_values or p2 not in possible_values:
                raise ValueError("Preferences must be in range [0, n - 1].")


def _build_inverses(women_preferences: list) -> tuple:
    """Builds the inverse matrix of the preferences matrix for women, according
    to the algorithm described in the doc-strings above of this module.

    Time complexity: Θ(n²)."""
    n = len(women_preferences)
    inverses = [[None for _ in range(n)] for _ in range(n)]
    for w in range(n):
        for p in range(n):  # p for preference.
            inverses[w][women_preferences[w][p]] = p
    return inverses


def gale_shapley(men_preferences: list, women_preferences: list) -> list:
    """Suppose we have n = len(men_preferences) = len(women_preferences) men and
    women. We number men and women from 0 to n - 1.

    Time complexity: O(n²), where n = # of men = # of women, or O(N), where N is
    the number of preference lists, i.e. N = n². In other words, this is a
    linear-time algorithm in terms of the size of the input."""
    n = len(men_preferences)

    _validate_inputs(men_preferences, women_preferences, n)

    # To keep track of wives of men. So, wife[m] is the wife of m.
    wife = [None] * n

    # To keep track of husbands of women. So, husband[w] is the husband of w.
    husband = [None] * n

    inverses = _build_inverses(women_preferences)

    # To keep track of the number of proposals made by men. So, count[m] is the
    # number of proposals of man m.
    count = [0] * n

    def next_man() -> int:
        """Returns the index or number of the next man without a woman, or None
        if there is not such man."""
        for i, w in enumerate(wife):
            if w is None:
                return i

    def hook_up_with(m: int, w: int) -> None:
        # Assign m to be the current partner of w.
        husband[w] = m

        # Assign w to be the current partner of m.
        wife[m] = w

    def go_forward(m: int) -> None:
        """Makes m man go forward and forget about its current preference, i.e.
        m now goes forward to his next preference."""
        count[m] += 1
        assert 0 < count[m] < n

    def make_alone(o: int) -> None:
        wife[o] = None
        go_forward(o)

    def prefers(w: int, m: int, o: int) -> bool:
        """Returns true if w prefers m over o."""
        assert m != o
        return inverses[w][m] < inverses[w][o]

    m = next_man()

    while m is not None:
        # If there's still a man m without a woman.
        # This while loop takes at most n² iterations.

        # All of the following operations take O(1) time.

        # Look up the next preferred woman for m.
        w = men_preferences[m][count[m]]

        # If w does not have a partner.
        if husband[w] is None:
            hook_up_with(m, w)
        else:  # w is already matched with some man.

            # Get the current partner of w.
            o = husband[w]
            assert wife[o] == w

            # If w prefers m over o, then make m the new partner of w and make
            # o alone.
            if prefers(w, m, o):
                hook_up_with(m, w)
                make_alone(o)
            else:
                go_forward(m)

        m = next_man()

    # Assert that at the end of the while loop all men and women have a partner.
    assert all(x is not None for x in wife)
    assert all(x is not None for x in husband)

    return wife, husband
