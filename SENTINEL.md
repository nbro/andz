# SENTINEL


_This is a schematic and concise list of the things for which I should constantly be prepared to fix or improve_.


#### Make sure that...


- citations to resources used to implement an algorithm or data structure are provided at the beginning of each module.

- the doc-strings of the files containing each data structure or algorithm contain a (good) introduction to what's being implemented.

- I'm using `X is None` or `X is not None` in conditions, when I really mean that `X` should be respectively `None` or `not None`.
In other words, I should not be using `X` or `not X`, because `X` could be 0, and could conceptually still _contain_ a valid value.

- I'm raising the most appropriate exception for each specific anomaly.

- exceptions raised are consistent inside each module: the same exception should be raised when the "same" error occurs in different methods or even within the same method.

- I use the same naming conventions throughout the modules.

- unit tests 

    - are not redundant

    - cover all partitions

    - cover all statements

    - cover all boundary values
