# Coding conventions

## General

- Do not introduce features that are
    - incomplete, or
    - not tested

 to the `master` branch!!

## Assertions

- Use assertions for assumptions ?
	- Assertions could be disabled eventually!
- Use assertions for pre-conditions, invariants and post-conditions or should exceptions be raised ?

## Parameters

- Use type hints
- Do not check the type of the arguments if using type hints, unless 

	1. you need to decide between portions of code to execute
	2. the state of the data structure (in the case of the input is an input to a data structure's method) needs to be preserved (defensive programming)
	3. If the function supports more than one type for a certain parameter

	_Comment_: in general, assume the client passes the right types because he's read the documentation, otherwise _undefined behavior_ may happen.


## Return value

- Use type hints

## Names

- Names should be as explicit and descriptive as possible:
	- If abbreviated, they should have an associated comment explaining its purpose.

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
