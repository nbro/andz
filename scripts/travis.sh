#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: travis.sh                                                        #
#                                                                               #
# PURPOSE: script called by Travis CI                                           #
#################################################################################

cd tests/
coverage run -m unittest discover . -v
mv .coverage ../.coverage
cd ../
