#!/usr/bin/env bash

# Source: http://stackoverflow.com/a/22916141/3924118

# pyclean removes all .pyc and .pyo files, and __pycache__ directories.

# Run this file on the terminal with the following command: ./pyclean.sh 
# But first make this script executable by doing: chmod +x pyclean.sh

pyclean() {
    find . -type f -name "*.py[co]" -delete && find . -type d -name "__pycache__" -delete && rm -rf ands.egg-info
}

pyclean