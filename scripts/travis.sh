#!/usr/bin/env bash

# Script called by Travis CI to report the code coverage.

cd tests/
coverage run -m unittest discover . -v
mv .coverage ../.coverage
cd ../
coveralls