# Algorithms and Data Structures (ands)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/stability-experimental-red.svg)](http://www.engr.sjsu.edu/fayad/SoftwareStability/)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](./LICENSE.md)

## Introduction

`ands` stands for **a**lgorithms a**n**d **d**ata **s**tructures.  

So, in this repository, you can find some of the most common algorithms and data structures studied in Computer Science, such as quick-sort or binary-search trees. The algorithms are divided into main categories, such as sorting algorithms or dynamic programming algorithms. 

The current main goal of this project is for me to learn more about new algorithms and data structures, but I hope these implementations can also be useful to anyone interested in them.

## Development

I use [poetry](https://python-poetry.org/) for development, so you should install it if you want to contribute to this project. 
Given that this is a library, we do not commit the `poetry.lock` file.

I recommend that you use [`pyenv`](https://github.com/pyenv/pyenv) to manage your Python versions.

I also use a [`Makefile`](./Makefile) to declare common commands, for example, to the tests.

This project officially only supports Python 3.9, but it will most likely run on any Python 3 version.

For more info about how to develop, see [`./docs/dev/how_to_develop.md`](./docs/dev/how_to_develop.md).

## How to install?

To install this package, you can use

```
poetry install
```

## Documentation

Almost if not all modules and functions have been thoroughly documented, so the best way to learn about the algorithms 
and data structures is to read the source code and the related docstrings and comments.

You can find more documentation under [`docs`](./docs). There you will find the history of the project, development 
conventions that should be adapted, etc.