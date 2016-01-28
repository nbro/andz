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

In this repository, you will find data structures, 
such as _binary-search trees_ or _graphs_, and _algorithms_ that often work on those data structures. 
You will also find some algorithms related to some particular _design paradigm_, for example algorithms related to the _greedy_ or _dynamic programming_ design paradigms.

## Warnings

I have tried to make runnable from the **`IDLE`** all scripts from everywhere (i.e. from the folder they are situated), so that you don't need to move files, etc. In case you have some import errors, because either you are not running the scripts from the `IDLE` (but for example from another IDE or from the terminal) or because you are using a different version of Python than `3.5`, you should try to fix the imports by yourself, eventually also by appending paths to `sys.path`. If you still have a problem, I encoure you to open an issue.


## Dependencies

- `tabulate` (module)

I have decided to use the [`tabulate`](https://pypi.python.org/pypi/tabulate) module because it is a nice way of displaying data (for example, the fields of a graph). It can easily be installed with `pip`, for example

    pip3.5 install tabulate

## References

The main references that I have used are:

- _Introduction to Algorithms_ (3rd ed.)
by Cormen, Leiserson, Rivest, Stein

- Slides provided by the professor of the course Algorithms and Data Structures, i.e. Antonio Carzaniga

- Wikipedia

- Stack Overflow



## TODO

Algorithms, data structures and tools I would like to include in this project. Some might be missing. 

### Data Structures

|                 Name                | State     | Comments                                                        |
|:-----------------------------------:|-----------|-----------------------------------------------------------------|
| Adjacency matrix representation of a graph | S  | Convert all current algorithms that work with the adjacent list |
| Max Heap                            | F |                                                                 |
| Red-Black Tree                      | F |                                                                 |
| AVL Tree                            | S  |                                                                 |
| Splay tree                          | S  |                                                                 |
| TST                                 | F |                                                                 |
| B-Tree                              | S  |                                                                 |
| Radix-Tree                          | S  | What's the difference between Trie or Radix-Trie?               |
| Trie                                | S  | What's the difference between Radix-Tree or Radix-Trie?         |
| Hash-Table                          | F |                                                                 |
| Min-Max heap                        | S  |                                                                 |
| Double-Ended Priority Queue         | S  | This might be implemented using a min-max heap.                 |


Where `F` indicates that the data structure needs to be finished and `S` indicates that nothing has been done yet.
### Algorithms

|                Name                | State | Comments                                                                                                                                                                                                                              |
|:----------------------------------:|-------|--------------------------------------------------------------------------------------                                                                                                                                                                                       |
| Pseudo-Random generator            | S     |                                                                                                                                                                                                       |
| Hamming code                       | S     |                                                                                                                                                                                                       |
| CNF to DNF                         | S     |                                                                                                                                                                                                       |


There are many other algorithms I hope to implement in a near future. You can find those lists in each `README.md` file of each section under [`algorithms`](algorithms). What I would also like to include are some _linear programming_ algorithms.

### Other

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
