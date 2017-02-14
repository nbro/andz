#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: run_tests.sh                                                     #
#                                                                               #
# PURPOSE: run (unit) tests in a virtual environment and report code coverage   #
#                                                                               #
# RUN ALL TESTS: ./run_tests.sh                                                 #
#                                                                               #
# RUN SPECIFIC TEST: ./run_tests.sh -st [folder_path_inside_tests] test_name.py #
# EXAMPLE: ./run_tests.sh -st algorithms/recursion test_reverse.py              #
#################################################################################

# Colors used when printing.
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
    printf "${YELLOW}Environment cleaned.${NORMAL}\n"
}

create_virtual_environment()
{
    printf "${YELLOW}Creating new virtual environment...${NORMAL}\n"
    assert_virtualenv_installed
    virtualenv venv
    printf "${GREEN}Done.${NORMAL}\n\n"
}

switch_to_virtual_environment()
{
    printf "${YELLOW}Entering virtual environment 'venv'...${NORMAL}\n"
    source venv/bin/activate
    printf "${GREEN}Done.${NORMAL}\n\n"
}

install_dependencies_in_virtual_environment()
{
    printf "${YELLOW}Installing required dependencies...${NORMAL}\n"
    pip3.5 install coveralls
    pip3.5 install pdoc
    pip3.5 install -e .
    printf "${GREEN}Done.${NORMAL}\n\n"
}

exit_from_virtual_environment()
{
    printf "${YELLOW}Exiting from virtual environment...${NORMAL}\n"
    deactivate
    printf "${GREEN}Done.${NORMAL}\n\n"
}

run_tests()
{
    # See function below 'run_specific_test' if you don't understand what this function does.
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
    # Source: http://stackoverflow.com/a/16679459/3924118.
    SLASH="/"
    NUMBER_OF_SLASHES=$(grep -o "$SLASH" <<< "$1" | wc -l)
    for (( i = 0; i < NUMBER_OF_SLASHES; i++));
    do
      cd ..
    done
}

run_specific_test()
{
    printf "${YELLOW}Executing tests under './tests/$1'...${NORMAL}\n"

    # Enter the specific folder where the test is.
    cd tests/$1

    # Executes the test and and produces a file '.coverage' with code coverage statistics.
    coverage run -m unittest $2 -v

    # We need to go back at least twice in order to be in the root folder of the project.
    cd ../../

    # This to ensure we're in the root folder of the project,
    # since the specific test could have been executed in a depth greater than 2.
    cd_n_times "$@"

    # Move the file '.coverage' to the root folder of the project.
    mv tests/$1/.coverage ./.coverage

    # Add option -m at the end if you want to see the lines not covered.
    coverage report -m

    printf "${GREEN}Done.${NORMAL}\n\n"
}

test_in_virtual_environment()
{
    create_virtual_environment
    switch_to_virtual_environment
    install_dependencies_in_virtual_environment

    # If we have 3 parameters, then probably the user wants to execute a specific test.
    if [ "$#" =  "3" ];
    then
        # First parameter must be -st
        if [ "$1" = "-st" ];
        then
            run_specific_test $2 $3
        else
            printf "${RED}To execute a specific test the format is the following:\n"
            printf "${NORMAL}  ./run_tests.sh -st [folder_path_inside_tests] test_name.py\n"
            printf "${RED}For example, you try to run the 'test_reverse.py' unit test "
            printf "under './tests/algorithms/recursion' as follows:\n"
            printf "${NORMAL}  ./run_tests.sh -st algorithms/recursion test_reverse.py\n"
            printf "${RED}Cannot continue with procedure. Exiting...${NORMAL}\n\n"
            clean
            exit 1
        fi
    else
        run_tests
    fi

    exit_from_virtual_environment
}

# Assert functions

assert_virtualenv_installed()
{
    command -v virtualenv

    if [ $? != 0 ];
    then
        # Based on: http://stackoverflow.com/a/27875395/3924118

        printf "${RED}Command 'virtualenv' not found.\n"
        printf "Do you want me to install 'virtualenv' using 'pip3.5' (y/n)?${NORMAL} "
        read ANSWER

        if echo "$ANSWER" | grep -iq "^y"
        then
            pip3.5 install virtualenv
            printf "${GREEN}Done.${NORMAL}\n"
        else
            printf "${RED}Cannot continue with procedure. Exiting...${NORMAL}\n"
            exit 1
        fi

    fi
}

assert_python35_installed()
{
    command -v python3.5
    if [ $? != 0 ];
    then
        printf "${RED}'python3.5' not installed. Install it first before proceeding. Exiting...${NORMAL}\n"
        exit 1
    fi

    command -v pip3.5
    if [ $? != 0 ];
    then
        printf "${RED}'pip3.5' not installed. Install it first before proceeding. Exiting...${NORMAL}\n"
        exit 1
    fi
}

main()
{
    # Python 3.5 is currently being used to develop.
    assert_python35_installed
    clean
    printf '\n'
    test_in_virtual_environment "$@"
    clean
}

# "$@" expands all command-line parameters separated by spaces which are passed to the run function
main "$@"