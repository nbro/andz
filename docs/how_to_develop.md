# How to develop?

If you want to develop a new feature or fix a bug, here are the steps.

1. Clone the repository `git clone git@github.com:nbro/andz.git`
2. Checkout `master` with `git checkout master`
3. Make sure it's up-to-date: `git pull`
4. Create the feature branch: `git checkout -b <local-branch-name>`
5. Make the changes that you want
6. Run the checks and tests: `make check test`
7. Add your changes e.g. with `git add -u` or `git add .`
8. Commit your changes with a commit message that starts with a verb (e.g. `git commit -m "Update the README"`)
9. Push your changes to the remote: `git push --set-upstream origin <remote-branch-name>`
10. Make a pull request (PR)
11. Ask for code review (if there's another developer)
12. Once the PR is approved, merge your feature branch into `master`

## How to run the tests?

To run all tests, you can do

```
make test
```
To run all the tests under e.g. `tests/algorithms/sorting/integer`, use

```
poetry run coverage run --source=. -m unittest discover -s tests/algorithms/sorting/integer -v
```

Or run a specific test

```
poetry run coverage run --source=. -m unittest tests/ds/test_MinMaxHeap.py -v
```

> See the `Makefile` for more info about other commands.