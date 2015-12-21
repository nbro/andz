# How to develop?

If you want to develop a new feature or fix a bug, here are the steps.
 
1. Checkout `dev` with `git checkout dev`
2. Make sure it's up-to-date: `git pull`
3. Create the feature branch: `git checkout -b <local-branch-name>`
4. Make the changes that you want
5. Run the tests and other checks: `make quality`
6. Add your changes with `git add -u` (adds only tracked files) or `git add .` (adds all files)
7. Push your changes to the remote: `git push --set-upstream origin <remote-branch-name>`
8. Make a pull request (PR)
9. Ask for code review (if there's another developer)
10. Once the PR is approved, merge your feature branch into `dev` (**not** `master`)

## How to run the tests?

To run all tests, you can do

```
make test
```

See the `Makefile` for more info about this and other commands.

To run all the tests under e.g. `tests/algorithms/sorting/integer`, use

```
coverage run --source=. -m unittest discover -s tests/algorithms/sorting/integer -v
```

## Type checking

To type-check all the code in the `ands` package, run

```
mypy ands
```

To type-check a specific module (e.g. `ands/algorithms/sorting/integer/radix_sort.py`), run

```
mypy ands/algorithms/sorting/integer/radix_sort.py
```

## PyLint

To run PyLint on all `ands` package, run

```
pylint ands
```

## Format the code

To format the code with `black` and `isort`, run

```
make format
```

## How to run all quality assurance checks?

```
make quality
```