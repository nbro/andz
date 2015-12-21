# [Changelog](https://keepachangelog.com/en/1.0.0/)

## v0.1.0

### Algorithms

#### Cryptographic Algorithms

- Add the Caesar cipher algorithm
- Add the one-time pad algorithm

#### Divide-and-Conquer (DaC) Algorithms

- Add multiple implementations (in particular, iterative and recursive versions) of the binary search algorithm
  - Add a linear search to compare it with the binary search
- Add the `find_max` and `find_min` functions, which, respectively, find the maximum and minimum elements of a list in a DaC fashion
- Add the `find_peak` function
  - Add the `find_peak_linearly` function to compare it with `find_peak`
- Add the `select` function, which finds an element in a list such that at most `k` elements are less than it

#### Dynamic Programming (DP)

- Add the `change_making` and `extended_change_making` functions
- Add the `recursive_fibonacci`, `memoized_fibonacci` and `bottom_up_fibonacci` functions

#### Matching Algorithms

- Add the `gale_shapley` function

#### Numerical Algorithms

- Add the `barycentric` and `compute_weights` functions
- Add the `gradient_descent` function
- Add the `horner` function
- Add the `neville` function
- Add the `newton` function

#### Ordinary Differential Equations (ODE) Algorithms

- Add the `forward_euler` and `forward_euler_approx` functions

#### Recursive Algorithms

- Add the `ackermann` function
- Add the `count` function
- Add the `factorial`, `iterative_factorial`, `smallest_geq` and `multiple_factorial` functions
- Add the `hanoi` function
- Add the `is_sorted`, `iterative_is_sorted` and `pythonic_is_sorted` functions
- Add the `make_decimal` function and the `ALPHA_NUMERIC_ALPHABET` constant
- Add the `is_palindrome` and `iterative_is_palindrome` functions
- Add the `power` function
- Add the `reverse` function

#### Sorting Algorithms

##### Comparison-based Sorting Algorithms

- Add the `bubble_sort` function
- Add the `heap_sort`, `build_max_heap` and `max_heapify` functions
- Add the `insertion_sort` function
- Add the `merge_sort`, `merge` and `merge_recursively` functions
- Add the `quick_sort` and `partition` functions
- Add the `selection_sort` function

##### Integer-based Sorting Algorithms

- Add the `counting_sort` function
- Add the `radix_sort` function

### Data Structures

- Add the `Stack` class
- Add the `Queue` class
- Add the `BST` class (that implements binary-search trees)
- Add the `RBT` class (that implements red-black trees)
- Add the `TST` class (that implements ternary-search trees)
- Add the `BinaryHeap` abstract class
- Add the `MaxHeap` class
- Add the `MinHeap` class
- Add the `MinMaxHeap` class
- Add the `HashTable` abstract class
- Add the `LinearProbingHashTable` class
- Add the `DisjointSets` abstract class
- Add the `DisjointSetsForest` class

### Tests

- Add tests for all functions and data structures

### Development

- Add the `pyproject.toml` and `setup.py` files
- Add a `.gitignore`
- Add a `Makefile`
- Add this changelog `CHANGELOG.md`
- Add the `docs` folder, which also contains info about this project
- Add the `LICENSE.md` file, which contains the MIT license
