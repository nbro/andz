#!/usr/bin/env bash

# The function _source_script tries to source the scripts, whose names are passed as parameters to the same function.

export ALREADY_SOURCED__SOURCE_SCRIPT

if [ -z "${ALREADY_SOURCED__SOURCE_SCRIPT}" ]
then
    _source_script()
    {
        # Define a few colors for the possible error messages below.
        RED=$(tput setaf 1)
        NORMAL=$(tput sgr0)

        EXPECTED_DIR="scripts"

        if [ "$#" -ge  "1" ]
        then
            EXPECTED_DIR=$1
        fi

        # Based on: http://stackoverflow.com/a/1371283/3924118
        CURRENT_DIR=${PWD##*/}

        if [ "$CURRENT_DIR" = "$EXPECTED_DIR" ]
        then
            for (( arg = 2; arg <= $#; arg++ ))
            do
                # Based on:
                # - http://askubuntu.com/questions/306851/how-to-import-a-variable-from-a-script
                # - http://unix.stackexchange.com/questions/114300/whats-the-meaning-of-a-dot-before-a-command-in-shell
                # - http://stackoverflow.com/questions/20094271/bash-using-dot-or-source-calling-another-script-what-is-difference

                # printf ". ./%s.sh\n" "${!arg}"
                # Try to load script ${!arg}.sh
                # shellcheck source=/dev/null
                . ./${!arg}.sh

                # If it was not loaded successfully, exit with status 1.
                if [ $? -ne 0 ]
                then
                    printf "%sScript '${!arg}.sh' not loaded successfully. Exiting...%s\n" "${RED}" "${NORMAL}"
                    exit 1
                fi
            done
        else
            printf "No script loaded: %s != %s.\n" "$CURRENT_DIR" "$EXPECTED_DIR"
            exit 1
        fi
    }

    ALREADY_SOURCED__SOURCE_SCRIPT="true"
fi