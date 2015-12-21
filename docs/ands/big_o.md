# [Big-O](https://en.wikipedia.org/wiki/Big_O_notation)

Big-O notation is used to indicate the _computational complexity_ of an algorithm, both in terms of 

- number of operations (_time complexity_), and 
- space/memory (_space complexity_)

with respect to the input _size_ (or length), _in the limit_, i.e. as the input size/length grows to infinity, i.e. _asymptotically_.

For example, if we say that an algorithm has time complexity `O(n)`, then it roughly means that there's a _linear_ function that _upper bounds_ the time complexity of our algorithm. So, the time required to run the algorithms grows linearly with the size of the input. Here, `n` depends on the algorithm and how we want to analyse our algorithm. For example, if you want to know how much time you will need to sort a list, as the number of elements grows to infinity, then `n` is the number of elements in the list. 

The complexity can also be given as a function of the _output size_ (e.g. for output-sensitive algorithms) or other parameters (e.g. number of layers in a neural network).

Note that the computational complexity is usually expressed asymptotically. This is useful when you think of how your algorithm would scale as a function of the input/output or other parameters. However, in practice, if you know e.g. that the input size to your algorithm does not change, then you might consider (more) the _running time_ (e.g. measured in minutes) and actual memory that your algorithm takes and uses, respectively.

We can analyse the time/space complexity of an algorithm in the _best_, _average_ and _worst cases_. Moreover, it can be given as _lower_ bound, an _upper bound_, or both.

These 2 concepts are orthogonal. For example, you can provide the computational complexity for the average case as a lower bound, or maybe in the worst case as lower and upper bound.

## Best, average and worst cases

### Example: sorting

- Best case: array is already sorted
- Average case: it's the average time across "many" possible inputs
- Worst case: it depends on the sorting algorithm, but it would be the case where you perform the maximal number of operations; so it could be e.g. when the array is completely reversed

## Lower, lower and upper, and upper bounds

- lower bounds (Omega/`Ω`)
- lower and upper bounds (Theta/`Θ`), i.e. we bound the complexity of our algorithm from above and below
- upper bounds (`O`)

## Common complexities

- constant time/space: `Ω(1)`, `Θ(1)`, and `O(1)` 
- linear time/space: `Ω(n)`, `Θ(n)`, and `O(n)` 
- logarithmic time/space: `Ω(log(n))`, `Θ(log(n))`, and `O(log(n))`
- "n log n" time/space: `Ω(n*log(n))`, `Θ(n*log(n))`, and `O(n*log(n))` 
- quadratic time/space: `Ω(n²)`, `Θ(n²)`, and `O(n²)` 
- cubic time/space: `Ω(n³)`, `Θ(n³)`, and `O(n³)` 
- exponential time/space: `Ω(2ⁿ)`, `Θ(2ⁿ)`, and `O(2ⁿ)` 

## Terminology

Sometimes, rather than saying that the complexity of an algorithm is e.g. `O(n)`, people will say that it's "linear" or "n". Of course, in this case, they are not specifying whether it's a lower or upper bound, or both, but, in many cases, this description is sufficient.

## Importance

It's important to have an idea of the time and space complexity of the most commonly used algorithms because the performance of our programs highly depends on the computational complexity. For example, you should know that there's a lower bound for comparison-based sorting (i.e. not comparison-based sorting can do better than this lower bound), or that searching in a balanced binary search tree takes "log n" time. It's also important to know how to analyse the complexities of your own algorithms, to understand if you can improve them or not.

## Resources

- https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation
- https://en.wikipedia.org/wiki/Big_O_notation
- CLRS book