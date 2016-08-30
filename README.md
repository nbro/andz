# Algorithms and Data Structures (AnDS)


[![Python 3.3, 3.4, 3.5](https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5-blue.svg)](https://www.python.org/downloads/)
[![Build Status](https://travis-ci.org/nelson-brochado/ands.svg?branch=master)](https://travis-ci.org/nelson-brochado/ands)
[![Coverage Status](https://coveralls.io/repos/github/nelson-brochado/ands/badge.svg)](https://coveralls.io/github/nelson-brochado/ands)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c88538816f424aea916c251428f78c0a)](https://www.codacy.com/app/nelson-brochado/ands?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dossan/ands&amp;utm_campaign=Badge_Grade)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](./LICENSE.md)


## Introduction

This project was created for _personal use_ mostly while studying for an _exam_ (starting in the month of June in 2015) of a previous course that I followed called _Algorithms and Data Structures_ I decided to make it publicly available to use and modify, so that people with difficulties in understanding and applying these topics can take benefit from it. 

I discourage every beginner from copying **shamelessly** the source code, but instead you should definitely give a chance to your brain and sense of challenge first! At the end, you will definetely feel a better and more serious programmer! If you really do not have any ideas on how to do something, try to read the comments next to each function and/or class (or even the code itself) that you are interested in. They are there for areason!

Any suggestions to improve the code, or the design of an algorithm or data structure, or corrections are of course welcome, and therefore I encourage you to _fork_ this repository and eventually send a [_pull request_](https://help.github.com/articles/about-pull-requests/). See below for more info.

## Content

In this repository, you will find data structures, such as _binary-search trees_ or _graphs_, and _algorithms_ that often work on (those) data structures. 
You will also find some algorithms related to some particular _design paradigm_, for example algorithms related to the _greedy_ or _dynamic programming_ design paradigms.

## Notes, Warnings and "Philosophy"

- This is a **work in progress**, don't expect to find here all the data structures and algorithms you're searching. Consider to contribute to the quality and size of the project.

- Again, **mistakes are possible**, even if decent tests are starting to being done. You can find them under the folder [`tests`](tests). So, as the [license](LICENSE.md) says, this project is provided "as is", etc.

- **No optimisation** has been done to any algorithm or data structure. The purpose of the implementations is just for demonstration.

- The `master` branch only contains **usable** (therefore complete) data structures and algorithms, that is, more details can be added, but the basic behaviour is implemented. If a bug is found in a data structure or algorithm, the respective data structure or algorithm is removed from that branch and moved to another one, for example to the one called `dev` or `debug`, until it's fixed.

- My intent is to continue to contribute to this repository in my free time, and **new data structures and algorithms** will therefore be added. I have also other semi-implemented data structures and algorithms that I will include once I finish implementing them.


## How can you support this project?

You can support this project by either reporting a bug or suggesting an improvement after reading the source code, the documentation and/or the doc strings, or you can do it by fixing the problem or introducing new algorithms and data structures by writing the code by yourself.

To accomplish the first one, I suggest you to simply [_open an issue on Github_](https://help.github.com/articles/creating-an-issue/). To accomplish the second one, read the next section.
 
## How to contribute by writing code?

### Notes

- This description and commands are for unix-like systems, i.e. Linux and Mac OS X. If you need help to do it on Windows, just send me an e-mail eventually. Note that the process should be identical, only the commands and eventually tools could be slightly different.

- I'm currently using Python 3.5 and also `pip3.5` to develop, but the module is currently being tested against Python 3.3, 3.4 and 3.5 on Travis CI. Use other versions of Python and `pip` at your own responsibility!

- I really advise you to use `Git` and `Github` as your tools to develop, but you could eventually do it in different ways, and I would try to merge what you have done with the current structure of the module. 

    This means that you can simply write your own Python script containing an algorithm or a data structure independently, and send it to me via either e-mail or by posting it as an issue, and I (or someone else) would be responsible for porting your code for the module, etc. **Just avoid this option, please.**
    
    I allow this second option because some people could not be very familiar yet with Git and Github.

### Using Git and Github

First things first, you should fork the [`ands` repository from my `Github`'s account](https://github.com/nelson-brochado/ands) to your own. After that you should download your forked repository to your local machine. Once that's done, follow the following steps.

1. Open a terminal, and enter inside the `ands` folder. For example, if `ands` is in your desktop and your current working directory is your desktop, type:

        cd ands

2. You're going to install the `ands` module in _editable_ mode in a virtual environment. If you don't know what's a virtual environment, it's time to know it. Here are a few useful resources:

    - [http://docs.python-guide.org/en/latest/dev/virtualenvs/](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

    - [http://stackoverflow.com/questions/5844869/comprehensive-beginners-virtualenv-tutorial](http://stackoverflow.com/questions/5844869/comprehensive-beginners-virtualenv-tutorial)

    The essential reason for developing in a virtual environment is that you probably just want to develop or simply modify the code, i.e. you probably don't want to use this module in other projects yet, because it's in early stage.
    
     So, the first thing to do is to install the `virtualenv` module, which you can do as follows

        pip3.5 install virtualenv


    Then, to create a virtual environment named `venv` (you can name it as you want), type:
    
        virtualenv venv
    
    
    Finally just type the following command to install `ands` on the virtual environment `venv`:
    
        pip3.5 install -e .
        
3. Once you finish developing, you need to commit your changes and then do a pull request. If you don't know what this means, check online, because these things are very useful for any serious programmer.

## Tests

If you want to create tests (_I strongly recommend you to write or modify them whenever respectively you write something new or modify something_), you need to write them within the folder [`tests`](tests), and their names' conventions (i.e. scripts' and functions' names) should follow the same name conventions of the already existent tests.

### How to run tests?

From inside either `tests/ds` or `tests/algorithms`, you can do

    python -m unittest discover . -v

or, after installing the package `coveralls`

    coverage run -m unittest discover . -v


This last one should also report you the amount of code covered by the tests, after your run the command

    coverage report

You can also simply run the [`./run.sh`](./run.sh) script on the terminal, which does that and other things...

## References

The main references that I have used are:

- [_Introduction to Algorithms_ (3rd ed.)](https://mitpress.mit.edu/books/introduction-algorithms), book by Cormen, Leiserson, Rivest, Stein

- Slides provided by the professor of the course Algorithms and Data Structures, i.e. [Antonio Carzaniga](http://www.inf.usi.ch/carzaniga/)

- [Wikipedia](https://www.wikipedia.org/)

- [Stack Overflow](http://stackoverflow.com/)

- [MIT 6.006 Introduction to Algorithms, Fall 2011](https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)

- [Interactive Python](http://interactivepython.org), website by Brad Miller and David Ranum

- [Algorithms, 4th Edition](http://algs4.cs.princeton.edu/home/), online book by Robert Sedgewick and Kevin Wayne

- [Algorithms: Design and Analysis, Part 1](https://www.coursera.org/learn/algorithm-design-analysis), Coursera's course taught by Tim Roughgarden

- [Algorithms: Design and Analysis, Part 2](https://www.coursera.org/learn/algorithm-design-analysis-2), Coursera's course taught by Tim Roughgarden


## TODO

I would like to improve the _citation of references_ that I used to implement an algorithm or a data structure in all modules.


I also want to develop a lot more algorithms and data structures. See the `README.md` files of the subpackages [`algorithms`](ands/algorithms) and [`ds`](ands/ds) for more info. In some cases, you will also find a `README.md` file under the subpackages of the subpackages I've just mentioned.


## Developers

* Nelson <nelson.brochado@outlook.com>