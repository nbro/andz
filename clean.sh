#!/usr/bin/env bash

# source: http://stackoverflow.com/a/22916141/3924118

# make first this script executable (if not already) with: chmod +x name_of_this_script.sh

# run this file with: ./name_of_this_script.sh

clean() {

    # pyclean removes all .pyc and .pyo files
    find . -type f -name "*.py[co]" -delete && \
    
    # removes directory with name __pycache__
    find . -type d -name "__pycache__" -delete && \
    
    # removes directory ands.egg-info
    rm -rf ands.egg-info && \

    # deletes all .coverage files
    find . -type f -name ".coverage" -delete && \
    
    rm -rf venv

}

clean