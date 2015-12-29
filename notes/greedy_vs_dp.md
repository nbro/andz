## Greedy Strategy

### Greedy-choice property

The first ingredient of a _greedy strategy_ is the **greedy-choice property**:

> One can always arrive a globally optimal solution my making local optimal (or best) choices.

In other words, this simply means that greedy algorithms should give an optimal solution to a problem by simply making at each step of the algorithm the best looking choice (the greedy choice). _The choice made by a greedy algorithm might depend on choices made so far, but it cannot depend on any future choices or on the solutions to subproblems_. In fact, greedy algorithms do not even consider future subproblems (or results from those subproblems), but only the current one.

As an analogy to this greedy choice, you can think of a person that acts without considering future possible problems, but does whatever seems best at the moment. Think about a smoker that smokes because it feels better at the moment, or a kid that does not want to study and decides to play, without thinking about the future consequences and problems that might arise. They are basically making greedy choices.

One possible difference between how these people act and the greedy-choice property that a greedy algorithm should have is: most of the times, these people don't even care or think about a "final optimal result" (when doing a greedy choice), whereas, in a (useful) greedy algorithm, by making the local best choice, a globally optimal solution is expected. This of course must be proven (we must prove that a greedy choice at each step yields a globally optimal solution).


### Optimal substructure property

The second ingredient is the **optimal substructure property** (which is also an ingredient of dynamic programming algorithms):

> A problem exhibits optimal substructure if an optimal solution to the problem contains within it optimal solutions to subproblems.


This can be proved by induction: if the solution to the subproblem is optimal, then combining the greedy choice with that solution yields an optimal solution.


### Developing a greedy algorithm

In general, inventing a greedy algorithm is easy, but proving it yields the optimal solution can be difficult: it requires deep understanding of the structure of the problem.


### Greedy versus Dynamic programming

Because both greedy algorithms and dynamic programming exploit optimal substructure, you might be tempted to generate a dynamic programming solution to a problem where a greedy algorithm suffices, or, conversely, you might mistakenly think that a greedy algorithm works when instead a dynamic programming solution is required.

To illustrate the subleties betweeen these two techniques, let us invistigate two variants (the integer and the fractional ones) of a classical optimisation problem, the knapsack problem.

The integer (or 0-1) knapsack problem is the following. A thief robbing a store finds n items. Each item has an integer value or price and a integer weight. The thief wants to take as valuable a load as possible, but it can only carry a certain amount of weight with him, say W, where W is an integer. The question is: which items should the thief take in order to maximise the total value? 

Note that the thief can only take or leave an item, it cannot take a fraction of an item, like, we will see, in the fraction knapsack problem.

In the fractional knapsack problem, the setup is similar. The only difference, as mentioned above, is that the thief can take fractions of items, instead of needing to take entire items.

Both versions, the integer and the fractional versions, exhibit optimal substructure.

... [page 426, Cormen]




