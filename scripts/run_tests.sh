#!/usr/bin/env bash

# See the file CONTRIBUTING.md under the root folder of the ands package to know more about this script.
# Run all tests with: ./run_tests.sh
# Run specific test: ./run_tests.sh -st [folder_path_inside_tests] test_name.py


export ALREADY_SOURCED_RUN_TESTS

if [ -z "${ALREADY_SOURCED_RUN_TESTS}" ]
then
    run_all_tests()
    {
        # See function below 'run_specific_test' if you don't understand what this function does.
        printf "%sExecuting tests under './tests/'...%s\n" "${YELLOW}" "${NORMAL}"

        cd tests
        coverage run -m unittest discover . -v

        if [ $? -ne 0 ]
        then
            printf "%sUnit tests did NOT run successfully.%s\n" "${RED}" "${NORMAL}"
            cd .. # otherwise we're still inside tests/
            clean_environment
            exit 1
        fi

        cd ..
        mv tests/.coverage ./.coverage
        coverage report -m

        printf "%sDone.%s\n\n" "${GREEN}" "${NORMAL}"
    }

    run_specific_test()
    {
        printf "%sExecuting test '%s/tests/$1/$2'...%s\n" "${YELLOW}" "${PWD}" "${NORMAL}"

        # Enter the specific folder where the test is.
        cd tests/"$1"

        # Executes the test and and produces a file '.coverage' with code coverage statistics.
        coverage run -m unittest "$2" -v

        # In case an error occurs while running coverage.
        # An error that occurred to me was that a unit test module was not found.
        # So we just proceed if we have actually run the tests and created the file .coverage.
        if [ $? -ne 0 ]
        then
            printf "%sUnit test(s) did NOT run successfully.%s\n" "${RED}" "${NORMAL}"
            exit 1
        fi

        # We need to go back at least twice in order to be in the root folder of the project.
        cd ../../

        # This to ensure we're in the root folder of the project,
        # since the specific test could have been executed in a depth greater than 2.
        cd_back_n_times "$(count_occurrences "/" "$1")"

        # Move the file '.coverage' to the root folder of the project.
        mv tests/"$1"/.coverage ./.coverage

        # Add option -m at the end if you want to see the lines not covered.
        coverage report -m

        printf "%sDone.%s\n\n" "${GREEN}" "${NORMAL}"
    }

    test_in_virtual_environment()
    {
        create_virtual_environment

        switch_to_virtual_environment

        install_dependencies_in_virtual_environment coveralls pdoc "-e ."

        # If we have 3 parameters, then probably the user wants to execute a specific test.
        if [ "$#" =  "3" ]
        then
            # First parameter must be -st
            if [ "$1" = "-st" ]
            then
                run_specific_test "$2" "$3"
            else
                printf "%sTo execute a specific test the format is the following:\n" "${RED}"
                printf "%s  ./run_tests.sh -st [folder_path_inside_tests] test_name.py\n" "${NORMAL}"
                printf "%sFor example, you try to run the 'test_reverse.py' unit test " "${RED}"
                printf "under './tests/algorithms/recursion' as follows:\n"
                printf "%s  ./run_tests.sh -st algorithms/recursion test_reverse.py\n" "${NORMAL}"
                printf "%sCannot continue with procedure. Exiting...%s\n\n" "${RED}" "${NORMAL}"
                clean_environment
                exit 1
            fi
        else
            run_all_tests
        fi

        #new_docs

        exit_from_virtual_environment
    }

    _main()
    {
        cd ..

        assert_installed 1 python3.5 pip3.5

        clean_environment
        printf '\n'

        test_in_virtual_environment "$@"

        clean_environment

        cd scripts
    }

    . ./_source_script.sh
    # Need to source the scripts individually!
    _source_script scripts colors
    _source_script scripts clean_environment
    _source_script scripts asserts
    _source_script scripts cd_back_n_times
    _source_script scripts virtual_environment
    _source_script scripts count_occurrences
    #_source_script scripts new_docs

    # "$@" expands all command-line parameters separated by spaces which are passed to the run function
    _main "$@"

    ALREADY_SOURCED_RUN_TESTS="true"
fi