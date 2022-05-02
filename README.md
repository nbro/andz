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

1. Create a virtual environment (optional but recommended)
2. Install `ands` in editable mode: `pip install -e .`

### Testing

Example

    coverage run --source=. -m unittest discover -s tests/algorithms/sorting/integer -v

This will run all the tests under `tests/algorithms/sorting/integer`. 

### Type checking

Example

    mypy ands/algorithms/sorting/integer/radix_sort.py

### Conventions

See [`CONVENTIONS.md`](./md/CONVENTIONS.md).

## WARNINGS

See [`WARNINGS.md`](./md/WARNINGS.md).

## Resources

See [`RESOURCES.md`](./md/RESOURCES.md).