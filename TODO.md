# TODO

_This is a schematic and concise list of the things for which I should constantly be prepared to fix or improve or simply things that I found unnecessary to be reported as an issue.


- Improve the _citation of references_ (that I used to implement an algorithm or a data structure) in all modules

- Add some material (or links to articles) talking about test-driven development (TDD).

- Find an automatic way of enumerating the data structures and algorithms that have been implemented already.

    - Since not all algorithms and data structures are tested yet, it may also be a good idea to specify if a class or algorithm has already been tested or not.

- Make sure that the doc-strings of the files containing each data structure or algorithm contain an introduction to what's being presented.

- Make sure that I'm using `X is None` or `X is not None` in conditions, when I really mean that `X` should be respectively `None` or `not None`.
In other words, I should not be using `X` or `not X`, because `X` could be 0, and could conceptually still be a "valid input".


- When testing, should I just test the interface of what I'm testing or should I also test the properties of the objects?
In a usual case I think we should just test the interface, but since we're dealing with data structures, we want to control everything inside them?!