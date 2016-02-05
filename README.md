# Algorithms and Data Structures (AnDS)


| Author               | Nelson Brochado |
|----------------------|-----------------|
| Programming Language | Python 3        |
| Created on           | June, 2015      |

## Introduction

This project was created for _personal use_ mostly while studying for an _exam_ of a previous course that I followed called _Algorithms and Data Structures_. I decided to make it publicly available to use and modify, so that people with difficulties in understanding and applying these topics can take benefit from it. 

I discourage every beginner from copying **shamelessly** the source code, but instead you should definitely give a chance to your brain and sense of challenge first! At the end, you will definetely feel a better and more serious programmer! If you really do not have any ideas on how to do something, try to read the comments next to each function and/or class that you are interested in. They are there for reason!

Note that this is a **work in progress** project, and there might be some mistakes, as a matter of fact no serious tests have been done. Anyway, this respository only contains data structures and algorithms whose implementation can be considered complete (i.e. more details can be added, but the basic behaviour is implemented). I have also other semi-implemented data structures and algorithms that I will include once I finish implementing them.

Any suggestions to improve the code, or the design of an algorithm or data structure, or corrections are of course well accepted, and therefore I encoure you to _fork_ this repository and eventually send a _pull request_.

## Structure

In this repository, you will find data structures, such as _binary-search trees_ or _graphs_, and _algorithms_ that often work on (those) data structures. 
You will also find some algorithms related to some particular _design paradigm_, for example algorithms related to the _greedy_ or _dynamic programming_ design paradigms.


## How to Use

Download this repository. Open a terminal, and enter inside the `ands` folder. For example, `ands` is in your desktop, type:

    cd ands

Once inside `ands` type

    python3.5 setup.py install
    
You might want to install this package in a virtualenv in order not to pollute your Python's distribution. See for example the following tutorials and posts on how to setup a virtualenv:

- [http://docs.python-guide.org/en/latest/dev/virtualenvs/](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

- [http://stackoverflow.com/questions/5844869/comprehensive-beginners-virtualenv-tutorial](http://stackoverflow.com/questions/5844869/comprehensive-beginners-virtualenv-tutorial)


## References

The main references that I have used are:

- [_Introduction to Algorithms_ (3rd ed.)](https://mitpress.mit.edu/books/introduction-algorithms), book by Cormen, Leiserson, Rivest, Stein

- Slides provided by the professor of the course Algorithms and Data Structures, i.e. [Antonio Carzaniga](http://www.inf.usi.ch/carzaniga/)

- [Wikipedia](https://www.wikipedia.org/)

- [Stack Overflow](http://stackoverflow.com/)

- [MIT 6.006 Introduction to Algorithms, Fall 2011](https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)



## TODO

See `README.md` files of subpackages [`algorithms`](ands/algorithms) and [`ds`](ands/ds).


## Future

I would like to create a simple simulation of two kinds of networks: one that uses the link-state routing protocol and the other that uses the distance-vector routing protocol.


### Tools
There's a program called "yEd" which allows us to create "visual" graphs (among other similar things) using a drag-and-drop approach, which can definitely be useful if you want to visualite a graph.

It would also be nice to have a program, which generates random graphs, in order to tests the functions more randomly, instead of using similar graphs every time.

This  random generator of graphs should provide
at least the following options and functionalities:

1. Specify if the graph is directed or undirected
2. Specify the the edges are weighted or unweighted
3. Specify the maximum and minimum number of outgoing and incoming edges.
5. Specify the maximum and minimum number of vertices in the graph
6. Specifying if the graph can be disconnected
7. ...
