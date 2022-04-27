# TODO

## Next features

- <s>Change the tests of counting_sort to take into account the new API (e.g. the key parameter)</s>
- All sorting algorithms should support a key attribute, like Python's built-in sort and sorted functions, which is used to sort the items according to this key, which should be a function
  - Other functions, like is_sorted, should also support this
- The implemented sorting algorithms should be consistent with Python's sort and sorted, provided they have the same properties. 
  - For example, if both algorithms are stable, they should produce the same output
- [IN PROGRESS] Implement Radix Sort
  - [IN PROGRESS] Add example of how radix sort and counting sort would work on strings or key-indexed data, and test this functionality
- [IN PROGRESS] Test radix sort
- Implement Introsort

- Implement the Catmull-Rom spline

## Design

- <s>Consider dividing the sorting algorithms into sub-categories, like comparison-based and integer sorting algorithms</s>
- Each module should contain the link to the original paper, book or article that proposed the algorithm or data structure.
- Some dependencies listed in setup.py are only needed for testing, so we might want to separate them from the normal dependencies
- Given that now I am using Python 3.9, the hints like `list`, could probably be replaced with more specific type hints, like `list[int]`. Note that, before Python 3.9, we couldn't do this directly with `list`, but we need to import `List` from typing and then do `List[int]`. That's why I avoided using `List[int]`.

## CI/CD

- Travis CI is no longer free. I need to find a free alternative.
- <s>The scripts inside [`scripts`](../scripts) are a bit inflexible. For example, they return an error if the specific version of Python is not installed. We can probably get rid of them and simplify the way the algorithms can be test locally.</s>
- It might also be a good idea to migrate from virtual environments to docker containers (optional)

## Testing

- See [`tests/README.md`](../tests/README.md)
