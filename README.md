# Algorithms and Data Structures (andz)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/stability-experimental-red.svg)](http://www.engr.sjsu.edu/fayad/SoftwareStability/)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](./LICENSE.md)
[![Tests](https://github.com/nbro/andz/actions/workflows/tests.yml/badge.svg)](https://github.com/nbro/andz/actions/workflows/tests.yml)

## Introduction

`andz` stands for **a**lgorithms a**n**d **d**ata structure**z**. 

> The `s` was replaced with `z` because  
> there was already a dummy package called `ands` on PyPI.

In this package, you can find some of the most common algorithms and 
data structures studied in Computer Science, 
such as quick-sort or binary-search trees. 
The algorithms are divided into main categories, 
such as sorting algorithms or dynamic programming algorithms, but note that
some algorithms and DS can fall into multiple categories .

> The current main goal of this project is for me to learn more about 
new algorithms and data structures, but I hope these implementations 
can also be useful to anyone interested in them.

## Development

I use

- [poetry](https://python-poetry.org/) for development
- the [`Makefile`](./Makefile) to declare common commands
- [`pyenv`](https://github.com/pyenv/pyenv) to manage different Python versions locally
- GitHub Actions for CI/CD

For more info about how to develop, 
see [`./docs/how_to_develop.md`](docs/how_to_develop.md).

## How to install?

```
pip install andz
```

## Documentation

Most modules and functions have been thoroughly documented, 
so the best way to learn about the algorithms and data structures is 
to read the source code and the related docstrings and comments.

You can find more documentation under [`docs`](./docs). 
There you will find the history of the project, 
development conventions that should be adapted, etc.
