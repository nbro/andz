#!/usr/bin/env bash

coverage run --source=. -m unittest discover -s tests/ -v

# Send results to https://coveralls.io/.
coveralls
