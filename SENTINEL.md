# SENTINEL


_This is a schematic and concise list of the things for which I should constantly be prepared to fix or improve_.


#### Make sure that...

- **_default mutable values (like lists) end up acting as expected_**

    - Default parameter values seem to be treated as static
        
            def foo(a=[]):
                a.append(1)
                return a
                
            foo() # returns [1]
            foo() # returns [1, 1]

    - This is one of the features that I hate more about Python!!!    
    - See:   
        - [http://effbot.org/zone/default-values.htm](http://effbot.org/zone/default-values.htm)
        - [http://stackoverflow.com/questions/4841782/python-constructor-and-default-value](http://stackoverflow.com/questions/4841782/python-constructor-and-default-value)

- I'm using `X is None` or `X is not None` in conditions, when I really mean that `X` should be respectively `None` or `not None`.
In other words, I should not be using `X` or `not X`, because `X` could be 0, and could conceptually still _contain_ a valid value.

- citations to resources used to implement an algorithm or data structure are provided at the beginning of each module.

- the doc-strings of the files containing each data structure or algorithm contain a (good) introduction to what's being implemented.

- I'm raising the most appropriate exception for each specific anomaly.

- exceptions raised are consistent inside each module: the same exception should be raised when the "same" error occurs in different methods or even within the same method.

- I use the same naming conventions throughout the modules.

- unit tests 

    - are not redundant

    - cover all partitions

    - cover all statements

    - cover all boundary values
