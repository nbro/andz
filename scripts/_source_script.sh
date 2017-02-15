#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: _source_script.sh                                                #
#                                                                               #
# PURPOSE: the function _source_script tries to "source" the scripts, whose     #
# names are passed as parameters to the same function.                          #
#################################################################################

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

            printf ". ./${!arg}.sh\n"
            # Try to load script ${!arg}.sh
            . ./${!arg}.sh

            # If it was not loaded successfully, exit with status 1.
            if [ $? -ne 0 ]
            then
                printf "${RED}Script '${!arg}.sh' not loaded successfully. Exiting...${NORMAL}\n"
                exit 1
            fi
        done
    else
        printf "No script loaded: $CURRENT_DIR != $EXPECTED_DIR.\n"
        exit 1
    fi
}

is_function()
{
    # Based on: http://stackoverflow.com/a/85903/3924118
    if [ -n "$(type -t $1)" ] && [ "$(type -t $1)" = function ]
    then
        # true
        return 0
    else
        # false
        return 1
    fi
}