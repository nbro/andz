#!/usr/bin/env bash

# Script called by Travis CI to report the code coverage.

python -m unittest discover -s tests/
coverage run --source=. -m unittest discover -s tests/
coverage report -m
coveralls
