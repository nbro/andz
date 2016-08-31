#!/usr/bin/env bash

# colors used when printing
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
NORMAL=$(tput sgr0)
YELLOW=$(tput setaf 3)

clean() {
    # Cleans a little bit everything, including previously created virtual environments
    # source: http://stackoverflow.com/a/22916141/3924118
    # run this file with: ./name_of_this_script.sh

    printf "${RED}REMOVING ALL 'JUNK' FILES...${NORMAL}\n"

    # removes all .pyc and .pyo files
    find . -type f -name "*.py[co]" -delete && \

    # removes directory with name __pycache__
    find . -type d -name "__pycache__" -delete && \

    # removes directory ands.egg-info
    rm -rf ands.egg-info && \

    # deletes all .coverage files
    find . -type f -name ".coverage" -delete && \

    rm -rf venv

    printf "${GREEN}DONE.${NORMAL}\n\n"
}


format() {
    # Format the code under ./ands/ and ./tests/
    printf "${RED}FORMATTING CODE UNDER './ands' AND './tests' AGGRESSIVELY AND RECURSIVELY...${NORMAL}\n"

    command -v autopep8
    rc=$?
    if [[ $rc != 0 ]]; then 
        printf "${RED}COMMAND 'autopep8' NOT FOUND.\nINSTALLING IT USING 'pip3.5'...${NORMAL}\n";
        pip3.5 install autopep8
    fi

    autopep8 --in-place --aggressive --recursive --max-line-length 110 ./ands
    autopep8 --in-place --aggressive --recursive --max-line-length 110 ./tests
    printf "${GREEN}DONE.${NORMAL}\n\n"
}

run_tests() {
    printf "${YELLOW}EXECUTING TESTS UNDER './tests/'...${NORMAL}\n"
    cd tests
    coverage run -m unittest discover . -v
    cd ..
    cp tests/.coverage ./.coverage
    coverage report
    printf "${GREEN}DONE.${NORMAL}\n\n"
}

install_dependencies(){
    printf "${YELLOW}INSTALLING REQUIRED DEPENDENCIES...${NORMAL}\n"
    pip install coveralls
    pip install pdoc
    pip install -e .
    printf "${GREEN}DONE.${NORMAL}\n\n"
}

new_docs(){
    # Creating new documentation
    printf "\n${YELLOW}CREATING NEW DOCUMENTATION UNDER './docs'...${NORMAL}\n"
    rm -rf ./docs
    mkdir docs
    pdoc --html --overwrite --html-dir docs ands
    printf "${GREEN}DONE.${NORMAL}\n\n"
}

new_virtualenv(){
    # Creates and switches to the new virtual environment
    printf "${YELLOW}CREATING NEW VIRTUAL ENVIRONMENT...${NORMAL}\n"

    command -v virtualenv
    rc=$?; 
    if [[ $rc != 0 ]]; then 
        printf "${RED}COMMAND 'virtualenv' NOT FOUND.\nINSTALLING IT USING 'pip3.5'...${NORMAL}\n";
        pip3.5 install virtualenv
    fi

    virtualenv venv
    printf "${GREEN}DONE.${NORMAL}\n\n"

    source venv/bin/activate
    printf "${YELLOW}USING THE NEWLY CREATED VIRTUAL ENVIRONMENT...${NORMAL}\n\n"

    # installing dependencies inside the virtual environment
    install_dependencies

    run_tests

    new_docs

    deactivate
    printf "${YELLOW}EXITED FROM VIRTUAL ENVIRONMENT.${NORMAL}\n\n"
}

run() {
    clean

    format

    new_virtualenv

    clean
}

run