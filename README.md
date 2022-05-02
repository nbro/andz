# Algorithms and Data Structures (ands) 


[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/stability-experimental-red.svg)](http://www.engr.sjsu.edu/fayad/SoftwareStability/)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](./LICENSE.md)

## Introduction

`ands` stands for **a**lgorithms a**n**d **d**ata **s**tructures.  

So, in this repository, you can find some of the most common algorithms and data structures studied in Computer Science, such as quick-sort or binary-search trees. The algorithms are divided into main categories, such as sorting algorithms or dynamic programming algorithms. 

The current main goal of this project is for me to learn more about new algorithms and data structures, but I hope these implementations can also be useful to anyone interested in them.

## How to use?

### Installation

I'm currently using **Python 3.9**.

1. Create a virtual environment
2. Install `ands` inside that virtual environment in editable mode: `pip install -e .`

### Testing

Example

    coverage run --source=. -m unittest discover -s tests/algorithms/sorting/integer -v

### Type checking

Example

    mypy ands/algorithms/sorting/integer/radix_sort.py

### More info

- [`CONTRIBUTING.md`](./md/CONTRIBUTING.md)
- [`CONVENTIONS.md`](./md/CONVENTIONS.md)

## Notes

- This is a **personal project**.
  - I will **not accept pull requests**.
  - However, if you find issues in the code, you can report them in the issue tracker.
- This is a **work in progress**, don't expect to find here all the algorithms and data structures you are searching. 
- Expect **breaking changes** across versions/commits, as this is an experimental project. 
  - Every once in a while, **I also rewrite the history of the commits** to make it more logical, so the time of the commits or pushes might not correspond to when I originally implemented and added the features.
  - Moreover, if you fork this repo, and if you try to fetch my updates or try to make a pull request (which I will not accept anyway), you could have conflicts after I have rewritten history.
- **Mistakes are possible**, even if I always try to test all the algorithms and data structures. You can find the unit tests under the folder [`tests`](tests). So, as the [license](LICENSE.md) says, this project is provided "as is".

- **No optimisation** has been done to any algorithm or data structure. The 
purpose of the implementations is just for **_exposition of the concepts_**!

- My intent is to continue to contribute to this repository in my free time, and **new data structures and algorithms** will therefore be added.


## References

For each module, I always try not to forget to specify the specific references that I used to implement the particular concept exposed in that module. 

Apart from those, the following are the references which I always keep an eye on:

- [_Introduction to Algorithms_ (3rd ed.)](https://mitpress.mit.edu/books/introduction-algorithms),  book by Cormen, Leiserson, Rivest, Stein

- [Algorithms, 4th Edition](http://algs4.cs.princeton.edu/home/), online book  by Robert Sedgewick and Kevin Wayne

## Resources

There many useful resources around the web to help you (and me) understand how certain algorithms or data structures work. Examples are

- [The Archive of Interesting Code](http://www.keithschwarz.com/interesting/) 
by Keith Schwarz

- [Notes on Data Structures and Programming Techniques](https://www.cs.yale.edu/homes/aspnes/classes/223/notes.html)

- [https://github.com/tayllan/awesome-algorithms](https://github.com/tayllan/awesome-algorithms)

- [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code)