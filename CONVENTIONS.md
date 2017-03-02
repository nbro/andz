# Conventions

Conventions that should be adopted for this project.

## General

- Do not introduce features that are
    - incomplete, or
    - not tested

 to the `master` branch!!
  
- Expose only public interface!!
    
    - For example, clients of a BST may not care about the existence of a BSTNode, which is only useful to store information about the keys.
    
### Github Issue Tracker

The _issue tracker_ should be used to report 

- issues regarding existing code, or 
- possible improvements of existing code

and **not** to report:

- possible future features which have nothing to do with the existing code, or 
- report issues of code that is no more part of this project
 
## Design by contract

- Consists in asserting:

    - _preconditions_, 
    - _invariants_, and 
    - _postconditions_

- _Use assertions to ensure preconditions, invariants and postconditions_

    > An assertion is instead a correctness condition governing the relationship between **two software modules** (not a software module and a human, or a software module and an external device). 
    
    > If `sum` is _negative_ on entry to `deposit`, violating the precondition, the culprit is some other software element, whose author was not careful enough to observe the terms of the deal.
    
    - Essentially, if a programmer of a function `A` establishes a contract (which, apart from the assertion statements, could also be specified as a comment of the same function) with the world about, for example, a certain input `x`'s range, then he can assume whoever is going to use `A` is going to pass a correct value (in the acceptable range) for `x`. So, in this case, we should not check for the input `x`'s correctness (using for example `try .. catch` constructs), but we should use assertions.

        - Why? Assertions are used to check what **should never happen**!

    - We should also use assertions if the programmer of a certain function `A` ensures to the world that the function is going to maintain a certain invariant or postcondition, but he breaks it because of a logical error.
    
    > **Rule - Assertion Violation**: _A run-time assertion violation is the manifestation of a bug_.
    
    > To be more precise: 

    > - A _precondition violation_ signals a bug in the client, which did not observe its part of the deal.
    > -  A _postcondition (or invariant) violation_ signals a bug in the supplier -- the routine -- which did not do its job.
    
    > That violations indicate bugs explains why it is legitimate to enable or disable assertion monitoring through mere compilation options: for a correct system -- one without bugs -- assertions will always hold, so the compilation option makes no difference to the semantics of the system.
    
### Questions 

1. Should we establish contracts between a certain function `f` and a user `U`?
    
    - I think the answer depends (but not exclusively) on what `f` is intended to be used by, that is
        - if the users of `f` are intended to be programmers, then we should establish contracts
        
        - if the users of `f` are real users, then usually the real user doesn't care about the implementation of `f`, and therefore exceptions should be raised.
    
    1. We don't know 100% sure that only a certain type of user is going to use `f`, so what should we do in these cases?

        - The intended clients of `f` should be one of the first things specified in the documentation of the software. **We can't protect users that do respect the rules of the software**!!!

### References

- [[https://www.eiffel.org/doc/eiffel/ET%3A%20Design%20by%20Contract%20(tm),%20Assertions%20and%20Exceptions](https://www.eiffel.org/doc/eiffel/ET%3A%20Design%20by%20Contract%20(tm),%20Assertions%20and%20Exceptions)]([https://www.eiffel.org/doc/eiffel/ET%3A%20Design%20by%20Contract%20(tm),%20Assertions%20and%20Exceptions](https://www.eiffel.org/doc/eiffel/ET%3A%20Design%20by%20Contract%20(tm),%20Assertions%20and%20Exceptions))

## Assertions

- Use assertions for something that **should never happen**:

    - Use assertions in code **to catch implementation errors** (before releasing)!!!

    - Use assertions for preconditions, invariants and postconditions.
        
        - Preconditions may also be explicitly stated assumptions about the inputs.

    - Since these things should never happen, then in the release mode, assertions can be disable to speed up computations.


### References

- [http://stackoverflow.com/questions/1957645/when-to-use-an-assertion-and-when-to-use-an-exception](http://stackoverflow.com/questions/1957645/when-to-use-an-assertion-and-when-to-use-an-exception)

- [http://stackoverflow.com/questions/117171/design-by-contract-using-assertions-or-exceptions](http://stackoverflow.com/questions/117171/design-by-contract-using-assertions-or-exceptions)


## Exceptions

- Use exceptions for something that **may** happen

    - Use exceptions to check correctness of input arguments to functions, if there are no assumptions about the same inputs. If there are assumptions, use assertions instead!

        - When to make assumptions???
    
    - The level of paranoia to check for correctness of inputs may depend on a few factors:
        
        - readability of the code
        
        - robustness of the software

        - efficiency of the software

        - cost and consequences of erroneous behaviour  

    - Use exceptions to handle possible erroneous behaviour after computation?? Why???

        - Examples: division by zero .. ?? 


### References

- [http://stackoverflow.com/questions/117171/design-by-contract-tests-by-assert-or-by-exception](http://stackoverflow.com/questions/117171/design-by-contract-tests-by-assert-or-by-exception)

- [http://softwareengineering.stackexchange.com/questions/125399/differences-between-design-by-contract-and-defensive-programming](http://softwareengineering.stackexchange.com/questions/125399/differences-between-design-by-contract-and-defensive-programming)

- [http://www.engr.mun.ca/~theo/Courses/sd/5895-downloads/sds-spec-1.ppt.pdf](http://www.engr.mun.ca/~theo/Courses/sd/5895-downloads/sds-spec-1.ppt.pdf)


## Type hints

- Use type hints (both for parameters and return values) as a form of documenting the code!!

    - Should we use it in every case???


## Parameters

- Use `isinstance` if 

    - the function supports more than one type for a certain parameter, and
 
    - you need to decide between portions of code to execute
 
 

## Names

- Names should be as explicit and descriptive as possible:

	- If abbreviated to improve readability, they should have an associated comment explaining its purpose.

## Comments

- Modules' doc-strings should contain the
	- author name,
	- the creation date,
	- the last update date,
	- a description of module,
	- references used to implement the module (if any), and eventually
	- links to resources talking about the topic


## Functions

- Functions should have a doc-string comment containing:
	- A description of the purpose of the function
	- Assumptions about parameters and return values (optional, if using assertions for this!)
	- Complexity analysis of the algorithm !!!

- Use closures ?? When ???
    - See: [http://stackoverflow.com/a/3182622/3924118](http://stackoverflow.com/a/3182622/3924118)
- Closures instead of private functions to modules that start with `_`?

## Testing

- Test only the public interface
    - but make sure all statements, even those containing private fields or methods, are covered!!

- Unit tests should test only one feature:
    - unit tests should be short
    - signature of unit test methods should be descriptive
