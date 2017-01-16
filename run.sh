#!/usr/bin/env bash

# RUN SPECIFIC TEST
# ./run.sh -st folder_name_inside_tests test_name.py
# Example: ./run.sh -st algorithms/recursion test_reverse.py

# colors used when printing
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
NORMAL=$(tput sgr0)
YELLOW=$(tput setaf 3)

clean()
{
    find . -type f -name "*.py[co]" -delete
    find . -type d -name "__pycache__" -delete
    rm -rf ands.egg-info
    find . -type f -name ".coverage" -delete
    rm -rf venv
    printf "${RED}All 'junk' files removed.${NORMAL}\n\n"
}


format()
{
    # Format the code under ./ands/ and ./tests/
    printf "${RED}Formatting code under './ands' and './tests' aggressively and recursively...${NORMAL}\n"

    command -v autopep8
    if [ $? != 0 ];
    then
        printf "${RED}Command 'autopep8' not found.\nInstalling it using 'pip3.5'...${NORMAL}\n";
        pip3.5 install autopep8
    fi

    autopep8 --in-place --aggressive --recursive --max-line-length 120 ./ands
    autopep8 --in-place --aggressive --recursive --max-line-length 120 ./tests
    printf "${GREEN}Done.${NORMAL}\n\n"
}

new_docs()
{
    printf "\n${YELLOW}Creating new documentation under './docs'...${NORMAL}\n"
    rm -rf ./docs
    mkdir docs
    pdoc --html --overwrite --html-dir docs ands
    printf "${GREEN}Done.${NORMAL}\n\n"
}

run_tests()
{
    printf "${YELLOW}Executing tests under './tests/'...${NORMAL}\n"
    cd tests
    coverage run -m unittest discover . -v
    cd ..
    cp tests/.coverage ./.coverage
    coverage report -m
    printf "${GREEN}Done.${NORMAL}\n\n"
}

cd_n_times()
{
    # source: http://stackoverflow.com/a/16679459/3924118
    slash="/"
    number_of_slashes=$(grep -o "$slash" <<< "$1" | wc -l)
    for (( i = 0; i < ${number_of_slashes}; i++));
    do
      cd ..
    done
}

run_specific_test()
{
    printf "${YELLOW}Executing tests under './tests/$1'...${NORMAL}\n"
    cd tests/$1  # entering the specific folder
    coverage run -m unittest $2 -v
    cd ../../  # we need to go back at least twice in order to be in the main folder
    cd_n_times "$@"
    cp tests/$1/.coverage ./.coverage
    # add option -m at the end if you want to see the lines missing
    coverage report -m
    printf "${GREEN}Done.${NORMAL}\n\n"
}

install_dependencies()
{
    printf "${YELLOW}Installing required dependencies...${NORMAL}\n"
    pip3.5 install coveralls
    pip3.5 install pdoc
    pip3.5 install -e .
    printf "${GREEN}Done.${NORMAL}\n\n"
}

test_in_virtual_environment()
{
    # Creates and switches to the new virtual environment
    printf "${YELLOW}Creating new virtual environment...${NORMAL}\n"
    assert_virtualenv_installed
    virtualenv venv
    printf "${GREEN}Done.${NORMAL}\n\n"

    source venv/bin/activate
    printf "${YELLOW}Using newly created virtual environment...${NORMAL}\n\n"

    # installing dependencies inside the virtual environment
    install_dependencies

    if [ "$#" =  "3" ];
    then
        if [ "$1" = "-st" ];
        then
            run_specific_test $2 $3
        fi
    else
        run_tests
    fi

    #new_docs

    deactivate
    printf "${YELLOW}Exited from virtual environment.${NORMAL}\n\n"
}

# ASSERT FUNCTIONS

assert_virtualenv_installed()
{
    command -v virtualenv
    if [ $? != 0 ];
    then
        printf "${RED}Command 'virtualenv' not found.\nInstalling it using 'pip3.5'...${NORMAL}\n";
        pip3.5 install virtualenv
    fi
}

assert_python35_installed()
{
    command -v python3.5
    if [ $? != 0 ];
    then
        printf "${RED}'python3.5' not installed. Install it first before proceeding.${NORMAL}\n";
        exit 1
    fi

    command -v pip3.5
    if [ $? != 0 ]; then
        printf "${RED}'pip3.5' not installed. Install it first before proceeding.${NORMAL}\n";
        exit 1
    fi
}

main()
{
    assert_python35_installed
    clean
    # format
    test_in_virtual_environment "$@"
    clean
}

# "$@" expands all command-line parameters separated by spaces
# which are passed to the run function
main "$@"